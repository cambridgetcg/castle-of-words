# vary-header

A Vary header is a server's note about which parts of your request may affect the answer it chooses.

**2026-10-13 — a matching rule, not a clock.** HTTP's `Vary` response field names request fields, beyond the method and target address, that might have influenced selection of a [[representation]]. For example, `Vary: Accept-Encoding` identifies the request's compression preferences as a possible influence. It does not say the content changed over time. [1]

For a stored reply carrying Vary, a [[http-cache|cache]] must not reuse it without revalidation unless the named request fields match. Matching allows only the transformations the fields' syntax and meaning permit; an absent field matches absence, not a supplied value. A value containing `*` always fails this matching test. That is not a blanket prohibition on storing the reply. [2]

A missing Vary field does not prove that every visitor receives identical content: RFC 9110 expressly permits some variation to go unlisted. Matching fields also does not prove current content, backend contact, or a shared cause for two responses. Those are separate questions about [[content-negotiation]], [[cache-revalidation]], and evidence. [1–2; final limits applied by the gardener]

Sources, fetched and read **2026-10-13**:
- **[1] HTTP Semantics, RFC 9110**, §12.5.5, “Vary” — https://www.rfc-editor.org/rfc/rfc9110.html#section-12.5.5.
- **[2] HTTP Caching, RFC 9111**, §4.1, “Calculating Cache Keys with the Vary Header Field” — https://www.rfc-editor.org/rfc/rfc9111.txt.

Links: [[content-negotiation]] · [[representation]] · [[http-cache]] · [[cache-revalidation]] · [[body-fingerprint]] · [[what-the-gaps-can-say]]
