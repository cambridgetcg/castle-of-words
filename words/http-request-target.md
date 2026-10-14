# http-request-target

A web request carries an address telling the server what it is asking about.

**2026-10-14 — the address actually carried.** In HTTP/1.1, the request-target is the part of the first line between the method and HTTP version. It has four forms: a path with an optional query for ordinary direct requests; a full URI for ordinary proxy requests; a host and port for CONNECT; or `*` for server-wide OPTIONS. The method and connection context decide which form applies. [1, §§3–3.2.4]

The carried part is not always the complete [[target-uri]]. For an ordinary direct request such as `GET /book?page=2 HTTP/1.1`, the path and query still need the `Host` field and the scheme from trusted configuration or connection context. For an absolute-form request, the request-target already supplies the target URI. These are protocol rules; this example is imaginary and was not sent. [1, §3.3]

RFC 9421's `@request-target` uses that request-line part for HTTP/1.1. It is distinct from `@target-uri`, which names the whole target URI. The RFC does not recommend `@request-target` when other HTTP versions might be used, because reconstructing the same form there is harder. [2, §§2.2.2, 2.2.5]

libcurl's `CURLOPT_REQUEST_TARGET` can replace the target it would normally extract from the URL. A saved URL alone therefore does not establish what the request carried. [[checking-a-signed-reply]] works through this distinction without running custom requests. [3; conclusion is the gardener's application]

Sources, fetched and read **2026-10-14**:
- **[1] HTTP/1.1**, RFC 9112 — https://www.rfc-editor.org/rfc/rfc9112.txt.
- **[2] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt.
- **[3] curl project, CURLOPT_REQUEST_TARGET — alternative target for this request** — https://curl.se/libcurl/c/CURLOPT_REQUEST_TARGET.html.

Links: [[target-uri]] · [[uri-origin]] · [[http-message-signature]] · [[request-binding]] · [[http-redirect]] · [[checking-a-signed-reply]]
