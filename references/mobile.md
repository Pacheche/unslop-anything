# Mobile app screens

Read this together with `ui-signs.md` and `ui-passes.md`. Mobile slop has the same causes, plus one more: controls that imitate the platform badly.

## Signs specific to mobile

- A home screen that is a column of full-width saturated cards, each a different gradient, with an emoji in every title.
- A greeting header ("Hey Mike! 💪", "Morning, Jordan! ☀️") with a motivational subtitle.
- A full-width gradient "START WORKOUT 🚀" button in caps.
- Rebuilt toggles, sliders and sheets that animate slightly wrong; a fake status bar or home indicator drawn by hand.
- Bottom tab bars with 5+ items, icons in different styles, or no labels.
- Five tiny metric columns crammed into one row → a 2x2 grid or a short list.
- Initial-letter avatars where photos exist; red count badges on every row → a small unread dot.
- Rows of very different heights in one list; list rows much taller than the platform norm.
- Tap targets under 44pt (iOS) or 48dp (Android).

## Platform conventions to respect

- **Type:** SF Pro on iOS with the system text styles (Large Title 34, Title 28/22/20, Headline 17 semibold, Body 17, Callout 16, Subheadline 15, Footnote 13, Caption 12/11). Roboto or the brand font on Android with Material's scale. Support Dynamic Type / font scaling without overlaps.
- **Navigation:** large title that collapses on scroll (iOS); a tab bar with 3-5 labeled items; push to go deeper, back to undo navigation; a self-contained task opens as a modal; a short interruption opens as a sheet.
- **Sheets:** system detents or detents from the content (medium/large), never arbitrary percentages; drag yields to inner scroll; dimmed backdrop that fades; dismiss by distance or velocity.
- **Controls:** native or faithful wrappers. Menus anchored to their trigger. Destructive actions confirm.
- **Lists:** single-line rows about 44pt; rows with avatar and two lines about 60-76pt. Pick one height per list.
- **Forms:** label above the field, the right keyboard type and autofill, validate on blur or submit, error under the field.
- **Corners:** continuous (squircle) corners on iOS (`borderCurve: 'continuous'` in React Native, `.continuous` in SwiftUI).
- **Safe areas** and the Dynamic Island are part of the layout, not obstacles.
- **Icons:** SF Symbols on iOS, Material Symbols on Android, or one custom set. Never three families.
- **Haptics:** one per meaningful action, fired with the visual change.

## Motion on mobile

- Two families that must not mix: responsive motion follows a finger (springs that keep the gesture's velocity, rubber-banding, interruptible) and narrative motion runs on time (150-350ms, ease-out). Mixing them is what makes UI feel fake.
- Entrances from `scale(0.95)` plus fade, exits about 0.7x the entrance time, never ease-in for entrances.
- Reduce Motion: replace movement with a crossfade.

## What good mobile unslops looked like (observed patterns)

- A neutral light or dark canvas, one strong accent, and one hero element that carries the color (a big glucose number on a warm header, a recovery score set large with a small bar history).
- Saturated gradient cards replaced by neutral cards where only the key value or a status gets color.
- A floating, compact tab bar with labels and one highlighted item, or a plain native tab bar; the header trimmed to the page title and one or two actions.
- Spacing unified to one value between blocks (for example 24) and one radius family.
- Clip-art illustrations replaced by an illustration that shows the real place or object of the product.
- Pinned contacts with real photos, filter chips under the large title, unread as a dot, dividers removed.

These are results, not a style to copy. Reaching them through the direction is the point.

## Verify on a device or simulator

A mobile screen is not done until it runs. Render at real device size with the platform font. Check a large phone (with Dynamic Island) and a small one (SE-class). Walk the flow one step before and after the screen, open and dismiss every sheet, try every back path and the keyboard. If you have simulator or device tools, use them; otherwise take screenshots from the simulator or emulator.
