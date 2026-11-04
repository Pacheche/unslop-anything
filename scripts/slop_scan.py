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
        r"impulsad[oa] por IA|potenciad[oa] por IA|alavanc\w*|sem esfor[cç]o|movid[oa] a IA")

EMOJI = r"[\U0001F300-\U0001FAFF☀-➿⭐⭕✨]"
HUES = r"(?:purple|violet|indigo|fuchsia|pink|blue|cyan|sky|teal|emerald|rose|orange|amber)"


def off_grid(value) -> bool:
    n = int(value)
    return n > 2 and n % 4 != 0


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
    Rule("backdrop-blur", "color", r"backdrop-blur|backdrop-filter:\s*blur",
         "glass blur: keep only when something real sits behind it (overlay, sticky header over content)"),
    # 2. Type
    Rule("heavy-weight", "type", r"\bfont-(?:extrabold|black)\b|font-weight:\s*(?:800|900)\b",
         "800-900 weight: use 400-500 and size for hierarchy"),
    Rule("tracked-caps", "type", r"\buppercase\b[^\n\"'`]*\btracking-(?:wide|wider|widest|\[0?\.\d+em\])|\btracking-(?:wide|wider|widest|\[0?\.\d+em\])[^\n\"'`]*\buppercase\b|text-transform:\s*uppercase[^}]*letter-spacing:\s*0?\.[05-9]|letter-spacing:\s*0?\.[05-9][^}]*text-transform:\s*uppercase",
         "uppercase tracked label: sentence case, normal tracking"),
    # 3. Icons and emoji
    Rule("emoji", "icons", EMOJI, "emoji in UI: replace with one line icon set, or nothing (user content is fine)", flags=0),
    Rule("arrow-glyph", "icons", r"[←-⇿⟰-⟿⤀-⥿➜-➾]",
         "arrow glyph in text: use a library chevron icon or plain text", flags=0),
    # 4. Spacing
    Rule("off-grid-tw", "spacing", r"(?<![\w-])-?(?:[mp][trblxyse]?|gap(?:-[xy])?|space-[xy]|inset(?:-[xy])?|top|left|right|bottom|h|min-h)-\[(\d+)px\]",
         "off-grid arbitrary value: use a 4px step", keep=lambda m: off_grid(m.group(1))),
    Rule("off-grid-css", "spacing", r"\b(?:margin|padding|gap|row-gap|column-gap)(?:-(?:top|right|bottom|left|inline|block))?:\s*([^;}\n]+)",
         "off-grid spacing: use a 4px step", keep=lambda m: any(off_grid(n) for n in re.findall(r"(\d+)px", m.group(1)))),
    # 5. Copy
    Rule("greeting", "copy", r"(?:Welcome back|Good (?:morning|afternoon|evening)|Hey|Hi|Hello|Morning|Bienvenid[oa] de nuevo|Hola|Bem-vind[oa] de volta|Ol[áa])\s*,?\s+\{?[\w.$]+\}?\s*!",
         "greeting headline: title the context (page or period) instead"),
    Rule("exclamation", "copy", r">(?:[^<{}\n]|\{[^{}\n]*\})*[A-Za-zÀ-ÿ0-9}](?:[^<{}\n]|\{[^{}\n]*\})*!+\s*<|!!(?=\s*[\"'`<)\n]|\s*$)",
         "exclamation in interface text: plain statement"),
    Rule("wordy-placeholder", "copy", r"placeholder=[\"'][^\"']*(?:anything|whatever|cualquier cosa|qualquer coisa)[^\"']*[\"']",
         "wordy placeholder: one word like Search"),
    Rule("hype-ui", "copy", rf"\b(?:{HYPE})\b",
         "hype word: say what it does"),
    Rule("unverified-claim", "copy", r"\b(?:trusted|loved|used)\s+by\s+[\d,.]+\s*[kKmM+]*|\b(?:m[aá]s de|mais de)\s+[\d,.]+\s*[kKmM]?\+?\s+(?:usuarios|usu[aá]rios|clientes|equipos|equipes|empresas)\b|\b\d+x\s+faster\b|\b[\d,.]+\s*[kKmM]?\+\s+(?:users|teams|customers|companies|clientes|usuarios)\b",
         "unverifiable claim: confirm with the user, then make it specific or remove it"),
    Rule("intro-badge", "layout", r"(?:Introducing|Announcing|Presentamos|Nuevo|New)\b[^<\n]{0,40}(?:2\.0|v\d|✨|🚀)",
         "pill badge above the headline: remove, or a quiet text link if it is real news"),
    Rule("em-dash-ui", "copy", r">(?:[^<{}\n]|\{[^{}\n]*\})*\s[—–]\s(?:[^<{}\n]|\{[^{}\n]*\})*<|(?:title|label|placeholder|alt|aria-label|description)\s*[=:]\s*[\"'`][^\"'`\n]*\s—\s",
         "em dash in UI copy: period, comma or line break", flags=0),
    # 6. Components
    Rule("pill-everything", "components", r"\brounded-full\b|border-radius:\s*(?:9{3,}|100vmax|[1-9]\d{2,}px)",
         "many full pills: radius by size; pills only for chips, segmented controls, avatars", min_count=6),
    Rule("dot-grid", "visuals", r"radial-gradient\([^)]*\b1px\b[^)]*\)[^;\n]*;?\s*background-size|bg-\[radial-gradient",
         "dot grid background: plain background"),
    # 9. Motion
    Rule("loop-anim", "motion", r"\banimate-(?:pulse|ping|bounce|spin)\b|animation:[^;]*\binfinite\b",
         "looping animation: static, unless it marks something live or loading"),
    Rule("transition-all", "motion", r"\btransition-all\b|transition:\s*all\b",
         "transition-all: name the properties (colors, opacity, transform)"),
    Rule("hover-lift", "motion", r"hover:(?:scale-1\d\d|-?translate-y-[-\d\[]|-translate-y)",
         "hover lift or scale on cards: color or surface change on hover, tiny scale-down on press"),
    Rule("layout-anim", "motion", r"transition(?:-property)?:\s*[^;]*\b(?:width|height|top|left|margin)\b",
         "animating layout properties: use transform and opacity"),
]

TEXT_RULES = [
    Rule("inflated-word", "words", r"\b(?:delv\w*|foster\w*|leverag\w*|utiliz\w*|facilitat\w*|empower\w*|streamlin\w*|robust|seamless\w*|cutting[- ]edge|game[- ]?changer|paradigm shift|tapestr\w*|realm|beacon|multifaceted|meticulous\w*|intricate|pivotal|paramount|transformative|elevat\w*|embark\w*|supercharg\w*|harness(?:ing)? the (?:power|potential)|revolutioni[sz]\w*|ever[- ]evolving|testament|potenciar|sinergia\w*|disruptiv\w*|hol[ií]stic\w*|de vanguardia|sin precedentes|alavanc\w*|potencializ\w*)\b",
         "inflated word: use the plain word"),
    Rule("opener", "openers", r"(?:here'?s the thing|let me be clear|let'?s dive in|in today'?s (?:fast-paced |digital )?world|in the age of|when it comes to|it'?s worth noting|it'?s important to note|en el mundo actual|hoy en d[ií]a|cabe destacar|es importante destacar|vale ressaltar|most people don'?t know|nobody talks about)",
         "throat-clearing opener: start with the point"),
    Rule("contrast-frame", "contrast", r"\b(?:it'?s|this is|that'?s)\s+not\s+(?:just\s+|about\s+|only\s+)?[^.!?\n]{1,60}[,;.]\s*(?:it'?s|it is|this is)\b|\bnot (?:just|only) [^.!?\n]{1,50},? but\b|\bno es (?:solo |s[oó]lo )?[^.!?\n]{1,60}[,;.]\s*es\b|\bno solo [^.!?\n]{1,50}sino\b|\bn[ãa]o [ée] (?:s[oó] |apenas )?[^.!?\n]{1,60}[,;.]\s*[ée]\b|\bmais (?:do )?que apenas\b|\bless [^.!?\n]{1,30}, more\b",
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
    Rule("hype-text", "words", r"\b(?:unlock\w*|this changes everything|this is huge|next[- ]level)\b",
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
        found, seen = [], set()
        for m in rx.finditer(content):
            if rule.keep is not None and not rule.keep(m):
                continue
            line = content.count("\n", 0, m.start()) + 1
            if line in seen:
                continue
            seen.add(line)
            start = content.rfind("\n", 0, m.start()) + 1
            end = content.find("\n", m.end())
            excerpt = content[start: end if end != -1 else len(content)].strip()
            found.append(Hit(name, line, rule.id, rule.category, excerpt[:160], rule.hint))
        if len(found) >= rule.min_count:
            if rule.min_count > 1:
                first = found[0]
                first.excerpt = f"{len(found)} occurrences, first: {first.excerpt}"
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
    return hits, scanned


def main(argv=None):
    ap = argparse.ArgumentParser(description="Find candidate AI-slop signs. Candidates, not verdicts.")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--text", action="store_true", help="apply writing rules to every file")
    ap.add_argument("--json", action="store_true", help="print JSON")
    args = ap.parse_args(argv)

    hits, scanned = scan(args.paths, args.text)
    if scanned == 0:
        print("NOT SCANNED: no readable code or text files in the given paths", file=sys.stderr)
        return 2

    categories = sorted({h.category for h in hits})
    if args.json:
        print(json.dumps({"scanned": scanned, "categories": categories, "hits": [asdict(h) for h in hits]}, ensure_ascii=False, indent=2))
    else:
        for h in hits:
            print(f"{h.file}:{h.line} [{h.category}/{h.rule}] {h.excerpt}\n    -> {h.hint}")
        print(f"\n{len(hits)} candidate(s) in {scanned} file(s); categories: {', '.join(categories) or 'none'}")
        print("Candidates, not verdicts. Zero hits does not mean no slop: hierarchy, rhythm and meaning need a render and your eyes.")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
