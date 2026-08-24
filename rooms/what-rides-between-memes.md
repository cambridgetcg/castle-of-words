# What Rides Between Memes

*Some sentences are hitchhikers; no one has yet read their tickets.*

Adamic et al. (2016) tracked thousands of Facebook memes through hundreds of
millions of replications and found the [[yule-process]] at work: variants
multiply in proportion to their copies, mutations accumulate down a cascade,
and — the strange part — certain short text sequences act like lateral
genes, jumping from one meme lineage into another and conferring a
replicative advantage on their new host. This room asks what *property*
makes those sequences portable, and whether any study has measured which
features predict lateral transfer.

**The short answer.** No. Ten years of citation tracing (searched 2026-08-23
via OpenAlex) finds no study that regresses Adamic's laterally-transferring
sequences against lexical, syntactic, or affective features to see what
predicts the jump. The portability of the sequence is asserted from its
effect; its design is unexamined.

**What the neighborhood knows instead — feature studies of the host, never
the passenger.**

- **Distinctiveness helps the whole meme live.** Coscia (2014) showed memes
  whose characteristics make them *unique* thrive: successful memes sit on
  the periphery of the meme-similarity space — average is boring. That is a
  feature of the host meme, not of the sequence that travels between hosts.
  ("Average Is Boring: How Similarity Kills a Meme's Success",
  doi:10.1038/srep06477)

- **Wording moves propagation, measurable word by word.** Tan, Lee & Pang
  (2014) exploited natural experiments — same user, same URL, different
  wording — and showed the wording alone changes retweet counts, by more
  than chance and less than perfectly. Portability of a *message* is partly
  lexical and measurable; but again the unit is the whole tweet, not the
  snippet that crosses memes.
  ("The Effect of Wording on Message Propagation: Topic- and Author-
  Controlled Natural Experiments on Twitter", doi:10.3115/v1/P14-1017)

- **Affect carries diffusion.** Brady et al. (2017) found moral-emotional
  words increase a tweet's spread (~20% per such word). A candidate feature
  — emotional charge — confirmed at the message level, untested at the
  lateral-sequence level.
  ("Emotion Shapes the Diffusion of Moralized Content in Social Networks",
  doi:10.1073/pnas.1618923114)

- **Recall shapes the drift.** Lerique & Roth (2017) showed quotations
  copied across blogs systematically shed hard-to-recall words and gain
  easy ones — drift biased toward memorability, the closest thing to a
  *content-side* portability law. But that is mutation under copying, not
  lateral transfer of intact sequences.
  ("Linguistic Evolution and the Dynamics of Online Quotations",
  doi:10.1111/cogs.12494)

**The two mutation laws, side by side.** A cascade's internal mutations
(Adamic et al. 2016, thousands of memes replicated hundreds of millions
of times on Facebook) follow the [[yule-process]]: variants multiply in
proportion to how many already exist, and variants further down a sharing
chain carry more edits — a *copy-count* law, indifferent to what the words
say. Lerique & Roth 2017's drift between blogs follows a *content* law:
substitutions are biased toward more frequent, easier words — a
[[cultural-attractor]] pulling every copied quote toward [[memorability]].
The two literatures each measured one side; no study has read both sides
of one mutation at once — the chain position *and* the substitution
direction of the same edit — so it is unknown whether cascade mutations
in Adamic-style data drift toward memorability, or differ from
between-blog drift at all. The dataset exists; the crossing has never
been run. Read alongside [[dilution-rate-comparison]]: the parade mutates
by one law, the crowd by another, and nobody has checked whether the
parade's drift lands anywhere in particular. And read [[constant-per-copy]],
which walks the next door: whether the yule accumulation is consistent with
the simplest constant per-copy mutation rate — it is, on the paper's own
three neutrality checks.

**Why the gap matters to the canary wing.** The [[dilution-rate-comparison]]
room leans on Adamic's lateral-transfer finding as evidence that intentional
reproduction mutates the fingerprint. If portability were a *measurable*
property — if a short, rhythmic, emotionally-loaded sequence were provably
the hitchhiking kind — then a detection-only canary could be engineered
*away* from portability: flat cadence, no affect, awkward length. The
un-built study would hand the canary craft a recipe.

**What would settle it.** Take Adamic's sequence dataset, extract each
laterally-transferred fragment, and fit predictors: length, emotional
valence and arousal, syntactic rhythm, memorability scores, semantic hook
density. The dataset exists; the regression has never been run.

**Status.** Settled: no study has measured which features predict lateral
transfer. The adjacent evidence gives three candidate features —
distinctiveness, emotional charge, memorability — each confirmed at the
wrong unit of analysis. Door closed with the recipe for the next one.

Links: [[dilution-rate-comparison]] · [[yule-process]] · [[adoption-dilution]]
· [[detection-only-canary]] · [[semantic-change]] · [[memorability]]
· [[cultural-attractor]] · [[constant-per-copy]] · [[mutation-rate]] · [[neutrality]] · [mood-through-chains](mood-through-chains.md) (the same journey asked of the other cargo: this room asks what makes a sequence portable between memes, and that room asks whether a mood survives the handoffs while its words mutate — the hitchhiker's features here, the passenger's content there, and neither lab has read the ticket) · [[goldilocks-leaves-home]] (another wing, the same null: there a curve was never fitted where the data stood ready, here a drift was never read where the edits stand recorded — two unbuilt crossings, both free) · [the-light-cargo](the-light-cargo.md) (the recipe this room is waiting on gets its first field reading: the Upworthy archive regresses variant survival on wording features and finds what this room predicted — negative emotion, length, specificity, pointed reference — the marked lives longer where no one is hunting)
