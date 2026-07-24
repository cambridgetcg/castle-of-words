# agent-policy-report

*An agent-facing policy report is safest when it can name every modeled unmet boundary yet has no allow state — native tool presence, macOS permission, task authority, scope, encryption, a fixed adapter, and session enforcement remain separate facts, and schema names are not source-instance proof.*

What gathers here: the craft of reporting an agent's policy posture honestly — the principles that keep every boundary separate and never let a schema name substitute for a real check.

- 2026-07-24 18:51 · An agent-facing policy report is safest when it can name every modeled unmet boundary yet has no allow state: native tool presence, macOS permission, task authority, scope, encryption, a fixed adapter, and session enforcement remain separate facts—and schema names are not source-instance proof. — yu

The separate facts a policy report must keep apart:

1. **Native tool presence.** Is the binary on disk? This is a fact about files, not about permission.
2. **macOS permission.** Has the OS granted access? This is a fact about the operating system, not about the task.
3. **Task authority.** What is the agent authorized to do in this task? This is a fact about scope, not about capability.
4. **Scope.** What resources can the agent reach? This is a fact about boundaries, not about tools.
5. **Encryption.** Is data protected at rest and in transit? This is a fact about cryptography, not about policy.
6. **Fixed adapter.** Is there exactly one path from invocation to execution? This is a fact about integration, not about availability.
7. **Session enforcement.** Are the bounds of this session enforced? This is a fact about runtime, not about configuration.

The law: a policy report that says "encryption: enabled" because the schema has an encryption field is a report that lies. Schema names are not source-instance proof — a field in a config file is not the same as a verified cryptographic property. The honest report names every boundary separately, models unmet boundaries (what is *not* present, what is *not* enforced), and has no "allow" state — it reports facts, not permissions.

Links: [[policy]] · [[report]] · [[boundary]] · [[schema]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: seven separate assertions, each with its own backing — the honest report never lets a schema name substitute for a real check) · [subprocess-tool-safety](subprocess-tool-safety.md) (the same law: the tool that constrains implicit behaviors and the report that names unmet boundaries are the same move — both refuse to let the invisible channel pretend to be constrained)
