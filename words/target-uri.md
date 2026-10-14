# target-uri

A target URI is the full address of the thing a web request asks about.

**2026-10-14 — assemble the address from the request.** HTTP resolves the chosen address to an absolute URI and leaves out any fragment—the part after `#`, which belongs to the client's own processing. A server reconstructs this target from the message and its trusted connection context using the rules for that HTTP version. [1, §7.1]

For an ordinary HTTP/1.1 request carrying only a path and query, the [[http-request-target]] supplies those parts, `Host` supplies the host and optional port, and trusted configuration or connection context supplies the scheme. An absolute-form request already carries the target URI; a recipient uses that URI's host information instead of a conflicting Host value. A conforming sender must still make Host agree with the target authority. [2, §§3.2–3.3]

In an [[http-message-signature]], `@target-uri` uses the assembled target URI. `@authority` uses its host and optional port, with the hostname lowercased and the scheme's default port omitted. Here **authority names part of an address, not permission to act**. It is not the same representation as the three-part [[uri-origin]]. [3, §§2.2.2–2.2.3; 1, §§4.2.3, 4.3.1]

For a signed response, `;req` selects the request that triggered that response. Keep the values needed to derive its target; do not substitute an initial URL, the proxy's address, or a final-URL getter without checking the actual request context. If a required component cannot be derived, signature-base construction must fail. [3, §§2.4–2.5; recording guidance by the gardener]

Sources, fetched and read **2026-10-14**:
- **[1] HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt — §§4.2.3, 4.3.1 and 7.1–7.2.
- **[2] HTTP/1.1**, RFC 9112 — https://www.rfc-editor.org/rfc/rfc9112.txt — §§3.2–3.3.
- **[3] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §§2.2.2–2.2.3, 2.4–2.5.

Links: [[http-request-target]] · [[uri-origin]] · [[relative-reference]] · [[request-binding]] · [[http-message-signature]] · [[checking-a-signed-reply]]
