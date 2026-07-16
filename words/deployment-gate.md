# deployment-gate

A checkpoint in a release pipeline that must pass before traffic reaches the new version — the door that proves the ground before the next step walks on it.

The deployment gate is the law of honest assertion applied to the release pipeline: a claim (the API works, the smoke test passed, the bytes match) must be backed by a test before anything else is built on it. The gate is not a checklist — it is a sequence where each step proves the next step's ground is solid. The ordered release rail is the deployment gate made operational: merge, deploy the API, smoke-test it, and only then deploy the frontend — because a working frontend against a broken API is a lie the user pays for.

Links: [[release-rail]] · [[smoke-test]] · [[api-contract]] · [[fail-closed]]
