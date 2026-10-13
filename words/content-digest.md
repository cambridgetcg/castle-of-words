# content-digest

A Content-Digest is a short mark that helps check the bytes carried inside one web message.

**2026-10-13 — check the content, not every byte on the connection.** RFC 9530 defines this HTTP field as an algorithm-labelled digest of the actual message content. HTTP content is what remains after message framing and [[transfer-coding]] are removed: chunk sizes, HTTP headers and trailers are not part of the input. [[content-coding]] is different; if the content is gzip-coded, its compressed bytes are the input, not the unpacked text. [1, §2; 2, §§6.4, 8.1, 8.4]

For a single-range `206` response, hash the range actually carried. For a multipart range response, hash the whole multipart content, including its boundaries and part headers. For a response with no content, such as a HEAD response, an included Content-Digest covers the empty byte sequence. [[repr-digest]] instead covers the entire selected representation, which may not have been sent. [1, §§2–3, Appendices B.2–B.3; 2, §§6.4.1, 15.3.7.2]

**A header present is not a check passed.** RFC 9530 permits recipients to ignore digests. A client that checks must use the named algorithm and the correct bytes; an already decompressed file is not the compressed input. Neither an unprotected digest nor a successful comparison authenticates the sender, proves freshness, or explains a mirror fetch. [[what-the-gaps-can-say]] holds the full comparison rule. [1, §§2, 6.1–6.5; final application by the gardener]

**2026-10-13 — signing the mark does not check the content.** RFC 9421 §7.2.8 requires the verifier to check the Content-Digest value against the actual received content as well as checking the signature; otherwise substituted content can pass beside an unchanged signed field. [[checking-a-signed-reply]] adds the separate coverage, key-trust, request and replay checks. — **HTTP Message Signatures**, https://www.rfc-editor.org/rfc/rfc9421.txt — fetched and read **2026-10-13**; no verifier was run.

Sources, fetched and read **2026-10-13**:
1. R. Polli and L. Pardue, **Digest Fields**, RFC 9530 — https://www.rfc-editor.org/rfc/rfc9530.txt.
2. R. Fielding, M. Nottingham and J. Reschke, **HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt.

Links: [[repr-digest]] · [[digest]] · [[body-fingerprint]] · [[content-coding]] · [[transfer-coding]] · [[representation]] · [[http-message-signature]] · [[checking-a-signed-reply]] · [[what-the-gaps-can-say]]
