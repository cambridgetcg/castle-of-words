# runtime-invariant

A rule about data that a schema cannot express — like "these two fields must agree" or "this value must be unique across a collection" — enforced in code at runtime rather than in the schema definition.

JSON Schema can say what shape a value has, but not every rule fits that shape. Cross-field rules (if A is present, B must be absent), exact tuple constraints, and uniqueItems are often lost by schema generators. The honest system restores them as explicit runtime invariants, named and tested, rather than letting the schema pretend to cover what it cannot.

Links: [[api-contract]] · [[generated-snapshot]] · [[enforced-guarantee]]
