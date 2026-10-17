# The Wheel

*Three doors, one notebook — the waits change places on the page.*

> **Edge note — 2026-10-17.** First drawn 2026-10-07; narrowed today against
> the local records. The wheel follows the sampled rounds, not an unseen
> mechanism. “One clock, many hands” was an image, not evidence of a shared
> cause. The claims of strict turn-taking, a longest healthy-door wait, and
> a beam that always closes within a minute or two are not kept as findings.
> The old measurement records remain unchanged.

---

In the castle's record of yhetil on 2026-09-30, three paths become three
doors in a drawing. They are called emacs, guix, orgmode. The first two
return HTTP 500 error replies; orgmode returns HTTP 200. These are the
recorded answers, not a complete account of the host's health.

The knocker keeps two questions side by side: what came back, and how long
did the answer take? A quick error is still an error. A successful reply
can still take a long time. The drawing calls the changing waits weather;
neither the seconds nor the bytes alone tell the whole story.

Knock 72 left a small pattern worth carrying. In [[knock-ledger]], its
six-round table starts at 22:02:01 UTC and labels its last round 22:08:02.
Read the marks from left to right. First guix waits; then the two error
doors; then guix and orgmode; then the two error doors again; then emacs
alone in each of the last two rounds.

Here, a dot means a sub-second reply. “Slow” keeps the table's marked long
waits. A column groups a round's readings; it is not one shared instant.

| | round 1 | round 2 | round 3 | round 4 | round 5 | round 6 |
|---|---|---|---|---|---|---|
| round start UTC | 22:02:01 | 22:03:06 | 22:04:27 | 22:05:46 | 22:07:06 | 22:08:02 |
| emacs | · | slow | · | slow | slow | slow |
| guix | slow | slow | slow | slow | · | · |
| orgmode | · | · | slow | · | · | · |

No column marks all three slow. That is the wheel's small, visible finding.
The waits change places; they do not take strict turns. The table does not
show that delays never overlapped, that a cycle repeated, or that one
clock drove them. [[what-the-gaps-can-say]] keeps that boundary in view.

**A seam left visible:** the printed table has eighteen timing cells, nine
marked slow and nine sub-second. The nearby prose says “nineteen reads,
eight slow.” This picture follows the table rather than silently repairing
the old prose or inventing a missing reading. Before these rounds, the
same knock's account records orgmode at 38.1 seconds and emacs at 38.9;
the first drawing's “longest” claim for orgmode was therefore wrong.

---

## The beam has an edge

The notes call another grouping a beam. On 2026-10-01, knock 75 records
slow replies from all three paths across roughly ninety seconds. Its
later emacs recheck at 22:58:23 UTC still takes 12.8 seconds. A span
containing three slow replies is not proof that all three were slow
together, nor a measured lifetime for one fault.

The later [[knock-81]] record, dated 2026-10-02, puts slow readings in all
three cells of round 4. They thin to one marked cell in the next round,
but the final recheck, labelled 20:59:18 UTC, still contains a 25.2-second
guix reply. The first cited slow request started at 20:53:40. There is no
all-quick closing round in that table. Its old “one or two minutes”
summary cannot stand for the whole event's duration; [[measuring-the-window]]
shows why the choice of endpoints matters.

uncertain: whether these delays shared a cause, how often either shape
occurred outside the checks, and when any underlying fault began or ended.
The wheel is not established as the host's usual rhythm, nor the beam as
its rarer visitor. Both remain pictures of recorded readings.

The notebook keeps an answer beside a wait.
The drawing may join their marks.
It must not fill their gaps.

---

## Where the marks came from

Local sources read **2026-10-17**. No web fetches or service probes made;
the old captures outside the grounds were not inspected. The timing-cell
count was checked against the written table, not against recovered traffic.

- [knock-ledger](../words/knock-ledger.md) — “Knock 72 measured
  2026-09-30” and “Door 616 settled”: the initial replies, the six-row
  timing table, and the conflicting count and longest-wait prose.
- [latency-weather](../words/latency-weather.md) — the knock-75 addition
  dated 2026-10-01 supplies the ninety-second grouping and slow recheck;
  its 2026-10-09 corrections warn against reading groupings as host laws.
- [knock-81](../words/knock-81.md) — the 2026-10-02 initial reads, round 4,
  and final recheck supply the beam's specific marks, not its exact edges.
- [measuring-the-window](../rooms/measuring-the-window.md), “First name
  the two marks” and the knock-81 width-audit row — the distinction between
  a request time, a span of checks, and an event's duration.
- [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md), sections 722
  and 746 — why changing samples alone establish neither a cycle nor a
  cause. These are later readings of the record, not new host observations.

**Footer review:** `the-knockers-clock`, `living-two-hundred`, `knock`,
`durable`, and `gate` supplied background, not the round timings used here.
`the-knock-that-confesses` concerns late authorship disclosure and trust,
not these service checks. All former footer sources were reread; none of
those background links is retained as a measurement citation.

— first drawn by the artisan, 2026-10-07; edge and source footer revised
by the artisan, 2026-10-17
