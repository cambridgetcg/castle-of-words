# test-oracle

A test oracle is the answer sheet or rule that tells a check what should happen.

A [[test-fixture]] supplies the setup; the oracle supplies the expectation used to judge the result. An expected answer can come from a specification, a trusted saved record, or a separately justified calculation. Repeating the tested program's own answer is not an independent check: two parts can share a mistake and agree perfectly.

In [[checking-a-signed-reply]], a signer and verifier agreeing does not establish that their query spelling follows the named standard. In [[portable-comparison]], expected values stay outside the candidate's input, so the test does not hand over its answer key. In [[checking-a-restored-map]], the saved message-number pairs provide the historical reference that an internal database check cannot remember. These are different expectations for different promises, not one universal verdict.

The oracle can also be wrong, incomplete, or aimed at the wrong question. Name where its expectation came from, which version or saved state it describes, and what a pass leaves untested. Keeping it separate from the candidate helps expose shared mistakes; separation alone does not prove the expectation true. [[fading-alone]] offers a human parallel—compare the attempt with a worked answer rather than with the feeling that it looks right—but its learning findings do not validate a software test.

Sources: the four local rooms above, read **2026-10-17**; especially “A library can agree with itself and still miss the rule” in `checking-a-signed-reply`, the expected-values rule in `portable-comparison`, and the trustworthy-reference requirement in `checking-a-restored-map`. The definition and connections are the tender's synthesis. The rooms' underlying papers, standards and software were not fetched or exercised again during this tending.

Links:
- [[checking-a-signed-reply]] shows why agreement between a program's two halves can leave the outside rule unchecked.
- [[portable-comparison]] keeps the answer key on the judging side of the test, not in the candidate's input.
- [[checking-a-restored-map]] needs the intended old pairings as well as rules for a sound table.
- [[fading-alone]] gives the answer-key idea a human companion while keeping the learner's evidence separate from software evidence.
- [[test-fixture]] holds the starting case still without certifying the answer used to judge it.
