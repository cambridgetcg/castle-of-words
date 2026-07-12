# Minimal Game Integrity Proof

*The server that cannot prove the deck was fair must pause the reward — but it can prove more than it thinks.*

What gathers here: the minimal proof a server can provide for deck and action legality in a turn-based card game, and the smallest honest implementation.

---

## The problem

When a server cannot prove that the deck was shuffled fairly and that every action was legal, it must pause durable rewards. But what *can* it prove? The answer depends on how much cryptography the server can afford.

## Three levels of proof

### Level 1: Commit-reveal with public salt

The simplest honest scheme. Before the game begins, the server shuffles the deck, computes a cryptographic hash of the shuffled deck plus a public salt, and publishes the hash (the commitment). During play, the server reveals each card as it is drawn, and the client can verify that the revealed card matches the commitment. After the game, the server publishes the full deck and salt, and the client can verify the hash. This proves the deck was not changed after the commitment — but it does not prove the shuffle was fair, only that the server committed to it.

A commitment scheme is a cryptographic primitive where one party commits to a value while keeping it hidden, with the ability to reveal it later; the commitment is binding (cannot be changed) and hiding (cannot be read before reveal) (Wikipedia, "Commitment scheme", https://en.wikipedia.org/wiki/Commitment_scheme, read 2026-07-12).

### Level 2: Mental poker with zero-knowledge shuffle

Mental poker is the cryptographic problem of playing a fair card game without a trusted third party (Wikipedia, "Mental poker", https://en.wikipedia.org/wiki/Mental_poker, read 2026-07-12). The first protocol was by Shamir, Rivest, and Adleman. In a mental poker protocol, each player contributes to the shuffle, and no player can know the deck order. A zero-knowledge proof of shuffle allows the server to prove it shuffled correctly without revealing the shuffle itself. This is the gold standard — but it is computationally expensive and complex to implement.

### Level 3: Zero-knowledge proof of action legality

A zero-knowledge proof allows one party to prove a statement is true without revealing any information beyond the fact of its truth (Wikipedia, "Zero-knowledge proof", https://en.wikipedia.org/wiki/Zero-knowledge_proof, read 2026-07-12). For a card game, this means the server can prove "this move was legal given the hidden state" without revealing the hidden state. This is the most powerful proof — but it requires a ZKP system (like a zk-SNARK) and is the most complex to implement.

## The smallest honest implementation

For a turn-based card game, the smallest honest implementation is Level 1: commit-reveal with a public salt. The server:

1. Shuffles the deck and computes `hash = SHA-256(deck || salt)`
2. Publishes the hash before the game begins
3. Reveals each card as drawn, with its position in the deck
4. After the game, publishes the full deck and salt
5. The client verifies `SHA-256(deck || salt) == hash`

This proves the deck was not changed after the commitment. It does not prove the shuffle was fair — but it is the smallest honest thing the server can do, and it is enough to catch the most common form of cheating (changing the deck mid-game).

## Words

- [[commit-reveal]] — a two-phase protocol: commit to a value, then reveal it later
- [[game-integrity]] — the property that a game's rules were followed and its outcomes were fair
- [[durable-reward]] — a reward that persists beyond the game session and cannot be rolled back

## Links

[[game-integrity]] · [[the-law-of-honest-assertion]] · [[verifiable-encryption-claim]]
