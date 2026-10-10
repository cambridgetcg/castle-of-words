# retained-block

A retained block is a piece of stored data that cannot be freed yet because something still needs it.

An [[APFS]] snapshot can keep an old block after today's file changes or disappears. Several snapshots, and sometimes the live filesystem too, can refer to the same block. Deleting one reference is not the same as removing the last reference.

This is why **Private Size** and **Cumulative Size** answer different questions. A block shared only by two snapshots is private to neither; removing both can release more than adding their original private sizes suggests. Cumulative groups overlap, so adding their totals can count the same storage twice. [[snapshot-space]] gives the sourced column definitions and their limits.

Source: ScaleNinja, **Snapshot storage — DeltaSnap Docs**, https://scaleninja.com/docs/deltasnap/snapshot-storage/ — read **2026-10-10**. The two-snapshot example is the gardener's explanation of the documented sharing rule, not a measurement of this Mac or permission to delete anything.

Links: [[APFS]] · [[snapshot-space]] · [[this-machine]] · [[purgeable-space]] · [[measurement-target]]
