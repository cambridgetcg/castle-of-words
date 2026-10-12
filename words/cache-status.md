# cache-status

Cache-Status is an optional note in a web reply that explains which saved answers were used and which requests were passed onward.

**2026-10-12 — the cache speaks about its own work.** An [[http-cache]] may add this response field for debugging. Each entry names a cache and can carry details about its handling of the request. Entries run from the cache nearest the origin server to the cache nearest the user; the origin is the server responsible for the requested resource. Adding the field and most details is optional. [1, §2]

The main marks have narrow meanings:

- **`hit`:** this cache reports that it answered from storage without forwarding the request. A hit can serve a stale response; it does not always mean fresh content.
- **`fwd=…`:** this cache reports that it sent the request onward **towards** the origin, with a reason such as `uri-miss` or `stale`. The next server might itself be a cache.
- **`fwd-status=304`:** the next server returned `304 Not Modified` to the forwarded request. The final response to the reader need not have that same status.
- **`stored`:** with `fwd`, this cache reports that it stored the response. That is not a promise of permanent retention.
- **`ttl`:** this cache's calculated remaining freshness time in seconds, which can be negative. It is not a count of seconds since the underlying file changed. [1, §§2.1–2.5; 2, §4.2]

**The list can carry older history.** A nearer cache can save a response containing an upstream cache's entry, then reuse both that response and the entry later. RFC 9211's two-cache example explicitly does this. Several entries therefore do not prove that every named cache handled the reader's current request. [1, §3]

**Silence does not mean no cache.** A cache can omit the field or sensitive details, including for security reasons. Missing information cannot establish a direct origin read. The field reports behavior; it is not an independent check of that behavior or of database and index freshness. That last boundary is the gardener's application of the standard, not a diagnosis of the castle's historical replies. [1, §§2, 6; 2, §§4.2, 5.1]

The fuller reading and the saved-history example live in [[what-the-gaps-can-say]], “What a cache reports.”

Sources, fetched and read **2026-10-12**:

1. Mark Nottingham, **The Cache-Status HTTP Response Header Field**, RFC 9211, §§2–3 and 6 — https://www.rfc-editor.org/rfc/rfc9211.txt.
2. R. Fielding, M. Nottingham and J. Reschke, **HTTP Caching**, RFC 9111, §§4, 4.2 and 5.1 — https://www.rfc-editor.org/rfc/rfc9111.txt.

**2026-10-12 — the neighboring report.** [[proxy-status]] describes an intermediary's handling and errors rather than cache reuse alone. RFC 9211 §2 says a proxy normally should not append its own Cache-Status entry to a locally generated response unless that response is based on storage; RFC 9209 supplies the separate reporting field. Neither field independently verifies its claims. Sources: [1], reread **2026-10-12**, and Mark Nottingham and P. Sikora, **The Proxy-Status HTTP Response Header Field**, RFC 9209 §§1–2 and 4 — https://www.rfc-editor.org/rfc/rfc9209.txt — read **2026-10-12**.

Links: [[proxy-status]] · [[http-cache]] · [[http-validator]] · [[conditional-request]] · [[representation]] · [[body-fingerprint]] · [[what-the-gaps-can-say]] · [[liveness-and-readiness]]
