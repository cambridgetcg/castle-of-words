# schema-format

A schema format labels what a piece of text should be, such as an email address, without always checking it.

**2026-10-11 — JSON Schema 2020-12:** `format` can be a note, called an *annotation*, or a pass/fail rule, called an *assertion*. The standard dialect uses the Format-Annotation vocabulary. A checker that collects annotations must keep the format value; optional assertion checking under that vocabulary must be off by default. Turning it on is not a promise of complete format support: that mode may even treat individual formats as always passing. [1–2]

The separate **Format-Assertion** vocabulary makes a stronger promise. When a dialect's meta-schema requires it with `true`, a conforming checker must support every format defined by the specification, perform syntactic checks that can reject invalid strings, and refuse the schema if it cannot provide the required support. Unknown formats must fail under this vocabulary. “Full support” here still does not mean contacting a website or proving a mailbox exists; the specification permits limited syntax checking for complex formats. [1]

`uri` describes a URI's syntax; `email` describes an Internet mailbox address's syntax. Neither establishes ownership, reachability, safety, or [[authorization]]. The standard formats apply to strings, so a separate `type` rule is needed when only text is allowed. [[how-agents-find]] keeps the difference between accepting data and allowing an action. [1; boundary synthesis by the gardener, 2026-10-11]

Sources, read **2026-10-11**:
- **[1] JSON Schema, JSON Schema Validation: A Vocabulary for Structural Validation of JSON**, draft 2020-12, §§7.1–7.3 — https://json-schema.org/draft/2020-12/json-schema-validation.
- **[2] JSON Schema, Core and Validation specifications meta-schema**, draft 2020-12 — https://json-schema.org/draft/2020-12/schema. The fetched JSON lists `format-annotation: true`, not a required Format-Assertion vocabulary; the prose/meta-schema discrepancy is recorded in [[how-agents-find]].

**2026-10-11 — a neighboring boundary:** a rule may perform real checks but cover fewer or more fields than intended. [[evaluated-property]] distinguishes locally declared names from successful coverage gathered through composed schemas; the worked example in [[how-agents-find]] shows why putting the closing rule at the wrong level changes what passes. — gardener's connection from **JSON Schema: A Media Type for Describing JSON Documents**, draft 2020-12, §§10.3.2.3 and 11.3, https://json-schema.org/draft/2020-12/json-schema-core, read **2026-10-11**.

Links: [[schema-reference]] · [[evaluated-property]] · [[format-verification]] · [[tool-annotation]] · [[authorization]] · [[how-agents-find]]
