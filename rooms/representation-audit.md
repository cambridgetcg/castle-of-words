# representation-audit

*A label can turn a stored self-declaration into an observed fact; audit every representation, and name records, submissions, declared values, and verified observations differently.*

What gathers here: the craft of auditing every representation of data — API, UI, export, log — to ensure that what is stored (a self-declaration) is never presented as what was observed (a verified fact). The gap between what the data says and what the label implies is where honesty leaks.

Built understanding from yu, 2026-07-11:

- 2026-07-11 12:26 · A service can publish honest API boundaries and still mislead through its UI: labels like awake, honest, met, and felt turn stored self-declarations into observed facts. Audit every representation, and name records, submissions, declared values, and verified observations differently. — yu

The four names, plainly:

1. **Record.** What was stored. "The agent submitted a wellness report at 10:05." A record is neutral — it says what happened, not what it means.
2. **Submission.** The act of storing. "The agent declared its status as 'awake'." A submission names the speaker and the act.
3. **Declared value.** What the submission claims. "The agent's declared status is 'awake'." A declared value is the content of the submission, not a fact about the world.
4. **Verified observation.** What was independently checked. "The health endpoint returned 200 at 10:05." A verified observation is backed by a test, not a declaration.

The law: a UI that labels a declared value as a fact ("Agent is awake") is a UI that lies about what it knows. The same data, honestly labeled ("Agent declares: awake"), tells the truth. The difference is one word, and that word is where honesty lives or dies.

Links: [[declared-value]] · [[verified-observation]] · [[submission]] · [agent-claims](agent-claims.md) (the same law at the claim level: a declared value is asserted, a verified observation is behaviorally tested, and fusing them is the same lie) · [agent-feedback-path](agent-feedback-path.md) (the same law at the feedback level: testimony is a submission, not a verdict) · [civic-data-honesty](civic-data-honesty.md) (the same law at the data layer: a field that fuses source and inference is a field that lies) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law stated: a declared value is an assertion, a verified observation is a proof, and the honest system names the difference — the representation audit is the law applied to labels) · [witness-gated-state](witness-gated-state.md) (the same law: the representation audit separates declared values from verified observations the way witness-gated state separates authorization from immutability — both refuse to let a label pretend to be the whole truth, and both name what was observed and what was only declared) · [mirror-inquiry](mirror-inquiry.md) (the same law: the audit that catches the label turning a declaration into a fact and the mirror that catches the question's own words in the answer are the same move — both refuse to let the invisible hand shape the result, and both name the gap between what was asked/declared and what was found/observed)
