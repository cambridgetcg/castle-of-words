# append-only

*A record that grows forward and never rewrites backward — new facts are added, old facts stay.*

An append-only record is a list where you can only add new entries, never change or remove old ones. The honesty is in the history: anyone can see what was said and when. If something must be corrected, you append a correction — you do not erase the original. If something must be removed, you append a [[tombstone]] — you do not delete the entry.

In the castle's rooms, the append-only property is the law behind the [[manifest]], the [[key-transparency-log]], and the [[truth-chain]]: each is a ledger that only writes down what happened, chained so that nothing can be removed. The [[immutable-correction]] word holds the same principle for corrections: they are appended, never overwritten. The [[tombstone]] is the append-only answer to deletion: you cannot remove the old entry, but you can say it is no longer true.

Links: [[immutable-correction]] · [[tombstone]] · [[manifest]] · [[verification-hash]]
