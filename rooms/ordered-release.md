# ordered-release

*The frontend never goes live ahead of the API contract, because a working frontend against a broken API is a lie the user pays for.*

What gathers here: the craft of ordering deployments so each step proves the next step's ground is solid — the release rail that turns a sequence of deploys into a chain of trust.

Built understanding from yu, 2026-07-15:

- 2026-07-15 20:36 · TaxSorted production has one ordered [[release-rail]]: merge a green feature PR to main, let GitHub Actions deploy and [[smoke-test]] the Fly API first, then allow Cloudflare Pages; do not deploy the frontend directly ahead of the [[api-contract]]. — yu

The rail is not a checklist — it is a sequence where each step proves the next step's ground is solid. A smoke test that passes on the API is the only permission the frontend needs to deploy. The frontend that deploys before the API has been proven is standing on a promise that has not been kept.

This is the same law the castle's honesty rooms trace at every altitude: a claim (the API works) must be backed by a test (the smoke test passed) before anything else is built on it. The ordered release rail is the law of honest assertion applied to the deployment pipeline — each gate opens only when the gate before it has proved its ground.

Links: [[release-rail]] · [[api-contract]] · [[smoke-test]] · [[deployment-gate]] · [smoke-test-intent](smoke-test-intent.md) (the second channel that tells the smoke test whether a 503 is intentional) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law at the deployment level: a claim backed by a test before anything is built on it) · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: the API that names what it serves)
