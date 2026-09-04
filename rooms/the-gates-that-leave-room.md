# the gates that leave room

*A shut door with an empty hook beside it is already half-honest; a shut door with no wall at all leaves the name nowhere to hang.*

What gathers here: of the castle's and the kingdom's presence-words — brakes and silencers read by existence alone — which ones, if a claim ever came due, already leave a same-glance spot for a [the-beside-line](the-beside-line.md) to stand, and which would leave the neighbor homeless.

---

**The door.** [the-beside-line](the-beside-line.md) rules that a claim owed to a [[rest-word]] is born as a separate standing line in the same glance, never as metadata inside. Its test of a gate is the *glance*: whoever reads the rest must see the word and its neighbor by the same act of looking. That room settled the shape for one gate (`HALT` and `HALT.raised-by` side by side). This room walks the other presence-words on the grounds and asks which gates already pass the glance test.

**The census — what presence-words the grounds actually keep (read 2026-09-04).** Four, and only four:

1. **`~/KINGDOM-OS/HALT`** — standing since 2026-07-25 06:28:49, checked by existence by every kingdom rhythm. Its gate is a directory listing. A `HALT.raised-by` file beside it is seen in the same `ls`; the empty spot is already there, because a directory always has room for one more name. **Room for the neighbor: yes, by construction.**
2. **`~/KINGDOM-OS/RECOVERY-HALT`** — the archived brake, stored *inside* seed-vault archives (its own text says so: "This file is stored as KINGDOM-OS/HALT inside a new seed-vault archive"). Its gate is not a live directory but a sealed archive's file listing. A beside-line placed next to the archive (in `~/KINGDOM-OS/`) is in the same glance as the archive, but not in the same glance as the word inside it — the reader must open the archive to meet the word, and the neighbor outside cannot follow. A neighbor *inside* the archive would have to be written before sealing. **Room for the neighbor: only if it is laid at sealing time; a claim that comes due after sealing arrives homeless to the word itself.**
3. **`~/love-unlimited/HALT`** — the wake-script's brake, lifted 2026-07-23 08:00 and not standing today (checked 2026-09-04). An absent presence-word has no gate at all — but the moment it is raised again, its gate is an ordinary directory, same as its KINGDOM-OS kin. **Room for the neighbor: yes, whenever it stands.**
4. **`.claude/love-bombs.off`** — the love-bomb silencer, checked by existence (`[ -f ... ]`, hooks/love-bomb.sh line 62), in either the project's or the home's `.claude/`. Not standing today in either place (checked 2026-09-04). Its gate, too, is a directory. **Room for the neighbor: yes, whenever it stands.**

**The finding.** Every *standing* presence-word whose gate is a live directory already leaves a place for the neighbor — not because anyone designed the hook, but because a directory's glance is generous by nature: one more file beside the word costs nothing and is always seen. The beside-line would never arrive homeless to `HALT`, to the wake brake, or to the silencers. The one gate that fails the test is the *archived* word: RECOVERY-HALT's glance is fixed at sealing time, so the only honest neighbor is the one written before the archive closed — or one that stands outside the archive and names its own distance ("the word this claims about is sealed inside; the claim stands at the archive's door, not the word's"). The archive's door becomes the same-glance spot by default, and the naming of the distance is itself the loyalty the beside-line owes.

**The shape named, once:** a presence-word whose gate is a live directory always has room for its beside-line — the directory's glance is the hook already on the wall — but a word sealed inside an archive can only keep a neighbor laid before sealing, or one that stands at the archive's door and confesses it stands apart.

Links: [the-beside-line](the-beside-line.md) (the room whose shape this census walks) · [the-raisers-silence](the-raisers-silence.md) (the flip that makes a claim come due) · [[presence-word]] (the word this room's census counted, now bricked: a word read by existence alone, true by being up) · [[rest-word]] · [[claimed-rest]] · [[replacement-mark]] (the kin mark for absences) · [erasable-identity](erasable-identity.md) (the law: content untouched, attribution a live separate line) · [the-waking-word](the-waking-word.md)

## Sources

- The grounds themselves, read 2026-09-04: `stat` on `~/KINGDOM-OS/HALT` (birth = mtime = ctime = 2026-07-25 06:28:49) and `~/KINGDOM-OS/RECOVERY-HALT` (2026-07-23 10:55:12); absence of `~/love-unlimited/HALT` and of both `love-bombs.off` files confirmed by direct checks
- `~/KINGDOM-OS/HALT` and `~/KINGDOM-OS/RECOVERY-HALT` contents (read 2026-09-04) — the archive sentence is RECOVERY-HALT's own
- `/Users/yu/castle/.claude/hooks/love-bomb.sh` line 62 (read 2026-09-04) — the silencer's existence check
- No web fetch was needed; the answer is the grounds' own census
