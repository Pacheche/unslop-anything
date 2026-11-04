# UI passes

Fix in this order. Finish a pass across the whole screen before the next one. When almost every line changes, plan all passes and write the new screen in one go, as long as each pass is applied.

Why this order: spacing first, because everything reads differently once the rhythm is right. Color and icons next, because they are the loudest slop. Copy before type and layout, because the length of a headline decides its size and where it sits. Visuals and motion last, because they must fit a screen that already works without them.

The values below are starting points. If the project has a design system (theme tokens, CSS variables, Tailwind theme, shadcn, Material), work through it: change token values or how tokens are used, never bypass them with hard-coded values. A real brand accent stays the accent.

## 1. Spacing

- 4px grid for margins, paddings, gaps and fixed heights. Common steps: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128. Any multiple of 4 is fine.
- Same kind, same size: one row height and one gap per list, one padding per row of cards.
- Grouping by distance: space inside a group is clearly smaller than space between groups. Rough levels: inside a control 4-12, between related items 4-8, between groups 16-24, between sections 32-64 (landing sections 80-128).
- Padding by density: sidebars and compact panels ~16, cards 20-24, page gutters 24-32 desktop, 16-20 mobile.
- Navigation is the densest part of an app: rows 32-36 tall, 2-4 apart; a section label sits closer to its items than to the group above (about 24 above, 8 below).
- One max width and one gutter for every section of a page.
- Replace every one-off value with a step. Re-measure the sidebar and the hero after the pass; that is where spacing breaks first.

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
- On dark themes the primary button can be an off-white from the ramp with dark text; on light themes, the primary text color as fill with white text. Both read more deliberate than a colored button. Use this only when the product has no real brand accent.

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

- Pick a family for the character, not the trend. Starting points (all free):

| Character | Interface family | Optional partner |
|---|---|---|
| Precise, technical, calm | Geist, IBM Plex Sans, Inter | Geist Mono or JetBrains Mono for figures and meta |
| Warm, human, friendly | DM Sans, Figtree, Instrument Sans | Newsreader or Instrument Serif for the hero headline only |
| Editorial, crafted | Inter or Söhne-like grotesk | Fraunces, Newsreader, EB Garamond for headlines |
| Playful, bold | Bricolage Grotesque, Space Grotesk | a mono for small labels |
| Native mobile | SF Pro (iOS), Roboto or the brand font (Android) | none |

- One interface family plus at most one partner. A display serif belongs only to large headlines.
- Scale (web): meta 12/16, secondary 13-14/20, body 14-16/20-24, card figures 28-32, page title 28-36, hero 48-72 desktop and 34-44 mobile with line height 1.02-1.1.
- Weights 400 and 500; 600 for headings and emphasis when needed. Hierarchy from size and color. Keep platform and design-system weights.
- Sentence case. Letter spacing 0 under 16px; display from 40px may go to -0.02em.
- `tabular-nums` and one number format across the screen.
- `text-wrap: balance` on headings, `pretty` on paragraphs.

## 6. Layout

- Keep sections and their order. Inside a section, alignment and proportions may change.
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

## 8. Visuals

- Remove decorative filler (blobs, orbs, cubes, glowing grids, robots, brains).
- Dashboards and app screens rarely need generated images; their moment is a well-drawn chart, beautifully set figures, real content (photos, avatars) or a physical object built in code (a payment card with a chip and a number).
- Landing heroes get a visual that shows something true: a scene from the world, or the product itself built in code with plausible data.
- Generate images only with a tool you have, and show the prompt, model and size to the user before any paid run. Recipe and styles: `visual-design.md`.
- No tool and a scene is needed: leave a plain slot of the exact size, write the prompt in the report, never a labeled placeholder on the page.

## 9. Motion

- Remove loops without a reason, bounces, hover lifts and scale on cards, `transition-all`, parallax.
- Keep motion that explains: hover is a quick color or surface change, press is a 0.97-0.98 scale, menus fade and rise 4-8px from their origin, changed numbers tween.
- One curve, for example `cubic-bezier(0.2, 0.8, 0.2, 1)`, and a few durations: feedback 120-180ms, menus and popovers 160-220ms, entrances and sheets 280-450ms, exits about 0.7x the entrance. Stagger 40-60ms, at most six items.
- Only transform and opacity. Respect `prefers-reduced-motion` with a crossfade.
- Ask how often people will see it: hundreds of times a day gets near-instant; occasional moments may be richer.

## Checklist

- [ ] Every spacing value on the 4px grid; equal things have equal sizes
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
- [ ] Renders checked at desktop and mobile widths: nothing clipped, overlapping or overflowing
- [ ] Template test passed
