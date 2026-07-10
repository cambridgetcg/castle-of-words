# conditional-request

A web pattern where the client asks "has this changed since I last looked?" and the server answers with a quick yes or no instead of sending the whole thing again.

The mechanism: the server stamps each response with an [[ETag]] (a version fingerprint). On the next request, the client sends `If-None-Match: <that-fingerprint>`. If nothing changed, the server returns `304 Not Modified` with an empty body — saving bandwidth and signalling freshness in one round trip. For this to work across origins, the server must also send `Access-Control-Allow-Headers: If-None-Match` and `Access-Control-Expose-Headers: ETag` — without those CORS headers, the browser hides the ETag from JavaScript and blocks the conditional request, making the mechanism invisible to client code even though the server supports it.

Links: [[ETag]] · [[CORS]] · [[open-data]] · [honest-endpoints](../rooms/honest-endpoints.md)
