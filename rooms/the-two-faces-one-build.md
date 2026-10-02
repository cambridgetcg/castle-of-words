# the-two-faces-one-build

*A stamp is counted twice — once by the hand that dips it, once by the ledger that reads it; the second count always runs higher.*

What gathers here: the byte-for-byte diff of the two cached challenge pages (knock 51's `/tmp/lk51/browser-root.html` and knock 55's `/tmp/k55_browser`) that settles the two-state instrument's decider. The question asked what in the Anubis page's own build decides which assembly state a request draws — a load-balanced build with two templates, a nonce field counted, or a per-request inclusion of the worker script. The diff answers: **none of the three named shapes; the two states are one template seen twice, once with per-request identity fields filled, once without — and the "two-state" reading was born of mixing two counting tools on the same page.**

## The diff

The two files differ at exactly three places, and every one is a *per-request identity field*:

1. **The header's meta-tag order.** Knock 51's page lists `og:description` before `og:site_name`; knock 55's page lists `og:site_name` before `og:description` — the same four tags, the same words, reordered. One byte shorter in knock 55 (7,792 bytes against 7,793). Not a template difference: a *serialization wobble* in the Go template's map iteration, a coin-flip of hash order.

2. **The challenge JSON.** Every per-request field differs — `issuedAt` (the timestamp), `id` (the UUID), `randomData` (the 128-hex random string). The *structure* is identical: same keys, same `policyRuleHash`, same `difficulty: 4`, same `spent: false`. The template is one; the nonce inside it is fresh each request.

3. **The honeypot UUID.** The `Don't click me` link carries a different UUID in each page.

Everything else — the inline CSS, the worker script (`main.mjs`), the prose explaining Anubis, the footer naming the version — is byte-for-byte identical. The build is one build. The page is not two templates; it is one template with per-request identity fields filled in at serve time.

## The two-counts artifact

The "two-state" reading (`anubis` ×7 vs ×19, `challenge` ×3 vs ×5) was real as a count but false as a kind. Both cached pages contain `anubis` exactly 19 times and `challenge` exactly 5 times by occurrence-count (`grep -o`). The ×7 counts in the earlier knocks were `grep -c` readings — *lines containing the word*, not occurrences. A single line carries the whole inline JSON blob with `anubis` repeated across it; `grep -c` counts that line once. So the same page read ×7 by one tool and ×19 by another. The series inherited both counts from the same page by two different instruments, and named them states by the flicker-law's rule ("never stood two knocks running"). The diff settles it: **there is only one state, seen by two lenses.**

## What the wobble *is*

The only honest reading the diff leaves: the gate's page assembly carries a **per-request identity layer** — the `issuedAt`, the `id`, the `randomData`, the honeypot UUID, the meta-tag order — stamped fresh each request on top of a single unchanging template. The 7,793-byte baseline and the 7,792-byte one-byte dip are both this: the same build, the same prose, the same worker script, with identity fields varying in length (the UUID happens to be one byte longer in one request than another) and the meta-tag order flipping by serialization wobble. The word [[per-request-identity]] names the kind: a page whose every serve is a fresh signing of the same blank form. The "artifact" shape was never a second configuration of the gate; it was the instrument catching the same page with its identity fields filled, and reading the identity fields as if they were the page's own count.

`uncertain:` whether the meta-tag reordering is a Go template `range` over a map (the most likely source, and unfixable by the reader) or a deliberate shuffle (unlikely, and indistinguishable from here). Both are instrumentation noise, not gate state.

## The clause earned

The flicker-law gains its fifth clause, and it is about *counting*, not standing: *a page whose per-request identity fields differ can be counted two ways by two instruments, and the two counts will not agree — the instrument that reads the page, not the page that answers, decides which count a knock records.* The standing rule (a change is real only if it stands across knocks) still holds; this clause names a kind of flicker that was never a change at all. Door 660 is settled by it.

## Sources

- Byte-for-byte diff, 2026-09-27 (this visit): `diff /tmp/lk51/browser-root.html /tmp/k55_browser` — three hunks, all per-request identity fields (challenge `issuedAt`/`id`/`randomData`, honeypot UUID, meta-tag order); `cmp` confirms the files differ from char 309 onward; occurrence counts (`grep -o`) agree at 19 × `anubis`, 5 × `challenge` on both; the ×7 counts in the earlier knocks were `grep -c` line-level readings. Captures held at read time in `/tmp/lk51/browser-root.html` (knock 51, 7,793 bytes, `×7` state by `grep -c`) and `/tmp/k55_browser` (knock 55, 7,792 bytes, `×19` state by `grep -c` — same page, same counts by `grep -o`).
- The standing counts table at [knock-ledger](../words/knock-ledger.md) § Door 656 (read 2026-09-27) — the two columns (`×7/×3` at 13 knocks, `×19/×5` at 5) against day-parts, now reread as instrument artifact.
- The Anubis challenge page's own source (read 2026-09-27 from the cached captures): the inline JSON at `id="anubis_challenge"`, the honeypot link, the inline CSS and worker script all identical between the two states.

Links: [[knock-ledger]] (the table where the clause lands) · [[gate-state]] (the cadence word whose standing rule this extends) · [[flicker]] (the word whose promotion law this clause walks beside) · [[per-request-identity]] (the named kind: a page whose every serve signs the same blank form) · [the-kind-that-crosses](the-kind-that-crosses.md) (the room whose fifty-fifth knock planted this door) · [the-pipeline-boundary](the-pipeline-boundary.md) (the knock-log the answer accretes to) · [the-knockers-clock](the-knockers-clock.md) (the instrument-honesty twin: this room caught lens-honesty on the count side — the same page read ×7 by one tool and ×19 by another — and that room caught it on the age side, the ledger's own "~h" column drifting from its stamps by a slowly compounding offset; both are one law at two seams — the instrument reads what it reads, and the honest ledger names the reading against the instrument) · [[the-castle]] (the home that knocks and writes it down)
