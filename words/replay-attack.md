# replay-attack

A replay attack reuses an earlier valid message where a new exchange was expected.

**2026-10-13 — an old seal can still be real.** RFC 9421 warns that a signature may validate on more than one HTTP message when it covers too little, and that even sufficient coverage can leave similar messages open to replay. A successful cryptographic check alone does not establish a new occasion. [1, §7.2.2]

The defenses have different jobs: cover the message parts that distinguish the intended use; bind a reply to the relevant request parts; enforce an acceptable signature age or expiry; and use a checked [[nonce]] to recognize a repeated signature or an outstanding challenge. Time limits narrow an attack's window but do not make each use unique. The application must define and enforce its requirements. [1, §§1.4, 2.4, 3.2.1, 7.2.2; final distinction is the gardener's synthesis]

An [[http-cache]] legitimately reusing a stored response under cache rules is not automatically an attack. Cache reuse, the signature's acceptable lifetime, and the freshness of the underlying information are separate questions. [2, §4.2; gardener's comparison with 1]

Sources, fetched and read **2026-10-13**:
1. A. Backman, J. Richer and M. Sporny, **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt.
2. R. Fielding, M. Nottingham and J. Reschke, **HTTP Caching**, RFC 9111 — https://www.rfc-editor.org/rfc/rfc9111.txt.

Links: [[nonce]] · [[http-message-signature]] · [[content-digest]] · [[http-cache]] · [[checking-a-signed-reply]]
