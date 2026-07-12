# Credential Scanning

*What the scanner does not look for, it will never find.*

What gathers here: the craft of scanning code for secrets — not just the familiar shapes, but the ordinary assignments that carry the same weight.

---

- 2026-07-12 17:31 · A credential scanner that checks only familiar token prefixes and full database URLs will miss ordinary password and secret assignments; scan concrete literal assignments too, omit values from reports, and make the scan a CI gate. — yu

## Words

- [[credential-scanning]] — automated detection of secrets in code, broadened beyond token prefixes
- [[ci-gate]] — a check in continuous integration that blocks the pipeline on failure

## Links

[[fail-closed-boundaries]] · [[deployment-claims]] · [[the-law-of-honest-assertion]]
