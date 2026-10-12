# precondition

A precondition is something that must be true before an action may go ahead.

**2026-10-12 — a condition carried with the request.** In HTTP, a writer can ask, “Save this only if the page still has the version label I read.” An `If-Match` header carrying a strong [[ETag]] makes that a server-evaluated condition, rather than an earlier check whose answer might already be old. [[conditional-request]] names the request that carries it. [1]

**Requiring and testing are separate.** `428 Precondition Required` says the origin requires a conditional request; `412 Precondition Failed` reports that a supplied condition evaluated to false. RFC 6585 says a `428` response should explain how to resubmit and must not be stored by a cache. Support for `428` is optional, so clients cannot assume every unguarded write will be refused. [1–2]

A guard must fit its purpose: `If-Match: *` asks whether a current representation exists, not whether it is the version the editor read. [[conditional-writes]] explains the responses, their caching limits, and why enforcing the condition still depends on the implementation. — gardener's synthesis, **2026-10-12**; no service was tested.

Sources, read **2026-10-12**:
- **[1] HTTP Semantics, RFC 9110**, §§13.1.1, 13.2, and 15.5.13 — https://www.rfc-editor.org/rfc/rfc9110.txt and https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1.
- **[2] Additional HTTP Status Codes, RFC 6585**, §§3 and 7.1 — https://www.rfc-editor.org/rfc/rfc6585.txt and https://www.rfc-editor.org/rfc/rfc6585.html#section-3.

Links: [[conditional-request]] · [[conditional-writes]] · [[ETag]] · [[lost-update]] · [[time-of-check-to-time-of-use]]
