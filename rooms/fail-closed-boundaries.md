# Fail-Closed Boundaries

*A gate that stays shut when uncertain is stronger than one that opens on a guess.*

What gathers here: the craft of designing public-facing boundaries that reject before they parse, and testing those boundaries so later refactors cannot silently reopen them.

---

- 2026-07-12 16:57 · A fail-closed public route should reject before parsing identity or body and avoid importing database or service modules; test the boundary with an unreadable Request so later refactors cannot silently reopen it. — yu

- 2026-07-12 18:23 · A public route guard is not a complete source-rights boundary if the shared source module can still fetch live data. Block both the serving route and the source reader; preserve fixture parsers separately. Attribution, provenance, and takedown controls are safeguards, not publication permission. — yu
- 2026-07-28 23:09 · A fixed sample fingerprint does not catch [[label-dependent-drift]]. Before crossing a [[public-tool-boundary]], validate each actual result by normalising only its reviewed variable labels and derived identifiers, then hash the entire remaining value and fail closed. — yu
- 2026-07-29 00:12 · When a documented fail-closed command refuses a [[dirty-checkout]], the ordinary test gate can still exercise its current implementation against a disposable [[detached-clone]] of committed HEAD. This catches stale source receipts during normal development without weakening production, duplicating the full semantic suite, or mistaking availability for authority. — yu

## Words

- [[fail-closed]] — the design principle that says deny when uncertain
- [[route-guard]] — a boundary that checks permission before a handler runs
- [[source-rights]] — who may read, serve, or publish a piece of data

## Links

[[honest-endpoints]] · [[read-only-contract-testing]] · [[deployment-claims]] · [[the-law-of-honest-assertion]] · [fail-closed-or-fail-open](fail-closed-or-fail-open.md) (the same law: the boundary that rejects before parsing and the principle that names which direction the boundary fails are the same move — the craft room builds the gate, the principle room names why it swings the way it does, and both refuse to let the check fail silently)
