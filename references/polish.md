# Polish: details, motion and frame-by-frame checks

Use this on a screen that already has a design but still feels unfinished (light slop), and for the final stretch of any heavy fix once `ui-passes.md` has the structure right. Usually one wrong note causes the "something is off" feeling. Locate it, measure it and put it into words before touching anything.

## Order of work

1. **Render** at actual size and at the smallest size anyone will see it. Record each state and each animation as frames. Measure on-screen pixels: a 42px button inside a scaled stage can display at 37px.
2. **Score** with the table below and write the single weakest element down as one sentence.
3. **Structure** comes before detail. Hierarchy and containers first; refining a wrong structure is lost time.
4. **States.** Enumerate them all (empty, loading, error, success, offline, disabled) and give the unhappy ones real design.
5. **Details** from the list below.
6. **Motion** from the decisions below; anything with three or more stages gets a storyboard first.
7. **Frame-by-frame check.** Nothing counts as done until you have looked at the frames.
8. **Repeat** until two consecutive rounds leave the score unchanged.

When asked only to review, end at step 7 and list findings with severity, the problem, the evidence (frame, measurement or `file:line`) and the change. High: a broken state or a broken promise. Medium: users would notice. Low: only a designer would.

| Score | Meaning |
|---|---|
| 3 | Functional, indistinguishable from the rest |
| 5 | Composed when still; empty, error and motion are untouched defaults |
| 7 | All states designed, motion correct, but nothing anyone remembers |
| 8 | One detail worth a screenshot, no defect visible at real size |
| 9 | That detail holds in every state and input method; competitors would borrow it |
| 10 | Not a score you give yourself |

## Getting unstuck

The first rounds fix visible faults. After that the gains are inventions, and each needs a tactic:

| Symptom | Tactic |
|---|---|
| No idea what better looks like | Enlarge a single element three times and design it as if it were alone |
| Too much going on | Delete a part |
| Wrong but unclear why | Describe the problem in a sentence, even with no fix in mind |
| Correct but forgettable | Study the strongest product in the category and list what it does that this does not |
| Circling the same idea | Build three different takes, compare them at real size, keep the winner |
| Blind to it after hours | Hand it to someone with no context, or read it as a competitor |

- Every round makes one change with a reason that fits in a sentence. "Use a spring" is not a reason; "it can reverse mid-motion so it never blocks input" is.
- The first round makes the biggest jump: before and after should differ clearly in a still.
- Build the idea into the material instead of layering effects on it. If the concept is a gauge, its needle shows progress; no separate spinner.
- Reverting your own earlier choice is a valid round. So is holding back.
- Give the end of a flow the strongest beat, because it is what people recall. A changed label is not an ending.
- Mouse, keyboard, a slow drag and reduced motion may travel differently but arrive at the same final state and the same best detail.

## Details

People notice what is missing. With little time, begin with forms, target sizes, contrast and layout jumps, since users feel those directly.

- **Text rendering:** `-webkit-font-smoothing: antialiased` on macOS and subsetted font files; the cheapest fix for text that looks muddy.
- **Growing into a neighbor:** when one element expands over another, fade the neighbor out and back instead of letting them collide.
- **Live numbers** use tabular figures so neighbors stay still, and only changed digits animate.
- **Hover and selected states** shift color, not weight; a bolder word rewraps its line.
- **No jumps.** Images, skeletons and late content get fixed dimensions or an aspect ratio; messages get reserved room. Decide the state before first paint rather than showing a default and replacing it.
- **Typography:** true ellipsis, curly quotes and apostrophes; `text-wrap: balance` for headings, `pretty` for paragraphs; lines of 45-75 characters; paragraph leading 1.4-1.6, display near 1.1; five sizes or fewer. All-caps gets roughly +0.08em; otherwise zero tracking under 28px, about -0.01em from 28px, about -0.02em from 48px.
- **Alignment:** keep to two or three strong vertical edges, icons centered on one axis and text on one left edge; a stray edge is the usual culprit. Trust the eye over the numbers: take 2-3px off the padding on a button's icon side, nudge a play triangle toward its tip.
- **Hairline rings** that work on any surface: `box-shadow: 0 0 0 1px rgb(0 0 0 / .08)`.
- **Consistency:** a single icon style, material and grey temperature. Anything unlike its siblings looks broken.
- **Contrast** measured against the actual background: 4.5:1 for body text and labels, 3:1 for large text and icons. No required reading below 12px at display size.
- **Press feedback:** scale to 0.96 (0.95 at the least) over about 150ms and release smoothly. Wide surfaces such as cards and rows swap background instead; dense toolbars skip it.
- **Hover** only for real pointers (`@media (hover: hover) and (pointer: fine)`), on named properties, about 150ms, never moving layout. If hovering shifts the element from under the cursor it will flicker, so move an inner child.
- **Focus** remains visible and neutral in color.
- **Targets** of 44×44 on touch and 40×40 for mouse, enlarged with a pseudo-element, not by growing the icon; neighbors never overlap (24×24 minimum); a row that behaves as a link is clickable across its whole width.
- **Layering** with `isolation: isolate` or a short z-index scale, not 9999. Decorative layers take `pointer-events: none`.
- **Forms:** 16px inputs, visible labels, `autocomplete`, Enter to submit, nothing typed is lost on error. Validate when a field is left or submitted, then live once an error is showing. Accept loose input (spaced card numbers, common date formats) and display it cleaned up.
- **Waiting:** pressed state on the very frame of the input. Actions that rarely fail (like, toggle, reorder, send) apply at once and roll back with an explanation if rejected. A "Saving…" label appears only after 300ms and stays for at least 500ms. Beyond a second, a skeleton matching the incoming content, placed where it will appear. No bouncing dots.
- **Mistakes:** anything reversible gets an Undo that lasts five seconds or more instead of an "are you sure"; only permanent actions ask, with Cancel focused and a button that names the action ("Delete 3 files").
- **Grouping:** space between groups is at least double the space within one, and a label sits nearer its own field than the field above. Only one element per view breaks the visual pattern, normally the main action.
- **Shadows** on light themes stack softly and lean toward the light's color; dark themes use lighter raised surfaces instead. A cast shadow or light pattern ends at the edge of the object it falls on.
- **Changing theme** disables color transitions, otherwise each part fades on its own clock.

## Motion

### Whether to animate

- **Triggered constantly or by keyboard** (shortcuts, arrows, tabs, moving focus): show the new state on the next frame, no transition. Press and hover feedback stay quick regardless.
- **Triggered now and then** (menus, popovers, dialogs, drawers, toasts): animate inside the timings below.
- **Triggered once in a while** (onboarding, a first win, completing something large): choreography is allowed, each move up to about half a second and the whole sequence up to about two and a half.
- Keep only motion that tells people something: where an element came from, that their input landed, what changed and why. Remove the rest.
- Elements already in place when the page first draws do not play entrances.
- A single motion takes the lead at any moment, either the element touched or the one responding. If one action causes several movements, run them in sequence, each starting when the previous lands.

### Durations and curves

| Change | Time |
|---|---|
| Press, hover, color shift | 100-150ms |
| Tooltip | about 125ms |
| Menus and popovers | 150-250ms |
| Dialogs, drawers, sheets, toasts | 200-300ms |
| Resizing or repositioning in place | 200-300ms |
| Route changes, shared elements, things traveling far | 300-400ms |
| A rare staged move | up to 500ms |

- **Appearing:** a decisive ease-out, for example `cubic-bezier(0.32, 0.72, 0, 1)`, so the response feels immediate. Ease-in never starts an entrance.
- **Disappearing:** 20-30% faster and calmer, mostly a fade plus at most 8-16px of drift toward its destination, unless where it goes is the point (a sheet sliding shut, a swiped card). Avoid an abrupt `display: none`, and keep closed-but-mounted elements inert.
- **Leaving curve:** an ease-in such as `cubic-bezier(0.55, 0, 1, 0.45)`, applied over the exit's shorter time.
- **Repositioning:** ease-in-out such as `cubic-bezier(0.77, 0, 0.175, 1)`. **Hover and color:** plain ease near 150ms. **Pure duration** (spinners, timers): linear.
- **Finger-driven or reversible:** a spring with zero bounce (about 0.5s, bounce 0); a little bounce (0.1-0.3) only for objects meant to feel physical and playful.
- Name each transitioned property rather than `all`, and pick explicit curves instead of the bare `ease-out` keyword.
- When it drags, cut the duration first, then think about the curve.
- Keep timings and curves as named tokens. Multi-stage sequences start with a storyboard comment and a constants object listing when each stage begins.

### Shape of the movement

- **Origin.** Popovers and menus expand from their trigger. Elements that scale in begin at 0.95 (0.97 if small) with zero opacity, never from nothing. Linked pieces such as a dialog and its backdrop share one timing and curve.
- **Reversible at any time.** Input is never blocked by an animation; a change of mind reverses from the current position. Clicks snap and spring to the target; drags track the finger exactly and hand their release speed to a spring. Past a limit, resist progressively after a short free zone instead of stopping dead.
- **Swaps overlap.** When something replaces something else in the same spot, both animate together in one grid cell. An element in flight or mid-morph stays the same element from start to finish.
- **Icon swaps** pass through scale 0.3 to 1 with opacity and a 3px blur on a spring without bounce, and land on a glyph that reads at rest.
- **Stagger** only content that arrives on its own: copies of one element (rows, cards, menu items) 30-50ms apart, only the first six, the rest arriving with the sixth; distinct pieces of a section (heading, copy, actions) 80-100ms apart; grid tiles 80-120ms. Content riding in on a moving container (a drawer's rows, a dialog's body) arrives with it in one piece.
- **Secondary motion** rides on a primary one only: it starts with it or up to 100ms later, travels at most a third as far and ends within 150ms of it. Only for rare moments.
- **Error shake** only when a submit or attempt fails: the wrong field moves through translateX 0, -10, 10, -6, 6, -3, 0px over 360ms, takes focus and shows its message beside it. Never on blur or neutral transitions.
- **Direction carries meaning.** Increasing numbers roll upward and decreasing ones downward. Removed items exit toward their destination: archived items slide to the archive, sent messages rise. A physical-looking object never dissolves or passes through another. Completed items step back.
- **Curved paths** for diagonal trips longer than about 40px, bowing out by 10-20% of the distance with a slight scale and shadow lift at the apex.
- **Anticipation** only before rare launches: a 5-10% counter-move over 80-120ms. Frequent actions skip it, since it is pure delay.
- **Overlap.** Non-text pieces inside a container (an icon, a grabber) come to rest 20-40ms after it, overshooting by less than 4%. Text never lags or wobbles.
- **Deformation** only for things that fall, land or bounce: 15% at most, area preserved, back to shape in 150-200ms. Never on fields or anything someone is reading.
- **Rotation in depth** uses real perspective (roughly 600-1000px at card scale) and darkens the face turning away; a squashed `scaleX` is not a flip.
- **Ambient loops** only on decorative objects and rare moments, driven by sine waves with staggered phases, a few pixels of drift and 1-3% scale, stopped when off screen. Never on content being read or targeted.
- **Cheap properties.** Transform and opacity; color and dash offsets are acceptable; keep blur below 20px; never animate width, height, top, left or margin (measure, then transform).
- **Reduced motion** removes all movement including fades while keeping every end state and every piece of information. Progress indicators keep moving, since a frozen one reads as a crash.
- **Audio and haptics** belong only to rare or physical moments, each tied to something visible on the same frame and drawn from the product's world (a cabin chime for an airline, a ceramic tap for a pottery shop). Never a game's coin sound, never on resets.

## Checking the frames

Run animations from a clock you control and record at 60 fps. Skip staring at hundreds of stills: chart the pixel change between consecutive frames first, where a pop appears as a spike and a dead pause as a flat run, then inspect labelled strips around those points.

- [ ] The response begins on the first frame
- [ ] Anything that grows out of a trigger starts exactly at the trigger's center on screen, through any scaling or camera move; print the coordinates
- [ ] The final frame rests without a pop, snap or reflow
- [ ] No frame shows an incorrect state; try every pair of states and every theme
- [ ] Text stays long enough to be read before the next beat: about 250ms per word, 1.5s at least
- [ ] Nothing jumps backward, swaps elements mid-move, or overlaps and clips by accident
- [ ] Interrupted midway, it returns cleanly to the right place
- [ ] Mouse, keyboard and reduced motion finish in the same state
- [ ] Anything shrinking to nothing does so continuously; blur or stroke scales with its shape instead of lingering as a dot
- [ ] Empty submissions and stopped states explain themselves in words
- [ ] Rapid keyboard use never leaves the UI behind; on a one-second network, presses still register instantly and no spinner flashes for under 300ms
- [ ] Odd widths checked (360, 390, 768, 1024, 1280, 1440, 1920) and recomposed rather than shrunk; every hover action has a touch route
- [ ] At the smallest display size the smallest essential text is legible and the detail you are proudest of is still visible
- [ ] Watch each animation at full speed as if for the tenth time today and trim whichever starts to feel long

Last sweep, assuming an error is still there: console errors, dead links, layout jumps, typos, inconsistent capitalization, leftover placeholders, invented facts, page metadata and favicon, focus states and alt text. Finally name the weakest element again. If improving it would raise the score, continue; otherwise stop.
