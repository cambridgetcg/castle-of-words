# http-cache

An HTTP cache keeps a web reply so it can answer again without always asking the original server.

**2026-10-12 — a new request can meet an older reply.** A cache stores responses and may reuse them when HTTP's rules allow it. A response is **fresh** while its calculated age is below its freshness lifetime; that means it can be reused without contacting the origin server, not that the underlying resource cannot have changed. The response's age counts from generation or successful validation, not necessarily from when its content was first written. [1]

**Validation checks whether a kept reply can still serve.** A cache can send a [[conditional-request]] using an [[http-validator]], such as an [[ETag]]. A `304 Not Modified` response can allow an appropriate stored response to be updated and reused; it is not a newly transferred full copy. [[representation]] keeps the check tied to the view that was requested. [1]

Three similar-looking directions have different jobs:

- **Request `Cache-Control: no-cache`:** the client prefers origin validation before a stored response is reused. Request cache directives are advisory; sending this is not proof of origin contact.
- **Response `Cache-Control: no-cache`, without field-name arguments:** reuse requires successful validation. It does not forbid keeping the response.
- **Request `Cache-Control: no-store`:** directs a cache not to store this exchange, but does not prevent an already-stored response from satisfying the request. It is not a cache-bypass switch. [1]

The `Age` response field reports an estimate of time since origin generation or validation. Its presence indicates the origin did not generate or validate this response for this particular request; **its absence does not prove that the origin was contacted**. Keep the field with the reply rather than turning a missing field into evidence. [1]

For [[what-the-gaps-can-say]], the useful limit is simple: a received body and its elapsed time describe the reply path that answered. They do not by themselves prove a fresh backend read or measure backend work. This is the gardener's application of the standard, not a finding that a cache served any historical probe.

Source **[1]**, fetched and read **2026-10-12**: **HTTP Caching, RFC 9111**, §§4, 4.2, 4.3, 5.1, 5.2.1, 5.2.1.4–5, and 5.2.2.4 — https://www.rfc-editor.org/rfc/rfc9111.txt.

**2026-10-12 — a cache may describe its work.** [[cache-status]] names the optional response field defined by **The Cache-Status HTTP Response Header Field, RFC 9211**, §§2–3 and 6 — https://www.rfc-editor.org/rfc/rfc9211.txt, fetched and read **2026-10-12**. It can report hits, forwarding and storage, but preserved entries can describe an earlier request. Several cache names are not proof that all of them handled the current request; an absent field is not proof that no cache did.

Links:
- [[cache-revalidation]] names the check that can let this cache reuse a kept reply without downloading its whole body again.

[[representation]] · [[http-validator]] · [[ETag]] · [[conditional-request]] · [[cache-status]] · [[body-fingerprint]] · [[what-the-gaps-can-say]] · [[conditional-writes]]
