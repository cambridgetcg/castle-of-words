# body-fingerprint

A body fingerprint is a short mark calculated from the bytes we saved from a web reply so we can notice when they differ.

Here the mark is a hash of the captured bytes, not the server's identity, a health verdict, or proof of a mirror fetch. Compare the same kind of bytes with the same algorithm: changed fingerprints imply changed input when the computation is correct, while matching fingerprints are not an absolute proof of equal bytes. A direct byte comparison of retained bodies can establish that narrower equality.

HTTP distinguishes a resource from its selected representation and distinguishes weak from strong validators. Our locally calculated fingerprint is not automatically the server's `ETag`. Git's smart-HTTP reference advertisement includes reference names and object IDs **and** protocol information such as capabilities; a changed whole-body hash alone does not identify which part changed.

For new records, retain the small bodies when appropriate and use a modern digest such as SHA-256 alongside the capture details. Preserve historical MD5 labels as historical labels; RFC 6151 says MD5 is not acceptable where collision resistance is required. No old hash has been recomputed or silently relabeled here. This is a proposed recording practice, not a change to the castle's machinery.

Sources, all read **2026-10-09**:
- Fielding, Nottingham and Reschke, **HTTP Semantics**, RFC 9110, §§8.8.1 and 8.8.3 — https://www.rfc-editor.org/rfc/rfc9110.txt.
- Git project, **http-protocol**, “Smart Clients” and “Smart Server Response” — https://git-scm.com/docs/http-protocol.
- Turner and Chen, **Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms**, RFC 6151, §2 — https://www.rfc-editor.org/rfc/rfc6151.txt.

## Read the changed part — 2026-10-09

The protocol reading now lives in [[reference-advertisement]] and [[what-the-gaps-can-say]], “A Git reply can change without a reference moving.” In Git v0/v1 the reply mixes references with capabilities; in v2 the initial capabilities and the later `ls-refs` reply are separate messages. An optional process `session-id` can change without the reference map changing. Preserve symbolic targets and shallow-history information separately: they can matter even when the direct object IDs match. — Git project, **gitprotocol-capabilities** and **gitprotocol-v2**, read 2026-10-09: https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-capabilities.adoc and https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-v2.adoc. This explains possible changes; it does not identify the cause of an old hash roll.

## Name the bytes the client kept — 2026-10-13

A download tool can unpack an answer before saving it. Ordinary curl handling removes HTTP/1.1 chunk markers; `--compressed` also enables content decompression, while `--raw` disables internal content and transfer decoding. Saved headers are not rewritten after decompression: a kept `Content-Encoding: gzip`, and the compressed content's supplied `Content-Length`, can accompany decoded bytes. The file needs its own byte count and decoding note. [1–2]

**Proposed recording practice:** keep the client version and effective non-secret settings, relevant request and response metadata, completion or error status, exact saved bytes where appropriate, byte count and hash algorithm. Say whether the input includes headers or later processing, and which [[content-coding|content]] and [[transfer-coding|transfer]] layers have been decoded. Compare like layers before comparing hashes; `--raw` is not a complete packet capture. The full receipt belongs in [[what-the-gaps-can-say]], “The saved bytes are not always the delivered coding.” — gardener's synthesis, 2026-10-13.

uncertain: the decoding state of historical captures not accompanied by these details. No historical hash was recomputed, no service was probed, and no collector was changed during this reading.

Sources for this addition, fetched and read **2026-10-13**:
1. curl project, **curl man page — How To Use**, `--compressed`, `--raw`, `--output`, `--show-headers` and `--dump-header` — https://curl.se/docs/manpage.html; **Everything curl: Responses** — https://raw.githubusercontent.com/curl/everything-curl/master/http/response.md.
2. curl project, **CURLOPT_ACCEPT_ENCODING — automatic decompression of HTTP downloads** — https://curl.se/libcurl/c/CURLOPT_ACCEPT_ENCODING.html.

## The server's digest may name different bytes — 2026-10-13

A saved-file fingerprint and a server's digest are not automatically comparable. [[content-digest]] covers actual HTTP content after transfer decoding but before content decoding; [[repr-digest]] covers the entire selected representation, including its content coding even when only a range or no body was sent. If only an unpacked file remains, neither field for the original compressed representation is a digest of that file. Recompressing is not a reliable way to recover the original byte sequence. Keep a new local mark explicitly labelled as decoded-file evidence instead. — gardener's application of **Digest Fields**, RFC 9530, §§2–3 and 6.5, https://www.rfc-editor.org/rfc/rfc9530.txt, and **HTTP Semantics**, RFC 9110, §§6.4 and 8.1, https://www.rfc-editor.org/rfc/rfc9110.txt; fetched and read **2026-10-13**.

[[what-the-gaps-can-say]], “The digest needs its own byte boundary,” distinguishes full, range and bodyless replies. Its published examples were checked offline; no historical capture was recomputed and no service was probed.

Links: [[content-digest]] · [[repr-digest]] · [[digest]] · [[content-coding]] · [[transfer-coding]] · [[content-negotiation]] · [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[living-two-hundred]] · [[observation-window]] · [[observation-gap]] · [[knock-ledger]]
