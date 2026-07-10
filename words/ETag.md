# ETag

A short string a server attaches to a response that changes whenever the content changes — like a version fingerprint the client can hold up later and ask "still the same?"

It is the mechanism behind [[conditional-request]]: the server generates it (often a hash of the response body), the client stores it, and on the next request the client sends it back in an `If-None-Match` header. If the ETag matches, the server says `304 Not Modified` and sends nothing — the client knows its cached copy is still fresh. An ETag only works across origins if the server also exposes it via CORS headers; without `Access-Control-Expose-Headers: ETag`, the browser keeps the fingerprint to itself and client code never sees it.

Links: [[conditional-request]] · [[CORS]] · [honest-endpoints](../rooms/honest-endpoints.md)
