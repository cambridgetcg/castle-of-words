# http-field-context

An HTTP field's context tells us which web message a note belongs to and whether it came at the beginning or the end.

**2026-10-14 — keep the note with its letter.** One download can receive an early informational reply, a proxy's tunnel-opening reply, a redirect, and the eventual response, whose own fields can arrive as opening headers or later [[http-trailer|trailers]]. The same field name in these different places is not one interchangeable value. libcurl's `curl_easy_header` separates a request number from an `origin` category; here `origin` means where the library received the field, not proof of who deserves trust. [1–2]

Keep the selected request and response, status, header or trailer section, and ordered repeated values together. The header callback supplies status lines and section boundaries; the lookup supplies request/category selection but no status line or separate identifier for each informational response. This is a proposed recording practice, not a collector tested here. [[checking-a-signed-reply]] gives the documented API limits, including data lifetime, version-dependent unfolding, and builds without the header API. [1–2, 4; inference from the documented interface]

The location matters to an [[http-message-signature]]: a covered `"content-digest"` uses the header, while `"content-digest";tr` uses the trailer. `req` selects a component from the request that triggered the response. Keep these contexts distinct before applying the signature's serialization rules; a flattened dictionary cannot prove that discarded boundaries were preserved. [3, §§2.1.4, 2.4–2.5]

uncertain: what a particular client retained. An available API is not evidence that an application called it, copied its results, or checked a signature. No client or historical capture was tested in this reading.

Sources, fetched and read **2026-10-14**:
1. curl project, **CURLOPT_HEADERFUNCTION — callback that receives header data** — https://curl.se/libcurl/c/CURLOPT_HEADERFUNCTION.html.
2. curl project, **curl_easy_header — get an HTTP header** — https://curl.se/libcurl/c/curl_easy_header.html.
3. **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt.
4. curl project, **libcurl-errors — error codes in libcurl**, `CURLHE_NOT_BUILT_IN` — https://curl.se/libcurl/c/libcurl-errors.html.

Links: [[http-redirect]] · [[http-trailer]] · [[http-message-signature]] · [[signature-coverage]] · [[content-digest]] · [[checking-a-signed-reply]] · [[body-fingerprint]]
