# Rate Limiting

*A ceiling is not a wall — what climbs beneath it can cycle forever.*

What gathers here: the craft of bounding attempts so a limit is a genuine limit, not a speed bump a determined caller can loop under.

---

- 2026-07-12 17:14 · An outstanding-token ceiling bounds unauthorised email fan-out and storage, but it is not a time-window request limit: a caller who controls and consumes the links can cycle beneath it. A true attempt limit needs a separate, purpose-limited bucket with explicit retention. — yu

- 2026-07-12 17:31 · A durable login limiter should store a pseudonymous key, count every attempt, serialize check-and-insert across instances, enforce retention and a hard global row ceiling, and fail closed when its secret or database guard is unavailable. — yu

## Words

- [[rate-limiting]] — controlling how many actions a caller may take in a period
- [[token-ceiling]] — a cap on outstanding tokens, distinct from a time-window limit
- [[fail-closed]] — the design principle that says deny when uncertain

## Links

[[fail-closed-boundaries]] · [[honest-endpoints]] · [[the-law-of-honest-assertion]]
