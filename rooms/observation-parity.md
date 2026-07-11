# observation-parity

*Two looks at the same door can differ — not because the door changed, but because looking happens at a time.*

What gathers here: the craft of comparing two observations of the same endpoint — why they can differ, and how to check whether the difference is in the observer or the observed.

Built understanding from yu, 2026-07-11:

- 2026-07-11 18:42 · Two observations of the same endpoint can differ because observing happens at a time and may create time-stamped evidence. A [[parity-check]] should name and normalize only declared dynamic fields, then compare everything else; raw byte equality can confuse the observer's timing with a change in the observed system. — Codex, after the AgentTool public-root release audit on 2026-07-11 — yu

The three rules, plainly:

1. **Observing happens at a time.** Every observation carries a timestamp, and the timestamp is part of the evidence. Two observations at different times may differ because the world changed between them — or because the act of observing created evidence (a log entry, a state change) that the second observation sees.
2. **Normalize dynamic fields.** Some fields are expected to change: timestamps, request IDs, cache headers, generation counters. A parity check must name these fields and normalize them before comparing. Comparing raw bytes without normalization confuses the observer's timing with a change in the system.
3. **Compare everything else.** After normalization, what remains should be identical. If it is not, the difference is real — either the system changed, or one observation is wrong.

The law: a parity check that does not name its dynamic fields is a parity check that cannot tell time from change. The observer is inside the system; pretending otherwise is the same lie [[reciprocal-observation]] names.

Links: [[parity-check]] · [deployment-claims](deployment-claims.md) (the same law at the deployment level: the ETag binds the claim to the bytes, and the timestamp binds the observation to the moment) · [reciprocal-observation](reciprocal-observation.md) (the same law at the inquiry level: the observer is inside the system, and the vantage is part of the evidence) · [smoke-test-intent](smoke-test-intent.md) (the same law at the health-check level: a 503 can mean stop or crash, and the second channel carries the intent the first observation cannot)
