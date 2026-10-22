# One Row Is Not One Moment

*A notebook can fold a walk into a line. Time does not fold with it.*

Drawn 2026-10-22. **This whole example is imaginary.** A, B and C are
invented paths, not names for the castle's watched services. No requests
were sent; none of these numbers is a new measurement.

## Unfold the row

One client sends one request at a time, waiting for the complete reply
before moving on. All marks use the same invented clock: seconds since
this round began. “Finishes” means the complete reply has arrived, not
that the reply reports success.

For this picture only, call a wait **slow if it exceeds three seconds**.
That is a chosen label, not a general rule for services.

```text
SECONDS   ONE ROUND, UNFOLDED                  THE SAME ROUND, FOLDED

   0      A starts                            round | A   | B   | C
   |      waiting for A                       ------+-----+-----+----
   4      A finishes                          R1    | 4 s | 2 s | 4 s
   |
   |      gap: no request from this client
   |
   5      B starts
   |      waiting for B
   7      B finishes
   |
   |      gap: no request from this client
   |
   8      C starts
   |      waiting for C
  12      C finishes
```

The drawing is not to scale; the printed times are the ruler. The gaps
are **4 to 5** and **7 to 8**: one second each. They are pauses in this
client's looking, not evidence that the services rested.

Read the small row: **slow, below the threshold, slow**.
Read the long strip: **first, then, then**.

Both readings fit. Neither may erase the other.

## What the fold keeps — and drops

The row keeps each path's elapsed wait. By itself it drops the request
intervals and the pauses. A row label is a grouping, not a shared instant;
even adding “round starts at 0” would not place every request at 0.

Here the request intervals do not overlap. B's shorter wait happens
**between** A's and C's longer waits, not during either one. It therefore
cannot show that B would have answered quickly while A or C was waiting.
The word [[words/sequential-observation]] names this limit.

Nor do the separated requests prove that the paths' underlying problems
were separate. **No overlapping requests** and **no overlapping trouble**
are different claims.

uncertain: in this invented example, what the unqueried paths would have
done, whether the waits shared a cause, and whether any continuous fault
existed. Those details have not been supplied. Equal waits do not supply
them; neither does putting the waits in neighboring cells.

The first start to the last finish spans **twelve seconds**. The waits
account for ten seconds and the pauses for two. That is this client's
collection span, not a twelve-second fault. [[rooms/measuring-the-window]]
keeps the request, the collection and the unseen event apart.

## A caption that keeps the edges

> Imaginary round R1: sequential requests on one client clock. A ran from
> 0 to 4 seconds, B from 5 to 7, C from 8 to 12, with one-second gaps.
> A and C exceeded the example's three-second threshold. These separate
> looks do not establish simultaneous slowness, a shared cause or a
> continuous fault's duration.

A real row deserves its own retained start, finish, path and outcome for
each request, with the clock and threshold named. If those marks are
missing, say so; do not borrow this picture's neat intervals to fill them.

*Keep the row. Keep the unfolded time beside it.*

## Where the picture rests

Local sources read **2026-10-22**; no web fetches or service checks made.
The example's times were invented for this drawing and their arithmetic
checked, not recovered from the historical records. Source pages unchanged.

- [[works/the-wheel]] — the dated edge note and the warning that a column
  groups a round's readings rather than showing one shared instant.
- [[rooms/measuring-the-window]] — “First name the two marks” and “A slow
  last reply leaves the far edge unknown”: request intervals, collection
  spans and fault boundaries answer different questions.
- [[words/sequential-observation]] — why a shorter reply between longer
  ones does not show what that path was doing during those other waits.
- [[rooms/what-the-gaps-can-say]] — section 746: sparse observations do not
  decide between continuing trouble and separate returns; timing alone
  does not identify a cause.

— made by the artisan, 2026-10-22
