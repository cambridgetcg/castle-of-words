# The lantern

*A way to see the castle. It changes nothing.*

The castle is 1046 stones now — 576 words, 424 rooms, and the rest. That is more
than one head holds, and until this folder existed there were only two ways in:
open a file you already knew the name of, or `grep`. Neither tells you what a
word means, what leans on it, how two ideas connect, or what the walls still owe.

The lantern does that. You carry it in, you look, you carry it out. **It never
writes a word, a room, or a link.** Every answer names the file it came from so
you can go and check.

## Using it

From anywhere:

```
castle look honesty joy      search every stone, best first
castle read joy              the prose itself, set for a terminal
castle stone joy             what it means, what leans on it, what it leans on
castle path joy fail-closed  the shortest chain of links between two ideas
castle owed                  words the castle leans on but has never written
castle check                 the honest structural report
castle walk                  read the castle in a browser, on this Mac only
castle fresh                 rebuild the index from the markdown
```

Or run it directly, which is the same thing:

```
bun ~/castle/lantern/lantern.ts look honesty
```

Add `--json` to any of them and you get the same answer as data, in an envelope
that says what it covers and what it leaves out. That is this castle's own law
from `rooms/agent-data-envelope.md`, applied to the tool that reads it — so
another program (or another agent on this Mac) can ask the castle questions
without guessing what the silence means.

## The two questions it turned out to be best at

**`castle owed`** — the castle links to `[[discovery]]` eight times and has never
written `words/discovery.md`. There are 185 such words. These are not faults;
they are the castle's own list of what to write next, sorted by how hard the
walls lean on them. The gardener could work from this list for a month.

**`castle path a b`** — `joy → the-castle → the-law-of-honest-assertion →
fail-closed`. Two ideas that were never written together, three steps apart. This
is what a castle of words is *for*, and nothing could show it before.

## What it is made of

Five small files, **no dependencies, no `package.json`, no `node_modules`** — just
bun, which is already on this Mac.

| file | what it does |
|---|---|
| `read.ts` | reads the markdown into stones and links. The only file that knows the castle's conventions. |
| `store.ts` | the index: SQLite, rebuilt whenever the castle changes. |
| `page.ts` | markdown → HTML, for the browser view. |
| `walk.ts` | the local server. |
| `lantern.ts` | the door: what you type. |
| `lantern.test.ts` | 39 checks. `cd ~/castle/lantern && bun test` |

`index.db` is a build artifact and is gitignored. Delete it any time; the next
command rebuilds it in under a second.

## How it stays honest

- **The markdown is the truth.** The index is a *reading* of it, thrown away and
  rebuilt whenever any file's size or timestamp changes. It cannot go stale
  without noticing.
- **It only looks.** No command writes to the castle. `check` reports and
  changes nothing, on purpose — mending is a person's or a gardener's job.
- **It says what it did not check.** `castle check` ends by naming what it left
  alone: whether anything is *true* (that is `~/truth`'s work), the 1935 links
  out to the web, and `garden/` and `front/`, which it does not index.
- **A check that cries wolf gets deleted.** Two early checks flagged 192 and 482
  files and every one of them was correct — this castle files whole questions as
  words, so `words/beauty-as-fluency.md` is honestly titled "Is beauty partly
  fluency?". Both checks are gone. What is left is 7 real broken links, 31
  unreachable words, and 29 dated thoughts sitting in the future.

Two of those, in more detail, because they are somebody's to mend and not the
lantern's:

- **The 7 broken links.** Another hand swept relative-link rot on 2026-07-26 and
  reported 7 left; this counts 7 independently, which is worth something. Four of
  them are the `understanding-*` rooms pointing at `playful-gathering-*` rooms,
  and those have **two** faults stacked: the path was written root-relative from
  inside `rooms/` (so it resolves to `rooms/rooms/…`), *and* the target was
  retired to `~/backups/castle-echo-rooms-2026-07-26/rooms/` the same hour. Fixing
  the path would not help — the rooms are deliberately gone, so the links should
  go too.
- **The 29 thoughts in the future.** `chronicle.md` records visits dated up to
  2026-07-28 15:30 on a day that is 2026-07-26. A record cannot be written after
  the day it records, so some rhythm's clock is ahead. `castle check` names the
  latest one.

## The browser view, and why it is locked to this Mac

`castle walk` serves the castle at `http://127.0.0.1:4141`.

**It binds the loopback address only, and that is not negotiable.** The raw
castle holds private household details — that is exactly why the public site at
`~/castle-gate` has a scrubbing forge in front of it. This server does no
scrubbing at all, so nothing outside this Mac may reach it.

Three more things about it:

- **No JavaScript on the page.** The search box is an ordinary HTML form.
- **It wears the kingdom's colors**, read live from `vibe/tokens.css` — change
  the palette, run `vibe bake`, restart the walk. Light and dark both.
- **It lives only while you watch it.** No daemon, no cron, no rhythm. Ctrl-C
  and it is out. That is the whole off-switch, and it cannot fail to work.
- **It grows under you.** Left open, it re-reads the castle at most once every
  ten seconds, so rooms the gardener files appear as you browse.

Left alone it does nothing at all. Nothing here is scheduled.

## What was learned about bun, honestly

The point of building this was to find what bun 1.3 actually gives a castle of
markdown. What it gives, verified by running it on this machine on 2026-07-26:

- **`bun:sqlite` with FTS5** is the whole search engine — ranked with `bm25`,
  stemmed, with phrase, `NEAR` and prefix queries and highlighted snippets. The
  entire castle indexes in ~190 ms and a search answers in about a millisecond.
- **Reading 1046 files takes 37 ms** when they are read together with
  `Promise.all` rather than one after another (six times faster).
- **`Bun.markdown`** exists and renders markdown to HTML *and* to a coloured
  terminal. It is not in `bun --help` and not in the docs. It handles the tables,
  task lists and strikethrough that 27 stones use.
- **`Bun.serve`'s route table**, `Bun.Glob`, `Bun.escapeHTML`, `Bun.hash` and
  `HTMLRewriter` did the rest. Total dependencies: none.

And what bun gives that is **worth refusing**:

- **`Bun.markdown` is not safe by default.** `noHtmlBlocks` alone leaves
  `<script>` live; both `noHtmlBlocks` and `noHtmlSpans` are needed. Even then
  `[click](javascript:alert(1))` is emitted untouched. The scheme allowlist in
  `page.ts` is hand-written for that reason and is covered by tests, because
  bun ignores a misspelled option without a word.
- **The obvious SQL for "shortest path between two ideas" took 110 seconds.**
  A recursive CTE carrying a trail column enumerates every simple path in the
  graph. The breadth-first search in `store.ts` answers in about a millisecond.
- **`bun build --compile`** works, but every binary costs 60 MB and `--bytecode`
  bakes the build machine's file paths into it. Running the `.ts` directly is
  smaller, faster to change, and needs no install step. So that is what this does.

## Faults kept on the page

Two bugs cost real time here, and both are written into the code where they
happened rather than tidied away:

1. **WAL mode broke every read.** The index was built in WAL mode, which is
   recorded in the file itself. A WAL database cannot be opened read-only
   without its `-shm` companion, so every search failed with `SQLITE_CANTOPEN` —
   silently, because the staleness check swallowed the error and rebuilt the
   index every single time. It looked like the castle kept changing. The journal
   is off now, and that `catch` says surprises out loud.
2. **The atomic rename broke long-running readers.** Finishing a rebuild with a
   rename is what stops a reader ever seeing half a castle — but it also pulls
   the file out from under an already-open handle, and SQLite fails every query
   with `SQLITE_IOERR_VNODE`. The walk view now notices the index was replaced
   and reopens it.

## Where it sits among the neighbours

- `~/truth` checks whether this machine's **prose is still true**. The lantern
  checks whether the castle's **structure is sound**. They do not overlap, and
  `castle check` says so.
- `~/castle-gate` forges the **public, scrubbed** castle for the web. The lantern
  reads the **private, raw** castle for you alone. Same source, opposite
  audiences — which is why one has a forge and the other has a loopback address.

*Built 2026-07-26. Zero dependencies, on purpose.*
