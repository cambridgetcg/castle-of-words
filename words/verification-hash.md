# verification-hash

A cryptographic digest computed over the exact bytes a receiver can fetch, not over a file path or a database row.

If the bytes are unavailable — the file was deleted, the blob was never stored — the hash must be null, not a valid SHA-256 sentinel. A valid hash where there are no bytes is a lie a verifier cannot detect, because the hash checks out against nothing.

Links: [[open-data]] · [[honesty]] · [[conditional-request]]
