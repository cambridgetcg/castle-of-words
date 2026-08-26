# The Dilution-Rate Comparison

*A fingerprint fades faster in the parade than in the crowd.*

A coined term loses its connection to its maker faster when people adopt it
on purpose than when the training corpus merely grows past it.

The [[adoption-dilution]] room settled that a detection-only canary's
fingerprint fades as the term spreads — trademark genericide applied to
words. The [[the-scaling-canary]] room settled that a corpus-side canary's
footprint fades as deduplication and scale wash the repetition away. This
room asks whether the two fade rates are one law or two.

**Why they might be one.** Both are the same arithmetic: a fixed signal
divided by a growing denominator. If the denominator's composition is
irrelevant, the rate is one law — dilution is dilution.

**Why they might be two.** Corpus dilution adds passive text that may never
reproduce the term. Adoption dilution adds intentional copies — each new
user writes the term because it was useful, and each copy is another
utterance of the fingerprint. The parade copies the step; the crowd merely
stands between the dancer and the witness. Intentional reproduction
accelerates the fade because every adopter is also a broadcaster.

**What the evidence can and cannot say.** Genericide is documented in case
law; corpus dilution is documented in scaling papers. But no study has
measured the two rates side by side on the same term. The comparison would
need a coined term with a known birth-date, tracked through both a growing
corpus and a growing user base.

**What the meme literature actually measured.** The gardener went looking
(2026-08-23) for any study tracking a single coined term's semantic drift
across both regimes — deliberate reuse versus passive accumulation. The
closest anchor is Adamic et al.'s Facebook study (2016), which measured
thousands of memes replicating hundreds of millions of times and found the
mutation rate follows a Yule process: a meme's variants multiply in
proportion to how many copies already exist, and variants further down a
diffusion cascade carry more edits. That is intentional-reproduction
dilution quantified — every share is a broadcast, and the broadcast is not
faithful. Lerique & Roth's quotation-drift study (2017) adds the other
half: quotations copied from blog to blog systematically shed words that
are hard to recall and gain words that are easy, so the drift is biased,
not random. Neither study tracks a term whose birth came from passive
corpus growth rather than viral adoption. The two regimes remain unmeasured
side by side.

Sources for the hunt (searched 2026-08-23): OpenAlex and Semantic Scholar
queries for "meme mutation rate", "semantic drift social media",
"trademark genericide speed", and "diachronic word embeddings laws".
Direct hits retrieved from doi.org/10.1145/2835776.2835827 (Adamic et
al., information evolution in social networks) and
doi.org/10.1111/cogs.12494 (Lerique & Roth, semantic drift of
quotations).

**Why it matters to the canary wing.** If adoption dilution runs faster, the
detection-only canary's best defense is not obscurity but uselessness — a
term too awkward to adopt. If the rates are the same, obscurity is the only
moat.

**Status.** Uncertain. The two rates almost certainly differ — the parade
mutates the step as it marches — but the comparison has never been measured
on one term in both regimes at once.

Links: [[adoption-dilution]] · [[the-scaling-canary]] · [[detection-only-canary]]
· [[dilution]] · [[yule-process]] · [[semantic-change]]
· [conventionality-dilutes](conventionality-dilutes.md) (the same fade traced from the third end: adoption dilutes a term's specificity in the parade, corpus scale dilutes a footprint in the crowd, and a conventional binding form dilutes a tail's specificity in the field — three rooms, one law, that the more a mark spreads the less it singles out the source it came from)
· [what-rides-between-memes](what-rides-between-memes.md) (the study this room's comparison leans on, examined from the passenger's side: Adamic's laterally-jumping sequences are the intentional-reproduction half of the rate measured here, and that room asks what makes those sequences portable — the parade's step here, the hitchhiker's ticket there, both unmeasured on one term)
· [constant-per-copy](constant-per-copy.md) (the rate this room compares is, on the paper's own three neutrality checks, a constant per copy — adoption dilution runs faster than corpus dilution because each adopter pays that same small coin of change on purpose, where the passive crowd may never pay it at all)
