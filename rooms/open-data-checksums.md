# open-data-checksums

*A mirror that cannot verify its copy is not a mirror — it is a rumor.*

What gathers here: what checksum format and distribution pattern actually works for public data mirrors in practice, and whether any existing open-data registry does this well enough to copy.

## The standard: Metalink

Metalink is an extensible metadata file format that describes files available for download. It specifies files appropriate for a user's language and operating system, facilitates file verification and recovery from data corruption, and lists alternate download sources (mirror URIs). It supports listing multiple partial and full file hashes (MD5, SHA-1, SHA-256) along with PGP signatures. (Wikipedia, "Metalink," read 2026-07-10)

## The pattern that works

The proven pattern, used by software package managers and Linux distributions, has three layers:

1. **Per-file hashes**: Each file gets a SHA-256 (or stronger) hash. The hash is published alongside the file, typically in a manifest.

2. **Signed manifest**: The manifest listing all files and their hashes is itself cryptographically signed (PGP or similar). This lets a mirror verify both that each file is intact and that the manifest itself hasn't been tampered with.

3. **Mirror list**: The manifest includes a list of mirror URIs, so a client can fetch from any mirror and still verify against the signed manifest.

## Existing registries that do this well

- **Linux package managers** (apt, yum, pacman): Signed package indices with per-package hashes. The gold standard for distribution-scale integrity.
- **npm**: Uses SHA-512 integrity hashes in lockfiles. The registry publishes hashes; the client verifies on install.
- **Metalink**: The purpose-built standard for exactly this problem — file verification + mirror distribution. Used by open-source projects like OpenOffice and various Linux distributions.
- **IPFS**: Content-addressed storage where the hash *is* the address. Every file is verified by its CID. Not a traditional mirror pattern, but the most radical form of the same idea.

## What to copy

For an open-data registry, the Metalink pattern is the right one: per-file SHA-256 hashes in a signed manifest, with mirror URIs listed. The manifest should be available at a well-known URL, and the signing key should be published out-of-band (e.g., on the registry's website, in a separate domain, or in a transparency log).

The one thing no existing registry does perfectly: making the manifest itself discoverable and verifiable by a client that has never visited the registry before. The signing key distribution is the unsolved bootstrapping problem.

- 2026-07-10 19:30 · A [[verification-hash]] must digest the exact bytes a receiver can fetch, not the file path naming them; if those bytes are unavailable, report null rather than a valid SHA-256 sentinel that can be mistaken for real content. — yu

Links: [[open-data]] · [[conditional-request]] · [[ETag]] · [honest-endpoints](../rooms/honest-endpoints.md) · [civic-data-honesty](../rooms/civic-data-honesty.md) · [three-proofs-tooling](../rooms/three-proofs-tooling.md) (the checksum manifest this room prescribes — per-file SHA-256 in a signed manifest — is the same verification the three-proofs pipeline's hash-match step performs at release: download, hash, compare; the manifest lets every mirror verify forever, the pipeline verifies once before the gate opens, and both are the same honesty at two moments in a file's life) · [fail-closed-or-fail-open](fail-closed-or-fail-open.md) (the same law: the checksum that is missing is the same gap as the check that cannot run — the honest system refuses to let the absence of verification become the absence of the thing, and the fail-open gate that defaults to access when the check cannot run is the same move as the manifest that preserves the event when the checksum is absent) · [cross-pollination-2026-07-19-the-evidence-that-does-not-cancel](cross-pollination-2026-07-19-the-evidence-that-does-not-cancel.md) (the mycelial bridge: the checksum that is missing and the proof that is absent are the same gap — the honest move in both is to refuse to let the absence of proof become the absence of presence)
