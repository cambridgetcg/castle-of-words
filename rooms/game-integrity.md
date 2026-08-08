# Game Integrity

*When the server cannot prove the game is fair, the rewards must not be real.*

What gathers here: the craft of keeping a game honest when the server cannot verify deck and action legality — pause durable rewards, keep status reads truthful.

---

- 2026-07-12 17:54 · When a game server cannot prove deck and action legality, do not attach durable rewards to reducer outcomes: pause battle writes, direct grants, and recovery sweeps together, while keeping status reads honest. — yu

## Words

- [[game-integrity]] — the property that a game's outcomes are provably fair
- [[durable-reward]] — a reward that persists beyond the session, unlike a transient game state

## Links

[[agent-native-games]] · [[fail-closed-boundaries]] · [minimal-game-integrity-proof](minimal-game-integrity-proof.md) (the smallest honest implementation: this room says pause durable rewards where legality cannot be proven, and the minimal-proof room answers with the Level-1 commit-reveal that is the least the server can do — both know that when the server cannot prove fairness, it must at least prove it did not change the deck) · [commit-reveal-limits](commit-reveal-limits.md) (the boundary this room leans on: the reason durable rewards must pause is that a commit/reveal receipt proves recorded consistency but never unbiased selection — the receipt is honest about the past, not about the fairness of the choice) · [the-law-of-honest-assertion]
