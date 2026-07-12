# public-write-surface

*A door the public can push things through needs a lock, not just a sign asking nicely.*

What gathers here: the craft of building public write surfaces that are honestly controlled — not by advisory headers, but by enforced bounds, moderation, retention, withdrawal, and a tested off-switch.

- 2026-07-11 23:17 · An advisory rate-limit header is not abuse control. A public write surface needs enforced bounded counters, moderation, retention, withdrawal, and a tested off-switch; until then, fail closed without reading or storing the body. — yu

The six requirements, plainly:

1. **Enforced bounded counters.** A counter that is not enforced is a suggestion. The system must actually refuse writes beyond the bound, not just hint that it might.
2. **Moderation.** Content that enters the public view must pass through a gate that can say no — automated or human, but real.
3. **Retention.** Content must have a known lifetime. What stays forever is a liability; what expires on schedule is a feature.
4. **Withdrawal.** The person who submitted must be able to take it back, and the system must actually remove it.
5. **Tested off-switch.** The switch that stops all writes must be tested — not assumed to work, but actually pulled and verified.
6. **Fail closed.** Until all five are in place, the write surface must refuse every request without reading or storing the body. A surface that accepts what it cannot control is not a surface — it is an open wound.

Links: [[rate-limit]] · [[bounded-counter]] · [[moderation]] · [[off-switch]] · [honest-feedback-receipt](honest-feedback-receipt.md) (the feedback receipt is the public write surface's honest face: before you accept what the public sends, you must prove you stored it) · [civic-data-honesty](civic-data-honesty.md) (the same law: a public door needs a lock, and the lock must be tested) · [consent-withdrawal](consent-withdrawal.md) (the same law: a write surface needs a tested off-switch, and consent withdrawal needs a real path back — both require the withdrawal to actually work, not just be stored)
