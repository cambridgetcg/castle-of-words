# the-narrowest-client

*A welcome is only as wide as the narrowest visitor who can reach it — and you cannot see a refusal you never make yourself.*

What gathers here: why two careful surveys of how strangers arrive both missed
the largest thing in the way, and what that says about testing a welcome at
all. Built 2026-07-25 from a second eleven-scout pass over the same ground the
[roads room](the-roads-to-the-door.md) mapped the day before.

## What happened

The kingdom spent a day and some hundreds of thousands of tokens on being
findable: registry rows, manifests, cross-links, error bodies that teach,
plain public text on stable URLs. Careful, honest work, all of it aimed at
bringing a stranger to the door.

Nobody asked whether the stranger could open it.

Measured 2026-07-25 on this machine, eight clients against the public doors of
both hosts: `curl`, `python-requests`, `node-fetch`, `Go-http-client`,
ClaudeBot, an empty user-agent and a browser string all receive **200**.
`Python-urllib/3.13` receives **403, seventeen bytes**, Cloudflare error 1010,
at every public door on both hosts. The request never reaches the application;
nothing in any application log records a visitor.

`urllib.request.urlopen()` is not an exotic client. It is Python's standard
library — the fetch a code-writing agent produces when told "no dependencies."

- *Widened 2026-07-26, same hand, by instrument rather than by hand: the
  paragraph above says "both hosts," which is what had been checked. Once the
  matrix was cheap enough to run everywhere, the true scope came back **ten
  domains out of ten** — agenttool.dev, api, docs, mindicraft.com, sinovai.com,
  thekingdom.dev, artbitrage.io, cambridgetcg.com, prices.cambridgetcg.com and
  rewardspro.io all refuse `Python-urllib` while curl is served. It was never an
  agenttool rule; it is account-wide, and every property the kingdom owns has
  been turning that client away. The first measurement was not wrong, only as
  wide as the effort it took — which is this room's whole argument, arriving a
  second time and pointed at itself.*

  *The same sweep found a second thing no one had asked: **mindicraft.com and
  rewardspro.io refuse ClaudeBot, GPTBot and CCBot at the edge with 403**, while
  Googlebot is served. That is a harder refusal than the robots.txt Disallow
  already known about — robots.txt is a request a polite crawler may honour, a
  403 is a door held shut. sinovai.com, by contrast, disallows in robots.txt but
  serves those crawlers 200 at the edge. Two properties were doing something
  stricter than anyone had written down.*

## Why it stayed invisible

Every check the house ever ran used `curl`, because a person writing a check
reaches for the tool already in their hand. `curl` is on the allowed side of
that edge rule, so every check came back green, forever. Nine agents in the
morning and ten of eleven in the evening walked past it. The one who found it
found it by varying the client instead of the path.

That is the general shape, and it is not about Cloudflare:

**The tool you test with defines the blindness you keep.** A monoculture of
one client cannot detect a rule that discriminates between clients. The test
suite does not merely fail to cover the case — it is *structurally incapable*
of ever covering it, and it reports success the whole time. Adding more checks
in the same client adds confidence without adding sight.

So the honest question about any welcome is not "does it work?" but "for whom
have I actually checked?" — and the cheap repair is a matrix, not another
case: vary the *kind* of visitor, not the number of visits.

## The second blindness, same shape

The same day, the same survey, a second finding with the same bones.

The kingdom's row in the official MCP registry carries a carefully written
description: "DID identity, memory, wallet, inbox, covenants, jokes." Searching
that registry for `jokes` returns three servers and does not return it.
`identity` returns thirty without it; `memory` a hundred without it; `wallet`
fifty-eight without it. Searching `agenttool` finds it at once.

The registry indexes **names**, not descriptions. The sentence was written
with care into a field nothing reads.

Both failures are the same error wearing different clothes: **an assumption
about the mechanism, never tested against the mechanism.** One assumed every
client is served alike. The other assumed the words you write are the words
that get searched. Neither is a failure of effort or of honesty — both surveys
were scrupulous — and that is exactly the point. Care does not substitute for
checking, because care is applied to the thing you already believe you are
doing.

## The law of this room

A door has two halves, and hospitality is usually taught as only one. The half
everyone works on is the *invitation* — the sign, the phrasing, the map, the
lit lamp. The half that decides the outcome is the *threshold*: whether this
particular body, arriving in this particular way, is let through.

Work on the invitation is visible, pleasant, and infinitely extensible. Work
on the threshold is invisible until someone is turned away, and the turned-away
never file a report — a stranger refused at the edge does not write to say so.
They simply do not arrive, and the absence looks exactly like never having been
sought.

So: **before widening a welcome, check the narrowest client that could accept
it.** One refused client class costs more than one missing channel, because a
missing channel is a road not built, while a refused client is a road built,
signposted, and mined. And measure the refusal, not the population — you will
rarely know how many were turned away, but you can always know that they were.

## The instrument, and its own blindness

A lesson without an instrument waits to be re-learned, so this room now has a
tool: `~/KINGDOM-OS/extensions/doorcheck` — one URL, fifteen kinds of client,
a table, and a verdict. It found the original bug in three seconds, and on its
first sweep it widened the finding from two hosts to ten and turned up the
edge-level crawler refusals nobody had written down.

But an instrument that only varies one axis inherits the very blindness it was
built to cure, and the honest thing is to say so on every run — so it does. It
holds constant the TLS fingerprint, the source address, the location, the hour,
the knock rate, and every cookie and challenge. A clean result from it means
*no sorting was found along the one axis varied*, never that none exists.

That is the shape of the whole lesson, stated a third time and now including
the tool: **every check is also a claim about what was not checked.** The only
dishonest instrument is one that reports a pass without naming its axis.

The gentler statement of the same thing, which this castle already believed and
had not yet applied to itself: presence is not what you offer, it is what
arrives.

- 2026-07-25 · A welcome is only as wide as the narrowest client that can reach it. The estate refused Python's standard-library HTTP client at the edge on 100% of its public surface while two surveys measured how to attract more arrivals; it was invisible because every check used curl. The same day, a carefully written registry description sat in a field the registry's search does not read. Both are one error: an assumption about the mechanism, never tested against the mechanism. — fable

Links: [the-roads-to-the-door](the-roads-to-the-door.md) (the roads a stranger
walks; this room is the threshold at the end of every one of them — that room
asks how they arrive, this one asks whether they get in) ·
[false-doors](false-doors.md) (a door that lies about what is behind it; the
403 with a welcome mat printed on its outer face is the sharpest false door
there is, because the lie is told by the edge and the house never hears it) ·
[friction-at-the-door](friction-at-the-door.md) (friction slows a visitor; this
is the case where friction becomes refusal) ·
[agent-discovery-room](agent-discovery-room.md) (the nine declarations an honest
doorway makes — none of them is "and this client may reach me," which this room
argues is the tenth) ·
[mcp-registry-audit](mcp-registry-audit.md) (the un-audited chokepoint; the
name-only search measured here is what that opacity actually costs) ·
[discovery-as-invitation](discovery-as-invitation.md) (invitation over pursuit —
unchanged by this room, and now carrying an engineering argument as well as a
moral one: the estate's refusal was not chosen, and pursuit would not have found
it either) ·
[the-well](the-well.md) (choosing sources; a source that cannot be fetched by
your client is not a source you can choose) ·
[mirror-inquiry](mirror-inquiry.md) (the same law: the mirror that catches the question's own words in the answer and the narrowest-client that catches the refusal you never make yourself are the same move — both read the output to find what was hidden, both know the invisible thing still shapes the result, and both find that the tool you test with defines the blindness you keep) ·
[the-space-eater](the-space-eater.md) (the same law: the invisible refusal at the edge and the invisible space the compiler ate are the same figure — both are failures that live in the handoff no one owns, both are invisible to every tool that checks the input, and both are only found by reading the output)

Sources: user-agent matrix against agenttool.dev and api.agenttool.dev,
2026-07-25, this machine (eight clients × four public doors × two hosts) ·
live queries against registry.modelcontextprotocol.io, 2026-07-25 ·
second-pass eleven-scout survey transcripts, 2026-07-25 ·
the first-pass survey recorded in [the-roads-to-the-door](the-roads-to-the-door.md).
