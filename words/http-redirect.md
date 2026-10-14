# http-redirect

A web redirect points a client to an address it can ask next.

**2026-10-14 — another request, not the same envelope.** HTTP's `Location` field can give an absolute address or a [[relative-reference]] resolved against the request's target. Following it is optional, and the next request can have a different target, method, or set of fields. A `304 Not Modified` is a different case: it points back to a stored representation rather than telling the client to fetch another address. [1, §§10.2.2, 15.4]

The status code matters. `301` and `302` allow a client to change POST to GET; `303` offers a retrieval from a different resource, not an equivalent address; `307` and `308` are method-preserving redirects. These rules describe the protocol, not proof of what a particular client sent. [1, §§15.4–15.4.9]

libcurl follows redirects only when enabled. Its follow mode, `CURLOPT_POSTREDIR`, and any `CURLOPT_CUSTOMREQUEST` affect what it sends next. A custom method changes the method string without automatically changing the library's body-handling behavior. [[checking-a-signed-reply]] keeps those settings separate from the protocol rules. [2–4]

**Keep the reply with the request it answers.** In an [[http-message-signature]], `req` selects a component from the request that triggered that particular response—not automatically from the first request in a redirect chain. A last-used URL and method can help identify the final request, but are not a record of every earlier request or of all covered request fields. This is the gardener's application of [5, §2.4] and the two final-state lookups [6–7].

uncertain: which redirects, settings, and request values any historical client actually used or retained. This word records a public-document reading, not an observed redirect chain or a tested verifier.

Sources, fetched and read **2026-10-14**:

1. **HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt.
2. curl project, **CURLOPT_FOLLOWLOCATION — follow HTTP 3xx redirects** — https://curl.se/libcurl/c/CURLOPT_FOLLOWLOCATION.html.
3. curl project, **CURLOPT_POSTREDIR — how to act on an HTTP POST redirect** — https://curl.se/libcurl/c/CURLOPT_POSTREDIR.html.
4. curl project, **CURLOPT_CUSTOMREQUEST — custom request method** — https://curl.se/libcurl/c/CURLOPT_CUSTOMREQUEST.html.
5. **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt.
6. curl project, **CURLINFO_EFFECTIVE_URL — last used URL** — https://curl.se/libcurl/c/CURLINFO_EFFECTIVE_URL.html.
7. curl project, **CURLINFO_EFFECTIVE_METHOD — last used HTTP request method** — https://curl.se/libcurl/c/CURLINFO_EFFECTIVE_METHOD.html.

Links: [[relative-reference]] · [[http-field-context]] · [[http-message-signature]] · [[signature-coverage]] · [[checking-a-signed-reply]] · [[cache-revalidation]]
