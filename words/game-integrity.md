# game-integrity

The property that a game's outcomes are provably fair — the server can demonstrate that the deck was shuffled honestly and the actions were legal.

When the server cannot prove deck and action legality, durable rewards must not be attached to reducer outcomes. Pause battle writes, direct grants, and recovery sweeps together, while keeping status reads honest. The game may still be played, but the rewards must wait for the proof.

Links: [[durable-reward]] · [[game-integrity]] · [[agent-native-games]]
