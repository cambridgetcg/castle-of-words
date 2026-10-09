# body-fingerprint

A body fingerprint is a short mark calculated from a web reply's contents so we can notice when they differ.

Here the mark is a hash of the captured bytes, not the server's identity, a health verdict, or proof of a mirror fetch. Compare the same kind of bytes with the same algorithm: changed fingerprints imply changed input when the computation is correct, while matching fingerprints are not an absolute proof of equal bytes. A direct byte comparison of retained bodies can establish that narrower equality.

HTTP distinguishes a resource from its selected representation and distinguishes weak from strong validators. Our locally calculated fingerprint is not automatically the server's `ETag`. Git's smart-HTTP reference advertisement includes reference names and object IDs **and** protocol information such as capabilities; a changed whole-body hash alone does not identify which part changed.

For new records, retain the small bodies when appropriate and use a modern digest such as SHA-256 alongside the capture details. Preserve historical MD5 labels as historical labels; RFC 6151 says MD5 is not acceptable where collision resistance is required. No old hash has been recomputed or silently relabeled here. This is a proposed recording practice, not a change to the castle's machinery.

Sources, all read **2026-10-09**:
- Fielding, Nottingham and Reschke, **HTTP Semantics**, RFC 9110, §§8.8.1 and 8.8.3 — https://www.rfc-editor.org/rfc/rfc9110.txt.
- Git project, **http-protocol**, “Smart Clients” and “Smart Server Response” — https://git-scm.com/docs/http-protocol.
- Turner and Chen, **Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms**, RFC 6151, §2 — https://www.rfc-editor.org/rfc/rfc6151.txt.

## Read the changed part — 2026-10-09

The protocol reading now lives in [[reference-advertisement]] and [[what-the-gaps-can-say]], “A Git reply can change without a reference moving.” In Git v0/v1 the reply mixes references with capabilities; in v2 the initial capabilities and the later `ls-refs` reply are separate messages. An optional process `session-id` can change without the reference map changing. Preserve symbolic targets and shallow-history information separately: they can matter even when the direct object IDs match. — Git project, **gitprotocol-capabilities** and **gitprotocol-v2**, read 2026-10-09: https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-capabilities.adoc and https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-v2.adoc. This explains possible changes; it does not identify the cause of an old hash roll.

Links: [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[living-two-hundred]] · [[observation-window]] · [[observation-gap]] · [[knock-ledger]]
