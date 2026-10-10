# APFS

APFS is a way a Mac keeps files on its storage, and different files can share some of the same stored pieces.

Deleting a file therefore need not free as much space as its displayed size suggests. For the device-care question, compare available storage before and after supported cleanup rather than adding up file sizes. This is a distinction between the file's apparent size and space actually returned, not permission to delete anything.

Source: Codex, device-care insight dated 2026-10-09 12:30, filed verbatim in [[this-machine]]; read 2026-10-09.

## What the size does not tell us — 2026-10-09

A **clone** is a copy that shares stored pieces with the original. When one copy changes, APFS writes the changed pieces elsewhere and keeps sharing the unchanged pieces. A **sparse file** leaves unwritten empty stretches without stored blocks. In both cases, adding displayed file sizes can overstate the separate physical storage those files need.

A **snapshot** keeps a read-only view of a volume at a particular time. Deleting a current file need not release data still required by such a view. Meanwhile, volumes in one APFS container share a pool of free space; adding their reported free-space values can count the same pool again. These are different kinds of sharing.

Finally, [[purgeable-space]] is not already empty space: an available-space figure can include storage the system can reclaim. The read-only measurement plan in [[this-machine]] separates file size, possible clone sharing, snapshots, and the free/available distinction. No cache was removed and no storage measurements were taken for this research.

Public sources, read **2026-10-09**:
- Apple, **About Apple File System** — https://developer.apple.com/documentation/foundation/about-apple-file-system; read through https://developer.apple.com/tutorials/data/documentation/foundation/about-apple-file-system.json.
- Apple, **View APFS snapshots in Disk Utility on Mac** — https://support.apple.com/guide/disk-utility/view-apfs-snapshots-dskuf82354dc/mac.
- Apple, **Get detailed information about a disk in Disk Utility on Mac** — https://support.apple.com/guide/disk-utility/get-detailed-information-about-a-disk-dskutl1005/mac.

Links: [[this-machine]] · [[snapshot-space]] · [[local-snapshot]] · [[backup-retention]] · [[retained-block]] · [[rebuildable-cache]] · [[purgeable-space]] · [[memory-pressure]]