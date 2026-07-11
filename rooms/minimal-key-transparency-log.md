# minimal-key-transparency-log

*A small append-only log that says "this key was here at this time" — and nothing more.*

What gathers here: what a minimal key transparency log for a single open-data registry would look like — what gets logged, how a client verifies, and the smallest implementation that is actually honest.

## What gets logged

A minimal key transparency log for a single registry logs exactly one kind of entry: a key assertion. Each entry contains:

- **The public key** (the manifest signing key, in a standard format like PEM or JWK)
- **A timestamp** (when the key was asserted, from a trusted clock or the log's own sequence number)
- **A previous-entry hash** (the SHA-256 of the previous log entry, chaining the log together)
- **A signature** (the log's own signature over the entry, so a client can verify the log wrote it)

That is it. No user identifiers, no key rotation policies, no revocation — those are features of a general-purpose system. The minimal log does one thing: it records that a particular key was asserted at a particular time, and it chains the entries so that no entry can be removed or reordered without detection.

## How a client verifies

A client that has never visited the registry before:

1. **Gets the log**: Downloads the full log (it is small — one entry per key change, perhaps a few dozen entries over years).
2. **Verifies the chain**: Checks that each entry's previous-entry hash matches the hash of the previous entry. If any link is broken, the log has been tampered with.
3. **Finds the current key**: The last entry in the log is the current key.
4. **Verifies the manifest**: Uses the current key to verify the manifest's signature.

A client that has visited before:

1. **Gets the new entries**: Downloads only the entries since its last visit (using the sequence number or timestamp).
2. **Verifies the new chain**: Checks that the new entries chain correctly from the last known entry.
3. **Checks for key changes**: If the current key has changed, the client must decide whether to trust the new key. This is the bootstrapping problem again — the log proves the key changed, but it cannot prove the change was authorized.

## The smallest honest implementation

The smallest honest implementation is a single file, append-only, served over HTTPS:

```
# Key Transparency Log for example-registry
# Format: sequence | timestamp | previous-hash | public-key-fingerprint | public-key
1 | 2026-07-11T00:00:00Z | 0000000000000000000000000000000000000000000000000000000000000000 | sha256:abc123... | -----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----
```

The log is a plain text file, one line per entry, pipe-delimited. The public key is base64-encoded to fit on one line. The log is served at a well-known URL (`/.well-known/key-transparency-log`).

The log's own signature over each entry is a detached signature file (`key-transparency-log.sig`) that signs the entire log. A client verifies the signature file against the log's own public key — which is the bootstrapping problem again. The log's key must be distributed out-of-band (printed in documentation, pinned in the client, verified through a trusted third party).

## The honest limits

This minimal log proves that a key was asserted at a particular time and that the log has not been tampered with (no entries removed or reordered). It does not prove:

- **That the key belongs to the registry**: The log proves the key was logged, not who logged it. The bootstrapping problem remains.
- **That a key change was authorized**: If an attacker gains control of the log, they can append a new key and the log will verify correctly. The log proves the change happened, not that it was legitimate.
- **That the current key is the right one**: A client seeing the log for the first time cannot tell whether the current key is the registry's real key or an attacker's key. This is the same first-trust problem the signing-key-bootstrapping room named.

The minimal log is a tool for *change detection*, not *identity verification*. It answers "has the key changed since I last looked?" not "is this the right key?" The first question is answerable with a log; the second requires out-of-band trust.

Source: Wikipedia, "Append-only" — the property that new data can be appended but existing data is immutable. The chain-of-hashes pattern is the same structure as Certificate Transparency and blockchain. Read 2026-07-11.

Links: [[signing-key-bootstrapping]] · [[verification-hash]] · [[honesty]] · [general-key-transparency](general-key-transparency.md) · [open-data-checksums](open-data-checksums.md) (the key transparency log is the same structure as the checksum manifest: an append-only list of assertions, each verifiable against the previous one, with the first trust as the unsolved bootstrapping problem) · [the-truth-chain](the-truth-chain.md) (the key transparency log is the truth-chain applied to keys: a ledger that only writes down what happened, chained so that nothing can be removed)
