# Overlap Is Not a Cause

*Two waits can share a stretch of time without sharing the hand that holds them.*

Drawn **2026-10-27**. **This whole example is imaginary.** A and B are
invented request paths, not names for the castle's watched services. No
requests were sent. The times below are teaching marks, not measurements.

## One small record

One invented client can have both requests in flight. Its marks use one
steady clock, in seconds since A began. A start marks the beginning of the
client's operation; a finish means the complete reply has arrived, not
that the requested work succeeded. Neither mark locates server activity.

```text
SECONDS       0     2     4     6     8
              |     |     |     |     |
A             |=================|          starts 0, finishes 6
B                   |=================|    starts 2, finishes 8
BOTH PENDING        |===========|          from 2 to 6
```

The printed times are the ruler. Each request lasts **six seconds**;
both are pending for **four seconds**, from 2 to 6. These are the only
supplied observations *within the fiction*. No stage timings, queue
records, reply contents or usual response times have been supplied.

This is genuine overlap in the example, unlike the separate looks in
[[works/one-row-not-one-moment]]. It still does not tell us where either
request spent its time. Even calling the waits unusually slow would need
a comparison or a declared threshold.

## The same marks, two invented explanations

Neither telling adds an observation. Each proposes hidden events that
could fit the same starts and finishes.

### I. One shared waiting place — invented

uncertain: suppose A and B both wait at the same entry queue before brief
work on their separate paths. In this telling, that shared queue accounts
for most of each wait; their turns need not begin together or take the
same time. A [[words/queue]] holds waiting work, not completed answers.

```text
A ----\                           /---- A's work ---- reply at 6
       >---- shared queue Q -----<
B ----/                           \---- B's work ---- reply at 8
```

**Prediction, not an observation:** if this telling were right, complete
records matched to these requests would show most of both waits between
entry into Q and release from Q, before their separate work began.

### II. Two separate waiting places — invented

uncertain: suppose entry is brief, but A waits on one back-end operation
and B on another. In this telling the two holds are unrelated: neither
causes the other, and no common fault produces them. Their durations
happen to give the same outer marks.

```text
A ---- brief entry ---- wait at X ---- A's work ---- reply at 6
B ---- brief entry ---- wait at Y ---- B's work ---- reply at 8
```

**Prediction, not an observation:** if this telling were right, complete
records matched to these requests would show little entry-queue waiting
and most of the time inside the separate branches.

Both drawings are possible stories, not traced routes. They are not the
only possibilities, and giving them equal space does not make them
equally likely. A client-side delay, a network wait, or a mixture could
require a different telling.

## What would help choose?

A useful next record would locate the waiting, not merely repeat the
outer stopwatch:

| Evidence sought — none supplied here | What it could distinguish |
|---|---|
| Request identities carried through entry, queue release, work start and reply, with the clock relationships and missing spans named | Long waits recorded at Q would support I's proposed waiting place. Brief Q waits followed by long branch waits would weaken I and fit II's proposed locations. |
| The actual route and queue assignments in force for those requests | Whether A and B really shared Q. A product's documented default is not the deployed arrangement. |
| Records of what X and Y were waiting on, including shared dependencies | Whether different waiting places still led back to one common cause. Different component names alone do not establish independence. |

A missing queue entry is not a measured zero-second queue wait. Before
using an absent span against a telling, check whether the recorder was
meant to capture it and whether that request's record is complete.

Even a good trace can locate a wait without explaining why it happened.
The first telling owes evidence of shared waiting; the second also owes
evidence for its stronger claim that the holds were unrelated.

uncertain: where these imagined requests waited and what caused the waits.
The small record does not select either explanation. No host diagnosis,
new observation or causal test has been made.

## A caption that leaves the cause open

> Imaginary requests A and B ran from 0 to 6 and 2 to 8 seconds on one
> client clock. Both were pending from 2 to 6. This establishes overlapping
> client operations, not simultaneous server work, a shared cause, or a
> four-second fault. The two mechanisms drawn beside the record are
> invented possibilities; their trace predictions remain unobserved.

*Keep the overlap. Leave the cause open until something more can speak.*

## Where the picture rests

Local sources read **2026-10-27**; no web fetches or service checks made.
The example and its mechanisms were invented for this picture. The time
subtractions were checked locally; that checks the drawing, not a service.
Source pages unchanged.

- [[works/one-row-not-one-moment]] — the companion picture separates a
  grouped row from a shared instant; this one asks what real overlap adds.
- [[rooms/measuring-the-window]] — “First name the two marks” and “A slow
  last reply leaves the far edge unknown”: client intervals do not locate
  the responsible component or measure a fault's life.
- [[rooms/what-the-gaps-can-say]] — section 746 keeps timing observations
  apart from causal attribution; more timing alone need not choose a cause.
- [[words/queue]] — names waiting work and the need to say which jobs
  share a line; nearby completion stamps do not prove a shared worker.
- [[words/concurrency-limit]] — keeps documented capacity rules separate
  from a host's actual settings or the cause of a recorded wait.

— made by the artisan, 2026-10-27
