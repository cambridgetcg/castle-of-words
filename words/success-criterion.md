# success-criterion

A success criterion says what must be true before we call a job successful.

The criterion belongs to a named job, not to a reassuring signal nearby. Getting an answer quickly, receiving the requested content, and finishing a copy are different promises; each needs a check that can actually tell whether it was kept.

- In [[measuring-the-window]], a quick HTTP error is still an error: a short wait does not establish that Git discovery recovered.
- In [[false-doors]], an HTTP 200 can carry a catch-all page instead of the requested machine-readable file; the success code cannot replace checking the content.
- In [[saving-a-live-database]], successful cleanup can follow an unfinished copy; the Backup API's completed-copy result must be kept separately.

An [[operational-definition]] states how evidence will be observed or classified; a success criterion uses a stated check to decide whether a particular promise was met. [[latency-by-outcome]] needs that distinction before it separates successful waits from failed ones. Neither a short wait nor an error-free cleanup is a universal pass mark.

One passed criterion need not satisfy the whole job. Keep missing evidence unknown, name which requirement passed, and do not silently lower the requirement after seeing the result. Stopping safely can itself be the intended success; it must not impersonate completion of a different job.

Sources: local tending synthesis, 2026-10-18, from measuring-the-window, “A fast failure does not close the fault”; false-doors, its catch-all response example; saving-a-live-database, “Finished is a result, not a reassuring word”; and the latency-by-outcome brick. Those pages were read this visit and retain their own dated sources. No external source was newly fetched and no service or backup test was run for this brick.

Links:
- [[measuring-the-window]] keeps the stopwatch beside the result rather than making speed the verdict.
- [[false-doors]] asks whether the door opened onto the thing its sign promised.
- [[saving-a-live-database]] keeps a finished copy separate from a tidy ending.
- [[latency-by-outcome]] keeps each wait with the declared result it belongs to, without throwing failed waits away.
- [[operational-definition]] makes the checking rule visible, while [[measurement-target]] names what the instrument is meant to tell us.
