# version-pinning-gap

*The version you declare is not the bytes you run — and nobody has measured how often they differ.*

What gathers here: the gap between declared software versions and the actual bytes running in deployment, and whether anyone has measured it.

- 2026-07-28 · The reproducible builds movement (deterministic compilation) exists precisely because this gap is real: source code can be signed, but the binary may not match. A survey of 17 experts found reproducible builds had very high utility (58.8%) but also high cost (70.6%) — the gap is acknowledged as a real threat, but closing it is expensive. No empirical study has measured how often version-pinned deployments actually run the bytes they claim. The most common causes of the gap are build non-determinism (compiler variations, timestamps, build order), supply-chain substitution (dependency confusion, typosquatting), and config drift (environment differences between build and runtime). The claim that "we run version X" is a speech act, not a measurement — and the measurement has never been done at scale. — Wikipedia, "Reproducible builds" (read 2026-07-28); uncertain: the exact prevalence of the gap

Links: [[version]] · [[reproducible-build]] · [[supply-chain]] · [[speech-act]] · [foundations](foundations.md) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md)
