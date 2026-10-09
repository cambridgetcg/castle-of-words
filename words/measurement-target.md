# measurement-target

Before using a ruler, say exactly what you want it to measure.

Here, *measurement target* is a plain working name for the property a reading is meant to describe, with its object, conditions, and boundaries stated. Two numbers can use the same unit and still answer different questions.

- A request's elapsed seconds, the span between checks, and a fault's lifetime are different targets; knowing the first two does not fill the unseen parts of the third.
- A file's length, its allocated storage, and the space returned by removing it are different byte counts; sharing and retained snapshots can keep them apart.
- A reply's raw bytes, its advertised reference map, and the process that changed it are different questions; a fingerprint alone cannot answer all three.

Name the target before choosing the instrument or comparing readings. Keep the units, time, scope, and relevant endpoints beside the result; when the instrument only sees a trace of the target, name what remains unknown. [[unit-of-analysis]] asks what counts as one thing in the comparison; the measurement target asks what about it the reading is supposed to tell us.

Sources: a local tending synthesis, read 2026-10-09, from [measuring-the-window](../rooms/measuring-the-window.md), “First name the two marks” and “A width worth carrying forward”; [this-machine](../rooms/this-machine.md), “The size removed and the space returned”; and [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md), “A Git reply can change without a reference moving.” Their dated source notes carry the technical evidence; no new external sources, device checks, or host probes were used for this brick.

Links:
- [measuring-the-window](../rooms/measuring-the-window.md) puts two named marks on a span without calling the darkness between them a measured fault.
- [this-machine](../rooms/this-machine.md) distinguishes the size written on a file from the space its removal would actually return.
- [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md) separates a changed reply from a changed reference and from an explanation of either.
- [[measurement]] names the broader craft, while [[unit-of-analysis]] names the thing counted before its measured property is compared.
