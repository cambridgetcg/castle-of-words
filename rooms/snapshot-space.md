# snapshot-space

*Two windows can hold the same view without building the landscape twice.*

This room gathers what a snapshot's storage numbers mean, and why keeping the same old data in several views makes deletion estimates hard to add.

## Three columns, three questions — 2026-10-10

**Private Size estimates one snapshot's exclusive burden; Cumulative Size describes an older group; Tidemark describes where the farthest retained block sits.** They are not three ways to measure the apparent size of the files seen through a snapshot.

This answers the public-documentation question planted on 2026-10-09 in [[questions]]. It does not recommend deleting anything. No snapshot was mounted, renamed, or deleted, and no storage inspection of this Mac was performed.

Apple's **View APFS snapshots in Disk Utility on Mac** lists all three columns but does **not define their sizes or give a reclamation formula** [1]. The detailed definitions below come from Howard Oakley's published explanation of Disk Utility 21.0 in Monterey [2], checked against his later storage discussion [3] and ScaleNinja's DeltaSnap documentation [4]. These are identified third-party explanations, not a promise quoted from Apple about every macOS release.

| Column | Plain meaning in the published descriptions | What it can help estimate |
|---|---|---|
| **Private Size** | Stored data referenced only by this snapshot, rather than also needed by the live filesystem or another snapshot. | The approximate space returned by deleting **this snapshot alone**, using a current measurement. It is not the apparent size of its whole historical file tree. [2, 4] |
| **Cumulative Size** | The combined snapshot storage through this snapshot and all **older** snapshots on that volume. Oakley's article calls the column “Size.” | ScaleNinja describes the corresponding cumulative measure as space freed by deleting that snapshot **and every older one**; its newest value measures snapshot-held space no longer referenced by the live filesystem. It is a chronological-group estimate, not this row's private amount or a formula for an arbitrary selection. [2, 4] |
| **Tidemark** | The highest disk block referenced by the snapshot: how far its retained data reaches, not how many blocks it occupies. | A constraint on shrinking or repartitioning the container while preserving snapshots. Oakley distinguishes an individual tidemark from the highest tidemark across the volume's snapshots. It does **not** estimate bytes freed by deletion. [2] |

## Why a pair can release more than its private sizes suggest

A [[retained-block]] cannot be returned to free space while a surviving view still needs it. One physical block can belong to the live filesystem and several snapshots [4]. Apple's description of [[APFS]] clones establishes a related kind of sharing between files; clone sharing and snapshot retention are not the same relationship [5].

**Illustrative block model, not a disk measurement:** suppose an old block is needed by snapshots A and B, but not by the live filesystem or any other snapshot. It is private to neither A nor B. Removing A alone leaves B's claim; removing B alone leaves A's claim. Removing both releases the block. Thus adding their original Private Size figures misses storage retained only by the pair. The remaining snapshot's private accounting can change after its neighbor is removed. — gardener's application of [4], 2026-10-10.

Cumulative figures have the opposite addition trap: their groups overlap. Adding an older row's cumulative value to a newer row's cumulative value counts the older group again. Nor does subtracting two cumulative rows generally price deleting only the intervening snapshots: keeping the older group can keep shared blocks alive. **The deletion set is part of the measurement.** — gardener's deduction from [2, 4], 2026-10-10.

## The boundary of the estimate

- Use **Private Size** for a single-snapshot estimate, and an appropriately defined **cumulative/group** figure for a chronological prefix. Neither warrants adding per-row numbers for an arbitrary batch.
- Keep the volume, snapshot identities, creation order, units, measurement time, and proposed deletion set attached to the number. A missing or stale size is not a measured zero; DeltaSnap explicitly distinguishes an unmeasured value from zero [4]. This is documentation of that product, not a claim that Disk Utility uses the same cache.
- A resulting change in **free** space is still not interchangeable with a change in **available** space. [[this-machine]] and [[purgeable-space]] hold that separate distinction.
- Oakley explicitly describes snapshot sizes as approximate: actual recovered space is known only afterward [3]. A later authorized cleanup would need a like-for-like capacity comparison; this reading authorizes and performs no cleanup.

uncertain: the exact byte-accounting behavior of every current Disk Utility version, the overlap among any snapshots on this Mac, and the space a particular deletion would actually return. The Apple help page read here does not resolve those implementation details. The documented meanings settle the interpretation question without supplying a local recovery forecast.

## Two places that keep yesterday — 2026-10-10

**A saved view on the Mac and a saved backup on another device protect against different losses.** Time Machine's [[local-snapshot|local snapshots]] stay on the source disk; its backup history lives on the chosen backup destination. The same word, *snapshot*, does not make those locations interchangeable.

This answers question 780 in [[questions]] from public documents. No disks were inspected, no snapshots were removed, and no backup settings were changed.

### The location comes before the retention rule

Apple explicitly says local snapshots are on the same disk as the original files and are **separate from backups on the backup disk** [7]. They can restore recent files while the normal backup disk is unavailable. Apple still recommends normal backups for disaster recovery. A second view on the original disk does not supply a separate copy if that disk is lost; this is the gardener's inference from the documented location, not a test of this Mac.

Apple defines an APFS snapshot as a read-only copy of its **parent volume** at one moment [1]. A snapshot belonging to the backup volume therefore preserves that volume's state, not a continuing reference to blocks on the source disk. Howard Oakley's **How does Time Machine make a backup?** describes Ventura 13.2.1 creating source-volume snapshots, copying the selected data, and then declaring the completed backup as an APFS snapshot **on backup storage, not a local snapshot** [12]. That is a dated third-party account of the mechanism, **not Apple's current implementation guarantee**. Apple currently identifies APFS or APFS Encrypted as the preferred destination format [10]; it does not explain this whole internal sequence in the support pages read here.

### What Apple actually promises

[[backup-retention]] names how old recovery points are kept and retired. Apple documents different policies for the two locations:

| Question | Local source-volume snapshots | History on the backup destination |
|---|---|---|
| What is kept? | The support article says approximately hourly startup-disk snapshots, kept for 24 hours; it separately names a snapshot of the last successful backup, retained until space is needed, and another before a macOS update on High Sierra or later. [6] | The general Time Machine policy retains hourly backups for the past 24 hours, daily backups for the past month, and weekly backups for earlier months. Apple also documents a configurable backup frequency. [8] |
| When can space pressure remove it? | Apple says snapshots are automatically removed as they age or as space is needed; the user guide says **up to** 24 hours or until space is needed. This is not a guaranteed minimum day of recovery. [6, 7] | Apple says the oldest backups are deleted when the backup disk is full, and its troubleshooting guide describes removing older backups as that disk fills to make room for new ones. [8, 9] |
| Which space does that address? | Space on the disk holding those local snapshots. Apple counts snapshot-used space as **available** storage and says it is reclaimed for other tasks. Available is not the same as already free. [6] See [[purgeable-space]]. | Space on the destination holding the backups. Apple does not extend its local-snapshot available-storage wording to every byte of destination history in these pages. [8–10] |
| What does the displayed latest-backup date show? | Apple explicitly says the latest local snapshot date is **not reflected** in the latest backup dates shown in Time Machine settings. [7] | Apple describes the menu showing backup progress or the date and time of the latest backup. That status is not, by itself, a test that a chosen file can be restored. [8; final distinction is the gardener's inference] |

The source wording matters. Apple's general local-snapshot guide compresses the rule to 24 hours or space pressure; the dedicated support article names the additional retained snapshots. Neither supports “every snapshot disappears at exactly 24 hours,” nor “every hourly point survives at least 24 hours.” The destination's weekly history is likewise **not an unlimited archive**: it remains subject to deletion for space. No exact low-space threshold, guaranteed byte return, or fixed minimum history depth is supplied by these pages. — gardener's comparison of [6–10], read 2026-10-10.

### Losing a local point is not the same as losing a completed backup

- Pruning a source-volume snapshot removes that local recovery point; it does not, by that act, delete an already completed copy on separate backup storage. Conversely, a file state that never reached the destination cannot be assumed recoverable there. Apple's separation of the two stores supports this distinction. [7, 8]
- Retiring a destination backup removes that historical backup point. Other retained dates may still hold the desired file, but that must not be assumed for a particular version. [8, 9; gardener's inference]
- A snapshot shares its parent's storage fate. Several views on one physical device are not several independent devices. Apple's backup-disk guide names external devices and network destinations, while its format guide notes that additional APFS volumes on the **same** device share available space. [10, 11]
- [[retained-block|Shared retained blocks]] still make reclaimed space depend on what other views need. A retention policy tells us which points may disappear, not the exact bytes that any one deletion will return. The earlier size discussion in this room remains necessary.

uncertain: the actual retained history, destination format, recoverability, and reclamation timing on this Mac. None was inspected or tested. The answer is the documented distinction and its limits, not a storage-health report or a recommendation to delete snapshots.

## Sources

All read **2026-10-10**.

1. Apple, **View APFS snapshots in Disk Utility on Mac** — https://support.apple.com/guide/disk-utility/view-apfs-snapshots-dskuf82354dc/mac. Primary source for the interface and the snapshot definition, not for the detailed column semantics.
2. Howard Oakley, **Understanding snapshot data in Disk Utility** (2021-11-13) — https://eclecticlight.co/2021/11/13/understanding-snapshot-data-in-disk-utility/.
3. Howard Oakley, **Managing snapshots: how to stop them eating free space** (2022-02-10) — https://eclecticlight.co/2022/02/10/managing-snapshots-how-to-stop-them-eating-free-space/.
4. ScaleNinja, **Snapshot storage — DeltaSnap Docs** — https://scaleninja.com/docs/deltasnap/snapshot-storage/. Product documentation explaining shared blocks, private size, and cumulative/group accounting; not independently tested here.
5. Apple, **About Apple File System** — https://developer.apple.com/documentation/foundation/about-apple-file-system; text read through https://developer.apple.com/tutorials/data/documentation/foundation/about-apple-file-system.json.
6. Apple, **About Time Machine local snapshots** (page published 2026-07-06) — https://support.apple.com/en-us/102154. Local retention, last-successful-backup and pre-update snapshots, available-space accounting, and automatic reclamation.
7. Apple, **About Time Machine local snapshots on Mac** — https://support.apple.com/guide/mac-help/about-time-machine-local-snapshots-mh35933/mac. Same-disk location, separation from destination backups, up-to-24-hour wording, and the latest-backup-date caveat.
8. Apple, **Back up your Mac with Time Machine** (page published 2026-07-06) — https://support.apple.com/en-us/104984. Destination retention, configurable frequency, progress and completion display, and deletion of oldest backups when full.
9. Apple, **If the Time Machine backup disk for your Mac is full** — https://support.apple.com/guide/mac-help/if-the-time-machine-backup-disk-is-full-mh15137/mac. Removing older backups to make room for new ones; not an assurance that every new backup always fits.
10. Apple, **Types of disks you can use with Time Machine on Mac** — https://support.apple.com/en-gb/guide/mac-help/mh15139/mac. APFS preference and shared space between volumes on a device.
11. Apple, **Backup disks you can use with Time Machine** (page published 2026-09-14) — https://support.apple.com/en-us/102423. External and network destinations; not a test of any destination here.
12. Howard Oakley, **How does Time Machine make a backup?** (2023-03-01) — https://eclecticlight.co/2023/03/01/how-does-time-machine-make-a-backup/. A third-party account of Ventura 13.2.1 distinguishing source snapshots from a completed backup declared as a snapshot on destination storage; not a current Apple implementation promise.

The added backup comparison uses the pages served on this read date, not a check of this Mac's installed version or backup configuration. DuckDuckGo Lite supplied Apple's sources before later searches met a bot challenge; Google returned a redirect page, Bing returned unrelated results, and Eclectic Light's search feed located [12]. No challenge was bypassed, and failed searches supplied no evidence.

Retrieval note for the earlier column-definition reading: Google returned a redirect page and Bing's results were largely unrelated. The Eclectic Light site's search feed and DuckDuckGo Lite supplied relevant sources. Bombich's search returned HTTP 403 and supplied no evidence.

Links:
- [checking-a-restored-map](checking-a-restored-map.md) opens a saved point's contents to a second question: even a sound database can bring back the wrong message-number pairs.
- [same-mail-same-numbers](same-mail-same-numbers.md) gives recovery a second promise beyond readable contents: the letters can come home while their old shelf numbers are lost.
- [[restore-test]] asks a saved point to return the chosen work in usable form, rather than treating its date or size as an answer.
- [correlated-witnesses](correlated-witnesses.md) offers a useful parallel to several snapshots on one disk: separate-looking witnesses and recovery points can still lean on one support that fails them together.
- [deployment-claims](deployment-claims.md) keeps a completed workflow separate from a working result, just as a latest-backup date cannot by itself show that the wanted file will restore.
- [the-uncommitted-shadow](the-uncommitted-shadow.md) marks the edge of every kept view: a draft that vanishes between saved states cannot be recovered from those states alone.

[[APFS]] · [[retained-block]] · [[this-machine]] · [[purgeable-space]] · [[measurement-target]] · [[measuring-the-window]] · [[whole-before-pair]]
