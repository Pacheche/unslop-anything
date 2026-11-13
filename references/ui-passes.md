# UI passes

Fix in this order. Finish a pass across the whole screen before the next one. When almost every line changes, plan all passes and write the new screen in one go, as long as each pass is applied.

Why this order: subtract first, because every piece removed is one less to restyle. Then spacing, because everything reads differently once the rhythm is right. Color and icons next, because they are the loudest slop. Copy before type and layout, because the length of a headline decides its size and where it sits. Visuals and motion last, because they must fit a screen that already works without them.

The values below are starting points for deriving your own, not answers. A fixed recipe applied to every project becomes the next fingerprint (the double-bezel card and Satoshi spread exactly that way). Derive each value from this product's text, world and brand, and write down why.

If the project has a design system (theme tokens, CSS variables, Tailwind theme, shadcn, Material), work through it: change token values or how tokens are used, never bypass them with hard-coded values. A real brand accent stays the accent.

## Landing pages and marketing sites: impact first

Recoloring a page that says nothing still leaves a page that says nothing. On a landing page, decide these before the passes, in this order, because they move the result the most:

1. **Headline.** What the visitor gets and who it is for, under about ten words, with the product's own nouns. Write five genuinely different options from facts the user gave you; pick one and say why. If the facts are missing, ask.
2. **Something real at the top.** A screenshot of the product, a photo of the place, the person or the object. If there is nothing yet, good text alone beats an image nobody chose.
3. **Metadata and leftovers.** Pass 10 below. It is the cheapest fix and the one that weighs most in automated scores.

Then run passes 0-9. Within them, the three-card section, made-up proof and decorative motion are the next biggest wins.

## 0. Subtract

Generated screens have too much, and every extra piece competes. Before restyling anything, go over each icon, line, badge, caption, wrapper and sentence and ask what would break without it. If the answer is nothing, it goes; "it adds interest" or "it fills the space" are the reasons a model added it, so they do not count. Go over the screen twice, because each deletion reveals the next. The signature detail from the direction is the only exemption. Information people need (a price, a password rule) is moved, made smaller or turned into the moment, never lost.

What to cut first:

- Dividers that spacing already does. Keep rules only where they help the eye follow a row across a table or ledger.
- A subtitle that repeats the title with different words.
- Wrappers inside wrappers. A map, photo or chart that is itself the content goes edge to edge in its container.
- Two devices doing one job: a step counter beside a progress bar, a toast for a change already visible, an icon next to a label that says the same. Keep the better one; the job still gets done.
- A control parked beside the thing it acts on (a clear button next to a search box, a send button floating by a field): fold it into that element's states.
- Chrome the moment does not need yet, like Share on something with nothing to share.

Then run the passes on what is left.

## 1. Spacing

- One owned scale: 6-8 spacing values, decided once, stored as tokens, and nothing else. Using the project's existing scale is fine. The sign of an untouched page is not the 4px grid; it is reaching for any value from the framework's whole default list, and putting the same gap between everything.
- With no scale, derive one from the text: body size times line height gives one line (17px x 1.5 ≈ 26px); its fractions and multiples give the steps (for example 6, 13, 26, 39, 52, 104, 156). Or pick 4px-grid steps on purpose (4, 8, 16, 24, 40, 64, 96). Either way, few values with clear jumps.
- Same kind, same size: one row height and one gap per list, one padding per row of cards.
- Grouping by distance: space inside a group is clearly smaller than space between groups. Rough levels: inside a control 4-12, between related items 4-8, between groups 16-24, between sections 32-64 (landing sections 80-128).
- Padding by density: sidebars and compact panels ~16, cards 20-24, page gutters 24-32 desktop, 16-20 mobile.
- Navigation is the densest part of an app: rows 32-36 tall, 2-4 apart; a section label sits closer to its items than to the group above (about 24 above, 8 below).
- One max width and one gutter for every section of a page.
- Replace every one-off value with a step. If the project uses Tailwind, move the scale into the theme and drop the defaults you do not use, so later edits cannot drift back. Re-measure the sidebar and the hero after the pass; that is where spacing breaks first.

## 2. Color

Build one neutral ramp, tinted toward the product's world, then add one accent.

Neutral ramp in OKLCH (pick a hue `h` from the world: warm 60-80, ink/blue 250-265, green 140-160; or chroma 0 for pure graphite). Keep chroma between 0 and 0.015 so surfaces never read as a color:

| Role | Dark L | Light L |
|---|---|---|
| Deepest surface (sidebar) | 0.15 | 0.97 |
| Page background | 0.17 | 0.985 |
| Card | 0.20 | 1.00 |
| Raised (input, active row) | 0.24 | 0.955 |
| Hairline | primary text at 8% | primary text at 8% |
| Primary text | 0.94 | 0.21 |
| Secondary text | 0.74 | 0.44 |
| Muted text and icons | 0.62 | 0.50 |

- Apps and dashboards: surfaces stay near neutral; people look at them for hours and the content carries the color. Landing pages may tint further toward the world.
- Three text roles: primary, secondary, muted. Muted is for meta and captions and still passes about 4.5:1.
- One accent, from a real brand color or from the world (warm worlds: amber, coral, ember; cool: cobalt, teal, sky; natural: moss, sage). Avoid the violet-blue family unless the brand truly is violet.
- The accent covers a few percent of the screen: the primary action, the selection, one key figure. Text on the accent reaches 4.5:1; darken the accent or use dark text if not.
- Bold color is allowed when it is the direction (a red fitness brand, an orange glucose header), as long as it is one hue family, applied consistently, and every use means something.
- Semantic colors carry meaning only, toned to sit inside the palette.
- Remove hue-to-hue gradients, gradient text, glows, colored shadows, washes, neon borders. A gradient may stay as a small tone shift within one hue.
- Depth: on dark themes, lighter surfaces and hairlines, not shadows. On light themes, small neutral shadows (`0 1px 2px rgb(0 0 0 / .05)`, floating `0 8px 24px rgb(0 0 0 / .06)`).
- On dark themes the primary button can be an off-white from the ramp with dark text; on light themes, the primary text color as fill with white text. Use this only when the product has no real brand accent and the direction is quiet on purpose. A product whose page needs energy gets a decided accent from its world instead; a graphite button on a cream page is the newer default, not a decision.

## 3. Icons

- Every decorative emoji becomes a line icon from one set (the project's set, otherwise Lucide, Phosphor or the platform set).
- One size and stroke everywhere: 16-20px, stroke 1.5.
- Icons take the color of their text role. No per-icon colors and no pastel tiles behind them unless the tile is the category's real visual.
- Same icon box width in every row, fixed 8-10px gap to the label.
- Drop icons that add nothing. A category that needs color gets a small dot.

## 4. Copy

- Fix every sign in category 5 of `ui-signs.md`: titles name the context, no exclamations or hype, changes state their reference, short labels, plausible mock data, unverified claims go to the user.
- Headlines say what the product does for whom, with facts already on the page.
- Longer copy (hero text, feature blurbs, emails): run `writing.md`.

## 5. Type

- Pick a family for the character, not the trend, and write one line on why it fits this product. Check it is not what every product in the category already uses (see the overused list in `ui-signs.md`, category 2). Families to consider, never to default to:

| Character | Interface family | Optional partner |
|---|---|---|
| Precise, technical, calm | Geist, IBM Plex Sans, Inter | Geist Mono or JetBrains Mono for figures and meta |
| Warm, human, friendly | Figtree, Nunito Sans, Atkinson Hyperlegible | a humanist serif only if the world is print |
| Editorial, crafted | a grotesk with character (Schibsted Grotesk, Hanken Grotesk) | Newsreader, EB Garamond, Literata for long reading, not as a thin italic accent |
| Playful, bold | Bricolage Grotesque, Familjen Grotesk, a condensed display | a mono for small labels |
| Rooted in a place or craft | a family with that origin (a Latin American, Japanese, Swiss or signage face) | none |
| Native mobile | SF Pro (iOS), Roboto or the brand font (Android) | none |

- One interface family plus at most one partner. A display serif belongs only to large headlines.
- Six sizes, not twenty: one for labels, one for body, four for headings, with obvious jumps. Starting point: body size times 1.5 per level (17 → 25, 38, 57, 86, plus 14 for labels). Apps and dashboards stay denser: meta 12, secondary 13-14, body 14-16, card figures 28-32, page title 28-36.
- Landing hero: the only large text on the page, far above everything else. On strong sites the largest text sits near 8vw at 1440px (about 120px); on weak ones near 5vw. Start from `font-size: clamp(2.75rem, 8.4vw, 8.5rem); line-height: 0.95; letter-spacing: -0.03em; text-wrap: balance`, then tune to the sentence: if it runs past three lines on a 390px phone, shorten the sentence before shrinking the type. Section headings at most half its size.
- Weights 400 and 500; 600 for headings and emphasis when needed. Hierarchy from size and color. Keep platform and design-system weights.
- Sentence case. Letter spacing 0 under 16px; display from 40px may go to -0.02em to -0.04em.
- Eyebrow labels: delete the ones that repeat their heading; keep at most one per page that adds a fact, as `font-size: 0.875rem; text-transform: none; letter-spacing: 0` in the muted color.
- `tabular-nums` and one number format across the screen.
- `text-wrap: balance` on headings, `pretty` on paragraphs.

## 6. Layout

- Keep sections and their order. Inside a section, alignment and proportions may change. Sections that only exist because the template had them go in the report as suggestions; remove them only with the user's yes.
- Break the repetition: if every section is a centered heading over a grid, change the shape of some (a left-aligned split, a full-width figure, a plain list, a different background or width). The three-icon-card section becomes a list with one sentence each, one concrete example, or a before and after.
- Apps keep app proportions: sidebar 240-280, fluid content capped around 1440-1600, header 56-64.
- Landing hero, strongest to weakest: a full-bleed scene from the product's world with the headline on its calm area and the product view rising from the bottom; an asymmetric split with the visual at least half the width; text over a large product view. Centered stacks only for short heroes without a visual.
- Long headlines align left. One primary and one secondary action.
- Navigation: logo, existing links, one button. Log in is a text link.
- The first screen is composed as a whole, no dead band.
- Mobile web: stack in reading order, simplify dense previews instead of zooming them down, nothing under 11px.

## 7. Details

- Radius by size: tags and keycaps 4-6, inputs and buttons 8-10, cards 12-16, panels 14-20. Nested: inner = outer minus padding, never below 4. Pills only for real pill controls (chips, segmented controls, tab indicators).
- Counts and meta become quiet text. Shortcuts become small keycaps.
- One lead chart, clearly the biggest, drawn with care. Supporting data in a different, smaller form (ranked list with thin bars, short table).
- One accent per chart, on the thing that matters. Several hues only for real series, and one leads.
- Stat cards: label, figure, change with reference. A real-looking object only when it is the thing counted (a card next to card spend).
- Vary widths: a row of compact stats above one wide chart beats four equal cards.
- Chart type follows the data: trend = line, comparison = bars, share = one stacked bar or a list, single goal = progress bar.
- Active state: a small surface step and a hairline, not a gradient with a glow.
- Hover and focus inside the palette; a visible focus ring.
- The signature detail from the direction appears where it belongs and nowhere else.
- Every state exists and is designed: hover, focus, active, disabled, loading, error, empty. Empty states say how to fill them; errors say what happened and how to recover.
- Browser surfaces carry the design too, and models skip them most often: text selection (`::selection`), the caret (`caret-color`), scrollbars, focus rings, link underline offset (`text-underline-offset`), and tabular numerals in data. Theme them from the palette.
- Light or dark comes from where and when the product is used (a night-shift monitor, a kitchen tablet at noon), not from the category.

## 8. Visuals

- Remove decorative filler (blobs, orbs, cubes, glowing grids, robots, brains).
- Dashboards and app screens rarely need generated images; their moment is a well-drawn chart, beautifully set figures, real content (photos, avatars) or a physical object built in code (a payment card with a chip and a number).
- Landing heroes get a visual that shows something true: a scene from the world, or the product itself built in code with plausible data.
- Generate images only with a tool you have, and show the prompt, model and size to the user before any paid run. Recipe and styles: `visual-design.md`.
- No tool and a scene is needed: leave a plain slot of the exact size, write the prompt in the report, never a labeled placeholder on the page.

## 9. Motion

- Remove loops without a reason, bounces, hover lifts and scale on cards, `transition-all`, parallax.
- Keep motion that explains: hover is a quick color or surface change, press is a 0.97-0.98 scale, menus fade and rise 4-8px from their origin, changed numbers tween.
- Durations, curves and stagger come from `polish.md` (Durations and curves), which is the single source for these values; exits run 20-30% shorter than entrances.
- Only transform and opacity. Respect `prefers-reduced-motion` with a crossfade.
- Ask how often people will see it: hundreds of times a day gets near-instant; occasional moments may be richer.
- To tune what remains (interruption, replacements, frame-by-frame checks), use `polish.md`.

## 10. Metadata and leftovers

- Every page has its own `<title>` (the business name and what the page is, not the hyphenated project name) and a meta description of up to 160 characters, from facts on the page.
- A social image (`og:image`, 1200x630) and the brand's favicon replace the builder's defaults. If no asset exists, list them under `Not checked:` instead of inventing one.
- Remove builder badges, section comments (`<!-- Hero Section -->`), Tailwind from a CDN in production, `/lovable-uploads/` paths and builder-named tokens (`--primary-glow`, `--shadow-elegant`): rename tokens to the system's own names and values.
- Links to `#`, leftover sample copy, images named `hero-image.png` or loading from `picsum.photos` → real targets and assets, or list them in the report.
- Also check: `lang` on `<html>`, one `<h1>`, headings in order, `alt` text on content images.

## Lock the decisions

A model that does not remember what was decided drifts back to its defaults on the next request. In heavy mode, offer to save the decisions where every agent reads them:

- If the project has a `DESIGN.md`, design tokens or rules in `AGENTS.md`/`CLAUDE.md`, follow them and update them with what changed.
- Otherwise, with the user's yes, write a short `DESIGN.md`: typefaces with the reason for each, colors as hex or OKLCH with their roles, the type and spacing scales, radius and shadow rules, motion rules, and the bans as checkable rules ("never three icon cards", "no uppercase labels above headings"), not wishes ("feel elegant"). Link it from `AGENTS.md` or `CLAUDE.md`.

## Checklist

- [ ] Landing page: headline says what it is and for whom; something real at the top
- [ ] Every spacing value from one small owned scale; equal things have equal sizes; tight inside groups, open between them
- [ ] Six type sizes or so, with a lead step far above the rest
- [ ] Icons, labels and numbers in aligned columns
- [ ] One tinted neutral ramp, three text roles, one accent with enough contrast
- [ ] No hue gradients, gradient text, glows, colored shadows, blobs
- [ ] No emoji in the chrome; one icon set, one size, one stroke, text-colored
- [ ] Type chosen for the character; weights 400-600; no tracked caps; no negative tracking on small text
- [ ] No exclamation marks, greetings, hype, trailing periods on short strings, unverified claims
- [ ] Numbers in one format with tabular figures; labels match their data
- [ ] Nested radii add up; not everything is a pill
- [ ] Hero has a real visual or a product preview with a moment, never filler
- [ ] First screen composed as a whole
- [ ] No looping or bouncy motion; one curve; no animated layout properties
- [ ] Renders checked at desktop and mobile widths, region by region:
  - contrast: body and placeholders 4.5:1, large text 3:1; secondary text on a colored surface tinted from that hue, never grey
  - nothing clipped, overlapping, overflowing its box or the viewport; tooltips and menus not cut by an `overflow: hidden` parent; cards in scrollers inset on both sides
  - text: body measure 65-75ch, line height at least 1.3 (1.5-1.7 for body), not flush to the viewport edge (16px minimum), at least 8px (ideally 12-16px) inside any bordered or filled box, no one-word last lines on headings
  - headings in order (no h1 to h3 jump), more space above a heading than below it
  - no content stuck invisible after a reveal animation, no script errors in the console, no broken images
- [ ] Every state designed: hover, focus, disabled, loading, error, empty
- [ ] Selection, caret, scrollbars, focus rings and underline offset themed from the palette
- [ ] Own title, description, social image and favicon; no builder leftovers, `#` links or sample assets
- [ ] No recipe value from this or any other skill shipped unchanged; every chosen value has a reason
- [ ] Template test passed
