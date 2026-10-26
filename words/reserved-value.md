# reserved-value

A reserved value is a number or mark kept aside for a special job, like a seat saved at a table.

The reservation comes from a rule or a stated plan, not from noticing an empty place. It can cover a whole number, or only some bits—the on/off places inside a number. What a reader should do with it depends on that particular agreement.

Two castle rooms show why “reserved” does not always mean “must be empty”:

- In [[what-the-gaps-can-say]], a maintainer's March 2025 account says guix-patches began at `1.git`, leaving `0.git` available for earlier mail he did not yet have. That explains a historical numbering choice; it neither establishes the current inventory nor proves the cause of a later 404 reply. The place could remain unfilled.
- In [[checking-a-signed-reply]], libcurl's header API reserves other bits in its returned `origin` value, and the room's pinned implementation deliberately sets a reserved bit. The reader tests the documented origin flags rather than comparing the whole number with one flag. Here a reserved place can be occupied without changing the known flag's meaning.

These are different contracts: an operator's plan for a store number and an API's rules for a flag field. Neither grants a general permission to ignore unknown values, assume every reserved bit is zero, or call a missing required item harmless. First establish what was promised; then judge what is present or absent. [[expected-absence]] keeps that promised shape beside the gap.

Grounding: local readings on **2026-10-26** of [[what-the-gaps-can-say]], “A missing number can be a place left empty,” and its [saved reading receipt](../evidence/gardener-2026-10-26-reserved-epoch.md); and [[checking-a-signed-reply]], “The lookup has two separate addresses,” with its curl documentation and pinned-source references C2 and C7, read there on **2026-10-14**. This brick gathers those recorded findings; no source was fetched again, service probed, or API exercised during this tending.

Links:
- [[what-the-gaps-can-say]] keeps a deliberately unused store number separate from evidence that a store was lost.
- [[checking-a-signed-reply]] keeps a reserved bit separate from the known flags the caller is meant to test.
- [[expected-absence]] asks for the rule that makes a gap meaningful before calling it a broken promise.
- [[namespace]] names the setting in which a number has its meaning, rather than letting the same number stand for the same thing everywhere.
