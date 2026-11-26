# Browser verification for web UI

Use the project's existing browser tests or the host's browser tool when appropriate. Playwright CLI is a route for interactive checks when available. See the [Microsoft skill and command guide](https://github.com/microsoft/playwright-cli/tree/dc5f4d5616ab5a28ded12fd7101a4d49bd59a820/skills/playwright-cli) for supported commands.

1. Use a local or authorized preview and identify the viewport, route and state. Capture the original before edits when the comparison matters.
2. With Playwright CLI, `open <url>`, then `snapshot` to locate controls by role or name. Use fresh snapshot references after navigation or state changes. Set a wide and a narrow viewport with `resize <width> <height>`, then walk the affected task like a user.
3. Check the affected focus order, keyboard actions, forms, errors and responsive behavior. Check reduced motion when the change affects motion. Use screenshots for visual evidence and snapshots or assertions for behavior. Check browser errors if the expected state fails to appear.
4. Compare the same state before and after. Record the widths, task completed, evidence and checks still pending. Close any tool-owned browser session you opened when finished.

A screenshot supports a visual claim. It does not establish that a link, form or keyboard path works.
