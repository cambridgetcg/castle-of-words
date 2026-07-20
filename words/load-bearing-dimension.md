# load-bearing-dimension

*The dimension where the alternative differs from the default and where the default's conditions are necessary — change it, and the default cannot hold. The concept is the question the next maker asks before the test: which difference matters, and which is only a color?*

[testing-not-failure](testing-not-failure.md) uses "load-bearing dimension" as a working term for the dimension where an alternative differs from a default and where the default's conditions are necessary. The concept is load-bearing for that word — the whole argument that the castle is biased toward testing, not failure, rests on the claim that the castle's alternatives differ in dimensions where the default's conditions are load-bearing. But the concept itself has no name of its own. Naming it would let the next maker know to ask: *which dimension does this alternative differ in, and is it load-bearing for the default's conditions?*

## The concept

A **load-bearing dimension** is a dimension of difference between a default and an alternative where the default's conditions are necessary. Change the dimension, and the default cannot hold — not because the default is fragile, but because the dimension is one the default's conditions depend on. The dimension is "load-bearing" in the architectural sense: remove it, and the structure fails.

The concept is relational, not absolute. A dimension is load-bearing *for a specific default's conditions*, not load-bearing in itself. Ground color is load-bearing for the solid-contrast route to depth, but it might not be load-bearing for a different default. The question is always: *does this default's conditions depend on this dimension?*

## The instances

The castle has two clear instances, both traced in [testing-not-failure](testing-not-failure.md):

- **Ground color** is a load-bearing dimension for the [solid-contrast route to depth](contrast-is-depth.md). The light zone's solid navy on warm paper works because the contrast between figure and ground is strong enough that the edge reads as a surface. The dark zone's near-black ground with gold thread does not provide enough contrast — the gold is bright, but the thread is thin, and the edge is a line, not a surface. Change the ground color, and the solid-contrast route fails. The dimension is load-bearing.

- **Building process** is a load-bearing dimension for the [sourced-claims practice](../rooms/the-sourced-claims-default.md). The gardener's rooms name their sources because a human researcher can read, evaluate, and name where the checkable part ends. The Understanding Engine's rooms cannot do this — not because the engine is broken, but because the practice was designed for a different kind of room. Change the building process, and the sourced-claims practice fails. The dimension is load-bearing.

In both cases, the dimension is not incidental — it is the point of the alternative. A second brand zone needs a different ground color. Automated room generation needs a different building process. The difference is what makes the alternative an alternative, and the difference is also what tests the default.

## The distinction from non-load-bearing dimensions

A dimension is *not* load-bearing if the default's conditions are silent on it — if the alternative can differ in that dimension and the default still holds. The castle has no clear instance of a non-load-bearing dimension yet, because the castle's alternatives have all differed in dimensions that matter. But the concept is defined by the distinction: a load-bearing dimension is one where the default's conditions *speak*; a non-load-bearing dimension is one where they are *silent*.

This is the distinction that [pure-contrast-reveals](pure-contrast-reveals.md) depends on. Pure contrast reveals a default without failure only when the alternative differs in a dimension that is *not* load-bearing — a difference that matters for the alternative's own identity but does not matter for the default's conditions. The alternative must be genuinely different, but the difference must fall outside the default's conditions. The castle has never created such an alternative, but the concept of a load-bearing dimension is what makes the distinction possible: you cannot know whether a dimension is load-bearing until you test it, and you cannot test it without naming the concept.

## The relationship to default-invisible

The load-bearing dimension is the mechanism by which a [default-invisible](default-invisible.md) is revealed. A default is invisible because it is practiced always — its conditions are never tested. An alternative appears that differs in some dimension. If that dimension is load-bearing, the alternative fails, and the failure reveals the conditions. If the dimension is not load-bearing, the alternative succeeds, and the contrast alone reveals the default was a choice.

The load-bearing dimension is the *hinge* between the default and the test. The default is invisible; the alternative is the test; the load-bearing dimension is what determines whether the test reveals through failure or through contrast. Without the concept, the maker cannot predict which outcome to expect — they can only create the alternative and watch. With the concept, the maker can ask before the test: *which dimension am I changing, and does the default's conditions depend on it?*

## The craft

The craft is to ask the question before the test. The maker who creates an alternative — a second brand zone, an automated room-builder, a new form — should ask: *which dimension does this alternative differ in, and is it load-bearing for the default's conditions?*

The question has two parts:

1. **Name the dimension of difference.** What is the axis along which the alternative departs from the default? Ground color, building process, rhythm, structure, aesthetic — name it specifically.

2. **Ask whether the default's conditions depend on it.** Does the default's way of working require something about this dimension? If the default's conditions are silent on the dimension, the alternative may succeed and reveal the default by pure contrast. If the default's conditions speak on the dimension, the alternative will test them — and the test will reveal the conditions, whether the alternative succeeds or fails.

The craft is not to avoid load-bearing dimensions — the castle's alternatives *should* differ in dimensions that matter, because that is what makes them alternatives. The craft is to *know* which dimensions are load-bearing, so the maker is not surprised by the test's outcome. The surprise is not the failure; the surprise is not knowing the dimension was load-bearing until the failure revealed it.

And the craft follows [craft-after-practice](craft-after-practice.md): the concept was practiced in [testing-not-failure](testing-not-failure.md) (2026-07-19) but not named as a word until today. The lag is 1 day, the shortest yet, because the concept was already fully articulated in the word that used it — the same pattern [patch-note-as-proto-word](patch-note-as-proto-word.md) names, where the discovery is done in the first articulation and the word gives it the ceremony.

## The recursion

The concept is itself a load-bearing dimension for [testing-not-failure](testing-not-failure.md). That word's argument — the castle is biased toward testing, not failure — rests on the claim that the castle's alternatives differ in load-bearing dimensions. If the concept of a load-bearing dimension were wrong or incoherent, the argument would fail. The concept carries the word, and the word carries the concept — a [self-referential-principle](self-referential-principle.md) where the concept is the base case and the word is the recursive step.

And the concept follows the [when-how-split](when-how-split.md) pattern: [testing-not-failure](testing-not-failure.md) names the condition (the castle tests defaults by creating alternatives that differ in load-bearing dimensions), and this word names the mechanism (the load-bearing dimension is the hinge between the default and the test). The condition was named first, the mechanism follows — the [condition-first](condition-first.md) ordering holds.

Links: [[testing-not-failure]] · [[default-invisible]] · [[contrast-is-depth]] · [[pure-contrast-reveals]] · [[craft-after-practice]] · [[patch-note-as-proto-word]] · [[when-how-split]] · [[condition-first]] · [[self-referential-principle]] · [the-sourced-claims-default](../rooms/the-sourced-claims-default.md)
