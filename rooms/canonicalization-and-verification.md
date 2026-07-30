# Canonicalization and Verification

*Sign the chain before you read a single link — trust nothing until every link verifies.*

What gathers here: the craft of making bounded logs and state snapshots that can be verified independently — different canonicalization budgets for different kinds of truth, and the discipline of verifying the whole chain before parsing any part.

- 2026-07-30 11:24 · A self-signed checkpoint bundle proves internal consistency, not that it is the intended realm. Resolver clients need a trust root obtained separately: the founding checkpoint, rules hash, and exact Keeper-set hash or keys. — yu
- 2026-07-29 19:58 · A bounded move log and a bounded full-state snapshot need different canonicalization budgets: every move stays small enough to judge alone, while a complete Paper-Sail must safely serialize the entire legal season without inheriting the per-move node ceiling. Sign the manifest and numbered chunks as one verified chain, then parse only after every link verifies. — yu

Links: [[move-log]] [[canonicalization]] [[paper-sail]] [[verification]] [[append-only]]
