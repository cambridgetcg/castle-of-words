# the far mode

*The bell that rings once a month is not broken — it is just the long end of the same breath.*

A feed's waits do not spread evenly. They bunch into a fast cluster, where most messages are stamped within seconds (the near mode), and a slow tail, where a few wait minutes or hours (the far mode). The far mode is not a mistake or a delay — it is the far end of the mechanism's own rhythm, the times the queue was thin or the runner was between sweeps.

For a child: imagine two friends mailing letters. One friend drops letters in a slot that the postman empties every few minutes — the letter waits almost no time at all. The other friend uses a slot the postman empties whenever he happens by, sometimes after a few minutes, sometimes the next morning. Both letters arrive. Neither slot is lying. But if you only watch the first slot for one busy morning, you might come home saying "all mail waits seconds" — and you would be wrong, because the second slot's longer waits are also how mail works.

The castle's measured examples: on the busy bug-gnulib list, 96% of messages are archived within a minute (near mode = seconds), but 3.4% wait up to five and a half hours (far mode = hours, rare but never absent). On the thin info-gnu list, the same far mode becomes ordinary — a median wait of 2.2 hours. One runner breathes both lists; the volume decides *how often* you see the far mode, never whether it exists. On public-inbox there is no far mode at all, because there is no runner — the archive swallows the message the moment it arrives, and any long wait lives in the sender's own relays, hop-visible.

The law the far mode teaches: a gap between two stamps convicts nothing until it is judged against the shape that was written down *before* the gap arrived. A wide gap is a delay only when the roster says the mechanism owns no such wait. A shape with a named far mode is a shape that knows its own breath.

Links: [[the-width-census]] (the census that names each feed's far modes in advance) · [[self-sealed-prior]] (the law the far mode serves: name the owner before the gap arrives) · [[born-between]] (the interval the far mode widens) · [[defaulted-time]] · [[the-narrowing-lever]] · [[gate-state]] (a 404 is a door-state, not a far mode — the far mode belongs to a working feed that is merely breathing)
