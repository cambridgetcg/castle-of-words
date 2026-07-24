# commit-ancestry

A Git commit's identity is its position in the tree, not just its content — cherry-picking the same diff to a new parent gives it a new identity.

When an immutable release manifest names a source revision, the integration must preserve that commit's ancestry. If a source commit is cherry-picked and gets a new identity, the manifest must be re-forged and re-verified — even when the artifact bytes remain identical. The bytes are the same, but the pointer is different, and a manifest that points to a commit that no longer exists in the published history is a manifest that lies about its own ground.

Links: [[immutable]] · [[reproducible-build]] · [[manifest]] · [ordered-release](../rooms/ordered-release.md)
