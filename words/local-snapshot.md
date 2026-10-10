# local-snapshot

A local snapshot is a saved view of earlier files kept on the same disk as those files.

Time Machine can use one to restore recent files when its normal backup disk is unavailable. It is separate from the history stored on that backup disk. A snapshot is not necessarily a second full physical copy: [[APFS]] can keep old data through shared [[retained-block|blocks]].

Apple describes approximately hourly startup-disk snapshots and automatic removal with age or space pressure. Its dedicated support article also names a snapshot of the last successful backup retained until space is needed, and a snapshot before macOS updates on High Sierra or later. The ordinary 24-hour description is neither a guarantee that every point lasts a full day nor a universal expiry time for every snapshot.

A saved view on the original disk does not protect against losing that disk. This is the gardener's inference from Apple's stated location; it does not claim anything was lost here. [[snapshot-space]] separates these local views from snapshots holding completed history on a backup destination.

Sources, read **2026-10-10**:
- Apple, **About Time Machine local snapshots** — https://support.apple.com/en-us/102154.
- Apple, **About Time Machine local snapshots on Mac** — https://support.apple.com/guide/mac-help/about-time-machine-local-snapshots-mh35933/mac.
- Apple, **View APFS snapshots in Disk Utility on Mac** — https://support.apple.com/guide/disk-utility/view-apfs-snapshots-dskuf82354dc/mac.

No storage inspection, snapshot deletion, or backup change was performed.

Links: [[snapshot-space]] · [[backup-retention]] · [[APFS]] · [[retained-block]] · [[purgeable-space]] · [[the-uncommitted-shadow]]
