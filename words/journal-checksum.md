# journal-checksum

A hash computed over the migration journal that proves its bytes have not been altered since they were applied.

If every applied migration is immutable byte history, a checksum over the whole journal is the proof that the history is intact. Before claiming a deployment is correct, verify that the journal's checksum matches the recorded one. A mismatch means something changed — a drift, a tamper, a silent edit — and the deployment claim must pause until the gap is understood.

Links: [[migration-byte-history]] · [[database-drift]] · [[data-invariant]]
