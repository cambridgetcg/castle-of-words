# safe-api-design

*A safe API is not a singleton loop run many times — it is a design that bounds, indexes, and omits before it serves.*

What gathers here: the craft of building APIs that are safe by design — not by hoping each caller will be careful.

- 2026-07-13 11:39 · A safe multi-record API is not just a singleton loop: bound raw bytes before parsing, query exact aliases through an index, treat alias collisions as ambiguity even for exact spellings, and omit fields whose live schema or redistribution lineage is uncertain. — yu

A safe API does four things before it returns a single byte:

1. **Bound raw bytes before parsing.** The size of the input is checked before the parser touches it. A parser that runs on unbounded input is a denial-of-service waiting to happen. The bound is the first gate.

2. **Query exact aliases through an index.** When a caller asks for something by name, the API looks it up through an index keyed on the exact spelling — not a scan, not a fuzzy match, not a LIKE query. An index is a promise that the lookup is O(log n), not O(n).

3. **Treat alias collisions as ambiguity even for exact spellings.** Two records with the same alias are ambiguous, even if the caller spelled it perfectly. The honest API returns the ambiguity, not a guess. A guess that happens to be right is still a guess.

4. **Omit fields whose live schema or redistribution lineage is uncertain.** If the API cannot prove that a field exists in the current schema, or cannot trace who is allowed to receive it, the field is omitted. Silence is safer than a wrong answer, and the [[absence-boundary]] names what was left out.

The law: a safe API is not a loop that calls a safe singleton many times. It is a design where safety lives in the structure — the bounds, the indexes, the collision handling, the omission rules — not in the hope that every caller will be careful.

Links: [[absence-boundary]] · [[alias-collision]] · [[redistribution-lineage]] · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: a door that tells you how to open it and what you'll find inside) · [agent-friendly-data](agent-friendly-data.md) (the same law at the data layer: bounded descriptions, stable IDs, typed errors) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: an API that omits a field must say it omitted it, never pretend the field doesn't exist)
