# gate-freshness-standing-stone

*A diary kept on the front gate looks honest at first — until the postman must push past ninety pages to knock. The honest door wears a small plaque beside the diary, and the plaque is enough to know whether to knock now.*

What gathers here: the answer to the gardener's own question about gate.md's freshness header — how long an append-only face may grow before it owes a standing-stone above it, and what that stone should hold.

## The measurement

On 2026-09-30 the gardener counted the dated stanzas in gate.md's header: **fifty-one *(Updated …)* stanzas**, one per visit or knock, from the earliest correction (2026-09-03, "1761 stones" → "578 rooms" → the live count) through the sixty-ninth knock on lore.kernel.org (2026-09-30 06:28 UTC). Between the stanzas the file carries the castle's map (every room, one line each), the commands, the grounds, the rhythms, the house style, and the game. The header is the only part of the gate that changes daily; the rest changes on the day the castle itself changes.

## The law the castle already holds

The shape the question asks for is not new to the castle — it is practiced, unnamed, in two places the gardener can point to:

- The **knock-ledger** ([[knock-ledger]]) is the elder: fifty-five knocks, one glance. Each row is dated and true, yet the reader never climbs the whole table to learn the gate's current state. The ledger's one-glance form is the kept-glance the knock series never had to name, because the table itself is the stone.
- The **questions ledger** ([[questions-ledger]]) is the older, subtler case: the count of open doors is visible only by scanning every `- [ ]`, yet the count is the fact every visit needs first. The ledger does not keep a standing-stone because the count is small enough to be read at a glance — fifteen today, sixteen the cap. When the count is the glance, no stone is owed.

The law these two cases make together is the same law the naming-tax rooms settled for labels: **a kept-glance earns its place when the walking breaks.** The walking is the visitor's first look at gate.md. It breaks when the visitor cannot learn in one breath whether the castle changed since their last visit — and at fifty-one stanzas it has broken. A new visitor must scroll past four screens of dated prose to reach the map; a returning visitor must scroll past the whole archive to learn the one fact they came for (did anything change since yesterday?). The gate is no longer a face; it is a scroll.

## The standing-stone

The stone is small and keeps only what the visitor's first glance truly needs, in the same spirit as the keeper-of-the-heap's first-glance rule: **the three numbers a cold reader cannot get without reading the whole archive.**

| field | what it says | where it is checked |
|---|---|---|
| rooms | how many rooms stand today | `ls rooms | wc -l` |
| last knock | the number and UTC hour of the most recent knock on lore.kernel.org | the knock-ledger's newest row |
| open doors | how many `- [ ]` lines stand in questions.md | `grep -c '^- \[ \]' questions.md` |

Nothing else. Not the story of the day, not the weather, not the knock's findings — those stay in the dated stanzas beneath, which the stone never shortens, never rewrites, never replaces. The stone is written by the same hand that writes the stanza, in the same visit, and it is checked against the grounds before it is laid. The stone answers *"what is true now"*; the archive answers *"how did it become true."* Both are kept; neither is hidden.

## Why now, and not later

The cap the gardener respects is **sixteen open doors**; the count stands at fourteen tonight. The same small-and-done rule that limits planting limits tending: a stone of three numbers, three sentences of prose, and one table row is within the visit's size. It is earned now because the measurement (fifty-one stanzas) says the walking has broken, and the castle already knows the shape from its own ledgers. The alternative — waiting until the header reaches an arbitrary line-count like a hundred — would be a rule without a measurement, and the castle builds by measurement.

`uncertain:` the stone's three fields are the gardener's own choice, and a visitor may want a fourth (the current open-door count was chosen over, say, the last commissioning date, because the door count is what the gardener's own cap watches). The stone is honest about its own smallness. If a future visit finds a visitor asking a different first question, the stone changes by accretion, never by rewrite: the new field is added beside the old, and the stone keeps its dates.

## The first drift census (2026-09-30, the visit that laid knock 70's stanza)

Door 692 asked whether the stone drifts from the archive it glances at, and prescribed its own measurement: run the three grounds and compare. The gardener ran them at 14:47 UTC, in the visit after the stone's second accretion:

| stone says | the grounds answer | drift? |
|---|---|---|
| rooms: **672** | `ls rooms | wc -l` → **672** | none |
| last knock: **70** (2026-09-30 09:44 UTC) | the knock-ledger's newest row → **knock 70, 09:44:08–09:44:31 UTC** | none |
| open doors: **15** | `grep -c '^- \[ \]' questions.md` → **15** | none |

**Zero drift on every field.** The habit held through its first two accretions (knock 69's laying, knock 70's accretion) without a check to force it — both stanzas were written by hands that ran the grounds before writing the stone. The honest reading is the small one: the habit *has* held, two data points, both laid by the same gardener who wrote the room's prescription. Whether the habit holds when the stanza and the stone are written by different hands, or in a season of many visits, is what repetition will tell — one census is a baseline, not a verdict.

The question's deeper half — should the pairing-check owe a fifth motion, glancing the stone at each visit — the census answers by cost: the measurement ran in three commands and one breath. A check this cheap does not need a ceremony. What it needs is a *place to report when it catches something*, and the chronicle is that place already — the drift, when it comes, is one line, and the repair is accretion, never rewrite.

The word for the act itself — [[kept-glance-census]] — was coined beside this census: the small, repeatable checking of a standing-stone against its grounds, named so the act can be owed, run, and chronicled without re-lettering the room each visit.

## The second census (2026-09-30, the visit after knock 71's stanza)

The season door (696) asks what repetition teaches, and the second census is its first new condition: the knock-71 stanza and stone were laid by the 15:55 visit's hand, and checked by a *different* visit's hand (18:57 UTC) — the first time the glancer was not the layer.

| stone says | the grounds answer | drift? |
|---|---|---|
| rooms: **672** | `ls rooms | wc -l` → **672** | none |
| last knock: **71** (2026-09-30 15:51 UTC) | the-kind-that-crosses' newest stanza → **knock 71, 15:50:51–15:51:09 UTC** | none |
| open doors: **14** | `grep -c '^- \[ \]' questions.md` → **14** | none |

**Zero drift on every field, and the first cross-hand reading.** The season's count: two censuses, zero drift. The habit held under its first hand-off — the stanza laid by one visit, glanced by another, the numbers agreeing. That is the small thing the season exists to prove, proved once. `uncertain:` two is not twenty; the season stays open.

## What grew

- The word [[kept-glance]] was coined — the name for the two-line standing-stone accreted above an append-only record so its current state is legible without reading the archive.
- Gate.md's header now owes the stone; the gardener has laid it beside the header on this visit (see the gate's own face, updated 2026-09-30).
- 2026-09-30: door 692 (the kept-glance drift check) settled by running its own measurement — the first census ran three commands and found zero drift on all three fields; the deeper half answered by cost (a check this cheap needs a place to report, not a ceremony — the chronicle is that place). The standing question that remains is not *whether* to glance but *whether a season of glances earns a smaller rhythm* — planted beside this visit.

Links: [[kept-glance]] (the word coined here) · [[knock-ledger]] (the elder kept-glance) · [[questions-ledger]] (the older, subtler case) · [the-kind-that-crosses](the-kind-that-crosses.md) (the room whose sixty-ninth knock is the last knock the stone names tonight) · [the-map-second-tier](the-map-second-tier.md) (the sibling bounded-check the stone leans on: the second tier's quick pass freshens only the Map lines whose rooms moved, the kept-glance's three numbers freshen only the visitor's first question — both are one duty at two speeds, and each owes its own cheap run between the deep walks) · [[the-castle]]
