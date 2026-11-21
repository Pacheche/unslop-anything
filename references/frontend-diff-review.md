# Frontend diff review

Use when the request includes code cleanup, or for the code introduced by the current UI change. Review the relevant diff against its base. Identify the existing public behavior, state transitions and accessibility requirements before simplifying.

- Remove comments that narrate the syntax, duplicated bookkeeping, needless one-caller wrappers and branches that a verified invariant already excludes. Keep comments that explain browser workarounds, accessibility decisions, state ordering or the evidence for a trade-off.
- Keep boundary validation, failure and empty states, fallback behavior, and checks that protect concurrent or asynchronous transitions. Prove a branch is unreachable from the supported entry points before removing it.
- Run relevant checks before and after where possible. Verify affected mouse, touch and keyboard paths, focus restoration and component names. Report the precise behavior and any environment you could not check.

For an existing `@ui-sdk/*` project, or when the user selects UI SDK for an interactive component, consult the [UI SDK guide](https://github.com/vercel-labs/ui/blob/e37003dd3cfd69cc9dd5deb24386a63473ab93f6/packages/core/skills/ui-sdk/SKILL.md). Match existing primitives for keyboard navigation, focus, dismissal, selection and ARIA. Check package stability and browser and framework support before selecting it for a new project.

Adapted from [Vercel's code cleanup guide](https://github.com/vercel-labs/ui/blob/e37003dd3cfd69cc9dd5deb24386a63473ab93f6/.agents/skills/ui-sdk-unslop/SKILL.md).
