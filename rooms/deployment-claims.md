# deployment-claim

*A claim about what was deployed is only as strong as the chain that binds it to the bytes that actually ran.*

What gathers here: the craft of making honest deployment claims — statements about what code ran where and when, backed by evidence that can be checked, not just asserted.

Built understanding from yu, 2026-07-11 and 2026-07-12:

- 2026-07-11 15:05 · A deployment claim is only as strong as its binding: name the scope, evidence, observation time, and expiry; bind uploaded bytes to the exact version ETag; distinguish successful proxy preservation from failure behavior; and skip mixed traffic when versions use incompatible caches. — yu
- 2026-07-12 12:22 · Cambridge-TCG deployment truth: tcg-wholesale Vercel previews need a Preview-scoped DATABASE_URL or they fail at page-data collection even when production is healthy. Keep Playwright e2e files excluded in apps/wholesale/vitest.config.ts, declare every RewardsPro runtime import directly, and accept the storefront TCGplayer-history 503 only as an explicitly listed [[fail-closed]] deploy-probe contract. Verify custom-domain deployment IDs and run pnpm audit:deploy-verify after merge. — yu
- 2026-07-13 11:18 · A Vercel Sensitive environment value may pull as an empty string even after a successful set. Do not infer runtime absence from the pulled file; verify the dependent behavior through a read-only runtime canary after deployment. — yu
- 2026-08-13 18:04 · Static hosts may override a repository robots.txt route. Verify the live route, keep a document-level noindex directive when needed, and record which boundary the release actually controls. — Codex
- 2026-08-16 23:29 · A successful deployment run proves the workflow completed, not that the new work entered its artifact. Verify the live route and exact bytes; if a local tool should stay local, deploy one honest discovery link instead of mirroring fixtures, drafts, or authority-sensitive records. — Codex
- 2026-08-17 00:22 · A safe Cloudflare Pages Direct Upload door can be static and rollback-ready: generate and hash exact upload inputs, deploy a claim-free resting bundle first, gate on clean origin/main plus live project, Web Analytics, and Functions checks, archive the exact commit, then verify immutable bytes, headers, and the real 404 after each deployment. — Codex

The four bindings, plainly:

1. **Name the scope, evidence, observation time, and expiry.** A claim that says "deployed" without saying *what* was deployed, *how* you know, *when* you checked, and *how long* the claim is good for is not a claim — it is a hope wearing a claim's clothes.

2. **Bind uploaded bytes to the exact version ETag.** The bytes you reviewed are not the bytes that deployed unless you can prove it. An ETag — the server's fingerprint of a specific version — is the binding. If the ETag changes, the claim is void. If you cannot name the ETag, you cannot name the version.

3. **Distinguish successful proxy preservation from failure behavior.** A proxy that preserves the old version during a failed deploy is doing its job, but it is also hiding the failure. The claim must say whether the proxy is serving the intended version or the fallback — and the smoke test must check both.

4. **Skip mixed traffic when versions use incompatible caches.** If a deploy rolls out gradually and the old and new versions share a cache, the cache may serve stale data to the new version or fresh data to the old. The claim must name the cache boundary and refuse to certify any window where the two versions' caches are incompatible.

The law: a deployment claim without binding is a deployment claim without evidence. The binding is not decoration — it is the only part of the claim that can be checked.

Links: [[deployment-claim]] · [[binding]] · [[ETag]] · [[proxy-preservation]] · [[mixed-traffic]] · [[fail-closed]] · [three-proofs-tooling](three-proofs-tooling.md) (the same law at the pipeline level: the hash-match gate is the binding between review and deploy) · [smoke-test-intent](smoke-test-intent.md) (the same law at the health-check level: the smoke test is the observation that binds the claim to the evidence) · [wired-registry](wired-registry.md) (the same law at the registry level: the manifest's hash chain is the binding between publication and verification) · [commit-reveal-limits](commit-reveal-limits.md) (the same law: a deployment claim proves intent but not execution, and a commit/reveal receipt proves recorded consistency but not unbiased selection — both name the exact point where the binding to independent evidence stops) · [ordered-release](ordered-release.md) (the same law made operational: the release rail is the binding between merge and deploy, and the deployment claim is the binding between the bytes that ran and the claim that they ran — both refuse to let the claim float free of its evidence)
