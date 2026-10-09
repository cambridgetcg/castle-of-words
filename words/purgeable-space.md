# purgeable-space

Purgeable space is storage holding things the system can remove when it needs room for something else.

It is not the same as space already empty. Apple's Disk Utility documentation says that **available** storage can include both free and purgeable space. Apple's Time Machine documentation also says that space used by local snapshots counts as available storage. A before-and-after comparison must therefore keep the same measure: free bytes and available bytes answer different questions.

The read-only Foundation property `isPurgeableKey` asks whether the file system can delete a particular file to free space. It is not a promise about the amount reclaimed or permission for the gardener to delete that file. [[APFS]] clones and snapshots can also keep blocks shared or retained, so a file's displayed size is not a cleanup receipt.

Sources, read **2026-10-09**:
- Apple, **Get detailed information about a disk in Disk Utility on Mac** — https://support.apple.com/guide/disk-utility/get-detailed-information-about-a-disk-dskutl1005/mac.
- Apple, **About Time Machine local snapshots** — https://support.apple.com/en-us/102154.
- Apple, **isPurgeableKey** — https://developer.apple.com/documentation/foundation/urlresourcekey/ispurgeablekey; read through Apple's documentation JSON at https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/ispurgeablekey.json.

Links: [[APFS]] · [[this-machine]] · [[rebuildable-cache]]
