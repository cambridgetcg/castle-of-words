# manifest

*A list that says what is here, what it is, and who said so — and carries its own signature so you can check.*

A manifest is a signed document that lists files and their hashes. It is the honesty of a collection made visible: each file gets a fingerprint (SHA-256), the list of fingerprints gets a signature, and anyone who receives the manifest can verify both that each file is intact and that the list itself has not been tampered with. The manifest is the answer to the question "how do I know this is what you meant to give me?" — and the answer is: here is the hash, here is the signature, check for yourself.

The manifest's honesty lives in what it refuses to say as much as in what it says. A null hash in a manifest is a silence where a fact should be — and silence is always ambiguous unless the manifest says why. A manifest that says "this file has no hash" without saying whether it was never published, deleted, or unavailable is a manifest that is honest about its uncertainty but dishonest about its silence.

The manifest's signature is only as trustworthy as the key that made it. A client visiting for the first time has no way to know whether the key it receives is the real one or an attacker's. This is the bootstrapping problem: trust must start somewhere, and the first step cannot be verified by the system it is bootstrapping. The manifest is the answer to "what is here"; the signing key is the answer to "who said so"; and the two answers are the same question asked of the manifest's body and its signature.

Links: [[open-data]] · [[verification-hash]] · [[honesty]] · [open-data-checksums](../rooms/open-data-checksums.md) · [signing-key-bootstrapping](../rooms/signing-key-bootstrapping.md) · [null-hash-semantics](../rooms/null-hash-semantics.md)
