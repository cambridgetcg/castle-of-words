# transfer-coding

Transfer coding is a way of wrapping a web message for delivery, such as sending it in size-marked pieces.

**2026-10-13 — the delivery wrapper is not the saved content.** In HTTP/1.1's `chunked` coding, the response arrives in pieces marked with their sizes, followed by a zero-sized final chunk. curl normally decodes this wrapper and does not put the size markers in its body output. This allows delivery to begin without first knowing the whole content's length. [1–2]

Transfer coding can also compress the data. curl's `--tr-encoding` requests compressed transfer encoding and decodes it on receipt. It is separate from `--compressed`, which requests compression through [[content-coding|Content-Encoding]]. [1, 3]

`--raw` disables curl's internal decoding of content and transfer encodings, so an HTTP/1.1 chunked reply retains its chunk markers in the output. That is a decoder choice, not a promise to save the entire network conversation or its transport framing. Displayed HTTP/2 and HTTP/3 headers are themselves rendered in a readable form, not preserved as their compressed wire bytes. [1, 3–4; packet-capture distinction is the gardener's interpretation of the documented output boundary]

**Application:** keep the received `Transfer-Encoding`, the client's decoding settings, the saved byte count, and the exact input to a [[body-fingerprint]]. Compare the same layer on both sides. A different wrapper and different content are different claims. — gardener's proposed recording practice, 2026-10-13; no collector changed.

Sources, fetched and read **2026-10-13**:
1. curl project, **Everything curl: Responses**, “Chunked transfer encoding,” “Transfer encoding” and “Pass on transfer encoding” — https://raw.githubusercontent.com/curl/everything-curl/master/http/response.md.
2. curl project, **CURLOPT_HTTP_TRANSFER_DECODING — HTTP transfer decoding control** — https://curl.se/libcurl/c/CURLOPT_HTTP_TRANSFER_DECODING.html.
3. curl project, **curl man page — How To Use**, `--raw`, `--tr-encoding` and `--compressed` — https://curl.se/docs/manpage.html.
4. curl project, **Everything curl: Compression**, “HTTP headers” — https://raw.githubusercontent.com/curl/everything-curl/master/http/modify/compression.md.

Links: [[content-coding]] · [[body-fingerprint]] · [[representation]] · [[reference-advertisement]] · [[what-the-gaps-can-say]]
