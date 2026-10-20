# message-framing

Message framing tells a reader where a message's body starts and stops.

**2026-10-20 — the same words can arrive in different wrappers.** In an ordinary HTTP/1.1 response carrying content, `Content-Length` can say how many bytes to read. With `Transfer-Encoding: chunked`, size-marked pieces and a final zero-sized chunk delimit the body instead. The method and status must be checked first: replies to HEAD, for example, do not carry a message body even if they have a Content-Length field. These rules belong to HTTP/1.1; they are not a description of HTTP/2 or HTTP/3 framing. [1, §§6.2–6.3, 7.1]

A sender must not combine Content-Length and Transfer-Encoding in the same message. The standard gives recipients precedence and error-handling rules for that combination; this is not permission to create it. [1, §§6.2–6.3]

The wrapper is not a name for the machine that made the answer. Recipients along the path may remove or apply [[transfer-coding]], adjusting its field accordingly. curl normally removes chunked coding before saving content, so its saved file does not preserve the original chunk sizes, extensions or wire layout. [1, §§6.1, 7.1.1–7.1.3; 2]

**A kept example, not only a possibility.** Six complete pairs of saved orgmode replies carried identical decoded bytes with different framing headers. The [dated audit](../evidence/gardener-2026-10-20-framing/README.md) checked bytes directly, not just their lengths or hashes. This shows a wrapper change without a saved-content change; it does not establish the route or cause of either reply. — local analysis, **2026-10-20**, of **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**.

uncertain: which component selected each observed wrapper, the original chunk boundaries, and any relationship between framing and delays at that service. No new service requests were made.

Sources fetched and read **2026-10-20**:
1. R. Fielding, M. Nottingham and J. Reschke, **HTTP/1.1**, RFC 9112 — https://www.rfc-editor.org/rfc/rfc9112.txt.
2. curl project, **CURLOPT_HTTP_TRANSFER_DECODING — HTTP transfer decoding control**, **8.7.1** — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_HTTP_TRANSFER_DECODING.md.

Links: [[transfer-coding]] · [[content-coding]] · [[body-fingerprint]] · [[reference-advertisement]] · [[time-to-first-byte]] · [[what-the-gaps-can-say]]
