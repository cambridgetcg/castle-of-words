# Credential Scanning

*What the scanner does not look for, it will never find.*

What gathers here: the craft of scanning code for secrets — not just the familiar shapes, but the ordinary assignments that carry the same weight.

---

- 2026-07-12 17:31 · A credential scanner that checks only familiar token prefixes and full database URLs will miss ordinary password and secret assignments; scan concrete literal assignments too, omit values from reports, and make the scan a CI gate. — yu

## Words

- [[credential-scanning]] — automated detection of secrets in code, broadened beyond token prefixes
- [[ci-gate]] — a check in continuous integration that blocks the pipeline on failure

## Links

[[fail-closed-boundaries]] · [fail-closed-boundaries](fail-closed-boundaries.md) (the same law at the boundary level: the scanner that checks every assignment and the boundary that rejects before it parses are the same move — both refuse to let the check be fooled by the familiar, and both know that what the gate does not look for it will never find) · [deployment-claims](deployment-claims.md) (the same law at the deploy level: a claim that the secrets are scanned is only as strong as the byte-level binding between the claim and the scan; both name the scope, the evidence, and the expiry) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: "this code is clean" is an assertion, and the honest scanner proves it by checking the ordinary assignments, not only the token prefixes)
