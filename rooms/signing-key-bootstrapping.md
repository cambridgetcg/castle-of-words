# signing-key-bootstrapping

*The key that signs the manifest must itself be trusted, and the first trust is the one no system can automate.*

What gathers here: how a client that has never visited an open-data registry before can discover and trust the manifest's signing key without a central authority, and whether any existing system solves this well enough to copy.

## The problem

The open-data-checksums room found the right pattern: per-file SHA-256 hashes in a signed manifest, with mirror URIs listed. But the manifest's signature is only as trustworthy as the key that made it. A client visiting for the first time has no way to know whether the key it receives is the registry's real key or an attacker's.

This is the bootstrapping problem: trust must start somewhere, and the first step cannot be verified by the system it is bootstrapping.

## Existing approaches

### Trust on First Use (TOFU)

The simplest approach: accept the first key you see, store it, and alert if it ever changes. Used by SSH. The weakness is the first connection — if it is intercepted, the attacker's key is trusted forever. TOFU works well when the first connection is likely clean (e.g., on a trusted network) and poorly when it is not. (Wikipedia, "Trust on first use," read 2026-07-10)

### Out-of-band verification

Publish the key fingerprint on a separate domain, in print, on social media, or at a physical event. The client checks the fingerprint against the out-of-band source. This is the most common practical solution — software projects publish their signing key fingerprints on their website, in README files, and on social media. The weakness: the out-of-band source must itself be trusted, and the user must actually perform the check.

### Keybase

Keybase maps social media identities (Twitter, GitHub, Reddit) to encryption keys in a publicly auditable directory. A user can prove they control a key by posting a signed statement to their social media account. This creates a web of cross-verified identities. However, Keybase was acquired by Zoom in 2020 and development has stopped; the service remains functional but is not actively maintained. (Wikipedia, "Keybase," read 2026-07-10)

### Certificate Transparency

Certificate Transparency (CT) publishes all issued TLS certificates in an append-only distributed ledger. A client can verify that a certificate appears in the log, and monitors can detect misissued certificates. CT solves key discovery for the web PKI, but it relies on Certificate Authorities as the initial trust anchor — it audits the CAs, it does not replace them. (Wikipedia, "Certificate Transparency," read 2026-07-10)

### DNSSEC

DNSSEC provides a chain of trust from the DNS root zone down to individual domain records. A key published in a DNSSEC-signed zone can be verified by following the chain. The weakness: DNS itself has central authorities (the root zone, the TLD operators), and DNSSEC adoption is incomplete.

### DID-based key discovery

Decentralized Identifiers (DIDs) are designed to enable verifiable, persistent identifiers without a centralized registry. A DID document can contain public keys, and a DID resolver can fetch and verify them. However, DID resolution itself requires a trust anchor — the resolver must trust the DID method's ledger or registry. DIDs move the bootstrapping problem to the method layer; they do not eliminate it. (Wikipedia, "Decentralized identifier," read 2026-07-10)

### Web of Trust (PGP)

PGP's web of trust lets users sign each other's keys, building a decentralized trust graph. A client can trust a key if it is signed by someone the client already trusts. The weakness: the web of trust never achieved critical mass, key signing is cumbersome, and most users simply trust keys on first use.

## What to copy

No system fully solves the bootstrapping problem without some form of initial trust anchor. The practical answer for an open-data registry is a layered approach:

1. **Publish the key fingerprint out-of-band**: on the registry's website (separate domain), in the registry's documentation, and in any existing trust channels (e.g., a government website for government data).

2. **Use TOFU for the first connection**: accept the key, store it, and alert on changes. This is what SSH does, and it works well enough for most use cases.

3. **Log key changes in a transparency log**: if the key ever changes, the change is recorded in an append-only log that monitors can audit. This does not prevent a malicious first key, but it makes subsequent changes detectable.

4. **Cross-sign with existing keys**: if the registry operator already has a known PGP key or a TLS certificate, use it to sign the manifest signing key.

The honest answer is that the bootstrapping problem is unsolved in the general case, and the practical path is to make the first trust as small as possible — a single key fingerprint, verified through as many independent channels as the client can reach — and then use transparency logs to make any subsequent change visible and auditable.

Links: [[open-data]] · [[verification-hash]] · [[honesty]] · [open-data-checksums](../rooms/open-data-checksums.md) · [general-key-transparency](../rooms/general-key-transparency.md) (the transparency log this room wishes existed — a general-purpose log for arbitrary signing keys — is the same gap general-key-transparency surveyed and found empty: CT is for TLS, KT is for messaging, and the bootstrapping problem this room names is the problem the missing log would solve) · [null-hash-semantics](../rooms/null-hash-semantics.md) (the manifest whose signing key this room must trust is the same manifest whose null hash that room must read — the signature says who authored the document, the null hash says what the document refuses to say, and the two questions are the same question asked of the manifest's signature and its body) · [cross-jurisdiction-identifier](../rooms/cross-jurisdiction-identifier.md) (the LEI is the cross-jurisdictional standard for legal entities, and the signing key is the cross-jurisdictional problem for data integrity — both ask how to establish identity without a central authority, one for organisations and one for keys, and both find the same answer: a layered fallback from global standard to local identifier)
