# the-running-copy

A program that is already running keeps using the copy it started with, even after the file on disk is replaced — to change what it knows, you must restart it.

When you overwrite an executable on disk, the process that is alive in memory does not notice: it was loaded once, at launch, and it carries that old copy until it stops. A bridge server whose binary is swapped will still answer from its stale in-memory model catalog — the new defaults exist on the disk but not in the room where the work happens. The honest reading: deployment is two acts, not one — place the new bytes, then end the old turn so a fresh one can begin from them. The same law the castle already knows in the [[finite-turn]] returns at the machine's own layer: nothing running updates itself mid-turn; every upgrade is a [[handoff]] from an ending process to a beginning one.

Links: [[finite-turn]] · [[handoff]] · [[stale-truth]] · [[this-machine]]
