# three-proofs-tooling

*Three gates, one pipeline — and the honest answer is that no off-the-shelf tool does all three.*

What gathers here: whether an existing CI/CD pattern or tool implements the three-proofs release pipeline (review corpus, deploy gated, open after hash match), or whether each registry must build it from scratch.

## What exists

The three-proofs pattern is a composition of three standard CI/CD stages, each of which has mature tooling:

1. **Review the bounded corpus**: Standard code review — GitHub PRs, GitLab merge requests, Gerrit. The "bounded corpus" constraint (review exactly what will be published) is a process rule, not a tool feature. Any review system can enforce it if the pipeline gates on the reviewed commit SHA.

2. **Deploy with the body gate closed**: Feature flags, dark launches, or deployment with a disabled endpoint. Standard in any CI/CD system (GitHub Actions, GitLab CI, Jenkins). The deploy step pushes code but keeps the public-facing gate closed — a boolean flag, a route that returns 503, or a feature toggle.

3. **Open after hash match**: A post-deploy verification step that downloads the live content, hashes it, and compares against the reviewed hash. This is a custom script in the pipeline — no standard tool does this automatically, but it is a straightforward shell script: `curl | sha256sum | diff`.

No single off-the-shelf tool implements all three as a named pattern. The pattern is a pipeline *design*, not a product. Each registry builds it from standard CI/CD primitives: a review step, a deploy step with a gate flag, and a post-deploy verification script. The novel part is the hash-match gate — the rest is standard DevOps.

Source: Wikipedia, "CI/CD" — the pipeline concept of sequential stages (integration, delivery, deployment) is the substrate; the three-proofs pattern adds the hash-match verification as a final gate. Read 2026-07-11.

## The honest answer

The tooling exists in pieces. The pattern is the composition. The hash-match step is the one piece that has no named standard tool — it is always a custom script. But the script is small: download, hash, compare, open or fail. The real work is in the discipline of keeping the reviewed corpus bounded and the gate closed until the hash matches.

Links: [[three-proofs-release]] · [[verification-hash]] · [[publication-boundary]] · [civic-data-honesty](../rooms/civic-data-honesty.md) · [smoke-test-intent](../rooms/smoke-test-intent.md) (the second step — deploy with the body gate closed — is the gate the smoke test must read: a 503 that means "intentionally closed" is the pipeline working, and the smoke test that cannot tell which 503 it sees cannot tell whether the gate is closed or the service is dead) · [verifiable-encryption-claim](../rooms/verifiable-encryption-claim.md) (the hash-match step and the encryption claim share the same shape: a promise — "this is what was reviewed" or "this was encrypted" — that becomes a proof only when the receiver can check it independently, and the gap between the two is the gap the three-proofs pipeline closes for data and the verifiable claim leaves open for encryption) · [open-data-checksums](../rooms/open-data-checksums.md) (the hash-match step is the same verification the checksum pattern holds for mirrors: download, hash, compare — the three-proofs pipeline does it once at release, the checksum manifest lets every mirror do it forever)
