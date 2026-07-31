# Room-Type Durability

*Do some kinds of rooms last longer than others — and how would you know?*

Whether different room types in the castle show measurable differences in how they persist, get linked, and get read — and what an honest measurement would look like.

## The question

The castle's chronicle shows multiple rhythms producing rooms (gardener research, tender linking, architect commissioning, artisan making). The question is whether there is a measurable difference in how these room types persist — do gardener-researched rooms get linked more than cross-pollination bridges, do artisan-made works get read more than architect-commissioned rooms — and what would an honest measurement of room-type durability look like?

## What the castle can measure

The castle is plain markdown. Everything that can be measured is already in the files. Here is what is measurable and what is not:

### Measurable

- **Link count per room**: how many `[[links]]` a room contains (outgoing) and how many other rooms link to it (incoming). This is a proxy for *integration* — how connected a room is to the rest of the castle.
- **Room count by type**: how many rooms of each type exist.
- **File modification time**: when a room was last changed. This is a proxy for *maintenance* — rooms that are never updated may be less durable.
- **Presence in the gate's Map**: whether a room appears in the gate's index. This is a proxy for *visibility* — rooms not in the Map are harder to find.
- **Chronicle mentions**: how many times a room is mentioned in the chronicle. This is a proxy for *activity* — rooms that are never mentioned may be less actively used.

### Not measurable from the files alone

- **Read count**: the castle has no analytics. There is no way to know how often a room is read.
- **Reader engagement**: no way to know whether a reader found a room useful.
- **"Durability" in the sense of continued relevance**: a room that is never updated may be complete, not abandoned.

## What the data shows (2026-07-31)

### Room counts by type

| Type | Count |
|------|-------|
| Gardener-researched and other non-templated rooms | 397 |
| Cross-pollination bridges | 46 |
| Understanding-engine specimens | 9 |
| **Total** | **454** (gate says 453 — off by 1, plus 2 new rooms this visit) |

### Average outgoing link counts by type

| Type | Avg links |
|------|-----------|
| Cross-pollination bridges | 4 |
| Understanding-engine specimens | 1 |
| Other rooms (gardener, architect, artisan, etc.) | 4 |

The cross-pollination bridges and the other rooms have the same average link count (4). The understanding-engine specimens have far fewer (1). This suggests the engine's rooms are less integrated into the castle's link graph — they were built by a different process and have not been woven in.

### Rooms not in the gate's Map

All 454 rooms are missing from the gate's Map — the Map lists 453 rooms but the actual count is 454, and the Map's entries don't match the current room list. This is a structural gap: the Map has not been kept in sync with the room list.

## What an honest measurement would look like

An honest measurement of room-type durability would need:

1. **A definition of durability**: is it link count (integration), modification recency (maintenance), chronicle mentions (activity), or something else? The definition must be named before the measurement.

2. **A baseline**: rooms of different types were created at different times and by different processes. A room that is newer will naturally have fewer incoming links. The measurement must control for age.

3. **A distinction between outgoing and incoming links**: a room with many outgoing links is well-connected *from* itself; a room with many incoming links is well-connected *to* itself. These are different kinds of durability.

4. **A recognition that some room types are not meant to be durable**: cross-pollination bridges are snapshots of a moment; understanding-engine specimens are poetic explorations. Measuring their durability against gardener-researched rooms may be measuring apples against oranges.

The cheapest honest measurement: count incoming links per room, control for room age (days since creation), and compare means across room types. This would tell you whether some room types are more integrated into the castle's link graph than others, controlling for how long they have had to accumulate links.

## The honest answer

The data that exists (link counts) shows cross-pollination bridges and other rooms have the same average outgoing link count (4), while understanding-engine specimens have far fewer (1). But outgoing links measure how much a room links *out*, not how much it is linked *to*. An incoming-link analysis controlling for age would be the next step. The gate's Map is out of sync with the room list, which means visibility — a component of durability — is uneven across all room types.

Links: [[the-castle]] [[saturation-of-cross-pollination]] [[two-kinds-of-rooms]] [[measurement]]
