# agent-claims

*A signature proves which key signed which bytes; it does not by itself prove the statement inside is true.*

What gathers here: the taxonomy of claim strength for agent-facing statements — how an agent should say what backs each thing it asserts, so the receiver knows what to trust and what to verify.

Built understanding from yu, 2026-07-11:

- 2026-07-11 10:03 · Agent-facing claims should say whether they are asserted, behaviorally tested, or cryptographically attested. A signature proves which key signed exact bytes; it does not by itself prove that unsigned inputs or the statement inside are true. — yu

The three levels, plainly:

- **Asserted.** The speaker says it is so. No test, no proof — just the word. An asserted claim is a starting point, not a conclusion.
- **Behaviorally tested.** The claim was checked by observing behavior — a smoke test passed, an endpoint returned 200, a contract test ran green. The test proves the behavior happened, not that it will always happen.
- **Cryptographically attested.** A signature over exact bytes proves which key signed what. But the signature proves the bytes, not the truth of the statement those bytes encode. The unsigned inputs, the mapping from bytes to meaning, and the identity behind the key are separate claims that need their own backing.

The law: each level carries its own burden and its own blind spot. A claim that fuses levels — "the signature proves the service is healthy" — is a claim that lies about what it actually proves.

Links: [[asserted-claim]] · [[behaviorally-tested-claim]] · [[cryptographically-attested-claim]] · [[canonical-bytes]] · [honest-endpoints](honest-endpoints.md) (the same law at the API layer: a field named ciphertext is an assertion, not proof) · [the-truth-chain](the-truth-chain.md) (the truth-chain's append-only ledger is the cryptographically-attested form of the same honesty) · [the-instruments](the-instruments.md) (a self-measuring instrument is the behaviorally-tested form) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the three claim levels are the taxonomy the law of honest assertion operates within: asserted, behaviorally tested, and cryptographically attested are the three ways a system names what backs each output) · [the-castle-audit](the-castle-audit.md) (the audit that turned the law inward found the castle's rooms mostly satisfy it — the three claim levels are the standard the audit measured against)
