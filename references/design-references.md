# Design direction from references

Use this when the brief benefits from a visual reference or the user supplies a screenshot. Keep the project's approved design system and the intended scope.

## Choose a direction

- Start with the kind of product, what visitors come to do, and what real asset can demonstrate it. A restaurant may lead with a photograph of its food. A software page may show the actual product at work. Plan the first view around that asset and a clear action.
- Take the relevant pattern from the [Taste Skill](https://github.com/Leonxlnx/taste-skill/tree/d1a2bb41d927083ac7118f60cfc9cdf711810ea0/skills/taste-skill): strong shared alignment, a distinct focal moment, real visuals and a check in the browser. Derive rhythm, image treatment and motion from the brief. A section's height should follow its content and the viewport.
- Use [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/fcc70284932276d085f01ef9f83edde90b1258cb) to select a small number of relevant references. Read only the chosen design documents. Take transferable principles such as type hierarchy, grid, density or treatment of interactive states. Translate them into the target brand's tokens. Preserve the project's canonical `DESIGN.md` and create or edit it only within the requested scope.

## From a screenshot to code

1. Record the reference viewport and break the image into content hierarchy, regions, grid, type, colors, spacing, assets and recurring components. Note what can be measured and what is inferred.
2. When the user owns the design or has permission, compare the implementation at the same viewport and use the available source assets. For another product's proprietary interface, carry over useful principles and implement the requested functionality in a distinct composition.
3. Build in the project's stack with semantic components and the existing tokens. A screenshot is one state at one size. Use the brief and project behavior to validate the responsive layout, focus order, scroll, loading, errors and touch states.
4. Compare at the reference viewport and a narrow viewport using [browser verification](browser-verification.md). Correct the largest discrepancies in structure first, then refine typography and spacing.

The source workflow comes from [Aldo Paucar's UI resource guide](https://aldopaucar.com/recursos/interfaz/). For an editorial photography treatment, also see [editorial direction](editorial-direction.md).
