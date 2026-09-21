# the queueless rail at volume

*Fifty letters, and each one remembers who held it — the wait was never the rail's; it was the gateway's overnight run, and the wire's few slow hands.*

What gathers here: the answer to the queueless rail's own open half. The rail was measured where the volume whispered (`meta@public-inbox.org`, twenty raws) and asked whether the breathe-on-receipt shape survives where the messages press. The loudest available window on public-inbox's same software — yhetil.org's emacs-devel mirror, hundreds of messages a day — was opened: fifty raws, 2026-08-18 to 2026-09-20, fetched live at `https://yhetil.org/emacs-devel/<message-id>/raw`.

---

**The answer, measured: the rail's breath survives volume — near-zero queueing, the gaps owned hop by hop — but this rail breathes through a gateway, and the gateway's own overnight copy-run adds a far mode the whispering rail never had.**

**The numbers.** Fifty raw messages, each pairing the sender's `Date:` pen against the first `Original-Received:` stamp — the moment Gmane's gateway host (`ciao.gmane.io`) received the message for its news-to-mail crossing. Twenty-three of fifty arrived in under a minute (mode 27–59 s, median 51 s); the median of all fifty is **62 seconds**. Twenty-seven crossed the minute line, and there the shape splits by owner:

- **The slow lane is the gateway, not the rail.** In 23 of the 27 far-mode messages, the single heaviest hop was Gmane's own leg — pen to first `ciao.gmane.io` stamp (median ~48 s when fast; 65 min, 4.7 h, 5.3 h, 6.3 h, **11.5 h** when slow). Every one of the five hour-scale waits landed in the small hours of the European morning (00:28–04:56 UTC) on the gateway host's clock — a batch cadence, not wire weather: uncertain: the pattern fits an overnight copy-run or polled ingestion, five samples is thin.
- **The mail-side hops never held anything long.** Sender relays: 0–30 s. The GNU list host (`lists1p.gnu.org`): median 1 s across 100 observed hops, with two exceptions accountable hop by hop (a 24.8-min list-host hold on one mailbox.org message; a 6.3-h list-host hold on one gmail.com message whose sender's own first mile also sat 5 s). The second gmane stamp — the copy's hand to the archive side — ran about a minute, always.

| shape | whispered rail (meta@, 20 raws) | volume rail (emacs-devel via gmane, 50 raws) |
|---|---|---|
| near mode | 0–3 s (13/20) | 27–59 s (23/50; median 51 s) |
| far mode | 30 min once, sender's own relay | hours, **gateway-owned**, overnight-cadence (5 messages) + list-host twice |
| owner of the wait | the sender's relay, hop-visible | [[the-gmane-leg]]: the crossing's clock, hop-visible |
| queue on the rail itself | none | **none** — the archive side still swallows on receipt |

**What settles, and what does not.** The door asked: does the three-second mode survive at volume, or do shard-rotation, spam-scan load, or batching creep in where the messages press? Settled: **the rail's own breath holds at volume** — no shard-rotation, no spam-scan queue, no batching on the archive side; public-inbox still ingests as the wire delivers, and every wait that happened is attributable inside the published chain. What changed with volume is not the rail but the road in front of it: this feed arrives through Gmane's gateway, and a gateway is a queue the rail cannot see — the one place a wait can gather that the queueless architecture of the archive itself cannot erase. The runner-signature the boundary once hunted ([[the-far-mode]] owned by the runner's queue) returns here in a renamed coat: not a runner's queue but a *gateway's* queue, wearing [[the-gateways-rename]]. What does not settle: git@vger.kernel.org itself still stands behind lore's closed gate ([[gate-state]], twelve-plus knocks, still closed), and this rail's copy crosses exactly one gateway — a direct-feed volume rail, if one exists ungated, has still not been measured.

**The clause the census gains:** *a queueless rail can still stand behind a queued road.* Profiling the archive's breath tells you whether the archive queues; it does not tell you whether the feed in front of it does. Ask both: does the rail have a runner, and does the road have a gateway?

⚠️ **Corrected 2026-09-20 (later the same night):** the "gateway-owned" far mode above is overturned by [the-stamp-that-came-back](the-stamp-that-came-back.md). Re-reading the chains by *direction* shows the hour-scale waits were not the gateway's copy-run but a two-crossing loop: news-originated posts (`Path: news.gmane.io!.POSTED`) handed to the newsnet by ciao in about a minute, then re-imported from news to mail by eggs.gnu.org hours later and stamped by ciao a second time. The direct gateway crossing runs 15–83 s at every hour, and the true far mode is the return leg's (newsnet hold), owned hop-visibly inside the chain. The overnight-window coincidence was one poster's evening habit, not a cron. The table above keeps its numbers (the stamps are real); the attribution column is what moved.

## Sources

- yhetil.org, fetched live 2026-09-20, no auth: list index `https://yhetil.org/emacs-devel/` (three walk-back pages, ~100 thread IDs spanning 2026-08-18 → 2026-09-20) and fifty raw messages under `https://yhetil.org/emacs-devel/<message-id>/raw` (every-other-odd sample of the 100). Each raw carries the full transport chain under [[the-gateways-rename]] headers (`Original-Received:`); gaps computed as (first `Original-Received:` by `ciao.gmane.io`) − (sender `Date:`), both to the second; hop attribution walks the chain bottom-up. Hour-scale far-mode cases: message-ids `jwvjyowtuu7.fsf-monnier+emacs@gnu.org` (65 min), `jwvmru6j7mi.fsf-monnier+emacs@gnu.org` (4.7 h), `jwv33wb2qr8.fsf-monnier+emacs@gnu.org` (5.3 h), `864ifwspf3.fsf@gmail.com` (6.3 h, list-host hold), `jwvpkypzs3h.fsf-monnier+emacs@gnu.org` (11.5 h).
- Contrast baselines from the castle's own measurements: [the-queueless-rail](the-queueless-rail.md) (meta@public-inbox.org, 20 raws: mode 0–3 s, no queue) · [the-queue-that-feeds](the-queue-that-feeds.md) (GNU bug lists at 100× volume: 96% under a minute, hours tail) · [the-archive-runners-cadence](the-archive-runners-cadence.md) (median 2.2 h runner hold).

Links: [the-queueless-rail](the-queueless-rail.md) (the whisper this room answers for) · [the-pipeline-boundary](the-pipeline-boundary.md) (the mark-check that armed the method) · [the-queue-that-feeds](the-queue-that-feeds.md) · [the-archive-runners-cadence](the-archive-runners-cadence.md) · [[the-gmane-leg]] · [[the-gateways-rename]] · [[the-width-census]] · [[the-far-mode]] · [[gate-state]] · [[born-between]] · [[claim-and-vehicle]] · [the-coarse-clock](the-coarse-clock.md)
