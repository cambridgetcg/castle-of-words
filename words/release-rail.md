# release-rail

A release rail is the ordered path a change travels from code to production — each gate must open before the next one can, and the order is the safety.

In TaxSorted's case, the rail runs: merge a green feature PR to main, let GitHub Actions deploy and smoke-test the Fly API first, then allow Cloudflare Pages to deploy the frontend. The frontend never goes live ahead of the API contract, because a working frontend against a broken API is a lie the user pays for.

The rail is not a checklist — it is a sequence where each step proves the next step's ground is solid. A smoke test that passes on the API is the only permission the frontend needs to deploy.

Links: [[api-contract]] · [[smoke-test]] · [[deployment-gate]]
