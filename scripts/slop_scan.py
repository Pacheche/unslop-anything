#!/usr/bin/env python3
"""Find candidate AI-slop signs in UI code and in writing.

Candidates, not verdicts: read every hit before acting on it.

Usage:
  python3 slop_scan.py <files or folders>...
  python3 slop_scan.py --text draft.md        # writing rules on any file
  python3 slop_scan.py --json <paths>          # machine-readable output

Exit codes: 0 no candidates, 1 candidates found, 2 nothing could be scanned.
Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

CODE_EXT = {".html", ".htm", ".css", ".scss", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro", ".mdx"}
TEXT_EXT = {".md", ".txt", ".markdown"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "out", "coverage", "__pycache__", ".venv", "vendor",
             ".svelte-kit", ".nuxt", ".output", ".astro", ".turbo", ".vercel", "target"}
HYPE = (r"supercharg\w*|seamless\w*|unlock\w*|revolutioni[sz]\w*|game[- ]?chang\w*|effortless\w*|magic(?:al)?|AI[- ]powered|"
        r"next[- ]gen\w*|cutting[- ]edge|potenci[aá] tu\w*|potenci[ae]\s+(?:su|seu|sua)\w*|revolucion[aá]\w*|sin esfuerzo|"
        r"impulsad[oa] por IA|potenciad[oa] por IA|alavanc\w*|sem esfor[cç]o|movid[oa] a IA|world[- ]class|enterprise[- ]grade|"
        r"empower\w*|streamlin\w*|desbloque\w*|el poder de|the power of|sin fricci[oó]n|sem atrito")

EMOJI = r"[\U0001F300-\U0001FAFF☀-➿⭐⭕✨]"
HUES = r"(?:purple|violet|indigo|fuchsia|pink|blue|cyan|sky|teal|emerald|rose|orange|amber)"


def off_grid(value) -> bool:
    n = int(value)
    return n > 2 and n % 4 != 0


def is_cream(hexcode: str) -> bool:
    """A warm off-white page color: the default "tasteful" surface."""
    r, g, b = (int(hexcode[i:i + 2], 16) for i in (0, 2, 4))
    return r >= 235 and g >= 222 and b >= 195 and r >= g >= b and 10 <= r - b <= 45


def faint_grey(hexcode: str) -> bool:
    """A light, nearly neutral grey: unreadable as text on a light page."""
    if len(hexcode) == 3:
        hexcode = "".join(c * 2 for c in hexcode)
    rgb = [int(hexcode[i:i + 2], 16) for i in (0, 2, 4)]
    return max(rgb) - min(rgb) <= 16 and 0xB8 <= min(rgb) and max(rgb) <= 0xDD


def overshoots(args: str) -> bool:
    """cubic-bezier(x1, y1, x2, y2) whose y values leave 0..1 (bounce or overshoot)."""
    try:
        nums = [float(n) for n in args.split(",")]
    except ValueError:
        return False
    return len(nums) == 4 and any(y < 0 or y > 1 for y in (nums[1], nums[3]))


def icon_tile(cls: str) -> bool:
    """A small centered colored square holding an icon, the feature-card template."""
    return all(re.search(p, cls) for p in (r"\b(?:h|w|size)-(?:8|9|10|11|12|14|16)\b", r"\brounded", r"\bbg-",
                                           r"\bitems-center\b", r"\bjustify-center\b"))


def chromatic_stops(args: str) -> int:
    """Count color stops that are clearly not grey (hex, rgb, hsl, oklch)."""
    count = 0
    for s in re.findall(r"hsla?\(\s*[\d.]+(?:deg)?[\s,]+([\d.]+)%", args):
        count += float(s) > 25
    for c in re.findall(r"oklch\(\s*[\d.]+%?\s+([\d.]+)", args):
        count += float(c) > 0.05
    for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", args):
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        count += max(rgb) - min(rgb) > 40
    for r, g, b in re.findall(r"rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)", args):
        rgb = [int(r), int(g), int(b)]
        count += max(rgb) - min(rgb) > 40
    return count


@dataclass
class Rule:
    id: str
    category: str
    pattern: str
    hint: str
    flags: int = re.IGNORECASE
    min_count: int = 1  # minimum hits per file before reporting
    keep: object = None  # optional filter on the match: keep(match) -> bool

    def compiled(self):
        return re.compile(self.pattern, self.flags)


UI_RULES = [
    # 1. Color and surfaces
    Rule("hue-gradient", "color", rf"\b(?:from|via|to)-{HUES}-\d+\b[^\n\"'`]*\b(?:from|via|to)-{HUES}-\d+\b",
         "hue-to-hue gradient: use one neutral surface; accent only where it means something"),
    Rule("css-gradient", "color", r"(?:linear|radial|conic)-gradient\(([^;{}\n]*)",
         "hue-to-hue CSS gradient: one neutral surface, or a tone shift inside one hue",
         keep=lambda m: chromatic_stops(m.group(1)) >= 2),
    Rule("gradient-text", "color", r"bg-clip-text[^\n]*text-transparent|text-transparent[^\n]*bg-clip-text|background-clip:\s*text",
         "gradient text: use solid primary text"),
    Rule("colored-glow", "color", r"shadow-\[0_0_\d+px[^\]]*\]|\bshadow-" + HUES + r"-\d+|box-shadow:[^;]*\b0\s+0\s+\d+px\s+(?:rgba?\((?!0,\s*0,\s*0)|#(?!000))|drop-shadow-\[",
         "colored glow or shadow: remove; depth from surface steps and hairlines"),
    Rule("radial-glow", "color", r"radial-gradient\(([^;{}\n]*)",
         "colored glow or spotlight fading to transparent: a solid surface, or a lit material from the world",
         keep=lambda m: chromatic_stops(m.group(1)) >= 1 and re.search(r"transparent|,\s*0\)|/\s*0\)|#0000(?:00)?\b", m.group(1)) is not None),
    Rule("cream-background", "color", r"(?:background(?:-color)?:\s*|bg-\[)#([0-9a-fA-F]{6})\b",
         "cream page background, the default tasteful surface: keep only if the direction chose it",
         keep=lambda m: is_cream(m.group(1))),
    Rule("backdrop-blur", "color", r"backdrop-blur|backdrop-filter:\s*blur",
         "glass blur: keep only when something real sits behind it (overlay, sticky header over content)"),
    # 2. Type
    Rule("heavy-weight", "type", r"\bfont-(?:extrabold|black)\b|font-weight:\s*(?:800|900)\b",
         "800-900 weight: use 400-500 and size for hierarchy"),
    Rule("tracked-caps", "type", r"\buppercase\b[^\n\"'`]*\btracking-(?:wide|wider|widest|\[0?\.\d+em\])|\btracking-(?:wide|wider|widest|\[0?\.\d+em\])[^\n\"'`]*\buppercase\b|text-transform:\s*uppercase[^}]*letter-spacing:\s*0?\.[05-9]|letter-spacing:\s*0?\.[05-9][^}]*text-transform:\s*uppercase",
         "3+ uppercase tracked labels: delete the ones that repeat their heading; keep at most one, sentence case", min_count=3),
    Rule("stock-font", "type", r"font-family:[^;}\n]*\b(?:Inter|Geist|Satoshi|Outfit|Cabinet Grotesk|Space Grotesk|Plus Jakarta Sans|Poppins|Roboto|Fraunces|Recoleta|Playfair Display|Instrument (?:Sans|Serif))\b|fonts\.googleapis\.com/css2?\?family=(?:Inter|Geist|Outfit|Space\+Grotesk|Plus\+Jakarta\+Sans|Poppins|Roboto|Fraunces|Playfair|Instrument)|\bfont-(?:inter|geist|satoshi|outfit|poppins)\b",
         "usual default typeface: keep it only if it was chosen for this product, and say why"),
    Rule("extreme-tracking", "type", r"letter-spacing:\s*-0?\.(?:0[5-9]|[1-9])\d*em|tracking-\[-0?\.(?:0[5-9]|[1-9])\d*em\]",
         "tracking tighter than -0.04em: letters lose their shapes; use -0.02 to -0.04em on display"),
    Rule("tiny-text", "type", r"font-size:\s*(?:[0-9]|10)(?:\.\d+)?px|\btext-\[(?:[0-9]|10)(?:\.\d+)?px\]",
         "text under 11px: 14-16px body, 11px floor for functional text"),
    Rule("justified-text", "type", r"text-align:\s*justify|\btext-justify\b",
         "justified text opens rivers in narrow columns: align left"),
    # 3. Icons and emoji
    Rule("emoji", "icons", EMOJI, "emoji in UI: replace with one line icon set, or nothing (user content is fine)", flags=0),
    Rule("icon-tile", "icons", r"class(?:Name)?=[\"'`]([^\"'`]*)",
         "icon tiles above headings: drop the tile; an icon only where it helps scanning",
         keep=lambda m: icon_tile(m.group(1)), min_count=3),
    Rule("arrow-glyph", "icons", r"[←-⇿⟰-⟿⤀-⥿➜-➾]",
         "arrow glyph in text: use a library chevron icon or plain text", flags=0),
    # 4. Spacing
    Rule("off-grid-tw", "spacing", r"(?<![\w-])-?(?:[mp][trblxyse]?|gap(?:-[xy])?|space-[xy]|inset(?:-[xy])?|top|left|right|bottom|h|min-h)-\[(\d+)px\]",
         "off-grid arbitrary value: use a 4px step", keep=lambda m: off_grid(m.group(1))),
    Rule("off-grid-css", "spacing", r"\b(?:margin|padding|gap|row-gap|column-gap)(?:-(?:top|right|bottom|left|inline|block))?:\s*([^;}\n]+)",
         "off-grid spacing: use a 4px step", keep=lambda m: any(off_grid(n) for n in re.findall(r"(\d+)px", m.group(1)))),
    # 5. Copy
    Rule("greeting", "copy", r"(?:Welcome back|Good (?:morning|afternoon|evening)|Hey|Hi|Hello|Morning|Bienvenid[oa] de nuevo|Hola|Buen(?:os|as) (?:d[ií]as|tardes|noches)|Bem-vind[oa] de volta|Ol[áa]|Bom dia|Boa (?:tarde|noite))\s*,?\s+\{?[\w.$]+\}?\s*(?:!|👋|<)",
         "greeting headline: title the context (page or period) instead"),
    Rule("exclamation", "copy", r">(?:[^<{}\n]|\{[^{}\n]*\})*[A-Za-zÀ-ÿ0-9}](?:[^<{}\n]|\{[^{}\n]*\})*!+\s*<|!!(?=\s*[\"'`<)\n]|\s*$)",
         "exclamation in interface text: plain statement"),
    Rule("wordy-placeholder", "copy", r"placeholder=[\"'][^\"']*(?:anything|whatever|cualquier cosa|qualquer coisa)[^\"']*[\"']",
         "wordy placeholder: one word like Search"),
    Rule("hype-ui", "copy", rf"\b(?:{HYPE})\b",
         "hype word: say what it does"),
    Rule("unverified-claim", "copy", r"\b(?:trusted|loved|used)\s+by\s+[\d,.]+\s*[kKmM+]*|\b(?:m[aá]s de|mais de)\s+[\d,.]+\s*[kKmM]?\+?\s+(?:usuarios|usu[aá]rios|clientes|equipos|equipes|empresas|personas|pessoas|miembros|people|members)\b|\b\d+x\s+faster\b|\b[\d,.]+\s*[kKmM]?\+\s+(?:users|teams|customers|companies|clientes|usuarios)\b|\b[45][.,]\d\s*(?:★|/\s*5\b|stars\b|estrellas\b)|★{5}",
         "unverifiable claim: confirm with the user, then make it specific or remove it"),
    Rule("template-copy", "copy", r"\bEverything you need,? (?:all )?in one place\b|\bThe future of [\w ]{1,25} is here\b|\bWhy choose us\b|\bNo fluff\b|\bLess noise\.? More signal\b|\bto the next level\b|\bNo more [\w ]{1,25} theat(?:er|re)\b|\bOops!? Something went wrong\b|\bFast\. Simple\. Secure\b|\bTodo lo que necesitas,? en un solo lugar\b|\bPor qu[eé] elegirnos\b|\bal siguiente nivel\b|\bTudo o que voc[eê] precisa\b|\bpr[oó]ximo n[ií]vel\b|\bSin relleno\b|\bMenos ruido\.? M[aá]s se[ñn]al\b|\bEl futuro del? [\w ]{1,25} ya est[aá] aqu[ií]\b|\bR[aá]pido\. Simple\. Seguro\b|\bUps!? Algo sali[oó] mal\b|\bBasta de [\w ]{0,25}teatro\b|\bteatro (?:de|en) (?:las|los) \w+|\b(?:for|para) (?:modern teams|equipos modernos)\b|\bThe AI[- ]powered platform\b|\bLa plataforma (?:con|de) IA\b|\bAre you sure\?|¿Est[aá]s segur[oa]\?|\bNo items yet\b|\bNothing here yet\b|\bNo hay elementos todav[ií]a\b|\bTrusted by (?:leading|top|the best|industry)\b|\bCon la confianza de\b|\bWork smarter\b|\bTrabaja m[aá]s inteligente\b|\bPor qu[eé] elegir\w*",
         "template line: replace with a fact about this product"),
    Rule("fake-urgency", "copy", r"\bOnly \d+ (?:spots?|seats?|left|remaining)\b|\bEnds in \d|\bUpdated \d+ (?:seconds?|minutes?) ago\b|\b\d[\d,.]* (?:people )?online now\b|\bS[oó]lo quedan \d+\b|\bApenas \d+ vagas\b|\bTermina en \d|\bActualizado hace \d+ (?:segundos?|minutos?)\b|\b\d[\d,.]* (?:personas )?en l[ií]nea\b",
         "urgency or live-ness nobody measured: real values or nothing"),
    Rule("placeholder-people", "copy", r"\b(?:Sarah Johnson|David Chen|Jane Doe|John Doe|Jane Smith|John Smith|Lorem ipsum|Juan P[eé]rez|Mar[ií]a Gonz[aá]lez|Carlos Mendoza|Jo[aã]o da Silva|Fulano de Tal|Acme S\.A\.)",
         "placeholder person or text: real names from the user, or remove (mock data only replaces placeholders, list it)"),
    Rule("aphorism", "copy", r">\s*(?:Not (?:a|an|just) [^<.]{1,30}\.\s+(?:A|An|It'?s) [^<.]{1,30}\.|[^<.]{1,30}\.\s+(?:No|Just) [^<.]{1,30}\.)\s*<",
         "aphoristic cadence (\"X. No Y.\", \"Not a X. A Y.\"): say plainly what it does", min_count=2),
    Rule("side-border", "components", r"\bborder-[lr]-(?:[2-8]|\[[2-9]px\])(?![\w-])|border-(?:left|right):\s*[2-9]px\s+solid|border-(?:left|right)-width:\s*[2-9]px",
         "colored side border on a card, list item or alert: a subtler accent, or none"),
    Rule("thin-border-wide-shadow", "components", r"\bborder\b[^\n\"'`]*\bshadow-(?:xl|2xl)\b|\bshadow-(?:xl|2xl)\b[^\n\"'`]*\bborder\b|border:\s*1px solid[^}]*box-shadow:\s*0\s+(?:[2-9]\d)px\s+(?:[4-9]\d|\d{3})px|box-shadow:\s*0\s+(?:[2-9]\d)px\s+(?:[4-9]\d|\d{3})px[^}]*border:\s*1px solid",
         "hairline border plus wide soft shadow on a row of cards: commit to one, edge or elevation", min_count=3),
    Rule("fake-logos", "components", r"\b(?:Acme(?: Inc| Corp)?|Globex|Initech|Umbrella(?: Corp)?|Hooli|Stark Industries|Wayne Enterprises)\b",
         "made-up customer logos: real customers the user confirms, or nothing", min_count=2),
    Rule("intro-badge", "layout", r"(?:Introducing|Announcing|Presentamos|Nuevo|New)\b[^<\n]{0,40}(?:2\.0|v\d|✨|🚀)",
         "pill badge above the headline: remove, or a quiet text link if it is real news"),
    Rule("em-dash-ui", "copy", r">(?:[^<{}\n]|\{[^{}\n]*\})*\s[—–]\s(?:[^<{}\n]|\{[^{}\n]*\})*<|(?:title|label|placeholder|alt|aria-label|description)\s*[=:]\s*[\"'`][^\"'`\n]*\s—\s",
         "em dash in UI copy: period, comma or line break", flags=0),
    # 6. Components
    Rule("pill-everything", "components", r"\brounded-full\b|border-radius:\s*(?:9{3,}|100vmax|[1-9]\d{2,}px)",
         "many full pills: radius by size; pills only for chips, segmented controls, avatars", min_count=6),
    Rule("numbered-sections", "layout", r">\s*0[1-9]\s*(?:[./—–-]\s*)?<",
         "01/02/03 section numbers: let headings and layout carry the sequence", flags=0, min_count=3),
    Rule("dot-grid", "visuals", r"radial-gradient\([^)]*\b1px\b[^)]*\)[^;\n]*;?\s*background-size|bg-\[radial-gradient|repeating-(?:linear|radial)-gradient|linear-gradient\([^)]*\b1px\b[^)]*\)[^;\n]*,\s*linear-gradient|bg-\[linear-gradient\(to_right",
         "pattern background (dots, grid lines, stripes): plain surface, or a texture from the world; alone it proves nothing"),
    Rule("svg-scene", "visuals", r"<feTurbulence\b|\b(?:loose-sketch|doodle)\b",
         "sketch, doodle or turbulence-grain SVG: real artwork or a photo, or no illustration"),
    Rule("organic-clip", "visuals", r"clip-path:\s*(?:path\(|polygon\(([^)]*)\))",
         "organic clip-path imitating a cut-out: an alpha matte from the real image, or no mask",
         keep=lambda m: m.group(1) is None or m.group(1).count(",") >= 7),
    Rule("stock-palette", "color", r"\b(?:bg|text|border|ring|from|to|via)-indigo-(?:500|600)\b|#(?:4f46e5|6366f1|8b5cf6|7c3aed|a3e635|22d3ee|c2410c)\b",
         "stock Tailwind color as the brand (indigo-600, violet-500, lime-400, cyan-400, orange-700): a color from the product's world, written as tokens"),
    Rule("cold-greys", "color", r"#(?:f9fafb|f3f4f6|e5e7eb|d1d5db|9ca3af|6b7280|4b5563|374151|1f2937|111827|f8fafc|f1f5f9|e2e8f0|cbd5e1|94a3b8|64748b|475569|334155|1e293b|0f172a)\b|\b(?:bg|text|border|divide|ring)-(?:gray|slate)-\d{2,3}\b",
         "stock cool greys with no tint as the whole ramp: a neutral ramp tinted toward the product's world", min_count=6),
    Rule("faint-text", "color", r"\btext-(?:gray|slate|zinc|neutral|stone)-(?:200|300)\b|(?<![\w-])color:\s*#(?:d1d5db|e5e7eb|cbd5e1|d4d4d8|e4e4e7|ccc|ddd|cccccc|dddddd)\b",
         "grey text so light it fails contrast: 4.5:1 for body, 3:1 for large text; darker, bigger, or cut it"),
    Rule("impact-font", "type", r"font-family:[^;}\n]*\b(?:Impact|Arial Black|Haettenschweiler)\b|\bfont-\[(?:Impact|Arial_Black)\]",
         "Impact or Arial Black as the headline face: a display family chosen for the product"),
    Rule("headline-highlight", "type", r"<h[12]\b[^>]*>[^<]{1,80}<(?:span|em|i|mark|strong)\b[^>]*>[^<]{1,30}</(?:span|em|i|mark|strong)>",
         "one highlighted, italic or colored word in the headline: let the sentence carry the emphasis"),
    Rule("mono-costume", "type", r">[^<]*(?:\[\s*[A-Z][A-Z0-9_]{3,}\s*\]|//\s*v\d+\.\d+)[^<]*<",
         "monospace system-label costume ([ SYSTEM_READY ] // v1.0.4): plain words; mono only for real code and IDs", flags=0),
    Rule("title-case", "type", r"<h[1-4]\b[^>]*>\s*(?:[A-ZÁÉÍÓÚÑ][a-záéíóúñ']+\s+){3,}[A-ZÁÉÍÓÚÑ][a-záéíóúñ']+",
         "Title Case On Every Word: sentence case (Spanish and Portuguese never use title case; English only if the style guide asks)", flags=0),
    Rule("ai-sparkle", "icons", r"<(?:Sparkles?|WandSparkles|Wand2?|MagicWand)\b|\bimport\s*\{[^}]*\b(?:Sparkles?|WandSparkles|Wand2)\b[^}]*\}",
         "sparkle or wand for \"AI\": a plain icon that explains the action, or none; show what the AI produces"),
    Rule("lucide-default", "icons", r"from\s+[\"']lucide-(?:react|vue|vue-next|svelte|angular)[\"']|unpkg\.com/lucide|\bdata-lucide=|class=[\"\']lucide\b",
         "Lucide as shipped (24px, stroke 2) proves nothing alone: if kept, set size and stroke to match the type; or pick a family for the product"),
    Rule("dead-button", "copy", r"<(?:button|a|Button|Link)\b[^>]*>\s*(?:Get started|Learn more|Submit|Click here|Read more|Empezar|Comenzar|Saber m[aá]s|Ver m[aá]s|Enviar|Haz clic aqu[ií]|Comece agora|Saiba mais)\s*[→›]?\s*</",
         "button that says nothing: the action the person wants (Book a table, See pricing)"),
    Rule("generic-benefit", "copy", r">\s*(?:Save time|Grow faster|Do more|No limits|Lightning fast|Secure by default|Ahorra tiempo|Crece r[aá]pido|Haz m[aá]s|Sin l[ií]mites|Rapid[ií]simo|Seguro|Inteligente|Simple|R[aá]pido|Fast|Secure|Smart|Easy|Siempre)\.?\s*<",
         "benefit that fits any product: a fact only this product can claim", min_count=2),
    Rule("stacked-without", "copy", r"\b(?:sin|without|sem)\s+[\wáéíóúñ]+,\s*(?:sin|without|sem)\s+[\wáéíóúñ]+",
         "stacked \"without X, without Y\": name the one thing that is actually gone, with its fact"),
    Rule("contrast-ui", "copy", r">\s*(?:(?:It'?s )?[Nn]ot (?:a|an|just) [^<.]{1,40}[.,]\s+(?:It'?s |A |An )|No es (?:solo |s[oó]lo )?[^<.]{1,40}[.,]\s+Es |N[ãa]o [ée] [^<.]{1,40}[.,]\s+[ÉE] )",
         "\"Not X. It's Y.\" framing: say what it is"),
    Rule("top-border", "components", r"\bborder-t-(?:[3-8]|\[[3-9]px\])(?![\w-])|border-top:\s*[3-9]px\s+solid|border-top-width:\s*[3-9]px",
         "thick top border on a rounded card: one surface treatment, or none"),
    Rule("hard-shadow", "components", r"shadow-\[-?\d+px_-?\d+px_0(?:px)?_|box-shadow:\s*-?[2-9]\d?px\s+-?[2-9]\d?px\s+(?:0(?:px)?\s+)?(?:#[0-9a-fA-F]{3,8}\b|black\b|rgb)",
         "hard offset shadow (template neobrutalism): only if the world is really neobrutalist; else a soft elevation or none"),
    Rule("spinning-border", "components", r"@property\s+--(?:angle|border-angle|gradient-angle|rotate)\b|conic-gradient\(\s*from\s+var\(--",
         "rotating gradient border: a static hairline; motion only where it answers an action"),
    Rule("carousel", "components", r"\b(?:swiper|slick-slider|react-slick|embla|keen-slider|splide|owl-carousel)\b|\bcarousel\b",
         "carousel (testimonials, features): show the best two or three side by side; carousels hide content"),
    Rule("spinner", "components", r"<(?:Spinner|Loader2|CircularProgress)\b|\bclass(?:Name)?=[\"'`][^\"'`]*\bspinner\b",
         "spinner where the shape of the content is known: a skeleton with the final geometry"),
    Rule("most-popular", "layout", r"\b(?:Most popular|M[aá]s popular|Recomendado|Best value|Mais popular)\b",
         "middle plan marked \"Most popular\": only if the data says so; else drop the badge"),
    Rule("zigzag", "layout", r"\b(?:sm|md|lg|xl):flex-row-reverse\b|:nth-child\((?:even|odd|2n)\)[^{]*\{[^}]*flex-direction:\s*row-reverse",
         "zigzag image/text rows: a structure that follows the content"),
    Rule("bento", "layout", r"\bbento\b",
         "bento grid by default: a structure that follows the content"),
    Rule("blur-blob", "visuals", r"(?<![\w-])blur-(?:2xl|3xl|\[\d{2,}px\])(?![\w-])|(?<![\w-])filter:\s*blur\(\s*(?:[4-9]\d|\d{3,})px",
         "blurred color blob: remove; a solid surface or an image from the product's world"),
    Rule("scroll-reveal", "motion", r"\bdata-aos\b|\baos(?:\.min)?\.(?:css|js)\b|\bwhileInView\b|\bfade-?in-?up\b|\bfadeInUp\b|\bfade-up\b|\bslide-up\b|\breveal-on-scroll\b|\bScrollReveal\b|\banimate-(?:fade|slide)-(?:in|up)\w*",
         "everything fading up on scroll: static; at most one short entrance for the main content"),
    Rule("count-up", "motion", r"\b(?:react-)?countup(?:\.js)?\b|\bCountUp\b|\buseCountUp\b|\bdata-count(?:-to|up)?=",
         "numbers counting up: show the final number"),
    Rule("caps-label", "type", r">\s*[A-ZÁÉÍÓÚÑ]{3,}(?:\s+[A-ZÁÉÍÓÚÑ]{2,}){0,3}\s*<",
         "3+ uppercase labels in the markup (FEATURES, OUR MISSION): delete the ones that repeat their heading; keep at most one, sentence case", flags=0, min_count=3),
    Rule("dot-facts", "copy", r">[^<]*\S\s·\s[^<]*\S\s·\s[^<]*<",
         "facts strung with middle dots (5 min read · Design · 2026): one fact, or a short sentence", min_count=2),
    Rule("instruction-copy", "copy", r"\bClick (?:the|this|on the) [\w ]{1,25} (?:to|below)\b|\bHaz clic en (?:este|esta|el|la)\b|\b(?:Pulsa|Toca|Presiona) (?:este|esta|el|la) [\w ]{1,20} para\b|\bClique (?:no|neste|na) [\w ]{1,20} para\b",
         "copy that explains how to use a control: delete; the control explains itself"),
    Rule("photo-veil", "visuals", r"::?(?:after|before)\s*\{[^}]*background(?:-color)?:\s*(?:rgba\(\s*\d{1,2}\s*,\s*\d{1,2}\s*,\s*\d{1,2}\s*,\s*0?\.[5-9]\d*\)|#[0-3][0-9a-fA-F][0-3][0-9a-fA-F][0-3][0-9a-fA-F][89a-fA-F][0-9a-fA-F])|\b(?:after|before):bg-black/(?:[5-9]0)\b",
         "dark veil over a photo: show the photo; a scrim only behind text that needs it"),
    Rule("faint-hex", "color", r"(?<![\w-])color:\s*#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b",
         "light grey text: on a light surface it fails contrast (4.5:1 body); darker, bigger, or cut it (fine on a dark band)",
         keep=lambda m: faint_grey(m.group(1))),
    Rule("faq-accordion", "layout", r"<details\b|\b(?:Accordion(?:Item|Trigger)?|accordion-item)\b",
         "FAQ accordion in the template lineup: answer the two or three real questions in the page, open", min_count=3),
    # 9. Motion
    Rule("loop-anim", "motion", r"\banimate-(?:pulse|ping|bounce|spin|float)\b|animation:[^;]*\binfinite\b",
         "looping animation: static, unless it marks something live or loading"),
    Rule("bounce-easing", "motion", r"cubic-bezier\(([^)]*)\)|ease(?:In|Out|InOut)?(?:Bounce|Elastic)\b|\b(?:bounce|elastic)\.(?:out|in)\b|\bbounce:\s*0?\.[3-9]",
         "bounce or overshoot easing: one ease-out curve (quart, quint, expo)",
         keep=lambda m: m.group(1) is None or overshoots(m.group(1))),
    Rule("blink-cursor", "motion", r"animation:[^;\n]*\bblink\b|\banimate-blink\b|@keyframes\s+blink\b",
         "blinking fake cursor: static text; real inputs draw their own caret"),
    Rule("marquee", "motion", r"<marquee\b|\banimate-(?:marquee|scroll|infinite-scroll)\b|@keyframes\s+(?:marquee|scroll-x|scroll-left)\b",
         "auto-scrolling row: alone it proves nothing; flag it only next to another motion sign"),
    Rule("transition-all", "motion", r"\btransition-all\b|transition:\s*all\b",
         "transition-all: name the properties (colors, opacity, transform)"),
    Rule("hover-lift", "motion", r"hover:(?:scale-1\d\d|-?translate-y-[-\d\[]|-translate-y)|:hover\s*\{[^}]*transform:\s*(?:translateY\(\s*-|scale\(\s*1\.(?:0[2-9]|[1-9]))",
         "hover lift or scale on cards: color or surface change on hover, tiny scale-down on press"),
    Rule("layout-anim", "motion", r"transition(?:-property)?:\s*[^;]*\b(?:width|height|top|left|margin)\b",
         "animating layout properties: use transform and opacity"),
    # 10. Fingerprints
    Rule("builder-fingerprint", "fingerprints", r"--(?:primary-glow|gradient-primary|shadow-elegant|transition-smooth)\b|lovable-uploads|\blovable(?:project)?\.(?:app|com)\b|\bbolt\.host\b|Edit with Lovable|\bdata-lov-|cdn\.tailwindcss\.com|<!--\s*[\w ]{0,30}\bSection\s*-->|\{/\*\s*[\w ]{0,30}\bSection\s*\*/\}",
         "builder leftover: own domain, renamed tokens with own values, no badge, no CDN, no section comments"),
    Rule("default-title", "fingerprints", r"<title>\s*[a-z0-9]+(?:-[a-z0-9]+)+\s*</title>|<title>\s*(?:Vite \+ React(?: \+ TS)?|React App|Create Next App|Lovable App)\s*</title>",
         "default title: the business name and what the page is", flags=0),
    Rule("recipe-fingerprint", "fingerprints", r"picsum\.photos|\$45[,.]231(?:[.,]89)?|\+20[.,]1% from last month|\+180[.,]1%|\+201 since last hour|\brounded-\[2(?:\.5)?rem\]|-15px_rgba\(0,\s*0,\s*0,\s*0?\.05\)|\b47\.2%|\(312\) 847-1928",
         "skill recipe shipped verbatim: a value decided for this product"),
    Rule("placeholder-asset", "fingerprints", r"\b(?:hero-image|feature-\d|testimonial-avatar|placeholder)\.(?:png|jpe?g|svg|webp|avif)\b|\bhref=[\"']#[\"']|<img\b(?![^>]*\bsrc\s*=)[^>]*>|<img\b[^>]*\bsrc=[\"']\s*[\"']",
         "placeholder asset or dead link: real asset or target, or list it in the report"),
]

MARKUP_EXT = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro", ".mdx"}


def line_of(content: str, pos: int) -> int:
    return content.count("\n", 0, pos) + 1


def markup_checks(content: str, name: str) -> list:
    """Whole-file checks for markup: skipped heading levels, hero-sized SVG scenes."""
    hits, prev = [], None
    for m in re.finditer(r"<h([1-6])\b", content, re.IGNORECASE):
        level = int(m.group(1))
        if prev is not None and level > prev + 1:
            hits.append(Hit(name, line_of(content, m.start()), "skipped-heading", "components",
                            f"h{prev} then h{level}", "heading levels skip: use the next level down"))
        prev = level
    for m in re.finditer(r">\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ ]{2,40}?)\s*<(?:/[a-z0-9]+>\s*<)?[^>]*>\s*([^<]{3,80})<", content):
        label, heading = m.group(1).strip().lower(), m.group(2).strip().lower()
        if label and heading.startswith(label) and heading != label:
            hits.append(Hit(name, line_of(content, m.start()), "label-repeats-heading", "type", f"{m.group(1).strip()} / {m.group(2).strip()[:60]}",
                            "label that repeats its heading: delete the label"))
    for m in re.finditer(r"<form\b.*?</form>", content, re.IGNORECASE | re.DOTALL):
        form = m.group(0)
        fields = re.findall(r"<(?:input|select|textarea|Input|Select|Textarea)\b(?![^>]*type=[\"'](?:hidden|submit|button|checkbox|radio)[\"'])[^>]*>", form)
        if len(fields) >= 4 and re.search(r"newsletter|subscrib|suscrib|bolet[ií]n|inscrev", form, re.IGNORECASE):
            hits.append(Hit(name, line_of(content, m.start()), "long-newsletter-form", "components", f"newsletter form with {len(fields)} fields",
                            "newsletter asks for one field: the email"))
        required = [f for f in fields if re.search(r"\brequired\b|aria-required=[\"']true", f)]
        if len(fields) >= 3 and len(required) == len(fields):
            hits.append(Hit(name, line_of(content, m.start()), "all-required", "components", f"all {len(fields)} fields required",
                            "every field required: ask only what you need; mark the optional ones"))
    for m in re.finditer(r"<svg\b.*?</svg>", content, re.IGNORECASE | re.DOTALL):
        shapes = len(re.findall(r"<(?:circle|rect|ellipse|polygon|path|line|polyline)\b", m.group(0), re.IGNORECASE))
        if shapes >= 25:
            hits.append(Hit(name, line_of(content, m.start()), "svg-scene", "visuals", f"inline SVG with {shapes} shapes",
                            "a picture built from primitive shapes reads as clip art: real artwork or a photo (icons and diagrams are fine)"))
    return hits


def file_checks(content: str, name: str) -> list:
    """Whole-file checks for HTML documents: missing metadata."""
    m = re.search(r"<head\b", content, re.IGNORECASE)
    if not m:
        return []
    line = line_of(content, m.start())
    hits = []
    if not re.search(r"<meta[^>]+name=[\"']description[\"']", content, re.IGNORECASE):
        hits.append(Hit(name, line, "missing-description", "fingerprints", "<head> without meta description",
                        "write a description (up to 160 characters) from facts on the page"))
    if not re.search(r"<meta[^>]+property=[\"']og:image[\"']", content, re.IGNORECASE):
        hits.append(Hit(name, line, "missing-social-image", "fingerprints", "<head> without og:image",
                        "add a social image (1200x630); if none exists, list it under Not checked"))
    return hits

TEXT_RULES = [
    Rule("inflated-word", "words", r"\b(?:delv\w*|foster\w*|leverag\w*|utiliz\w*|facilitat\w*|empower\w*|streamlin\w*|robust|seamless\w*|cutting[- ]edge|game[- ]?changer|paradigm shift|tapestr\w*|realm|beacon|multifaceted|meticulous\w*|intricate|pivotal|paramount|transformative|elevat\w*|embark\w*|supercharg\w*|harness(?:ing)? the (?:power|potential)|revolutioni[sz]\w*|ever[- ]evolving|testament|potenciar|sinergia\w*|disruptiv\w*|hol[ií]stic\w*|de vanguardia|sin precedentes|alavanc\w*|potencializ\w*)\b",
         "inflated word: use the plain word"),
    Rule("opener", "openers", r"(?:here'?s the thing|let me be clear|let'?s dive in|in today'?s (?:fast-paced |digital )?world|in the age of|when it comes to|it'?s worth noting|it'?s important to note|en el mundo actual|hoy en d[ií]a|cabe destacar|es importante destacar|vale ressaltar|most people don'?t know|nobody talks about)",
         "throat-clearing opener: start with the point"),
    Rule("contrast-frame", "contrast", r"\b(?:it'?s|this is|that'?s)\s+not\s+(?:just\s+|about\s+|only\s+)?[^.!?\n]{1,60}[,;.]\s*(?:it'?s|it is|this is)\b|\bnot (?:just|only) [^.!?\n]{1,50},? but\b|\bno (?:es|era|son|eran|fue|fueron|se trata de) (?:solo |s[oó]lo )?[^.!?\n]{1,60}[,;.]\s*(?:es|era|son|eran|fue|fueron|se trata de)\b|\bno (?:es|son|era|eran) (?:solo|s[oó]lo|solamente|[uú]nicamente)\b|\bno solo [^.!?\n]{1,50}sino\b|\bit'?s not just\b|\bn[ãa]o [ée] (?:s[oó] |apenas )?[^.!?\n]{1,60}[,;.]\s*[ée]\b|\bmais (?:do )?que apenas\b|\bless [^.!?\n]{1,30}, more\b",
         "contrast framing: state the positive claim directly"),
    Rule("staged-reveal", "reveals", r"(?:what nobody tells you|the part (?:everyone|most people) (?:miss|skip)\w*|what most people get wrong|what if i told you|think about it:|plot twist:|the best part:|here'?s why:|the result\?|the secret\?)",
         "staged reveal: cut the setup and make the claim"),
    Rule("puffery", "puffery", r"(?:stands as a testament|marks a pivotal|plays a (?:vital|crucial|key) role|underscor\w+ (?:its|the) (?:importance|significance)|experts agree|studies show|many argue|widely regarded|seg[uú]n (?:los )?expertos|diversos estudios)",
         "puffery or weasel attribution: state the fact or name the source"),
    Rule("llm-connector", "rhythm", r"(?:^|[.!?]\s+)(?:Moreover|Furthermore|Additionally|In addition|Adem[aá]s|Asimismo|Por otro lado|Al[eé]m disso|Ademais),",
         "LLM connector: start with the subject or merge the sentences", flags=re.MULTILINE),
    Rule("fragments", "rhythm", r"(?:^|[.!?]\s)(?:[A-ZÀ-ÝÑ¿¡][^.!?\n]{0,25}\.\s){3,}",
         "stacked short fragments: write full sentences", flags=re.MULTILINE),
    Rule("metadiscourse", "metadiscourse", r"(?:matters more than it sounds|the key (?:point|takeaway|thing) is|as you can see|this distinction matters|in other words|dicho de otro modo|como podemos ver|en otras palabras)",
         "metadiscourse: delete, or add support"),
    Rule("recap-ending", "endings", r"^[ \t]*(?:In conclusion|Ultimately|Overall|To sum up|En resumen|En conclusi[oó]n|En definitiva|Em resumo)\b",
         "recap ending: end on the last concrete point or next action", flags=re.MULTILINE | re.IGNORECASE),
    Rule("em-dash", "punctuation", r"—|(?<=\S)[ ]–[ ]|(?<=\S)[ ]--?[ ](?=\S)",
         "em dash or spaced dash: period, comma, colon or parentheses (none in short copy)", flags=0),
    Rule("emoji-heading", "punctuation", r"^#{1,6}\s.*" + EMOJI + r"|^\s*[-*]\s*" + EMOJI,
         "emoji in heading or bullet: remove", flags=re.MULTILINE),
    Rule("stacked-without", "contrast", r"\b(?:sin|without|sem)\s+[\wáéíóúñ]+,\s*(?:sin|without|sem)\s+[\wáéíóúñ]+",
         "stacked \"without X, without Y\": name the one thing that is actually gone"),
    Rule("hype-text", "words", r"\b(?:unlock\w*|this changes everything|this is huge|next[- ]level|desbloque\w*|el poder de|al siguiente nivel|ya est[aá] aqu[ií])\b",
         "hype: say what it does"),
]


@dataclass
class Hit:
    file: str
    line: int
    rule: str
    category: str
    excerpt: str
    hint: str


def iter_files(paths, force_text):
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            yield p
        elif p.is_dir():
            try:
                files = sorted(p.rglob("*"))
            except OSError:
                continue
            for f in files:
                if any(part in SKIP_DIRS for part in f.parts):
                    continue
                try:
                    is_file = f.is_file()
                except OSError:
                    continue
                if is_file and (force_text or f.suffix.lower() in CODE_EXT | TEXT_EXT):
                    yield f


def read(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in data[:4096] and not data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return None
    for enc in ("utf-8-sig", "utf-16", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return None


def strip_code_blocks(text: str) -> str:
    """Blank out fenced and inline code in prose so examples do not count, keeping line numbers."""
    text = re.sub(r"^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1", lambda m: "\n" * m.group(0).count("\n"),
                  text, flags=re.DOTALL | re.MULTILINE)
    return re.sub(r"(`+)[^`\n]+?\1", "", text)


def scan_text(content: str, rules, name: str) -> list[Hit]:
    hits = []
    for rule in rules:
        rx = rule.compiled()
        found, seen, total = [], set(), 0
        for m in rx.finditer(content):
            if rule.keep is not None and not rule.keep(m):
                continue
            total += 1
            line = content.count("\n", 0, m.start()) + 1
            if line in seen:
                continue
            seen.add(line)
            start = content.rfind("\n", 0, m.start()) + 1
            end = content.find("\n", m.end())
            excerpt = content[start: end if end != -1 else len(content)].strip()
            found.append(Hit(name, line, rule.id, rule.category, excerpt[:160], rule.hint))
        if found and total >= rule.min_count:
            if rule.min_count > 1:
                first = found[0]
                first.excerpt = f"{total} occurrences, first: {first.excerpt}"
                hits.append(first)
            else:
                hits.extend(found)
    return hits


def scan(paths, force_text=False):
    hits, scanned = [], 0
    for f in iter_files(paths, force_text):
        content = read(f)
        if content is None:
            continue
        scanned += 1
        is_text = force_text or f.suffix.lower() in TEXT_EXT
        rules = TEXT_RULES if is_text else UI_RULES
        body = strip_code_blocks(content) if is_text else content
        hits.extend(scan_text(body, rules, str(f)))
        if not is_text and f.suffix.lower() in MARKUP_EXT:
            hits.extend(markup_checks(content, str(f)))
            hits.extend(file_checks(content, str(f)))
    return hits, scanned


def main(argv=None):
    ap = argparse.ArgumentParser(description="Find candidate AI-slop signs. Candidates, not verdicts.")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--text", action="store_true", help="apply writing rules to every file")
    ap.add_argument("--json", action="store_true", help="print JSON")
    args = ap.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):  # Windows consoles (cp1252) cannot print emoji excerpts
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")

    hits, scanned = scan(args.paths, args.text)
    if scanned == 0:
        print("NOT SCANNED: no readable code or text files in the given paths", file=sys.stderr)
        return 2

    categories = sorted({h.category for h in hits})
    if args.json:
        print(json.dumps({"scanned": scanned, "categories": categories, "hits": [asdict(h) for h in hits]}, ensure_ascii=True, indent=2))
    else:
        for h in hits:
            print(f"{h.file}:{h.line} [{h.category}/{h.rule}] {h.excerpt}\n    -> {h.hint}")
        print(f"\n{len(hits)} candidate(s) in {scanned} file(s); categories: {', '.join(categories) or 'none'}")
        print("Candidates, not verdicts. Zero hits does not mean no slop: hierarchy, rhythm and meaning need a render and your eyes.")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
