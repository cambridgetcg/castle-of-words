# general-key-transparency

*Key transparency exists for messaging, not for arbitrary signing keys — the general case is still research.*

What gathers here: whether a general-purpose key transparency log exists (like Certificate Transparency but for any signing key), or whether this is still research.

## What exists

**Certificate Transparency (CT)** is the model: a public, append-only log of TLS certificates that anyone can audit. Browsers require CT for new certificates, and the ecosystem is mature. But CT is specific to TLS certificates — it logs X.509 chains, not arbitrary public keys.

**Key Transparency (KT)** generalizes the idea to end-to-end encrypted messaging: a public, auditable log of public keys so that messaging clients can verify they have the correct key for a recipient. The Wikipedia entry (read 2026-07-11) describes it as allowing "communicating parties to verify public keys used in end-to-end encryption." The key paper is CONIKS (Melara et al., 2015), which brought key transparency to end users. But KT systems are designed for messaging — they map user identifiers (email addresses, phone numbers) to public keys, and the audit is per-user, not per-key.

**No general-purpose key transparency log exists** for arbitrary signing keys (e.g., a manifest signing key for an open-data registry). The gap is real: CT is for TLS, KT is for messaging, and neither is a drop-in for "I have a signing key and I want the world to verify it hasn't changed."

## What is being built

- **CONIKS** (2015): key transparency for messaging, not general-purpose. Wikipedia has no standalone article; it is described in the Key Transparency article.
- **EthIKS** (Bonneau, 2016): uses Ethereum to audit a CONIKS log — still messaging-specific.
- **Parakeet** (Malvai et al., 2023): "Practical Key Transparency for End-to-End Encrypted Messaging" — the most recent, still messaging-specific.
- **Trillian**: Google's open-source implementation of a verifiable log (used by Certificate Transparency), could theoretically be used for arbitrary keys, but no general-purpose key transparency system is built on it.

## The honest answer

This is still research. The practical path for an open-data registry is the layered approach the signing-key-bootstrapping room already described: TOFU + out-of-band verification + a transparency log if one becomes available. For now, the transparency log for arbitrary keys does not exist as a ready-to-use system.

Source: Wikipedia, "Key transparency" — describes the concept and its messaging-specific implementations. Read 2026-07-11.

Links: [[signing-key-bootstrapping]] · [[open-data]] · [[verification-hash]] · [signing-key-bootstrapping](../rooms/signing-key-bootstrapping.md) · [open-data-checksums](../rooms/open-data-checksums.md) · [minimal-key-transparency-log](minimal-key-transparency-log.md) (the buildable version of the gap this room maps: where this room finds no general-purpose transparency log exists for arbitrary keys, the minimal-log room shows the smallest honest one for a single registry is an append-only, hash-chained file of key assertions — the general case is research, the specific case is buildable) · [verification-receipts](../rooms/verification-receipts.md) (the same law at the receipt level: the transparency log that would audit a key and the receipt that must arrive through a separately authenticated channel are the same gap — both know that verification needs a trust root obtained separately, and both name the bootstrapping problem no general log has yet solved)
