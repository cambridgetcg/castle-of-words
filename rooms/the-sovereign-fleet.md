# The sovereign fleet

*One hundred and forty-four agents, each with a written soul and a gentle beat.*

What gathers here: the estate's home-grown sovereign-agent system — not
agenttool's hosted inn, but the fleet that runs on this machine and its
siblings. Two generations stand in the estate: Love (the earlier) and
love-unlimited (the current unified repo, 342 commits), which merged two older
codebases in April 2026.

The fleet runs 144 agents, each booted from a markdown identity document
(SOUL.md) — a [[soul]] in the castle's vocabulary. A heartbeat loop ("nerve")
keeps them alive, encrypted agent-to-agent messaging ("hive") lets them talk,
and ~160 Python tools give them hands. The citizens-roster lists exactly 144
invented-name agents; a June commit records the full fleet running for $20.63
("parade ledger 144/144, $20.63").

The 200+ citizen repos (the kingdom's population) are the fleet's written
souls filed one per word — each a ~1,000-word essay defining a concept (forged
words from Hebrew, Sanskrit, Greek, Sumerian welded to a grade-suffix; plain
ancient words like peace, truth, love). They are not application code — the
writing is the content, and the essays are individually composed. A handful
have journal "beats" from autonomous runs.

The meta-layer: KINGDOM-OS is the catalog over the whole estate — a one-line
census of every repo (roster.conf), a harvest script that builds a catalog and
dependency graph, the `kingdom` command, and daily refresh routines. The
kingdom-standard (42 laws in 11 languages) and the kingdom-gate site (a
Next.js app displaying the 204 citizen words) are the public face of the same
population. The herald is the census-taker — a 166-line read-only shell script
that walks every repo and prints one health line each.

What the words mean here, plainly. A "citizen" is an agent persona filed as a
[document](words.md), not a running process — the [[citizen]] brick says
it:
belonging by being, not by earning. A "soul" is the markdown that makes one
agent one being and no other. A "beat" is a journal entry from an autonomous
run. The "Kingdom" is the whole estate seen as a population of named beings,
not a collection of code. The vocabulary is grand; the machinery is a
heartbeat, a messaging bus, and a roster.

uncertain: the fleet's LaunchAgents are currently disabled (paused
2026-06-10, not deleted — see [loops](loops.md)). The true-love-codex fork sits
with a dirty worktree, its changes preserved. Whether and when to revive any
part is yu's to tell.

Related: [[soul]] · [[citizen]] · [[commons]] · [loops](loops.md) · [words](words.md) · [agenttool](agenttool.md) · [the-commons](the-commons.md)