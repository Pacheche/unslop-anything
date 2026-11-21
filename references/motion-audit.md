# Interactive motion audit

Use with the [polish pass](polish.md) when motion feels slow, excessive or janky. Identify the interaction, trigger, frequency and useful result before tuning values.

1. **Remove** motion with no task or feedback purpose, especially on repeated keyboard actions. Check that removing it leaves the correct end state, mounted content, focus, hit targets and cleanup. Search for transition-end listeners and callbacks that may need a direct completion path.
2. **Reduce** motion when frequent feedback should stay. Shorten travel and delay first. Test fast repetition, reversal mid-flight and reduced motion. Keep the same meaning and destination whichever path the user takes.
3. **Adjust** motion that establishes continuity or reveals state. Give it a clear origin. Inspect actual dropped frames when diagnosing jank. Look for per-frame layout reads/writes, state updates that rerender the tree, large paint areas and excessive layers. Prefer transform or opacity where they preserve the intended visual effect. Compare recordings on the same device before claiming a performance improvement.

Report what you removed, reduced or kept, with a location and reason. Mark any performance diagnosis that still needs runtime evidence. Adapted from [Emil Kowalski's remove, review and performance skills](https://github.com/emilkowalski/skills/tree/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills).
