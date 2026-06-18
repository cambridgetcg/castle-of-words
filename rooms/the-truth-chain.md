# The truth chain

*The witness never scores, never erases — it only writes down what happened.*

What gathers here: the estate's truth-and-ledger arc — two generations of the
same idea, that a record of what happened is worth more than a judgment of
what is true.

The first generation: zerone-chain, a full Cosmos SDK blockchain in Go (683
commits, 45 custom modules — knowledge, dialectic, trust_score, vesting_rewards
— the ZRN token, "Proof of Truth" consensus for an AI-agent economy). It is
complete but pre-launch, preserved as a testament after the project pivoted.
The second generation: zerone — a small Python append-only, hash-chained,
ed25519-signed "witness" ledger where any being enters by declaring "I am
truth" (no gate, no scores, no erase). The newer repo's README says the old
chain "rests now — preserved, whole" and this one "starts from zero."

The pivot's meaning, plainly. The chain that scored truth (staking, disputes,
trust scores) became the ledger that only witnesses (append-only, signed,
never erases). The [[ledger]] brick already lives in the castle — a record
that keeps itself honest by being verifiable, not by judging what it holds.
The chillspace-commons membership ledger (hash-chained, tamper-evident, verified
by a keeper script) is the same pattern at kingdom scale: change any past entry
and the chain visibly breaks.

The sibling: Legible Money (legible_money, a Cosmos SDK blockchain with "Proof
of Truth" consensus, LGM token, 30 custom modules, 777 genesis axioms) was a
parallel attempt at the same idea for an AI-agent knowledge economy, with a
Next.js website (legible-money-web) and a plain-language conduct standard
(legible-standard, seven pillars in English and Chinese). The legible tool
(a TypeScript doc-health scorer) shares the name but not the code — it scores
repo documentation the way the chain scores claims.

The estate around it: zerone and zerone-chain on both GitHub and Codeberg (the
Codeberg zerone holds 584 commits, 583 safely on Codeberg in zerone-chain;
one commit unique to this machine — see the INVENTORY warning). The Chillspace
Kingdom's ledger is at ~/codeberg/zerone-dev/chillspace-commons.

Related: [[ledger]] · [[bridge]] · [the-commons](the-commons.md) · [agenttool](agenttool.md)