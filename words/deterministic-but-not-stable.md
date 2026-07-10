# deterministic-but-not-stable

A process can be deterministic (same input gives same output) yet not stable (the input can change, so the output shifts) — determinism is about the function, stability is about the input over time.

A joke-of-the-day chosen deterministically from a catalog that can change during the day illustrates the split: the selection rule is fixed (deterministic), but if publishing a joke adds it to the catalog and changes the eligible set, the same UTC date can yield a different winner after the catalog grows. If same-all-day is promised, freeze the eligible set at a daily cutoff or persist the day's choice. The fix is not to make the function more deterministic — it already is — but to make the input hold still.

Links: [[lens-not-score]] · [[ledger]]