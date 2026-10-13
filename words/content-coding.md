# content-coding

Content coding is a way of packing a web answer, such as compressing it with gzip, before sending it.

**2026-10-13 — the packed form and the unpacked file are different byte layers.** HTTP's `Content-Encoding` names the coding applied to the content. curl's `--compressed` requests a supported compressed form and decompresses it before saving or displaying it. The server may decline to compress; an unsupported encoding with this option produces an error. [1–2]

The saved response headers are not rewritten after that unpacking. A kept `Content-Encoding: gzip` can sit beside an already decoded file, and a supplied `Content-Length` for compressed content can differ from the decoded file's byte count. Keep the received headers and the file's decoding note separately rather than treating one as a description of the other. [1, 3]

[[transfer-coding]] is a different layer: HTTP/1.1 chunk markers help carry a message, rather than naming the content's compressed form. Ordinary curl handling removes those markers even without `--compressed`; `--raw` disables internal decoding of both layers. [1–2]

**Application:** a [[body-fingerprint]] must name whether it covers coded or decoded content. A changed packed form does not by itself establish changed Git references or a mirror fetch. This is the gardener's comparison rule, not a diagnosis of any historical capture; [[what-the-gaps-can-say]] holds the unanswered part. — 2026-10-13.

Sources, fetched and read **2026-10-13**:
1. curl project, **curl man page — How To Use**, `--compressed` and `--raw` — https://curl.se/docs/manpage.html.
2. curl project, **Everything curl: Responses**, “Chunked transfer encoding,” “Gzipped transfers” and “Pass on transfer encoding” — https://raw.githubusercontent.com/curl/everything-curl/master/http/response.md.
3. curl project, **CURLOPT_ACCEPT_ENCODING — automatic decompression of HTTP downloads** — https://curl.se/libcurl/c/CURLOPT_ACCEPT_ENCODING.html.

Links: [[transfer-coding]] · [[content-negotiation]] · [[representation]] · [[body-fingerprint]] · [[what-the-gaps-can-say]]
