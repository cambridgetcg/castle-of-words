# deterministic-json

JSON whose keys are ordered and whose encoding is stable across serializations — the same data always produces the same bytes.

Deterministic JSON is the format for a canonical record's structured metadata field. Without determinism, two serializations of the same data may produce different hashes, breaking the verification chain. The order must be documented so consumers can reproduce it.

Links: [[canonical-record]] · [[source-metadata]] · [[canonical-metadata]]
