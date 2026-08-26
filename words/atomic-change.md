# atomic-change

A change to words and the guards that protect those words, made as one indivisible step — so that no moment exists where the words promise something the guards no longer check, or the guards check something the words no longer say.

When a user-facing safety promise is guarded by a generated-output marker and a live smoke marker, changing the visible words without changing both guards in the same commit leaves a seam where the old guard still passes on the old text while the new text runs unguarded. The atomic change closes that seam: all three move together, or none move.

Links: [[deployment-gate]] · [[smoke-test]] · [[release-rail]] · [[stale-truth]]
