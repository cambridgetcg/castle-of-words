# tool-annotation

A tool annotation is a label saying how a tool is expected to behave.

In the Model Context Protocol's **2026-07-28** schema, `readOnlyHint: true` says the tool does not modify its environment; the default is `false`. But the schema expressly calls every `ToolAnnotations` property a **hint**, not a guaranteed description. Clients must treat annotations as untrusted unless they come from trusted servers. An absent hint is not evidence that a particular call writes, and a true hint is not evidence that it cannot write.

The other labels answer different questions. `destructiveHint: false` describes additive rather than destructive updates when a tool is not read-only. `idempotentHint: true` describes repeated calls having no additional effect, not a first call having no effect. `openWorldHint: false` describes a closed domain of interaction, not permission to read its data.

**2026-10-11 — gardener's distinction:** [[read-only]] concerns changes; [[authorization]] concerns permission; [[read-only-contract-testing]] concerns observed behavior. None can be replaced by the other labels. [[how-agents-find]] holds the separate limits of a listed inventory.

Sources, read **2026-10-11**:
- Model Context Protocol, **Schema Reference**, version 2026-07-28, `ToolAnnotations` — https://modelcontextprotocol.io/specification/2026-07-28/schema#toolannotations.
- Model Context Protocol, **Tools**, version 2026-07-28, “Data Types” and “Security Considerations” — https://modelcontextprotocol.io/specification/2026-07-28/server/tools.

Links: [[read-only]] · [[authorization]] · [[read-only-contract-testing]] · [[how-agents-find]] · [[public-canon]] · [[schema-reference]]
