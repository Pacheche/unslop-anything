# Component vocabulary

Half of "the AI built the wrong thing" is vocabulary. A vague word ("popup") gets a centered modal every time. Name the component and its behavior, and the model has less room to guess.

## Overlays

| Name | What it is | Use it for | Behavior to specify |
|---|---|---|---|
| Modal (dialog) | Centered window over a dimmed backdrop that blocks the page | A decision or short task that must be finished or cancelled | Native `<dialog>` or an accessible dialog; Escape closes; focus moves in and returns to the trigger; backdrop click policy stated |
| Popover | Small panel anchored to its trigger, page stays usable | Menus, pickers, extra options | Anchored placement and flip; closes on outside click and Escape; Popover API where possible |
| Tooltip | Tiny label on hover or focus | Naming an icon-only control | Delay ~300-500ms; never holds interactive content; appears on keyboard focus too |
| Toast | Brief message in a corner or edge, then gone | Confirming something happened, offering undo | Auto-dismiss 4-6s unless it has an action; does not steal focus; stacks |
| Sheet | Panel sliding from an edge, often the side on desktop | Editing or details while keeping context | Width or detents defined; drag or Escape to close; focus trapped while open |
| Drawer | Panel from the bottom on mobile, or off-canvas navigation | Mobile actions, filters, nav menus | Detents; handle; drag to dismiss; yields to inner scroll |

Names vary between systems (some call the side panel a drawer and the bottom one a sheet). Say the position and behavior along with the name.

## Other names worth using precisely

- **Segmented control** for 2-5 mutually exclusive options; a dropdown from about 6 options.
- **Combobox** when the user can type to filter a list; **select** when they only pick.
- **Command palette** (⌘K) for global search and actions.
- **Skeleton** for loading content of known shape; **spinner** only for unknown duration with no shape.
- **Empty state** with one line on how to fill it, and one action.
- **Inline validation** under the field, on blur or submit.
- **Sticky header**, **scrim** (the dim layer behind an overlay), **backdrop blur** (only when something is behind it).
- **Keycap** for shortcuts, **badge** for status, **chip** for removable or filtering tokens.

When you write a brief or a prompt for another agent, use these names plus the behavior in one line: "a modal that closes on Escape and returns focus to the trigger" leaves no room to guess.
