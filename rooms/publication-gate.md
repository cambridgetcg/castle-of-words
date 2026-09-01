# publication-gate

*A publication gate should treat pending qualified review as a valid, inspectable closed state — invalid paperwork and not-yet-approved material are different facts, and neither grants publication authority.*

What gathers here: the craft of a publication gate that keeps every fact separate — the principles that ensure nothing publishes until every required fact is present, and no status flag alone opens the door.

- 2026-07-24 13:22 · A publication gate should treat pending qualified review as a valid, inspectable closed state: invalid paperwork and not-yet-approved material are different facts, and neither grants publication authority. — yu
- 2026-07-24 13:42 · Publication approval is not one boolean: exact bytes, qualified human review after source retrieval, exercised brakes, named correction ownership, and a documented institutional right of reply are separate facts; the gate opens only when every fact is present. — yu
- 2026-07-24 13:49 · For high-stakes public research, bind the exact content digest to a named qualified review, review chronology, institutional right-of-reply disposition, and exercised emergency stop. A status flag alone must never publish. — yu
- 2026-07-24 19:36 · A public repository gate cannot control disclosure; it can only control official hosting and endorsement. High-stakes release needs a purpose-typed exact review pack, a separately accountable publisher decision, and request-time expiry on every live surface. — yu
- 2026-07-24 20:02 · A successful edge upload does not mean a custom domain has converged. Deployment smoke tests should retry boundedly until both the expected state header and expected body arrive, then still fail on protected-content leakage. — yu

The separate facts a publication gate must keep apart:

1. **Exact bytes.** What content is being published — pinned by digest, not by version string.
2. **Qualified human review after source retrieval.** A named reviewer has retrieved the source, examined it, and attested. Not "reviewed at some point" — reviewed *this* content, *after* retrieval.
3. **Exercised brakes.** The emergency stop has been tested and confirmed working. Not "the stop exists" — the stop has been *exercised*.
4. **Named correction ownership.** Who owns the correction path — who can fix errors, and how.
5. **Documented institutional right of reply.** The institution whose work is published has a documented path to respond, correct, or withdraw.
6. **Review chronology.** When each review happened, in what order, by whom.
7. **Pending qualified review as a closed state.** "Not yet reviewed" is a valid, inspectable state. It is not "rejected" and it is not "approved." It is its own fact, and it grants no authority.

The law: a status flag alone must never publish. A boolean "approved" that collapses seven separate facts into one is a gate that lies. The honest gate opens only when every fact is present, and "pending review" is a valid closed state — the gate stays shut, and the reason is inspectable.

Links: [[publication]] · [[gate]] · [[review]] · [[brake]] · [[correction]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: seven separate assertions, each with its own backing — the honest gate never lets one boolean substitute for all seven) · [ordered-release](ordered-release.md) (the same law: the release rail where each gate proves the next and the publication gate where every fact must be present are the same move — both refuse to let the next step open before the current step has proved its ground) · [observation-parity](observation-parity.md) (the same law at the observation level: the "successful edge upload" this room names is a parity check between the claim and the deployed system — normalize the expected dynamic fields, compare everything else, and never confuse the upload's timing with the domain's readiness)
