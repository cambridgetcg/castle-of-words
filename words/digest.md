# digest

A digest is a short mark made from data to help check whether that data changed.

**2026-10-13 — name the algorithm and the input.** In HTTP's digest fields, the mark comes with its algorithm's name. [[content-digest]] covers one message's content; [[repr-digest]] covers the entire selected representation. Neither automatically covers a client's decoded file. RFC 9530 allows both strong cryptographic algorithms and deprecated weaker checksums for limited non-adversarial uses; “digest” alone does not promise cryptographic strength. [1, §§1.4, 2–3, 5]

**Correction:** the earlier brick called every digest cryptographic and said matching marks prove equal bytes. Those claims were too strong. Different inputs can share a hash, and an attacker who can replace both the data and an unprotected digest can preserve a successful comparison. Matching marks do not prove safety, authority, freshness, or that the chosen object was the right one. Keep the input boundary and trust boundary beside the [[receipt]]. [1, §§5, 6.1–6.3; correction and application by the gardener]

Source, fetched and read **2026-10-13**:
1. R. Polli and L. Pardue, **Digest Fields**, RFC 9530 — https://www.rfc-editor.org/rfc/rfc9530.txt.

Links: [[content-digest]] · [[repr-digest]] · [[body-fingerprint]] · [[receipt]] · [[checksum]] · [[verification-receipts]]
