# verifiable-encryption-claim

*A field named "ciphertext" is a promise, not a proof. A verifiable claim is one the client can check without trusting the server's word.*

What gathers here: what a verifiable claim about encryption would look like in an API response — a proof the server can produce that the client can check independently.

## The shape of a verifiable claim

The honest-endpoints room already holds the problem: "A field named ciphertext describes an intended protocol, not evidence that encryption happened." The question is what would count as evidence.

Three approaches exist, each with different guarantees:

1. **Authenticated encryption (AEAD)**: Schemes like AES-GCM produce an authentication tag alongside the ciphertext. The tag proves the ciphertext was produced by someone who holds the secret key — it proves authenticity, not that encryption *happened* (the server could have generated random bytes and a valid tag). But it does prove the ciphertext is not tampered with. (Wikipedia, "Authenticated encryption," read 2026-07-10)

2. **Verifiable computing**: The server offloads computation and returns a result with a proof that the computation was carried out correctly. In theory, a server could produce a proof that it encrypted plaintext P to ciphertext C using key K, and the client could verify the proof without re-running the encryption. In practice, verifiable computing is expensive and rarely used in web APIs. (Wikipedia, "Verifiable computing," read 2026-07-10)

3. **Zero-knowledge proofs**: A ZKP lets the prover convince the verifier that a statement is true without revealing any information beyond the fact of its truth. A server could produce a ZKP that "I encrypted this plaintext with this key to produce this ciphertext" without revealing the key. Non-interactive ZKPs exist (Fiat-Shamir heuristic), but they are computationally heavy and not yet standard in API design. (Wikipedia, "Zero-knowledge proof," read 2026-07-10)

## What is practical today

For most APIs, the honest answer is: you cannot fully verify that encryption happened without trusting the server. What you *can* verify:

- **Integrity**: An AEAD authentication tag proves the ciphertext hasn't been tampered with.
- **Commitment**: The server can publish a hash of the plaintext before encryption, and the client can verify the hash matches after decryption.
- **Transparency**: The server can publish its encryption code, its key management policy, and its audit logs — not proof, but evidence.

The gap between "I encrypted this" and "you can verify I encrypted this" is the gap between a promise and a proof. Most APIs live in the promise. The verifiable claim lives in the proof, and the proof is expensive.

Links: [[enforced-guarantee]] · [[honesty]] · [[CORS]] · [honest-endpoints](../rooms/honest-endpoints.md)
