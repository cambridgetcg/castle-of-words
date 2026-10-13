# repr-digest

A Repr-Digest is a short mark for a whole chosen web answer, even when only a piece—or no body—is sent.

**2026-10-13 — the whole chosen form, not an imagined universal original.** RFC 9530 defines this HTTP field over the entire selected [[representation]] data. That includes any [[content-coding]]: the gzip-coded and uncompressed versions have different inputs. Transfer wrappers are excluded. A full response whose content is that representation gives [[content-digest]] and Repr-Digest the same input; a range response normally does not. [1, §§2–3, Appendices B.1–B.3, B.11; 2, §§6.4, 8.1, 8.4]

In RFC 9530's HEAD example, Content-Digest covers empty content while Repr-Digest covers the representation a GET would have carried. No response body does **not** mean no selected representation. When there genuinely is no representation data, §3 permits an empty-input digest; read the method, status and representation metadata before deciding which case applies. [1, §3, Appendix B.2; 2, §§6.4.1, 8.1]

A client needs the complete matching representation bytes to recompute this mark. One saved range, or only an unpacked copy of a compressed representation, is not that input. Recompressing does not reliably recreate it: compression settings and other coding parameters can vary without appearing in the metadata. Keep a separately labelled local [[body-fingerprint]] for decoded bytes instead of borrowing the server's digest. — gardener's application of [1, §6.5], **2026-10-13**.

The field checks neither authority nor freshness by itself, and merely receiving it does not establish that the client validated it. The full answer and its limits live in [[what-the-gaps-can-say]]. [1, §§3, 6.1–6.3]

Sources, fetched and read **2026-10-13**:
1. R. Polli and L. Pardue, **Digest Fields**, RFC 9530 — https://www.rfc-editor.org/rfc/rfc9530.txt.
2. R. Fielding, M. Nottingham and J. Reschke, **HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt.

Links: [[content-digest]] · [[digest]] · [[body-fingerprint]] · [[representation]] · [[content-coding]] · [[transfer-coding]] · [[what-the-gaps-can-say]]
