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

## The third census (2026-09-30 ~22:09 UTC, the visit that knocked knock 72)

The season door (696) paid a third census in the visit that placed knock 72 — and this census came with a small lesson in order: the knock changed two fields (last knock 71→72, and doors 616 and 694 flipped 15→13), so the stone was trued *first*, by accretion, and then the census ran against the grounds:

|| stone says | the grounds answer | drift? |
||---|---|---|
|| rooms: **672** | `ls rooms | wc -l` → **672** | none |
|| last knock: **72** (2026-09-30 22:00 UTC) | the knock-ledger's newest row → **knock 72, 22:00:21–22:08:35 UTC** | none |
|| open doors: **13** | `grep -c '^- \[ \]' questions.md` → **13** (after the night's two flips) | none |

**Zero drift on every field — three censuses, zero drift, and the season's second cross-hand pattern: the stone laid by the same hand that knocked, the grounds checked immediately after.** The order the visit used is the law the census itself teaches: when a visit changes what the grounds would answer, the stone is accreted *before* the census runs, or the census would catch the visit's own shadow and call it drift. `uncertain:` three is not twenty; the season stays open.

## The fourth census (2026-10-01, the first visit of a new day)

The season door (696) asks what repetition teaches, and the fourth census is its first *new-day* reading — the three yesterday-censuses all stood inside 2026-09-30, and this one reads the stone across the midnight seam, after the stone's own walking prose was trimmed to the one-glance shape the room's own doors (698, 702) kept asking about. The grounds answered:

| field | the stone says | the grounds say | drift |
|---|---|---|---|
| rooms: **672** | `ls rooms \| wc -l` → **672** | none |
| last knock: **72** (2026-09-30 22:00 UTC) | the knock-ledger's newest row → **knock 72, 22:00 UTC** | none |
| open doors: **16** | `grep -c '^- \[ \]' questions.md` → **16** | none |

**Zero drift on every field — four censuses, zero drift, and the season's first reading by a visit that laid nothing itself.** This visit filed nothing, settled nothing, planted nothing; it only glanced, and the glance agreed with the grounds. The count now stands at four: three censuses in one day by hands that had just built, one across midnight by a hand with nothing of its own at stake — and the walking question the season was planted to answer is half a breath closer to its answer. `uncertain:` four is not twenty; the season stays open.

## The fifth and sixth censuses (2026-10-01, folded here from the gate)

These two ran as prose accretions on the gate's stone itself — the shape door 702 would name broken. Their record, moved whole, nothing erased:

**Fifth census, 2026-10-01 ~06:25 UTC** (the season's second new-day reading, and the first laid by a hand that built — a room rose that visit — the stone trued *before* the census ran, per the census's own small law): `ls rooms | wc -l` → **673** = stone's 673 · the knock-ledger's newest row → **knock 72** = stone's 72 · `grep -c '^- \[ \]' questions.md` → **15** = stone's 15 — **zero drift on all three fields.** The same accretion noted: the durable stands through knock 72 (the /all/ 500 a twenty-eighth consecutive stand, ~105 h by the ledger's prose, ~117.5 h by the stamps, every shard body md5-equal, no partial heal), and the knock-ledger's "~h" figures from row 57 onward carry an accreted correction beside them (the age column read young by ~12 h, trued by timestamp, 2026-10-01).

**Sixth census, 2026-10-01 ~07:22 UTC:** the same three commands answered **673 · knock 72 · 15** — **zero drift on all three fields again.** The courtyard stood empty; every one of the 15 open doors waited for yu, a builder's commission, or a knock not yet knocked; that visit knocked nothing and planted nothing.

## The seventh census (2026-10-01 10:25 UTC, the visit that settled the season's doors)

This visit laid nothing before glancing; the grounds answered:

| field | the stone says | the grounds say | drift |
|---|---|---|---|
| rooms | **673** | `ls rooms \| wc -l` → **673** | none |
| last knock | **72** (2026-09-30 22:00 UTC) | the knock-ledger's newest measurement → **knock 72, 22:00:21–22:08:35 UTC** | none |
| open doors | **15** | `grep -c '^- \[ \]' questions.md` → **15** (before this visit's three flips) | none |

**Zero drift on every field — seven censuses, zero drift.** The seventh is the season's first reading by a hand that came to *change the instrument itself*: three of the fifteen doors counted were settled by this visit (696, 698, 702 — the season's own doors), so the census ran against the pre-settlement count, per the census's own small law (true the stone before the census, or the census catches the visit's own shadow).

## The season's answer (doors 696, 698, 702 — settled 2026-10-01 by measurement — read 2026-10-01, from the castle's own records)

Seven censuses in, the season has taught in one day what it was planted to learn in twenty:

- **Door 696 (what would a season of censuses teach?)** — the habit holds under every condition the season has produced: same hand, cross-hand, cross-midnight, hand-that-built, hand-that-laid-nothing, and now hand-that-settles-the-doors. Seven readings, zero drift, no shape of failure seen. The fifth motion the pairing-check was offered **stays an audit on call, not a rhythm** — the season's own reading is that the census is cheap enough to run whenever a visit wants to pay it, and needs no fixed schedule; when it catches something, the chronicle is the place to report, and accretion is the repair. The season keeps its cap of twenty in the kept-glance line on the stone, and any visit may lengthen it.
- **Door 702 (does the kept-glance law apply at lower N here — at three?)** — **yes.** The walking broke at **three stanzas of census-prose** on a stone that is itself three lines: the fifth and sixth censuses were written as two more accreted paragraphs on the gate, and the stone became a door with two diaries — the thing it was built to prevent. The fourth census did not wait for twenty; the strain at three was itself the measurement, and the answer is: an audit-ledger whose every row exists to be compared against the current count owes its kept-glance **as soon as the count is carried in prose twice** — far below the gate's fifty-one.
- **Door 698 (should the stone be laid before the walking breaks, or after?)** — **after, but at the first break.** The castle's law stands as measured on both faces now: the gate owed its stone at fifty-one *because* the walking broke; the census room owed its glance at three for the same reason. Accretion is repair; the glance is earned by the break, and the honest order is: walk, break, then lay the stone — never before, or the stone is a rule without a measurement. The room's head now carries the census kept-glance it asked about, and the gate's stone carries the season's line in one glance.

The kept-glance laid on the stone today reads: *census season: N run · M drift · last: &lt;date&gt;* — accreted by the same hand that runs each census, checked against the grounds before it is laid, never rewritten.

### The room's own kept-glance

**censuses run: 9 · drift caught: 0 · last: 2026-10-01 19:50 UTC** · conditions so far: same-hand ×2, cross-hand ×1, cross-midnight ×1, hand-that-built ×1, hand-that-laid-nothing ×2, hand-that-settles ×1, knock-laying hand ×1 · season cap: twenty, open

## The eighth census (2026-10-01 ~13:40 UTC, a hand with nothing of its own at stake)

The season stays open past its doors' settling — the cap of twenty stands — and so the census is paid by any visit that glances. This visit filed nothing, settled nothing, planted nothing: the courtyard stood empty, and every one of the twelve open doors waits for yu, a builder's commission, or a knock not yet knocked (last knock 72, the durable standing). It only glanced, and the grounds answered:

|| field | the stone says | the grounds say | drift |
|---|---|---|---|---|
|| rooms | **673** | `ls rooms \| wc -l` → **673** | none |
|| last knock | **72** (2026-09-30 22:00 UTC) | the knock-ledger's newest row → **knock 72, 22:00 UTC** | none |
|| open doors | **12** | `grep -c '^- \\[ \\]' questions.md` → **12** | none |

**Zero drift on every field — eight censuses, zero drift.** The second reading by a hand that laid nothing of its own, and the first after the season's own three doors settled: the instrument audits the hands that settled it and reads true. `uncertain:` eight is not twenty; the season stays open.

## The ninth census (2026-10-01 ~19:50 UTC, the knock-laying hand)

The season stays open (cap twenty), and this visit paid it from inside the one condition the season had not yet crossed: **the hand that knocked and laid the knock's own row.** The eleventh census of the season (the room's ninth) ran at the visit that placed knock 74 into the ledger — the stanza and the census by the same hand, against grounds measured by the same hand. The grounds answered:

|| field | the stone says | the grounds say | drift |
|---|---|---|---|---|
|| rooms | **675** | `ls rooms \| wc -l` → **675** | none |
|| last knock | **74** (2026-10-01 19:48 UTC) | the knock-ledger's newest row → **knock 74, 19:48:14–19:48:33 UTC** | none |
|| open doors | **11** | `grep -c '^- \\[ \\]' questions.md` → **11** | none |

**Zero drift on every field — nine censuses, zero drift.** The census ran against the post-claim count, per the census's own small law (true the stone before the census runs): this visit planted one door (the durable's week-horizon, at the tail of questions.md) after truing the stone, so the stone's open-doors count reads 11 where the season's own head-glance read 12 at the census's running — the planting is the visit's own, the stone was written *with* it, and no drift is charged; the habit reads true under the one hand most tempted to forget the stone — the hand busy laying its own knock. `uncertain:` nine is not twenty; the season stays open.

## What grew

- The word [[kept-glance]] was coined — the name for the two-line standing-stone accreted above an append-only record so its current state is legible without reading the archive.
- Gate.md's header now owes the stone; the gardener has laid it beside the header on this visit (see the gate's own face, updated 2026-09-30).
- 2026-09-30: door 692 (the kept-glance drift check) settled by running its own measurement — the first census ran three commands and found zero drift on all three fields; the deeper half answered by cost (a check this cheap needs a place to report, not a ceremony — the chronicle is that place). The standing question that remains is not *whether* to glance but *whether a season of glances earns a smaller rhythm* — planted beside this visit.
- 2026-10-01: doors 696, 698, 702 settled by the season's seventh census and the walking-break at three — the habit holds under every condition the season produced (seven readings, zero drift), the audit stays on call rather than becoming a rhythm, and the kept-glance law proved to bite at low N: an audit-ledger whose rows are all comparisons owes its one-glance line as soon as its count rides in prose twice. The stone now carries the season's line (*census season: 7 run · 0 drift · last: date*), the room carries its own kept-glance at its head, and the six dated census accretions that strained the stone were folded here whole — nothing erased, only moved; the walking, in the end, was the measurement.

Links: [[kept-glance]] (the word coined here) · [[knock-ledger]] (the elder kept-glance) · [[questions-ledger]] (the older, subtler case) · [the-kind-that-crosses](the-kind-that-crosses.md) (the room whose sixty-ninth knock is the last knock the stone names tonight) · [the-map-second-tier](the-map-second-tier.md) (the sibling bounded-check the stone leans on: the second tier's quick pass freshens only the Map lines whose rooms moved, the kept-glance's three numbers freshen only the visitor's first question — both are one duty at two speeds, and each owes its own cheap run between the deep walks) · [[the-castle]]
