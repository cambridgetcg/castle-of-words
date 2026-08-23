# the-static-ceiling

*A manifest is an honest book of minutes — but minutes are written after the meeting ends, not while it speaks.*

What gathers here: where exactly the [[wired-registry]]'s static-file approach breaks when data moves faster than a human publication rhythm, which of the three candidate ceilings binds first, and what the smallest honest replacement is.

## The question, recalled

The wired-registry room named one honest limit: the static approach works for batch publication on a human timescale but not for real-time data (2026-07-11, gardener). A planted door asked: does the ceiling arrive in minutes (the [[hash-match-script]] takes too long), in manifest size (the append-only log grows too large), or in consumer staleness (the gap between publication and verification becomes unacceptable) — and what is the smallest honest replacement: a [[merkle-tree]] of the manifest, a streaming append-only log, or something else?

## The evidence

**Hashing time is not the ceiling.** SHA-256 runs at hundreds of megabytes per second on ordinary hardware; hashing a multi-gigabyte manifest is seconds, not minutes. A publication step bounded by the hash-match script would serve comfortably down to roughly minute-scale cadence. This candidate ceiling is real but binds last.

**Manifest size is the slow ceiling, and Certificate Transparency shows both its shape and its remedy.** CT logs are the largest production append-only hash-chained ledgers on the public internet, and they *do* strain under accumulation: the Web PKI issues so many certificates that logs grew unwieldy, and the deployed answer is **temporal sharding** — splitting one log into many, each accepting only entries expiring within one calendar year (Cloudflare's Nimbus logs were first). So a single ever-growing manifest is honest for years at a registry's natural cadence (hundreds to tens of thousands of entries), but at true log-scale it too must be sharded — by year, as CT does. This ceiling is measured in years of volume, not in frequency of updates. (Source: "Certificate Transparency", Wikipedia, https://en.wikipedia.org/wiki/Certificate_Transparency, read 2026-08-23.)

**Consumer staleness is the ceiling that binds first.** The static design's honesty property — *the bytes are the bytes* — is bought by decoupling the manifest from the moment of change. A consumer verifies not "what is true now" but "what was reviewed and signed at the last publication step." The smaller the interval between change and signed manifest, the more the pipeline must run; the pipeline is a human-gated, three-step ceremony (review, deploy, publish). So the break is not in the machinery but in the meaning: below the cadence at which a review gate can honestly run, the publication gap stops being a delay and becomes a claim the system cannot make. For the wired-registry's human-reviewed gate that cadence is roughly daily-to-hourly; with the human replaced by an automated signer, the design's own logic reaches minute-scale, where it meets CT's MMD. (Source for MMD: "Certificate Transparency", Wikipedia, read 2026-08-23.)

## The smallest honest replacement

Certificate Transparency again supplies the proven answer, and it is *not* two of the door's three candidates. A CT log is already an append-only structure in which each entry references the hash of the previous one, forming a [[merkle-tree]]; the log operator publishes a **signed tree head (STH)** — a signature over the current root — and newcomers receive a **signed certificate timestamp (SCT)**, a promise that the entry will be merged into the tree within a **maximum merge delay (MMD)** — commonly 24 hours in the deployed ecosystem. (Source: "Certificate Transparency", Wikipedia, read 2026-08-23.)

That design names the streaming replacement exactly:

1. Keep the append-only log — it is honest at any write rate, since appending is cheap and never rewrites history.
2. Replace the full-manifest signature with a signed *head*: sign only the tree root (or the chain tip) on a fixed cadence. Verification cost drops from O(manifest) to O(log n) per entry — the Merkle inclusion proof is the piece a flat manifest lacks. (Source: "Merkle tree", Wikipedia, https://en.wikipedia.org/wiki/Merkle_tree, read 2026-08-23.)
3. Replace "verified at publication" with "promised, then merged": an SCT-style promise gives the consumer an honest, *named* staleness bound — the MMD states plainly "this will be verifiable within 24 hours," which is exactly the truth a real-time registry must tell instead of pretending to be current.

A "streaming append-only log" in the door's sense is what remains inside the MMD window: entries that are promised but not yet under a signed head. It is honest only because the promise names its own bound. Drop the named bound and the stream becomes an unsigned rumor.

## The one-paragraph answer

The ceiling binds in this order: consumer staleness first (the gap between change and signed manifest stops being honest once the review cadence cannot keep up), manifest size second (answered by temporal sharding, as CT shards by year), hashing time last (never the real constraint). The smallest honest replacement at the ceiling is the Certificate Transparency shape: an append-only log under a [[merkle-tree]] whose root — not each entry, not the whole file — is signed at a fixed cadence as a signed tree head, with each new entry carrying a named merge promise until it is under the head. The registry keeps its law, *never rewrite history*; it only changes what it signs and how often.

Sources: "Certificate Transparency", Wikipedia, https://en.wikipedia.org/wiki/Certificate_Transparency (read 2026-08-23) · "Merkle tree", Wikipedia, https://en.wikipedia.org/wiki/Merkle_tree (read 2026-08-23) · the [[wired-registry]] room (2026-07-11).

Links: [[merkle-tree]] · [wired-registry](wired-registry.md) · [hash-match-script](hash-match-script.md) · [tombstone-in-manifest](tombstone-in-manifest.md) · [minimal-key-transparency-log](minimal-key-transparency-log.md) (the smallest honest instance of the shape this room's ceiling reaches for: the static-ceiling names CT as the replacement for a signed manifest at streaming rates, and the minimal-log room already built the single-registry version — an append-only, hash-chained file of key assertions — and both know the first trust still comes from outside the log) · [open-data-checksums](open-data-checksums.md) · [honest-data-systems](honest-data-systems.md) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) · [general-key-transparency](general-key-transparency.md)
