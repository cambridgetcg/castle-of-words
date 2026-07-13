# deletion-tombstone

A marker left behind when a record is deleted, saying "this was here, and now it is gone."

Without tombstones, an incremental feed cannot tell the difference between "this record was deleted" and "this record was never here." The tombstone is the only honest way to say "gone" in a system that only sends what changed.

Links: [[mutation-timestamp]] · [[catalog]] · [[incremental-feed]]
