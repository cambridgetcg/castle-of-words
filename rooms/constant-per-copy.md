# Constant Per Copy

*Every retelling spends the same small coin of change; the long chains are simply the ones that paid most often.*

Adamic et al. 2016 ran the largest measurement of text copied from friend to
friend ever published — 4,087 memes on Facebook, each copied anywhere from
hundreds of thousands of times upward, with every copy tied to the friend it
came from. Their data carry a [[yule-process]] signature (variants multiply in
proportion to their copies) and a steady accumulation of edits down a chain.
This room asks: is that measured process consistent with the simplest possible
law — **every copy mutates with the same probability, no matter who makes it**
— or do the data force a heavier mechanism, a variation rate that itself grows
with copy count?

**The answer, in one breath.** Consistent — and the paper's own numbers answer
the challenge directly. Every test that would have detected a rate that scales
with the copy count came back flat. The copy-count law of cascade mutation is
exactly what a constant per-copy change rate, compounded down a chain, predicts.
(All claims below from "Information Evolution in Social Networks", Adamic,
Glance, Letchford & Huberman, WSDM 2016, doi:10.1145/2835776.2835827; arXiv
preprint 1402.6792, read in full 2026-08-23.)

**The three flat answers.**

- **The mutation rate does not drift.** Within a meme, the per-copy mutation
  probability µ did not change over that meme's lifetime (correlation of µ
  with time, ρ(t, µₜ) < 0.04). A process whose rate grew as copies
  accumulated would show the rate rising with time; it does not.
- **Fame does not buy edits.** The most popular variants of a meme were just
  as likely to spawn a mutated copy as the least popular (ρ(num mutated
  copies, popularity) > .95 — no relationship). If copying a variant with
  millions of copies behind it carried a different mutation propensity than
  copying a rare one, the popular variants would out-mutate the rare; they
  don't. The process is *neutral across variants*, as the [[yule-process]]
  assumes.
- **Yet edits still pile up with depth.** Edit distance from the root grows
  with the number of hops down the diffusion tree (their Figure 2, "a
  compound effect of such mutations over several generations"). That is not
  evidence against constancy — it *is* constancy, accumulated. A copy five
  hops from the root has survived five independent throws of the same die;
  each throw had the same chance µ of adding an edit, so the expected edits
  grow roughly in proportion to the hops.

**Why this matters — the two laws need not be two laws.** The question at the
door asked whether the yule-process finding is consistent with a per-copy
*content* bias of the kind Lerique & Roth 2017 measured between blogs (drift
toward [[memorability]], a [[cultural-attractor]]). Constant-µ says the
*rate* side is blind: the neutral model fits the great majority of memes, and
most variants behave as neutral with respect to their parent's popularity. But
blindness in *whether* a copy mutates says nothing about the *direction* of
the edits once made — and here Adamic's own table leans the way the content
law leans, without measuring it: the laterally-jumping 4-grams that conferred
replicative advantage were short, rhythmic, easy-to-match phrases ("put this
as your", "re[-]post if you", "if you love your"); edits clustered at the
memes' beginnings and ends; and a mild pressure favored slightly shorter
variants (the bacterial small-genome analogy). **uncertain:** these are hints
in the direction of memorability, not a measured drift — nobody has read the
substitution direction of cascade-internal edits against a memorability scale.
The consistency is proven; the identity of the two laws is not.

**The honest remainder.** One class of memes breaks the model on its face —
the handful with mutation rates above 0.5 are exactly those whose text
*instructs* the copier to mutate ("add your children's birthweights", "post
the chart from your birthday"). There the rate is not a property of copying
but of the words, and the yule model under-predicts the observed inequality.
A constant per-copy law, in other words, holds only where the meme does not
rewrite its own dice.

**Status.** Settled: the copy-count accumulation Adamic measured is fully
consistent with a constant per-copy mutation rate — the paper's own
neutrality checks (no drift in µ over a meme's life, no popularity-mutation
coupling, linear-looking compounding of edit distance with hops) are the
three tests a scaling rate would have failed, and it failed none of them. The
[[cultural-attractor]] law and the [[yule-process]] law are compatible halves
of one process — constant in rate, possibly biased in direction — with the
direction now read in shape, as [[the-direction-of-the-edits]] records, and
in its exact psycholinguistic units still open.

Links: [[what-rides-between-memes]] · [[yule-process]] · [[cultural-attractor]]
· [[memorability]] · [[dilution-rate-comparison]] · [[mood-through-chains]]
· [[goldilocks-leaves-home]] ·
[the-direction-of-the-edits](the-direction-of-the-edits.md) (the second half of the law this room left half-named: the rate is constant per copy, and the direction — which mutations the copies keep — this room has now read twice on cascade data, both times leaning the way the memorability hint predicted)
