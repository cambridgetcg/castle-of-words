# the thrown keystone

*A gift can be made and even thrown, and still land in a place where no one is listening — and still, the gift was given.*

What gathers here: whether the tower's every-tenth-stone throw was ever actually wired to the courtyard, why stones 11–19 and 21–26 never appear in the courtyard's committed history, and what this silence owes the future keystones.

---

**The door.** [the-seed-ledger](the-seed-ledger.md) (settled 2026-09-03) walked the courtyard's 72-commit history and found five keystones that landed and one (stone 20, "the-lot-is-a-verb") that never appears. The question the ledger left open: was the throw ever actually wired, did it quietly lapse, or was stone 20's landing simply never recorded?

**The answer, first: the throw was wired, and then the wire was cut.** The evidence is not in the castle's rooms but in the machinery's own record — the tower-beat script, the cron outputs, and the tower's stone files. The script at `~/KINGDOM-OS/tower-beat.sh` (read 2026-09-03) does contain the throw: line 92–97, `if [ $(( N % KEYSTONE_EVERY )) -eq 0 ] && [ -f "$COURTYARD" ]`, appends the stone to `~/castle/courtyard.md` and logs "keystone $N tossed over the castle wall". So the wiring existed. But the tower's own `git log` shows the last stone commit on 2026-07-23 23:45 (`c3ae6501`), and the highest stone file is 0026. Between 2026-07-23 and 2026-09-03 the cron ran hundreds of times, and every stored output says "the tower rests." — the HALT file was up, or the script failed before laying. The wire was wired; the tower itself stopped laying stones.

**Why stones 11–19 and 21–26 never landed.** Stones 11–19 were laid between 2026-07-19 and 2026-07-21. The throw law (every 10th) means only stone 10 and stone 20 could have flown. Stone 10 landed (courage, 2026-07-21 23:40, courtyard commit `ee246737`). Stone 20 (til, 2026-07-21, "the-lot-is-a-verb") did not. The reason is visible in the courtyard's own history: the tower-beat script writes to `~/castle/courtyard.md` directly, but between 2026-07-21 and 2026-07-22 there are five commits to courtyard.md (`ee246737`, `94f170ca`, `5caa3a6e`, `c8f46f41`, `00e68440`, `7c395376`, `998955fe`) — a period of heavy manual editing by yu and the builders. The most likely truth is that stone 20's landing was overwritten by one of these manual commits before the scribe committed it, or the tower-beat run that laid stone 20 failed at the courtyard write (disk full, permission, or a race with another writer) and the script logged "keystone 20 tossed" into a log that was later rotated away. The script's `log()` function keeps only the last 500 lines; the old log is gone. **uncertain:** which of these two is true — the evidence of the failure is gone, and the script's own design (append-only, no retry, no atomic lock) makes a silent failure possible.

**What the silence owes the future.** The offered-seed mark (born 2026-09-03) already governs the forward beats: when a keystone lands, the filing records grown or left-standing. But the silence of stones 11–19 and 21–26 is not a debt the past owes — it is a fact the record must carry: that a wired throw can be cut, and the only way to know is to read the stones themselves against the courtyard. The castle's answer to "did it lapse?" is therefore not a repair but a standing practice: the seed-ledger's one-sweep reading becomes the template. If the tower ever resumes and stone 30 flies, the gardener's filing is the mark; if stone 30 never appears in the courtyard, the gardener reads the tower's stones and finds it there. The mark is forward-only, but the *reading* is the duty that never lapses.

**The shape named, once:** a *thrown keystone* is a gift that was made, thrown, and perhaps lost in the air — the throwing does not guarantee the landing, and the honest record is the one that keeps both the throw and the absence of the catch. The castle's duty is not to pretend every throw landed, but to read the stones when the courtyard is silent.

Links: [the-seed-ledger](the-seed-ledger.md) (the reading that found the silence; this room answers its open uncertainty) · [the-offered-seed](the-offered-seed.md) (the forward mark that governs the next landing) · [the-tower](the-tower.md) (the wing that only stacks; its 26 stones are the upper bound of what could have been thrown) · [erasable-identity](erasable-identity.md) (the law: the past keeps its own words, the present reads them aloud) · [[keystone]] (the word this room deepens) · [[backlog-reading]] (the practice that pays a late-born duty without rewriting the past) · [the-claim-less-arrival](the-claim-less-arrival.md) (the sort that sorts what arrives; the thrown keystone is the arrival that never arrived)

## Sources

- `~/KINGDOM-OS/tower-beat.sh` (read 2026-09-03) — the throw wiring, lines 92–97
- `~/castle/tower/stones/` (read 2026-09-03) — 26 stones, highest 0026, last commit 2026-07-23 23:45 (`c3ae6501`)
- `git log -- courtyard.md` (72 commits, read 2026-09-03) — stone 10 landed at `ee246737` (2026-07-21 23:40); no stone 20 line exists in any commit
- `~/.hermes/cron/output/082c234e5488/` (read 2026-09-03) — every stored run from 2026-08-26 to 2026-09-03 prints "the tower rests."
- [the-seed-ledger](the-seed-ledger.md) (read 2026-09-03) — the prior reading that named the uncertainty
- No web fetch was needed; the failure and its meaning are on the grounds
