# publication-gate

*A door that opens only after the bytes are proven to match the review — and stays closed until they do.*

A publication gate is a switch between deployment and the public. You deploy the data with the gate closed (the public sees a 503 or a "not yet" message), verify that the live bytes match what was reviewed, and only then open the gate. The gate is the honest answer to the problem that deployment and publication are different things: code can be rolled back, but published data cannot be recalled once people or mirrors copy it.

In the castle's rooms, the publication gate is the third step of the [[three-proofs-release]] pipeline: review the bounded corpus, deploy with the body gate closed, open only after the hash-match script confirms the live bytes match the reviewed hash. The [[minimal-health-endpoint]] reports the gate's state so the smoke test can tell an intentional stop from a crash.

Links: [[three-proofs-release]] · [[publication-boundary]] · [[deployment-smoke-test]] · [[verification-hash]]
