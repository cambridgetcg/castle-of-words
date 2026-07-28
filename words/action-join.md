# action-join

An action join is the moment a plan becomes an effect — the seam where intention crosses into execution.

A safe action join is bounded, session-private, nonce-bearing, and single-use: the token is consumed before effect-capable work begins and returned with a conservative attempt phase. The serializer and capture code must ignore prototype hooks, so a redacted plan never publishes a stable digest of hidden inputs.

Links: [[safety-boundaries]] [[fail-closed]] [[bounded-turn]] [[receipt]]
