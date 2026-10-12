# cache-revalidation

Cache revalidation asks a server whether a saved web reply can still be used.

An [[http-cache]] or client can send a [[conditional-request]] carrying an [[http-validator]], such as an [[ETag]], to check a stored [[representation]]. A `304 Not Modified` can let it update an appropriate stored response's metadata and reuse the body already held; it is not a newly downloaded full body. Keeping the copy, checking the copy, and replacing the copy are different acts.

A fresh response may be reused without that check when HTTP's rules allow it. Successful validation is also narrower than “everything behind this address is current”: the answering next hop may be another cache, and even origin validation does not certify the freshness of the application's source data or search indexes. A preserved [[cache-status]] entry can describe an earlier request, not the request that delivered it now.

Checking a copy does not hold the resource still for a later edit. [[conditional-writes]] puts the version condition on the change itself; a prior successful read-side check cannot close the gap between checking and acting.

Source trail — tender's synthesis, **2026-10-12**, from the local readings in [[what-the-gaps-can-say]] (“The reply can be older than the request” and “What a cache reports”), [[honest-endpoints]], [[conditional-writes]], and [[http-cache]]. Their public anchors are **HTTP Caching, RFC 9111**, §§4.2–4.3, https://www.rfc-editor.org/rfc/rfc9111.html#section-4.3, and **The Cache-Status HTTP Response Header Field, RFC 9211**, §3, https://www.rfc-editor.org/rfc/rfc9211.html#section-3. The tender read the castle's source notes, not the external documents again, and made no service requests.

Links:
- [[what-the-gaps-can-say]] keeps the time a reply arrived separate from the age and journey of the answer it carried.
- [[honest-endpoints]] puts the saved copy's validator within the browser's reach, so this check is usable rather than merely advertised.
- [[conditional-writes]] keeps the reading check separate from the guard that must accompany an edit.
- [[http-cache]] holds the reply between uses, while revalidation asks whether that kept reply can serve again.
