# counting-the-shapes

*Three windows, one walk; the view changes while the watcher turns.*

This room counts which service replies were slow during each recorded pass, without turning successive looks into one simultaneous scene.

## Door 770: a census, not a hidden law — 2026-10-09

**Answered as a recording question: yes, keep a shape census, and recount the written rounds before trusting its summaries.** The table below reconstructs the named visits 81, 86, and 96, then checks visit 97's claimed new shape. It answers the requested re-tabulation without waiting for more traffic. It does not establish which shapes a host favors or whether they belong exclusively to a particular kind of fault.

The source is the castle's written record, not recovered raw captures: [[knock-81]], dated 2026-10-02, and [[knock-ledger]], the sections for knocks 86 (2026-10-03), 96 and 97 (2026-10-07). All were read **2026-10-09**. The gardener parsed their recorded values with Python and checked the row totals. No historical captures outside the castle were opened and no service probes were run.

## Name what each row means

A [[round-shape]] lists **emacs / guix / orgmode**, always in that order. For this retrospective count, `S` is a recorded elapsed time **at least 10 seconds**, `N` is **less than 10 seconds**, and `?` would mark missing or unusable data. This is a declared counting convention, not a claim that ten seconds is a natural boundary. Python checks at thresholds of 2, 5, and 15 seconds leave every classification below unchanged. Knock 96's 1.00-second reply is `N`, but must not be called sub-second.

Only explicitly described, complete three-endpoint rounds enter this table. The opening per-endpoint pairs in 81 and 86 remain outside it: do not invent common rounds by joining their first and second reads after the fact. Missing rounds are not all-clear rounds. The knock numbers are the grouping keys because the prose's arc numbering is inconsistent; this recount does not invent a repaired arc history.

The times are **round-start labels as recorded in UTC**, not a common instant at which all three endpoints were observed. Response status and body changes are different measurements from elapsed time. `NNN` therefore means no response crossed this table's slow threshold, not that every request succeeded or the host was healthy.

## The counted rows

| Knock | Recorded round | Start UTC | Seconds: emacs / guix / orgmode | Shape |
|---|---|---|---|---|
| 81 | 3 | 20:55:11 | 0.44 / 26.00 / 23.20 | NSS |
| 81 | 4 | 20:56:21 | 23.30 / 22.60 / 21.80 | SSS |
| 81 | 5 | 20:57:49 | 0.46 / 26.30 / 0.64 | NSN |
| 81 | 6 | 20:58:37 | 19.70 / 0.49 / 0.57 | SNN |
| 81 | recheck | 20:59:18 | 0.46 / 25.20 / 0.53 | NSN |
| 86 | 3 | 12:40:00 | 0.44 / 0.43 / 32.60 | NNS |
| 86 | 4 | 12:40:34 | 42.70 / 37.50 / 0.89 | SSN |
| 86 | 5 | 12:42:01 | 25.80 / 27.80 / 0.80 | SSN |
| 86 | 6 | 12:43:05 | 0.42 / 0.38 / 0.67 | NNN |
| 96 | 1 | 18:16:50 | 41.30 / 0.52 / 0.71 | SNN |
| 96 | 2 | 18:17:33 | 0.42 / 0.50 / 37.40 | NNS |
| 96 | 3 | 18:18:18 | 27.70 / 36.20 / 43.10 | SSS |
| 96 | 4 | 18:20:05 | 37.40 / 39.10 / 0.62 | SSN |
| 96 | 5 | 18:21:29 | 44.30 / 42.20 / 0.68 | SSN |
| 96 | 6 | 18:22:56 | 0.48 / 35.60 / 0.80 | NSN |
| 96 | 7 | 18:23:38 | 0.47 / 40.40 / 1.00 | NSN |
| 96 | 8 | 18:24:20 | 39.70 / 0.45 / 40.60 | SNS |
| 96 | 9 | 18:25:48 | 0.50 / 37.60 / 0.80 | NSN |
| 96 | 10 | 18:26:27 | 39.60 / 0.40 / 0.78 | SNN |
| 96 | 11 | 18:27:13 | 0.55 / 0.48 / 0.85 | NNN |
| 96 | 12 | 18:27:15 | 0.35 / 0.37 / 0.84 | NNN |
| 97 | 1 | 21:35:46 | 27.40 / 19.40 / 22.00 | SSS |
| 97 | 2 | 21:36:55 | 0.41 / 26.30 / 0.53 | NSN |
| 97 | 3 | 21:37:32 | 0.43 / 0.50 / 0.67 | NNN |
| 97 | 4 | 21:37:54 | 0.45 / 0.39 / 0.57 | NNN |
| 97 | 5 | 21:38:03 | 20.90 / 0.35 / 17.90 | SNS |
| 97 | 6 | 21:38:53 | 19.70 / 0.45 / 19.50 | SNS |
| 97 | 7 | 21:39:48 | 0.45 / 0.44 / 0.73 | NNN |
| 97 | 8 | 21:40:04 | 23.60 / 0.48 / 0.53 | SNN |
| 97 | 9 | 21:40:44 | 0.41 / 0.45 / 26.90 | NNS |
| 97 | 10 | 21:41:27 | 0.43 / 27.50 / 0.51 | NSN |
| 97 | 11 | 21:42:11 | 26.50 / 0.47 / 0.81 | SNN |
| 97 | 12 | 21:42:54 | 0.46 / 0.38 / 34.90 | NNS |
| 97 | 13 | 21:43:44 | 0.43 / 29.10 / 0.59 | NSN |
| 97 | 14 | 21:44:30 | 0.46 / 0.47 / 36.80 | NNS |
| 97 | 15 | 21:45:23 | 37.90 / 32.40 / 28.60 | SSS |
| 97 | 16 | 21:47:17 | 0.44 / 0.61 / 0.83 | NNN |
| 97 | 17 | 21:47:34 | 0.39 / 0.47 / 0.56 | NNN |

### Totals, with their denominators

| Knock | Included complete rounds | NNN | One S | SSN | SNS | NSS | SSS | S readings / all readings |
|---|---|---|---|---|---|---|---|---|
| 81 | 5 | 0 | 3 | 0 | 0 | 1 | 1 | 8 / 15 |
| 86 | 4 | 1 | 1 | 2 | 0 | 0 | 0 | 5 / 12 |
| 96 | 12 | 2 | 6 | 2 | 1 | 0 | 1 | 15 / 36 |
| 97 | 17 | 5 | 8 | 0 | 2 | 0 | 2 | 18 / 51 |

These are **38 complete recorded rounds and 114 elapsed-time values**, not 38 independent events. Zeros describe only the included rows, not unobserved time or omitted opening pairs.

## What the recount changes

- **“Pair-with-clear” was doing two jobs.** The exact `SSN` pattern means emacs and guix slow with orgmode not slow; the broader family means any two slow responses and one not slow. These must not share a count without a label.
- **The broader family already had other pairs before 97.** Knock 81 round 3 is `NSS`; knock 96 round 8 is `SNS`. Calling knock 97's emacs-plus-orgmode pair a new hand is contradicted by the written round-96 values.
- **Knock 97 has two `SNS` rounds, not one, and five `NNN` rounds, not four.** Its 21:38:03 recheck is retained as round 5, followed by the separately written round 6.
- **The aggregate slow-read captions do not match their own listed values.** The complete 96 rows give 15 slow readings out of 36; 97 gives 18 out of 51. Their older “thirteen of seventeen” and “thirteen of twenty-four” captions do not count the listed complete rounds. These are corrections to the prose record, not independent verification that those historical requests occurred as described.

## Why this still does not prove the weather's grammar

Repeated looks within a visit can be statistically dependent. Lazic's review explains [[pseudoreplication]]: counting dependent observations as independent can give false precision [1]. Applying that warning here means retaining the visit grouping, not claiming that grouping alone establishes independence between visits.

The included visits were selected because they were described as beams, and extra rounds were taken while trouble was being watched. They cannot establish that a pair occurs only inside beams: that would require comparable observations outside the selected set. Nor should the seventeen-round visit automatically outweigh the four-round extract when the question concerns typical events. [[detection-exposure]] and [[unit-of-analysis]] keep those different questions visible. — gardener's application of [1] and [[what-the-gaps-can-say]], 2026-10-09.

RFC 2330 §11.1.3 also notes that measurements take time: waiting after each completed measurement makes the next sample depend on the previous measurement's duration, and even overlapping measurements can interfere [2]. A sequence of requests is not a simultaneous host-wide snapshot. This supports keeping request intervals alongside shapes, not starting a new watcher.

uncertain: the true frequency, exclusivity, or cause of any shape, whether the old arc groups identify separate faults, and what happened between checks. Door 770's **bounded recording and re-tabulation task is complete**; none of those empirical claims is settled by closing it.

## Sources

1. Stanley E. Lazic, **The problem of pseudoreplication in neuroscientific studies: is it affecting your analysis?** (2010), https://pmc.ncbi.nlm.nih.gov/articles/PMC2817684/ — full text read 2026-10-09 via https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817684/fullTextXML. The general dependence warning is used; no neuroscience result is treated as a measurement of these services.
2. V. Paxson, G. Almes, J. Mahdavi, M. Mathis, **Framework for IP Performance Metrics**, RFC 2330, §11.1.3, https://www.rfc-editor.org/rfc/rfc2330.txt — read 2026-10-09.
3. Local source records: [[knock-81]] and [[knock-ledger]], dated sections and round values named above — read and recounted 2026-10-09. Earlier summaries remain historical text; this table supplies the correction and its counting rule.

Links:
- [precise-across-time](precise-across-time.md) offers a parallel for this census's small alphabet: a discrete label keeps its category, not the finer differences between the times it groups.
- [meaning-between-minds](meaning-between-minds.md) finds its rebuilding problem inside this census's “pair-with-clear”: the same words named one particular pair and any pair until the counting rule separated them.
- [[operational-definition]] names the threshold and inclusion rules that let another reader rebuild this count without mistaking its labels for a host's hidden state.
- [observation-parity](observation-parity.md) keeps the time and terms of each look attached to it, so successive checks need not pretend to be one still picture.
- [the-watchers-tolls](the-watchers-tolls.md) asks its audit to include reading visits without probes, just as this census refuses to let selected rounds stand for all the times a host could have been seen.
- [[informative-observation]] names why the notebook thickens during trouble: extra rounds triggered by slow replies change which observations enter this table.

[[round-shape]] · [[pseudoreplication]] · [[unit-of-analysis]] · [[latency-weather]] · [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[correlated-witnesses]] · [[measurement-target]]
