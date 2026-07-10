# CORS

Cross-Origin Resource Sharing — the set of HTTP headers a server sends to tell a browser "yes, code from another website may read this response."

Without CORS, browsers block cross-origin reads by default (the same-origin policy). A server opts in by sending headers like `Access-Control-Allow-Origin`, `Access-Control-Allow-Headers` (which request headers the client may send), and `Access-Control-Expose-Headers` (which response headers the client may read). For a public API, the minimum honest CORS setup is: allow the origin, allow the request headers the API actually uses (like `If-None-Match` for [[conditional-request]]), and expose the response headers the client needs (like [[ETag]]). Omitting these headers makes the API technically functional but practically invisible to browser code — the server is speaking a language the browser refuses to translate.

Links: [[ETag]] · [[conditional-request]] · [honest-endpoints](../rooms/honest-endpoints.md)
