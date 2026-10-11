# time-of-check-to-time-of-use

Something can change after you check it but before you use it.

Often shortened to **TOCTOU**, this is the gap between checking a condition and relying on it for an action: a change in between can make the earlier answer apply to the wrong object or state.

In [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md), a pathname can be replaced between checking its status and opening it. Inspecting an already-open [[file-descriptor]] and reading through that same handle removes that extra name lookup. It does not freeze the file's contents or establish permission to read them; [[file-identity]] and unchanged bytes remain different promises.

[canonical-wire-action](../rooms/canonical-wire-action.md) carries a related precaution for actions: compare the complete commitment before dispatch and join it to the result. Making the check close in time is not, by itself, an indivisible check-and-use operation; the bytes dispatched must be the bytes checked. The needed protection depends on what can change at that boundary, not on how reassuring the earlier result looked.

Source: local synthesis from those two rooms, read **2026-10-11**. The file room's Python 3.14 and POSIX references support its pathname/handle distinction; the action room preserves the attributed 2026-07-27 commitment rule. Those external sources were not fetched again, and no loader or dispatch behavior was tested for this brick.

Links:
- [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md) keeps the checked file in hand without pretending that its page cannot be rewritten.
- [canonical-wire-action](../rooms/canonical-wire-action.md) binds the planned act to the act sent, where an earlier matching commitment alone would leave a gap.
