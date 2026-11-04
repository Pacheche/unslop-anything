# UI signs of slop

Ten categories. In an audit, write one line per sign found: sign, where it lives, fix. File each sign under the first category that lists it. The slop level is the number of categories with at least one sign, times 10%. In category 10, builder fingerprints always count; the template-look signs count only when categories 1-9 are empty.

One sign proves nothing. Careful sites use a small uppercase label or a dot background too. What gives a page away is the pile-up, and the sense that nobody chose any of it. The strongest single sign is not a color: it is a page where no default was ever changed.

`[scan]` marks signs that `scripts/slop_scan.py` can find in code. Everything else needs your eyes on a render.

## 1. Color and surfaces

- Violet-to-blue, violet-to-pink or any hue-to-hue gradient on backgrounds, cards, buttons or the active nav item `[scan]` → one neutral surface; the accent only where it means something.
- Gradient text in headings, numbers or the logo `[scan]` → solid primary text.
- Colored glows and colored shadows (`shadow-[0_0_20px_rgba(139,92,246,.5)]`, `drop-shadow` on icons) `[scan]` → remove; depth from surface steps and hairlines.
- Radial washes, blurred blobs, nebulas or a glow ring behind content → remove.
- Neon or saturated borders → hairline in the text color at 6-10% opacity.
- Every card a different saturated color (green sleep card, red heart card, orange calories bar) → neutral cards; color only on the value that matters or on a status.
- Five near-identical tints for text (five lavenders) → three text roles from one ramp.
- Everything highlighted, so nothing leads → one accent, used once or twice per screen.
- `backdrop-blur` / glass on cards with nothing behind them `[scan]` → plain raised surface.
- Drop shadows on cards that sit on a dark grey page, shadows that escape a clipped mockup → remove the shadow, use a subtle border or a lighter surface; clip what overflows.
- The stock palette as the brand: Tailwind's `indigo-600` button, `violet-500`, `slate-900`; shadcn's neutral greys plus one accent at 500-600 (green, orange or blue) on every icon → a color decided from the product's world, written down as tokens. The restrained look is still a default if every value is stock.
- The newer "tasteful" defaults: cream page, serif headline and a terracotta or sage accent; near-black with one acid accent (`lime-400`); cyan or neon on black because the product is "for developers" → only when the direction leads there, never as the safe alternative to purple.
- Over-correction: everything grey, primary action invisible, data unreadable → bring back an accent and status colors with meaning.

## 2. Type

- Headings at 800-900 weight `[scan: 800-900]`, or 700 on every heading and label → 400-600, hierarchy from size and color. Platform styles (iOS Large Title) and an existing design system keep their weights.
- Small `UPPERCASE` tracked labels above headings or in nav (`FEATURES`, `PAID THIS MONTH`) `[scan: 3+ per file]`. One is fine; three or more, same size and tracking, is the sign → delete every label that repeats its heading; keep at most one that adds a fact (a date, a category), in sentence case, normal tracking, grey, slightly smaller than body.
- A label that repeats its heading (`OUR MISSION` over "Our mission is simple") → delete the label.
- Too many sizes and weights on one screen → a few sizes from a scale, two weights.
- Numbers in mixed formats (`$48,210` next to `$124,860.40`, `07`) → one format, `tabular-nums`.
- Money or plain numbers set in mono for decoration → proportional with `tabular-nums`; mono only for IDs, hashes, commands, code.
- Negative tracking on small text, or display tracking tighter than -0.04em `[scan]` → zero on small text; -0.02 to -0.04em on display.
- Body text under 12px or UI text (links, buttons, labels, table cells) under 11px `[scan]`; justified text in narrow columns `[scan]` → 14-16px body, 11px floor for functional text, left-aligned.
- A thin serif headline with one word in italics, the "editorial" look models fall back to when asked for something different → a type decision from the direction; one emphasis device, if any.
- One highlighted or colored word in the headline → let the sentence carry the emphasis.
- A landing headline that is too small, so nothing leads: on weak sites the biggest text sits near 5vw (72px at 1440); on strong ones near 8vw (about 120px) → make the top step far above everything else and the sentence short (see `ui-passes.md`). Apps and dashboards are different: their lead is the data.
- A five-line headline, Title Case On Every Word, facts strung with middle dots (`Design · Code · Strategy`), monospace as a tech costume (`[ SYSTEM_READY ] // v1.0.4`) → a short sentence in sentence case; mono only for real code and IDs.
- No type scale: sizes picked ad hoc, or every size straight from the framework's default list → six sizes of your own.
- Subtitle font so small it does not read; a light grey that fails contrast → bigger, darker, or cut the subtitle.
- Ragged two-line headlines and subtitles with a one-word last line → `text-wrap: balance` (headings) or `pretty` (paragraphs).
- An unchosen default typeface on a product whose character is different: Inter, Geist and the system font; the usual Google picks (Poppins, Plus Jakarta Sans, Space Grotesk, Instrument Sans/Serif); and the fonts anti-slop skills hand out (Satoshi, Outfit, Cabinet Grotesk) `[scan]` → pick a family for the character and write down why (see `ui-passes.md`). Any of them is fine when it was chosen for this product.

## 3. Icons and emoji

- Emoji as nav icons, status, label decoration or in buttons (🏠 🚀 💰 🔥 ⚠️ ✨) `[scan]` → one line icon set, or nothing.
- Colored icons, each one a different hue, often inside pastel tiles or bubbles → icons in the text color (secondary or muted); category color, if needed, as a small dot.
- A sparkle, wand or star for anything "AI", purple as the AI color → remove, or a plain icon only where it explains the action. Show what the AI produces.
- Icons in several sizes, strokes and families → one family, one size (16-20px in web UI), one stroke.
- Icons hand-drawn as inline SVG paths next to library icons → import from the library; a hand glyph never matches its neighbors.
- An icon tile above every heading or card (an icon in a small colored square) → drop the tile; an icon only where it helps scanning.
- A sparkle, bolt or Lucide glyph in a gradient square as the logo → the name set in type, plus a real mark if one exists.
- A check mark before every list item, an arrow after every link, or the arrow in its own circle flush against the button edge → plain items and labels; one arrow where it means "go".
- Arrow glyphs in text (`View all →`, `Next ➜`) `[scan]` → a library chevron icon, or plain text.
- Icons nudged off the column → same icon box width in every row, fixed gap to the label.

## 4. Spacing and alignment

- One-off arbitrary values (`mt-[13px]`, `py-[11px]`, `padding: 13px`) `[scan]` → a step of the project's scale.
- Every margin and size straight from the framework's default list, with the same gap between everything: the most reliable sign of an untouched page → a small scale of your own (6-8 spacing values, see `ui-passes.md`), close inside groups and far between them.
- Same kind of thing, different size: rows with different heights, sibling cards with different padding → one height, one padding.
- Uniform spacing everywhere (`space-y-4` on everything) → tight inside a group, open between groups; each level roughly double the one inside it.
- Inverted proximity: a label closer to the section above than to its own items → label close to what it names.
- Section widths and side margins that change from section to section → one max width, one page gutter.
- Text touching a neighboring box, or 1-3px near-tangents that look like accidents → at least 8px or a deliberate overlap.
- A big empty band above a section and cramped space below it → balanced rhythm.
- Things off the line: icons, labels and numbers not in their own aligned columns → align them; numbers right-aligned in one column.

## 5. Copy inside the UI

- Greeting headlines (`Welcome back, Damir! 👋`, `Hey Mike! 💪`) `[scan]` → the context as the title: page name or period (`October 2026`).
- Exclamation marks, `!!`, hype in labels ("Keep pushing!!", "You're absolutely crushing it!") `[scan]` → plain statements.
- Changes without a reference (`+12%!!`, `3 less!!`) → `+12% vs last month`, `3 fewer than last week`.
- Wordy placeholders (`Search anything...`, `Ask AI Coach anything...`) `[scan]` → `Search`.
- Hype words: supercharge, seamless, unlock, magic, revolutionize, effortless, AI-powered everywhere `[scan]` → what the thing does.
- A headline that promises instead of saying what this is ("The all-in-one platform to grow your business") → what the visitor gets and who it is for ("Appointment booking for barbershops, with WhatsApp reminders"). Read it aloud: if a stranger cannot tell what you sell, nothing lower down saves it.
- A subline that repeats the headline in other words ("Work smarter. A smarter way to get work done.") → a line that adds a fact.
- Template lines: "Everything you need, in one place", "The future of X is here", "Why choose us?", "No fluff. Just results.", "Fast. Simple. Secure.", "Take your business to the next level", "No more X theater" `[scan]` → a fact about this product.
- Buttons that say nothing (`Get started`, `Learn more`, `Submit`) → the action the person wants (`Book a table`, `See pricing`, `Get directions`).
- Adjectives where a fact exists ("quality ingredients", "a unique experience") → the name, number or rule (the supplier, the price per gram, "guests leave by 10pm").
- Live-ness and urgency nobody measured: "Updated 2 minutes ago · 1,284 online", "Only 3 spots left!", a countdown that resets on reload `[scan]` → real values or nothing.
- Talking like the system, not the person ("Configure webhook endpoints" where the goal is "Get notified when an order ships"); "Oops! Something went wrong" → the person's goal; an error that says what happened and what to do.
- Trailing periods on labels, buttons, titles → none. Paragraphs keep them.
- Em dashes and decorative separators (` — `, ` · `, ` | `) in UI strings `[scan]` → a period, a comma, a slash or a line break.
- `PRO`, `New ✨`, `Beta 🚀` badges everywhere → remove, or one quiet text badge where it is true.
- Fake-looking data: `$123,456`, `[X]`, `Lorem`, everyone named John Doe → plausible numbers and names.
- Unverifiable social proof (`Loved by 10,000+ teams`, five stars on every card, single-letter avatars and "+2,000", testimonials from "Sarah Johnson, CEO") → ask the user; make it specific or remove it. One real testimonial with a full name beats ten invented ones.
- Instructions next to a control that already explains itself ("Click the button below to start") → delete.
- A caption narrating what comes next ("Here are your stats") → delete.
- The same verb repeated on every item ("Add X", "Add Y", "Add Z") → keep it once or drop it.
- Labels that disagree with data or state ("Delete selected" with zero selected; "Excellent" on a mediocre score) → the label follows the state and the scale.

For longer copy (hero text, feature blurbs, emails inside the product), also run `references/writing.md`.

## 6. Components and data

- Everything a pill: search, buttons, cards, tags `[scan: counts rounded-full and huge border-radius]` → radius by size, nested radius math.
- Glowing count pills, plan pills, shortcut pills → quiet mono text, a plain number or a keycap.
- Initial-letter avatars (`MK`, `SC`) in testimonials or lists where real people exist → real photos, or no avatar.
- Tags and badges on everything (6+ per card) → only tags that filter or change a decision.
- Box inside box inside box, including the "double-bezel" card (faint shell, 1px ring, 6-8px padding, 32px corners, a second card inside) → one container level.
- A colored side border (`border-left` above 1px) on cards, list items, callouts or alerts, or a thick top border on a rounded card `[scan]`; a hairline border with a huge soft shadow on every card of a row `[scan]` → one surface treatment, from the ramp: a border or a shadow, not both.
- The hero-metric template: big number, tiny label, supporting stats, accent → the number only where it is the thing people come for, with its reference.
- Hard offset shadows (`box-shadow: 4px 4px 0`) outside a world that is really neobrutalist → a soft, offset elevation, or none.
- Section numbers (`01 / 02 / 03`) next to headings when the order carries no information `[scan]` → let the headings and the layout carry the sequence.
- "Trusted by" rows of made-up logos (Acme, Globex, Initech, Umbrella, Hooli) `[scan]` → real customers the user confirms, or nothing.
- Decorative product props: charts that measure nothing, a made-up terminal (`$ npm install magic`), a window full of grey bars → the real product with plausible data, or nothing.
- Every button primary; every form field required; six fields for a newsletter; a modal for everything → one primary per view, ask only what is needed, inline confirmation where a modal is overkill.
- A different-colored badge for every status → color only the states that need attention.
- Untouched shadcn/ui or component-library defaults: stock theme colors, the same radius on every corner, stock shadows → change the theme tokens (colors, radius, shadows), not each component.
- Dividers between everything → space groups things; lines only in dense tables and lists.
- Charts with rainbow bars inside one series, glowing or pill-shaped bars, uppercase day labels → one series color, muted grid, quiet labels, one highlight on the value that matters.
- Sparklines, mini bars and icons added to every stat card → label, number, change with its reference.
- Equal cards side by side with the same layout → one lead element, smaller supporting ones, varied widths.
- Spinners where the shape of the content is known → skeleton with the final geometry.
- `0.0%`, `NaN`, empty charts shown as if they were data; errors shown as "empty" → an honest empty state that says how to fill it; errors distinct from empty.
- A progress bar pinned at 100% red with "274.6%" → say how far over the limit it is.
- Logo as a gradient tile with a sparkle, a glossy orb, a gradient wordmark → the product name in the interface family, plus a flat one-color mark if one exists.
- Clickable elements without `cursor: pointer`, hover-only affordances on touch screens, no visible focus ring → fix the states.

## 7. Layout and composition

- Everything stacked and centered (badge, headline, text, two buttons, picture below) → an asymmetric split, or text over a large product view. Centered only for a short hero with no visual.
- A short hero that leaves a dead band before the next section → the first screen composed as a whole; the hero fills the viewport or the product view runs past the fold.
- A pill badge above the headline (`✨ Introducing X 2.0`) `[scan]` → remove, or a quiet text link if it is real news.
- Three or more buttons in the hero, chips and avatar rows stacked under them → one primary, at most one secondary.
- Visual weight all on one side, an empty quadrant on the other → balance the blocks or center short text against the visual.
- A final CTA that is flatter than the nav button → the last CTA is the strongest one on the page.
- An app shrunk into a narrow centered column on desktop → real app proportions: sidebar, fluid content, capped width.
- Layout structure copied from a template: three equal feature cards with an emoji, a bold title and a vague line → a list with one sentence per item, one concrete example with a screenshot, or a before and after.
- Every section on the same template (centered heading + grid), every block centered under the previous one → vary the shape: width, alignment, background, scale.
- The template lineup in the template order: hero, logo row, three features, how it works in 01/02/03, testimonials, three pricing tiers with the middle "Most popular", FAQ accordion, gradient CTA band, footer columns → in the report, name the sections the product does not need. Remove one only with the user's yes; never add one.
- Costumes: a bento grid by default, zigzag image/text rows, a newspaper broadsheet look, template neobrutalism, a floating pill navbar, a full-screen hero with a scroll cue, one narrow centered column on a wide screen → a structure that follows the content.

## 8. Visuals and imagery

- Nothing real at the top: no screenshot, photo, place or object that could only belong to this product → the product itself, or one concrete image from its world. Well-written text alone beats an image nobody chose.
- Glossy 3D blobs, orbs, liquid chrome, floating cubes, purple nebulas, aurora backgrounds as the hero visual → the product itself, or one concrete image from the product's world.
- Stock people smiling at a laptop; pastel isometric illustration; a made-up phone with grey screens; photos cropped into blobs or buried under a dark overlay → a real photo or the real UI, shown plainly.
- `picsum.photos` or grayscale stock made to "not look like stock" `[scan]` → real photos from the user, or a plain slot listed in the report.
- Images named after their section (`hero-image.png`, `feature-1.jpg`, `testimonial-avatar`) or an image that never loads `[scan]` → real assets with real names, or no image.
- Robots, glowing brains, circuit lines, holograms for anything AI → show what the AI produces.
- Generic flat clip-art illustration → an illustration with a point of view that belongs to the product's world (a train app gets the actual route and landscape, not a stock train).
- Text, fake buttons or a fake logo baked into an image → real text in the page, clean image.
- An image with a hard edge and a different black or white than the page → match the background and mask the edges.
- Dot grids, graph paper, hairline line grids, `repeating-linear-gradient` stripes, grain and noise as backgrounds `[scan]` → plain background, or a texture from the product's world (a grid only under a real canvas, map or blueprint).
- A colored radial glow or spotlight behind the hero, fading to transparent `[scan]` → a solid surface, or a lit material from the world.
- A hero-sized inline SVG assembled from piles of circles and rectangles, sketch or doodle SVG scenes, `feTurbulence` grain `[scan]` → real artwork or a photo, or no illustration. SVG for icons, diagrams and exact geometry is fine.
- A `clip-path` polygon with many points, or a circle mask, imitating a torn edge or a person's silhouette `[scan]` → a real cut-out or alpha matte from the image, or no mask. A dot or grid background alone proves nothing; count it only next to another sign here.
- A visual on every section → one visual where it helps, usually only the hero.

For making or fixing the images themselves, use `references/visual-design.md`.

## 9. Motion

- `animate-pulse`, `animate-ping`, `animate-bounce`, breathing glows on things that are not live `[scan]` → static.
- `transition-all` `[scan]` → name the properties: color, background, border, opacity, transform.
- `hover:scale-105`, `hover:-translate-y-1` on cards `[scan]` → a color or surface change on hover; a tiny scale-down on press.
- Bouncy springs, `bounce`/`elastic` easing and `cubic-bezier` curves that overshoot on simple UI `[scan]` → one ease-out curve (quart, quint or expo).
- A blinking text cursor in a hero where nothing can be typed `[scan]` → static text.
- Everything flying in on load, list items staggered by index forever → at most one short entrance for the main content.
- Parallax and elements floating on scroll → static layout.
- Everything fading up on scroll, numbers counting up, a blinking cursor in the headline, a spinning gradient border, logos scrolling forever → static; motion only where it answers something the visitor did.
- Animating width, height, top, left, margin or large blurs → transform and opacity.
- Abrupt slider or carousel cuts; popups whose close animation glitches → a short crossfade; test every open and close.

## 10. Template look and fingerprints

**Builder fingerprints** (always count). They are about provenance, not design, and they are almost never wrong. A visitor who recognizes them has made up their mind before reading.

- Default metadata: a `<title>` that is the hyphenated project name `[scan]`, no meta description or social image `[scan]`, the builder's favicon → a title and description written for each page, a social image, the brand's favicon.
- Builder leftovers: `lovable.app`, `lovableproject.com` or `bolt.host` domains, `/lovable-uploads/`, "Edit with Lovable" or "Made with" badges, Lovable's design variables (`--primary-glow`, `--gradient-primary`, `--shadow-elegant`, `--transition-smooth`), section comments (`<!-- Hero Section -->`), Tailwind loaded from its CDN in production `[scan]` → the user's domain, renamed tokens with their own values, no badge, no CDN.
- Leftover sample copy, links to `#`, half-built sections `[scan: href="#"]` → finish, link or remove (removing a section needs the user's yes).
- Recipes from anti-slop skills pasted verbatim: `rounded-[2rem]` or `rounded-[2.5rem]` on every container, `shadow-[0_20px_40px_-15px_rgba(0,0,0,0.05)]`, "47.2%" or "+1 (312) 847-1928" as example data, picsum photos `[scan]` → values decided for this product. Keep a skill's bans; never ship its examples, this skill's included.

**Template look** (counts only when 1-9 are empty). What a cleaned-up screen falls back to when nobody made a decision. Check them after the passes, even if the original had no slop.

- Pure grey page, default font, white text and the old brand color on one button, on a product whose world is warm or bright → a ramp tinted toward the world, an accent from it.
- A headline that would fit another product if you swapped the name → this product's own nouns and facts.
- A hero visual that is an empty box or a generic picture → a product preview in code with real-looking data, or an image from the world.
- The screen now looks exactly like a famous app (every chat app becomes iMessage, every dashboard becomes Linear) → keep the conventions people need, then add this product's signature and moment.
- Every product getting the same layout, type and palette → the direction decides, not habit.

## False positives (do not flag)

- An emoji that is user content (a message, a reaction, a name) is content, not an icon.
- Dark mode, a scrolling logo row, a dot or grid background and decorative animation appear as often on designer-made sites as on generated ones. Alone they prove nothing; flag them only next to another sign in the same category.
- One small uppercase label, one middle-dot line, one arrow link.
- A third-party booking, payment or form widget used as is. A standard system is not slop; wrapping it in made-up copy is.
- A real brand gradient or a purple that the brand owns, when the user confirms it.
- `uppercase` on a two-letter code, a keycap or a legal acronym.
- A gradient that is a small tone shift inside one neutral (`#2b2b2b` to `#1f1f1f`).
- `animate-pulse` on something that is actually live (recording, streaming, a live status dot).
- Off-grid values that exactly center an odd-sized asset, or 1-2px nudges inside small controls.
- Exclamation marks inside quoted user content or product names.
