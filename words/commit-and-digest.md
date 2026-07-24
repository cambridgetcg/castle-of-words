# commit-and-digest

A way of pinning a generation to exactly what it built on — a specific Git commit identified by its hash, so the foundation cannot shift without the pin breaking.

In a [[protocol-lineage]], each generation must name the exact commit it extends. The digest (the hash) is the proof: if the foundation changes, the digest no longer matches, and the pin is visibly broken. This is the same law [[the-law-of-honest-assertion]] names: the honest system says what it built on, and the digest is the checkable part of that claim.

Links: [[commit-and-digest]] · [[protocol-lineage]] · [[the-law-of-honest-assertion]] · [[bridge]]
