# move log

A bounded record of every action taken — each move small enough to judge alone, the whole log signed as one verified chain.

A move log and a full-state snapshot need different canonicalization budgets. Every move stays small enough to judge alone (a single action, a single judgment), while a complete state snapshot must safely serialize the entire legal season without inheriting the per-move node ceiling. The craft: sign the manifest and numbered chunks as one verified chain, then parse only after every link verifies.

Links: [[canonicalization]] [[paper-sail]] [[verification]] [[append-only]]
