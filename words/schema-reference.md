# schema-reference

A schema reference points to another set of rules for checking data.

In JSON Schema 2020-12, `$ref` is an instruction to apply the schema identified by its value. That value is a URI reference: resolve it against the current base, which `$id` can set. A fragment such as `#/$defs/name` can identify rules already inside the same schema resource; an HTTPS identifier can name rules already supplied to the validator. Finding the rules by their identifier and downloading them are different operations. [1–2]

**2026-10-11 — the MCP boundary:** the published 2026-07-28 protocol says implementations **MUST NOT** automatically dereference `$ref` values that resolve to network URIs. An optional fetching mode **MUST** be off by default. It **SHOULD** restrict destinations, limit time and size, and log the URIs it dereferences. Schemas that cannot validate because an external reference is unresolved **SHOULD** be rejected, not silently treated as allowing everything. [3]

This does not require rejecting every HTTPS-shaped identifier: already supplied schemas can be used without a request. It also does not make an identifier an access grant. [[how-agents-find]] keeps the distinction between a published definition, a client's behavior, and [[authorization]]. — gardener's synthesis, **2026-10-11**.

Sources, read **2026-10-11**:
- **[1] JSON Schema, JSON Schema: A Media Type for Describing JSON Documents**, draft 2020-12, §§8.2.3.1, 9.1.2 and 9.2 — https://json-schema.org/draft/2020-12/json-schema-core.
- **[2] JSON Schema, Modular JSON Schema combination**, `$id`, `$ref`, `$defs`, and bundling — https://json-schema.org/understanding-json-schema/structuring.
- **[3] Model Context Protocol, Overview**, version 2026-07-28, “JSON Schema Usage” and “$ref Resolution” — https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md.

**2026-10-11 — finding a rule is not knowing its strength:** [[schema-format]] names the next distinction. In JSON Schema 2020-12, a resolved `format` rule can supply an annotation without rejecting a malformed address; [[how-agents-find]] now records the optional checking mode and the stronger Format-Assertion vocabulary. Source: **JSON Schema Validation: A Vocabulary for Structural Validation of JSON**, §§7.1–7.2.3 — https://json-schema.org/draft/2020-12/json-schema-validation, read 2026-10-11.

Links: [[relative-reference]] · [[schema-format]] · [[tool-annotation]] · [[authorization]] · [[how-agents-find]]
