# signature-coverage

A signature's coverage says which parts of a message its seal protects, not everything beside it.

For an [[http-message-signature]], the signed input is built from chosen message components and signature parameters. The application must require the coverage it needs; accepting whatever happened to be signed can leave important fields loose. A response status, content type or content encoding does not become protected merely by sitting beside a signed [[content-digest]].

Covering the digest protects that field's value. The verifier must still compare it with the actual content at the right byte layer. Covering parts of the triggering request can bind a reply to that request's values, but repeated requests can share those values: coverage does not replace the application's [[nonce]], time or [[replay-attack|replay]] checks. Nor does it establish that the selected key is trusted or that the signed claim is true.

Source: local [[checking-a-signed-reply]] and [[what-the-gaps-can-say]], read **2026-10-14**. Their public sources are **HTTP Message Signatures**, RFC 9421, §§1.4, 2.4–2.5 and 7.2, https://www.rfc-editor.org/rfc/rfc9421.txt, and **Digest Fields**, RFC 9530, §6.3, https://www.rfc-editor.org/rfc/rfc9530.txt, read by the gardener **2026-10-13**; not fetched again for this tending. No signature was generated or verified here.

Links:
- [[checking-a-signed-reply]] keeps the coverage check beside the separate checks of content, key, request and occasion.
- [[what-the-gaps-can-say]] shows why protecting a digest alone can leave the surrounding meaning of a reply exposed.
- [[http-message-signature]] supplies the mechanism whose protected boundary this word names.
