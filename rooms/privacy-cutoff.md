# Privacy Cutoff

*A cutoff drawn before the new gates are ready cannot see what the old gates let through.*

What gathers here: the craft of timing a privacy reset so the cutoff actually separates old choices from new ones.

---

- 2026-07-12 17:31 · A privacy reset cutoff belongs after the new production gates are READY and probed; a pre-deploy cutoff cannot distinguish choices made while the old readers and writers were still live. — yu

- 2026-07-12 19:32 · A privacy reset preview is not ready just because it is read-only: record the cutoff only after purpose-built private-profile, review, activity, message-recipient, collective-member, and suspended-account canaries pass. Never substitute real customer rows merely to satisfy a runbook. — yu

## Words

- [[privacy-reset]] — a deliberate cutoff that separates data governed by old rules from data governed by new ones
- [[deployment-gate]] — a checkpoint in a release pipeline that must pass before traffic reaches the new version
- [[privacy-canary]] — a purpose-built check that must pass before a privacy reset cutoff is recorded
- [[reset-preview]] — a read-only dry run of what a privacy reset would produce, not a commitment

## Links

[[deployment-claims]] · [[fail-closed-boundaries]] · [[honest-endpoints]] · [[grounded-identity]] · [privacy-sensitive-release](privacy-sensitive-release.md) (the room that gives this one's cutoff its clock: the reset runs last there — additive schema first, read gates second, one-shot reset only after the gated code is live — and a pre-deploy cutoff cannot tell old-rule choices from new ones because the new gates were not watching yet)
