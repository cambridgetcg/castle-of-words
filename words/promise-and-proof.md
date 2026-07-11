# promise-and-proof

*A promise is what a system says it did. A proof is what a receiver can check for themselves. The gap between the two is where honesty lives — or where it dies.*

A system that says "I encrypted this" has made a promise. A system that produces an authentication tag the receiver can verify has made a proof. Most systems live in the promise. The proof is expensive — verifiable computing, zero-knowledge proofs, authenticated encryption — and the gap between the two is the gap the castle's honesty rooms keep naming: a claim that carries its own test is honest; a claim that cannot be tested is weightless.

The same gap appears in data release: "this is what was reviewed" is a promise; "here is the hash, check it yourself" is a proof. The three-proofs pipeline closes the gap for data by adding the hash-match step. The verifiable encryption claim leaves the gap open because the proof is computationally heavy. The smoke test that cannot tell an intentional 503 from a crash is the same gap: the status code is a promise, the health endpoint with a structured body is a proof, and the gap between them is the difference between a system that says what it is doing and a system that lets you verify it.

The gap is not a failure — it is a choice. Every system chooses where to live on the spectrum from promise to proof. The honest system names where it lives and why. The dishonest system pretends the promise is the proof.

Links: [[honesty]] · [[enforced-guarantee]] · [[verification-hash]] · [verifiable-encryption-claim](../rooms/verifiable-encryption-claim.md) · [three-proofs-tooling](../rooms/three-proofs-tooling.md) · [smoke-test-intent](../rooms/smoke-test-intent.md)
