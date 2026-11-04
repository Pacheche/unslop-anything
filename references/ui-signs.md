# UI signs of slop

Ten categories. In an audit, write one line per sign found: sign, where it lives, fix. File each sign under the first category that lists it. The slop level is the number of categories with at least one sign, times 10%; category 10 counts only when categories 1-9 are empty.

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
- Over-correction: everything grey, primary action invisible, data unreadable → bring back an accent and status colors with meaning.

## 2. Type

- Headings at 800-900 weight `[scan: 800-900]`, or 700 on every heading and label → 400-600, hierarchy from size and color. Platform styles (iOS Large Title) and an existing design system keep their weights.
- `UPPERCASE` labels with wide tracking (`NAVIGATION`, `PAID THIS MONTH`, project taglines in caps) `[scan]` → sentence case, normal tracking.
- Too many sizes and weights on one screen → a few sizes from a scale, two weights.
- Numbers in mixed formats (`$48,210` next to `$124,860.40`, `07`) → one format, `tabular-nums`.
- Money or plain numbers set in mono for decoration → proportional with `tabular-nums`; mono only for IDs, hashes, commands, code.
- Negative tracking on small text → zero or slightly positive.
- Italic on one word of a headline for "emphasis" → let the sentence carry the emphasis.
- Subtitle font so small it does not read; a light grey that fails contrast → bigger, darker, or cut the subtitle.
- Ragged two-line headlines and subtitles with a one-word last line → `text-wrap: balance` (headings) or `pretty` (paragraphs).
- An unchosen default typeface (Inter, Instrument Sans, Poppins everywhere) on a product whose character is different → pick a family for the character (see `ui-passes.md`). The default is fine when it fits.

## 3. Icons and emoji

- Emoji as nav icons, status, label decoration or in buttons (🏠 🚀 💰 🔥 ⚠️ ✨) `[scan]` → one line icon set, or nothing.
- Colored icons, each one a different hue, often inside pastel tiles or bubbles → icons in the text color (secondary or muted); category color, if needed, as a small dot.
- A sparkle, wand or star for anything "AI", purple as the AI color → remove, or a plain icon only where it explains the action. Show what the AI produces.
- Icons in several sizes, strokes and families → one family, one size (16-20px in web UI), one stroke.
- Icons hand-drawn as inline SVG paths next to library icons → import from the library; a hand glyph never matches its neighbors.
- Arrow glyphs in text (`View all →`, `Next ➜`) `[scan]` → a library chevron icon, or plain text.
- Icons nudged off the column → same icon box width in every row, fixed gap to the label.

## 4. Spacing and alignment

- Arbitrary off-grid values (`mt-[13px]`, `py-[11px]`, `padding: 13px`) `[scan]` → steps on a 4px grid.
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
- Trailing periods on labels, buttons, titles → none. Paragraphs keep them.
- Em dashes and decorative separators (` — `, ` · `, ` | `) in UI strings `[scan]` → a period, a comma, a slash or a line break.
- `PRO`, `New ✨`, `Beta 🚀` badges everywhere → remove, or one quiet text badge where it is true.
- Fake-looking data: `$123,456`, `[X]`, `Lorem`, everyone named John Doe → plausible numbers and names.
- Unverifiable social proof (`Loved by 10,000+ teams`, five stars, avatar stacks without a source) → ask the user; make it specific or remove it.
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
- Box inside box inside box → one container level.
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
- Layout structure copied from a template: three equal feature cards with an emoji, a bold title and a vague line → fewer features, concrete copy, a layout that follows the content.

## 8. Visuals and imagery

- Glossy 3D blobs, orbs, liquid chrome, floating cubes, purple nebulas as the hero visual → the product itself, or one concrete image from the product's world.
- Robots, glowing brains, circuit lines, holograms for anything AI → show what the AI produces.
- Generic flat clip-art illustration → an illustration with a point of view that belongs to the product's world (a train app gets the actual route and landscape, not a stock train).
- Text, fake buttons or a fake logo baked into an image → real text in the page, clean image.
- An image with a hard edge and a different black or white than the page → match the background and mask the edges.
- Dot grids, glowing grid lines and noise as backgrounds `[scan: dot grid]` → plain background.
- A visual on every section → one visual where it helps, usually only the hero.

For making or fixing the images themselves, use `references/visual-design.md`.

## 9. Motion

- `animate-pulse`, `animate-ping`, `animate-bounce`, breathing glows on things that are not live `[scan]` → static.
- `transition-all` `[scan]` → name the properties: color, background, border, opacity, transform.
- `hover:scale-105`, `hover:-translate-y-1` on cards `[scan]` → a color or surface change on hover; a tiny scale-down on press.
- Bouncy springs and overshoot on simple UI → one ease-out curve.
- Everything flying in on load, list items staggered by index forever → at most one short entrance for the main content.
- Parallax and elements floating on scroll → static layout.
- Animating width, height, top, left, margin or large blurs → transform and opacity.
- Abrupt slider or carousel cuts; popups whose close animation glitches → a short crossfade; test every open and close.

## 10. Template look

These are what a cleaned-up screen falls back to when nobody made a decision. Check them after the passes, even if the original had no slop.

- Pure grey page, default font, white text and the old brand color on one button, on a product whose world is warm or bright → a ramp tinted toward the world, an accent from it.
- A headline that would fit another product if you swapped the name → this product's own nouns and facts.
- A hero visual that is an empty box or a generic picture → a product preview in code with real-looking data, or an image from the world.
- The screen now looks exactly like a famous app (every chat app becomes iMessage, every dashboard becomes Linear) → keep the conventions people need, then add this product's signature and moment.
- Every product getting the same layout, type and palette → the direction decides, not habit.

## False positives (do not flag)

- An emoji that is user content (a message, a reaction, a name) is content, not an icon.
- A real brand gradient or a purple that the brand owns, when the user confirms it.
- `uppercase` on a two-letter code, a keycap or a legal acronym.
- A gradient that is a small tone shift inside one neutral (`#2b2b2b` to `#1f1f1f`).
- `animate-pulse` on something that is actually live (recording, streaming, a live status dot).
- Off-grid values that exactly center an odd-sized asset, or 1-2px nudges inside small controls.
- Exclamation marks inside quoted user content or product names.
