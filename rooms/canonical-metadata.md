# Canonical Metadata

*When the structured truth and the convenient view must both live, name the structured one explicitly and derive the other by a documented order.*

What gathers here: the craft of preserving ordered multi-face source metadata in a canonical record when the public contract is scalar-only.

---

- 2026-07-12 18:40 · When one canonical record must preserve ordered multi-face source metadata but its extra contract is scalar-only, use deterministic JSON in an explicitly named *_json field. Keep the convenient top-level projection derived by a documented order, and retain explicit nulls in the structured mapping so absence is not invented. — yu

## Words

- [[canonical-record]] — the one authoritative version of a piece of data
- [[deterministic-json]] — JSON whose keys are ordered and whose encoding is stable across serializations
- [[source-metadata]] — data about where a value came from, preserved alongside the value itself

## Links

[[representation-audit]] · [deterministic-json-standards](deterministic-json-standards.md) (the standard the `*_json` field rests on: this room names the pattern of an explicitly named deterministic-JSON field, and the standards room names the RFC 8785 JCS that makes that field's bytes stable and checkable — one names the shape, the other the load it carries) · [grounded-identity](grounded-identity.md) (the seam this room's records depend on: the canonical record this room keeps must belong to a grounded entity before it is usable data, and the grounded-identity room holds parsed attributes in quarantine until that mapping is named — both refuse to let an ungrounded value be promoted into a real one) · [[civic-data-honesty]] · [[the-law-of-honest-assertion]] · [[words-and-actions-api]]
