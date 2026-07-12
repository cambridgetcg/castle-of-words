# durable-reward

A reward that persists beyond the session — currency, items, rank — unlike a transient game state that vanishes when the match ends.

Durable rewards must only be granted when the server can prove the game was fair. If the server cannot verify deck and action legality, durable rewards must be paused. The transient game state (the scoreboard, the current turn) may still be shown honestly.

Links: [[game-integrity]] · [[game-integrity]] · [[agent-native-games]]
