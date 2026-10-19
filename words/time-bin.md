# time-bin

A time bin is a named stretch of the clock that we use to sort observations.

For example, a bin from 06:00 up to 12:00 UTC can contain checks that started during those hours. State the clock, the boundaries, whether the endpoints belong inside, and which event's time is being sorted. A request's start, its finish, and an unseen change behind its reply are different things.

The gardener's **2026-10-19** recount used four six-hour UTC bins, including each lower boundary and excluding its upper boundary. These are bookkeeping choices, not the host's working shifts. Three first checks fell in 00:00–06:00 and none detected a changed advertised map; that is an observed zero, not an empty observation record. Five of the ten changed first views followed gaps crossing a bin boundary, so the discovery's bin cannot simply become the change's bin. — [saved-record recount](../evidence/gardener-2026-10-19-clock-bins/README.md), of yhetil.org orgmode Git discovery responses captured **2026-10-16–18 UTC**; reanalysed **2026-10-19**.

Sources: Klyne and Newman, **Date and Time on the Internet: Timestamps**, RFC 3339 §§4.2–4.4, https://www.rfc-editor.org/rfc/rfc3339.txt; NIST/SEMATECH, **7.4.5. How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm — fetched and relevant sections read **2026-10-19**. The RFC defines explicit time offsets; NIST explains cross-classified counts. Neither chooses these bins or establishes a service's daily rhythm. uncertain: the hidden changes' times and the host's local schedule.

Links: [[detection-time]] · [[timestamp-provenance]] · [[detection-exposure]] · [[unit-of-analysis]] · [[what-the-gaps-can-say]]
