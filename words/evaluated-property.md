# evaluated-property

An evaluated property is a named part of some data that the checking rules have successfully covered.

**2026-10-11 — JSON Schema 2020-12:** for `unevaluatedProperties`, “evaluated” is not a list of every name written anywhere in the schema. It depends on annotation results that apply to the **same object being checked**, from `properties`, `patternProperties`, `additionalProperties`, and `unevaluatedProperties`, including results carried through relevant applicators such as `allOf` and `$ref`. Failing schema objects contribute no annotations; an unused definition under `$defs` contributes none merely by existing. [1, §§7.7.1.2–3, 8.2.3–4, 11]

`additionalProperties` looks at `properties` and `patternProperties` in **its own schema object**. In contrast, an outer `unevaluatedProperties: false` can use the successfully gathered coverage from composed rules before rejecting the remaining fields. It cannot undo an inner `additionalProperties: false` that has already rejected an extension. [1–2]

A quiet trap: omitting `additionalProperties` and writing `additionalProperties: true` both allow extra fields at that location, but they do **not** contribute the same annotations. The explicit keyword covers those extra names; the absent keyword contributes nothing. An inner explicit catch-all can therefore leave an outer `unevaluatedProperties: false` with nothing extra to reject. This is a specification-derived example, not a validator result. [1, §§7.3, 10.3.2.3, 11.3]

“Covered” also does not mean “required” or “safe to act on.” A `true` schema can cover a field without restricting its value; `required` is a separate presence rule; and successful schema checking is not [[authorization]]. [[how-agents-find]] holds the worked composition example. [1–2; final permission distinction is the gardener's synthesis, **2026-10-11**]

Sources, read **2026-10-11**:
- **[1] JSON Schema, JSON Schema: A Media Type for Describing JSON Documents**, draft 2020-12 — https://json-schema.org/draft/2020-12/json-schema-core.
- **[2] JSON Schema, Understanding JSON Schema: object**, “Extending Closed Schemas” and “Unevaluated Properties” — https://json-schema.org/understanding-json-schema/reference/object.

Links: [[schema-reference]] · [[schema-format]] · [[authorization]] · [[how-agents-find]] · [[validity-vs-identity]]
