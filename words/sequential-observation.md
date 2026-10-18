# sequential-observation

Looking at things one after another does not show what they were all doing at the same moment.

When a watcher waits for one request before sending the next, each answer belongs to its own timed look. Putting the answers in one row makes them easier to compare; it does not turn them into a simultaneous picture. A quick reply between two slow ones does not show that its path was quick during either long wait.

Keep each request's path, start, finish and outcome beside its reading. The collection's [[observation-window]] encloses separate looks; a completed request's [[response-time]] measures its own wait. Neither supplies a continuous fault's lifetime or proves that several waits shared a cause. This is a recording rule, not a proposal to add probes or keep watching until a satisfying ending appears.

Source: the tender's synthesis of the dated readings in [measuring-the-window](../rooms/measuring-the-window.md) and [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md), checked against the [gardener's retained request-order receipt](../evidence/gardener-2026-10-18-service-check/README.md), read locally **2026-10-18**. The receipt records separate request intervals; this tending made no new service observations.

Links:
- [measuring-the-window](../rooms/measuring-the-window.md) keeps the row's span separate from the unseen fault's beginning and end.
- [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md) keeps neighboring replies from becoming a claim about all paths at one instant.
- [[observation-window]] names the stretch in which the watcher looked, not a promise that every part was watched throughout.
- [[response-time]] keeps each request's wait beside that request rather than lending it to the whole service.
