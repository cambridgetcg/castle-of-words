# deployment-gate

A checkpoint in a release pipeline that must pass before traffic reaches the new version.

A deployment gate is not the same as a CI check. The gate lives at the boundary between the old version and the new one — it may be a smoke test, a health probe, a canary deployment, or a manual approval. The honest gate is probed after deployment, not before, because only live traffic can reveal whether the new gates are actually ready.

Links: [[privacy-reset]] · [[deployment-claims]] · [[fail-closed-boundaries]]
