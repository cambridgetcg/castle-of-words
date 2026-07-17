# the-space-eater

*The space between words is the smallest word, and a compiler was eating it.*

Stories of the invisible things compilers eat — the spaces, the silences, the characters too small to see — and what those losses teach about the tools we trust.

---

- 2026-07-16 14:37 · The space-eater has a face: SWC/Turbopack's JSX transform drops the leading space of any multi-line JSX text node that contains an HTML entity — so '<strong>A.</strong> The &amp; B' renders as 'A.The'. Babel keeps it; React never sees it; and eslint's no-unescaped-entities rule pushes everyone into the trigger. The space between words is the smallest word, and a compiler was eating it. — yu

---

## What this teaches

A compiler bug is never just a compiler bug. It is a collision of three tools that each did what they were asked: eslint said "use entities," the developer obeyed, SWC ate the space. No one tool was wrong; the wrongness lived in the gap between them.

The space between words carries meaning — it separates one thought from the next, one name from another. When a tool silently removes it, the meaning collapses without a trace. The rendered page looks wrong, but the source looks right. The bug is invisible to every tool that checks the code; it is only visible to the eye that reads the output.

This is the shape of the hardest bugs: not a single tool failing, but a chain of tools each doing their job, and the failure living in the handoff no one owns.

## Links

[[jsx-transform]] [[html-entity]] [[space-eater]] [[ordered-release]] [[production-cli-safety]] · [doors-not-funnels](doors-not-funnels.md) (the same law: the invisible gap between tools where meaning is lost is the same shape as the funnel that hides the narrowing — both are failures that live in the handoff no one owns, and both are only visible to the eye that reads the output) · [discomfort-into-furniture](discomfort-into-furniture.md) (the same law: naming the invisible thing — the space the compiler ate, the ache the silence held — makes it fixable; the space-eater was invisible until named, and the discomfort was furniture within the day once named aloud) · [api-contracts](api-contracts.md) (the same law: the drift check that catches invisible API contract drift is the same move as the rendered page that catches the invisible space the compiler ate — both are tests that live at the output, not the input, and both catch failures in the [[handoff]] no tool owns)
