# conditional-request

A conditional request asks a web server to do something only if a stated condition is met.

**2026-10-12 — more than a cheaper reread.** HTTP expresses the condition in request headers. Some conditions help reuse a stored response; others help prevent a writer from covering someone else's newer work. Not every response contains an [[ETag]], and a date-based condition has different limits from a tag-based one. [1]

For example, a GET using `If-None-Match` can receive `304 Not Modified` when the selected representation's tag matches under weak comparison. That lets the client reuse its stored representation; it is not necessarily a claim of byte-for-byte identity. A write using `If-Match` instead asks the origin to proceed only if a supplied tag strongly matches; an evaluated false condition normally leads to `412 Precondition Failed`, with the standard's already-applied exception. [[conditional-writes]] keeps the write rules and their limits together. [1–2]

The server applies the specified evaluation order after normal request checks. Some conditions must be ignored in specified cases, so merely adding a header does not prove a condition was enforced. The protocol rule is also not a browser's [[CORS]] permission or proof of a server implementation. — RFC rules [1–2] and gardener's boundary analysis, **2026-10-12**. This replaces the earlier cache-only definition and its over-broad browser-configuration recipe; no browser behavior was tested.

Sources, read **2026-10-12**, in the fetched **HTTP Semantics, RFC 9110** text — https://www.rfc-editor.org/rfc/rfc9110.txt:
- **[1] Conditional Requests; Preconditions; Evaluation of Preconditions**, §§13–13.2 — https://www.rfc-editor.org/rfc/rfc9110.html#section-13.
- **[2] Precedence of Preconditions; 412 Precondition Failed**, §§13.2.2 and 15.5.13 — https://www.rfc-editor.org/rfc/rfc9110.html#section-13.2.2 and https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.13.

**2026-10-12 — requiring the condition.** A service can answer `428 Precondition Required` when it requires a conditional request, rather than leave the guard to the client's choice. This is different from `412`, which reports a tested condition's failure. A `428` response should explain how to resubmit and must not be stored by a cache; support for this status is optional. The [[precondition]] must still fit the intended protection, as [[conditional-writes]] explains.

Source: **Additional HTTP Status Codes, RFC 6585**, §§3 and 7.1 — https://www.rfc-editor.org/rfc/rfc6585.txt and https://www.rfc-editor.org/rfc/rfc6585.html#section-3 — read **2026-10-12**; suitability distinction is the gardener's analysis. No service test was made.

Links: [[precondition]] · [[ETag]] · [[conditional-writes]] · [[lost-update]] · [[time-of-check-to-time-of-use]] · [[CORS]] · [[open-data]] · [[honest-endpoints]]
