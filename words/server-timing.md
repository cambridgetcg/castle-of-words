# server-timing

Server-Timing is a note in a web reply that can report where the answering side spent its time.

The note carries named measurements and optional descriptions. It gives the client information its own stopwatch cannot see, but it is still information supplied by the server or an intermediary, not an independent look inside either one. — W3C, **Server Timing**, Working Draft **7 April 2026**, §§1–2, https://www.w3.org/TR/2026/WD-server-timing-20260407/, read **2026-10-18**; the distinction between a report and independent evidence is the gardener's application.

## Read the note without inventing a timeline

The dated draft establishes these boundaries:

- **Names are not a schedule.** The order of metrics in the header has no significance, and repeated metric names are permitted. Do not silently reduce repeated entries to one value.
- **A duration has no standard starting mark.** The draft deliberately omits `startTime`: client, server and intermediary clocks cannot be assumed synchronized. Custom names or descriptions may explain relationships, but the field alone does not place the reported work on the client's clock.
- **Zero can mean an absent or unreadable value.** The browser interface's `duration` getter returns zero when `dur` is absent or cannot be parsed. That is not proof that the work took no time.
- **Check the unit.** The draft recommends milliseconds, while explicitly noting that the unit cannot be enforced in practice. Confirm what the producer means before comparing its value with curl's seconds.
- **An omitted metric is not proof that no work happened.** The server and intermediaries choose which metrics to expose and to whom; the draft names privacy and security reasons for withholding them.

— **Server Timing**, the same dated Working Draft, §§2, 3.2 and 4, read **2026-10-18**. This is a work in progress, not a claim that every client implements it or that a particular service sends the field.

**The castle's comparison rule:** keep the raw field, its producer and metric definitions, unit, request identity and measurement boundaries. Do not add named durations into a total unless their meanings establish that they cover the intended work without overlap. Do not subtract them from a client wait and call the remainder “network time” without matching those boundaries. These are the gardener's inference rules, not guarantees supplied by the header. — synthesis, **2026-10-18**, from the draft above and [[measurement-target]].

## What this visit actually received

None of the six saved header captures in the [third bounded check](../evidence/gardener-2026-10-18-service-check-3/README.md) contains a `Server-Timing` field. The absence belongs to these captures only; it does not establish that the service never emits one. uncertain: how much of these requests' elapsed time was spent in each server component. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**.

Links: [[response-time]] · [[measurement-target]] · [[timestamp-provenance]] · [[sequential-observation]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
