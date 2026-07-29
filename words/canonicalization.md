# canonicalization

The craft of turning a collection of records into a single verifiable form — choosing the right budget for the right kind of truth.

Different kinds of records need different canonicalization budgets. A move log (one action at a time) needs each entry small enough to judge alone. A full-state snapshot (the whole season at once) needs to serialize everything safely without inheriting the per-move ceiling. The craft is choosing the right budget and signing the whole chain before parsing any part.

Links: [[move-log]] [[paper-sail]] [[verification]]
