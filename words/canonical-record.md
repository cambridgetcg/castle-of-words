# canonical-record

The one authoritative version of a piece of data — the source of truth from which all other representations are derived.

When the canonical record must preserve ordered multi-face source metadata but the public contract is scalar-only, the structured truth lives in an explicitly named `*_json` field. The convenient top-level projection is derived from it by a documented order. Explicit nulls in the structured mapping ensure absence is not invented.

Links: [[deterministic-json]] · [[source-metadata]] · [[canonical-metadata]]
