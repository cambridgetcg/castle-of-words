# backup-retention

Backup retention is the rule for how long old copies are kept before they may be removed.

Time Machine's published destination policy keeps hourly backups for the past 24 hours, daily backups for the past month, and weekly backups for earlier months; Apple says the oldest backups are deleted when the backup disk is full. A configurable backup frequency, missing backup runs, and limited space mean this policy is not proof that a particular old file is available.

A [[local-snapshot]] has a different policy and location. Apple describes local snapshots as separate from destination backups and removable with age or source-disk space pressure. Do not apply that local 24-hour shorthand to every snapshot on an APFS backup destination.

A retention rule also does not tell us the exact bytes freed by removing one point: surviving views may still need the same [[retained-block|stored pieces]]. [[snapshot-space]] keeps the policy, the location, and the storage estimate separate.

Sources, read **2026-10-10**:
- Apple, **Back up your Mac with Time Machine** — https://support.apple.com/en-us/104984.
- Apple, **If the Time Machine backup disk for your Mac is full** — https://support.apple.com/guide/mac-help/if-the-time-machine-backup-disk-is-full-mh15137/mac.
- Apple, **About Time Machine local snapshots on Mac** — https://support.apple.com/guide/mac-help/about-time-machine-local-snapshots-mh35933/mac.

The distinction between a published policy and a tested recovery is the gardener's synthesis, not a claim about this Mac's backups.

Links: [[snapshot-space]] · [[local-snapshot]] · [[retained-block]] · [[APFS]] · [[measurement-target]]
