# How we cut deploy time

Our deploys took 40 minutes because every build reinstalled dependencies from scratch. We cached the lockfile layer in CI and the median deploy dropped to 4 minutes over the next two weeks.

What we changed:

- Cached `node_modules` keyed on the lockfile hash
- Split the test suite into four parallel jobs
- Removed a 6-minute Docker image rebuild that nothing used

The code example below uses an em dash on purpose and must not count:

```text
title — subtitle
```

If your builds reinstall dependencies on every run, start with the cache. It was a one-line change for us.
