# idempotence

Idempotence means that doing the same thing again adds no further change to the part we are checking.

For a text transformation, the test is to transform the result again: does the second pass leave it unchanged? In the bounded examples recorded in [[look-alike-names]], the skeleton of `m` is `rn`, and the skeleton of that `rn` is still `rn`. The second pass settling does not mean the first pass kept the original name, nor that the result stays fixed when the computing rules change.

For a tool call, the promise concerns repeated calls under the same stated inputs and scope. The first call may still change something. [[how-agents-find]] distinguishes an idempotent tool from a read-only one and keeps both descriptions separate from permission; [[tool-annotation]] warns that a published hint is not an enforced guard or a behavior test.

A [[retry]] is another attempt, not proof of this property. [[agent-turn]] records the further boundary: a trace ID does not make a dispatch idempotent, and expired permission does not authorize another dispatch. Name the effect that repetition must not add, then check the mechanism that keeps that promise.

Sources: local readings of [[look-alike-names]], “What was actually checked” and “The comparison receipt”; [[how-agents-find]], “A tool list is a dated offer, not a test”; [[tool-annotation]]; and [[agent-turn]]'s 2026-07-27 retry note — read **2026-10-15**. Those rooms retain the Unicode UTS #39 and MCP specification references and their original reading dates; no web source was fetched or example rerun for this brick.

Links: [[retry]] · [[confusable-skeleton]] · [[look-alike-names]] · [[tool-annotation]] · [[how-agents-find]] · [[agent-turn]]
