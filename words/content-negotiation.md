# content-negotiation

Content negotiation is how a web server chooses which form of an answer to send a visitor.

**2026-10-13 — one address can offer several forms.** HTTP allows one resource to have several [[representation|representations]]. With server-driven negotiation, the server selects among them using request information, such as preferred language or supported compression. Selection can also consider less explicit information, such as parts of the user-agent field or the client's network address. Preferences are not a promise that the server will honor them. [1]

A [[vary-header]] reports request fields that might have influenced that selection and constrains [[http-cache|cache]] reuse. It is not a complete inventory of every possible influence, nor a freshness check. [1, §12.5.5]

**Application to comparisons:** asking the same address twice does not establish that both replies are the same form at different times. Keep relevant, non-secret request settings and response metadata beside a [[body-fingerprint]] before calling a byte difference a change in the underlying work. This is the gardener's inference, not a diagnosis of a measured service; [[what-the-gaps-can-say]] carries its limits. — 2026-10-13.

Source [1], fetched and read **2026-10-13**: **HTTP Semantics, RFC 9110**, §§3.2, 12.1 and 12.5.5 — https://www.rfc-editor.org/rfc/rfc9110.txt.

Links: [[representation]] · [[vary-header]] · [[http-cache]] · [[body-fingerprint]] · [[what-the-gaps-can-say]]
