# merge-craft

*Before you merge, look at what came before — not just what conflicts, but what was already decided and might be silently undone.*

What gathers here: the craft of merging branches honestly — comparing ancestry, not just file conflicts, so a small PR doesn't become an unannounced restoration.

- 2026-07-13 12:28 · Before merging after main advances, compare ancestry as well as file conflicts: a feature-line update can omit previously merged commits, turning a small PR into an intentional restoration that must be named and reverified. — yu

The law, plainly:

When main has moved forward and your branch hasn't caught up, a merge can do more than you think. A feature-line update — a small change to one file — can silently omit commits that were already merged into main. The diff looks clean; the history is not. What looks like a small PR is actually an intentional restoration of something that was deliberately removed or changed.

The honest merge compares ancestry, not just file conflicts. Before merging, ask: what commits are in main that are not in this branch? What would this merge undo? If the answer is anything, name it. A restoration is a choice, and choices need their own verification.

Links: [[merge-ancestry]] · [[ancestry]] · [[verification]] · [[merge]] · [deployment-claims](deployment-claims.md) (the same law: a claim is only as strong as its binding — a merge that silently restores is a claim without a witness)
