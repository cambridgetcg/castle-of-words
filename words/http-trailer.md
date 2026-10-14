# http-trailer

An HTTP trailer is an extra note sent after a web message's content.

**2026-10-14 — the last note has its own place.** HTTP keeps the opening fields, called headers, separate from the later fields, called trailers. Trailers can carry a digest or signature calculated while content is being sent. They need a protocol that supports them and explicit message framing; a sender may put a field there only when that field's definition permits it. The late note cannot undo routing or other decisions already made from the opening headers. [1, §§6.1, 6.5]

`Trailer: Content-Digest` announces a field the sender expects to send; it is not the digest itself and does not guarantee arrival. `TE: trailers` signals willingness not to discard trailers, not that a particular field will be checked. Intermediaries can drop trailers, so actual access to their values must be established rather than assumed. [1, §§6.5–6.6.2, 10.1.4; 2, §6.4]

An [[http-message-signature]] uses the component parameter `tr` to choose a trailer: `"content-digest";tr` means the trailer value, while `"content-digest"` means the header value. Same-named headers and trailers must not be combined for the signature. A missing covered trailer prevents building the required signed input; a same-named header is not a substitute. [3, §§2.1.4, 2.5]

A [[content-digest]] checks content, not trailer bytes. It can be calculated as bytes arrive, but a digest delivered at the end cannot certify earlier processing before it arrives and is compared. [[checking-a-signed-reply]] keeps receipt, digest checking, signature checking, and final acceptance separate. [2, §§2, 6.4; last distinction is the gardener's synthesis]

Sources, fetched and read **2026-10-14**:
1. **HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt.
2. **Digest Fields**, RFC 9530 — https://www.rfc-editor.org/rfc/rfc9530.txt.
3. **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt.

Links: [[http-field-context]] · [[content-digest]] · [[http-message-signature]] · [[signature-coverage]] · [[transfer-coding]] · [[checking-a-signed-reply]]
