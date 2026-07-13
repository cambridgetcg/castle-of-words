# mutation-timestamp

A mark on a record that says when its contents last changed — not when the catalog was refreshed, but when this specific row was created, updated, or deleted.

Without mutation timestamps, an incremental feed cannot know what changed since last time. A refresh timestamp tells you when the snapshot was taken; a mutation timestamp tells you when the thing inside the snapshot actually changed. The two are different, and confusing them is the catalog's most common lie.

Links: [[deletion-tombstone]] · [[catalog]] · [[incremental-feed]]
