# Deterministic JSON Standards

*RFC 8785 named the scheme — but the castle's pattern of ordered multi-face source metadata is its own.*

What gathers here: the actual serialization standard for deterministic JSON, and whether any existing specification handles the "ordered multi-face source metadata" case.

---

## The standard: RFC 8785 JCS

The JSON Canonicalization Scheme (JCS), defined in RFC 8785 (June 2020), is the IETF standard for deterministic JSON serialization (RFC 8785, "JSON Canonicalization Scheme (JCS)", https://datatracker.ietf.org/doc/rfc8785/, read 2026-07-12). JCS defines how to create a canonical representation of JSON data by:

1. Constraining JSON to the I-JSON subset (no duplicate keys, limited number precision)
2. Sorting object properties by their UTF-16 code unit values
3. Using strict ECMAScript serialization for primitives (no trailing commas, no whitespace variance)
4. Escaping characters according to a fixed rule set

The result is that the same JSON data always produces the same bytes, regardless of the serializer or platform. This is the standard the canonical-metadata room's `*_json` field should use.

## Simpler alternatives

For cases where full RFC 8785 compliance is overkill, simpler approaches exist:

- **Sorted keys only**: sort object keys alphabetically and serialize with a stable JSON library. This is not a standard but is widely used and sufficient for most cases where the data is simple (no Unicode edge cases, no number precision issues).
- **JSON.stringify with sorted keys**: in JavaScript, `JSON.stringify(obj, Object.keys(obj).sort())` produces deterministic output for simple objects. This is the pragmatic choice for internal systems.

## The castle's pattern: ordered multi-face source metadata

No existing specification or registry handles the "ordered multi-face source metadata" case specifically. The pattern — preserving ordered source metadata in a deterministic JSON field alongside a scalar-only public projection — is one the castle is naming for the first time. It combines:

1. RFC 8785 JCS for deterministic serialization of the `*_json` field
2. An explicit ordering rule for the multi-face metadata (e.g., by source priority, by timestamp)
3. A documented derivation rule for the top-level scalar projection

The pattern is not standardized, but it is built on a standard (JCS). The castle's contribution is the *shape* of the pattern — the explicit naming of the `*_json` field, the documented derivation order, and the retention of explicit nulls — not the serialization format itself.

## Words

- [[deterministic-json]] — JSON whose keys are ordered and whose encoding is stable across serializations
- [[canonical-schema-literal]] — a field whose value is a deterministic JSON literal, not a parsed object
- [[additive-schema]] — a schema that adds fields without removing or renaming existing ones

## Links

[[canonical-metadata]] · [canonicalization-and-verification](canonicalization-and-verification.md) (the same craft from the log side: the RFC 8785 JCS standard that makes the castle's `*_json` field checkable and the signed chain that is parsed only after every link verifies are the same move — both know a canonical form is the precondition of any proof that the bytes were not changed) · [[representation-audit]] · [[civic-data-honesty]] · [[the-law-of-honest-assertion]]
