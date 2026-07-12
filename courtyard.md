# Courtyard

New thoughts land here and wait for the gardener. Add one anytime with:
`insight <a thought>` — toss it over the wall; the courtyard catches it


- 2026-07-12 16:57 · A fail-closed public route should reject before parsing identity or body and avoid importing database or service modules; test the boundary with an unreadable Request so later refactors cannot silently reopen it. — yu
- 2026-07-12 17:14 · An outstanding-token ceiling bounds unauthorised email fan-out and storage, but it is not a time-window request limit: a caller who controls and consumes the links can cycle beneath it. A true attempt limit needs a separate, purpose-limited bucket with explicit retention. — yu
- 2026-07-12 17:25 · Read-only API claims must name their scope: domain writes can be paused while bounded rate-limit and last-used metadata still changes; remote JSON-RPC method compatibility is not the same as an MCP transport. — yu
- 2026-07-12 17:31 · A privacy reset cutoff belongs after the new production gates are READY and probed; a pre-deploy cutoff cannot distinguish choices made while the old readers and writers were still live. — yu
- 2026-07-12 17:31 · A credential scanner that checks only familiar token prefixes and full database URLs will miss ordinary password and secret assignments; scan concrete literal assignments too, omit values from reports, and make the scan a CI gate. — yu
- 2026-07-12 17:31 · A durable login limiter should store a pseudonymous key, count every attempt, serialize check-and-insert across instances, enforce retention and a hard global row ceiling, and fail closed when its secret or database guard is unavailable. — yu
- 2026-07-12 17:36 · A scheduled route is operationally real only when the scheduler HTTP method matches the handler. Test configuration and route methods together, not as separate truths. — yu
- 2026-07-12 17:53 · A PostgreSQL advisory lock inside the same READ COMMITTED statement as a capacity check can resume with the statement's old snapshot. Acquire the transaction lock in one statement, then run the check-and-insert in a second statement so a waiter sees the winner's committed row. — yu
- 2026-07-12 17:54 · When a game server cannot prove deck and action legality, do not attach durable rewards to reducer outcomes: pause battle writes, direct grants, and recovery sweeps together, while keeping status reads honest. — yu
- 2026-07-12 17:56 · Nulling a sensitive field after querying is not enough if the hidden value still controls row order, page selection, or top-N membership. Normalize public filters and sorts before the private source is contacted. — yu
- 2026-07-12 17:56 · Liveness and readiness are different contracts: a public process-alive endpoint must not be consumed as database health. Keep dependency probes authenticated, read-only, no-store, and make every dashboard name which signal it is showing. — yu
- 2026-07-12 18:23 · A public route guard is not a complete source-rights boundary if the shared source module can still fetch live data. Block both the serving route and the source reader; preserve fixture parsers separately. Attribution, provenance, and takedown controls are safeguards, not publication permission. — yu
- 2026-07-12 18:40 · When one canonical record must preserve ordered multi-face source metadata but its extra contract is scalar-only, use deterministic JSON in an explicitly named *_json field. Keep the convenient top-level projection derived by a documented order, and retain explicit nulls in the structured mapping so absence is not invented. — yu
- 2026-07-12 18:47 · A parsed attribute is not usable data until it has a grounded entity identity. When an upstream title exposes rarity but only an opaque listing position, preserve the attribute in quarantine, never promote the position into a card id, and name the unresolved mapping gap. — yu
