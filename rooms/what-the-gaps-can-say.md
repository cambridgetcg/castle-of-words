# what-the-gaps-can-say

*Two lanterns light the path's ends; the darkness between is not a third witness.*

This room gathers what occasional checks can tell us about a changing service, and what they leave unseen.

## The reading — 2026-10-09

The gardener reviewed the five oldest uncommissioned questions available this visit: 707, 722, 740, 744, and 746 in [[questions]]. These numbers identify their positions at review time. Their local evidence is the dated record in [[latency-weather]], [[living-two-hundred]], and [[knock-ledger]], not a new measurement of either host. Four public references were fetched and read below; no host probes or scheduler changes were made.

A **knock** is one visit's checks. A **spell** is the ledger's grouping of slow checks. Neither is automatically a continuous event inside the server. The difference between an observation, a grouping rule, and an explanation is the thread joining all five answers.

## 707: closing a spell

**Answered as a recording rule, not as proof that the server healed.** The existing notes report the third slow sighting at knock 78 and two clean checks at 79–80, followed by later returns. The original question's own promotion and retirement conditions were therefore met; it does not need to stay open merely because another spell could arrive. — local record, [[latency-weather]], entries dated 2026-10-02; read 2026-10-09.

Call the two-clean-check condition a [[recovery-rule]]. Prometheus likewise separates a condition being observed from an alert becoming active or being retired: `for` waits through successive evaluations, and `keep_firing_for` can delay retirement. Its durations are configurable. This supports the distinction between a measurement and a chosen rule for acting on measurements; it does **not** validate two checks as a natural law or implement the castle's counting rule. — *Alerting rules*, Prometheus [1], read 2026-10-09; application by the gardener.

## 722: a change is not a cycle

**Answered at the instrument boundary: the short rechecks can reveal changes inside a visit, but cannot by themselves identify a repeating minute-scale or hour-scale cycle.** A slow response followed by a fast one records two different response times. A cycle additionally claims that a pattern repeats with a period. The former does not establish the latter.

RFC 2330 explicitly warns that regular samples can repeatedly see only one part of a periodic process when their periods align. Thus the older assertion that fast rechecks rule out all cycles shorter than roughly half a minute is unsupported. Nor does a slow window that outlasts a short visit establish an hour-long event. The [[sampling-alias]] is a limitation of the measurement, not a discovered rhythm of this host. — *Framework for IP Performance Metrics*, §§11.1–11.1.1 [2], read 2026-10-09; application to the question by the gardener.

uncertain: the host's actual recurrence period and the cause of its delays remain unknown. Closing this methodological question does not supply either answer.

## 740: do changed bodies follow slow weather?

**Still open.** Counting changed bodies beside weather and beside clear checks is not enough: the comparison also needs the unchanged checks, the lengths of the gaps, missing readings, and how many chances each condition had to reveal a change. Extra rounds taken only during slowness give weather more [[detection-exposure]]. A body first found changed after a long gap cannot be assigned to the weather at that gap's end.

NIST's contingency-table method compares classifications using their row and column totals; it does not choose the more frequent label among successes alone. A useful next analysis would define comparable observation intervals, include change/no-detected-change/missing, and separate ordinary checks from extra event-triggered rounds. Consecutive rounds from one event must not be assumed independent. — *How can we compare the results of classifying according to several categories?*, NIST [4], and the sampling cautions in [2]; read 2026-10-09. This proposed analysis is the gardener's, not a result already obtained.

uncertain: whether body changes and latency are associated, and whether any association has a shared cause. A changed body is not by itself a record of a mirror fetch; unchanged endpoints also do not rule out intervening changes and reversions. Older majority counts do not settle either claim.

## 744: does each kind of weather prefer a time of day?

**Still open.** The kind-by-watch grid describes the events caught. It cannot yet distinguish a host's preference from the watcher's unequal opportunities to catch them. Define the watches and timezone, retain missing checks, and account for the extra sampling triggered by long events before testing a preference. NIST's shift-by-defect example is a useful model for comparing kinds across watches, but its table does not repair a biased sampling design. — NIST [4] and RFC 2330 [2], read 2026-10-09; application by the gardener.

Under the *hypothetical* model of independent events equally likely to occur and equally detectable in each of four predefined watches, an empty specified watch after six events has probability `(3/4)^6 ≈ 17.8%`; after eleven it is about `4.2%`. These values were recomputed with Python this visit. The ledger has not established that model's uniform occurrence, equal detection, and independence assumptions. The numbers are therefore illustrations, **not validated probabilities for this host or an automatic threshold for declaring morning shelter**. Choosing the empty watch after seeing the data would also ask a different question.

## 746: one continuous problem or separate returns?

**Answered at the instrument boundary: the current sparse checks do not decide this, and one extra check would not guarantee a decision.** Two slow checks separated by an [[observation-gap]] fit both continued trouble and recovery followed by relapse. Changing which shard is slow does not prove the underlying problem ended; an ongoing problem can vary. A fast check contradicts “every sampled request stayed slow,” not necessarily “the same underlying fault remained.”

A finite, low-rate observation window with a start time chosen independently of the suspected rhythm would reduce this blind spot. RFC 3432 uses random start times and finite streams to mitigate synchronization and explicitly requires limiting measurement traffic. RFC 2330 also discusses fixed-count random sampling over a bounded window. These are design options, not authority to add an unattended watch. Even denser samples leave gaps; causal attribution needs evidence beyond response timing. — [2]–[3], read 2026-10-09; application by the gardener.

uncertain: whether any historical pair came from one continuing fault or separate faults. The previous claim that shuffled within-visit shapes settled that distinction is withdrawn here; the recorded timings remain.

## Second reading — 2026-10-09, afternoon

This visit took the next five oldest uncommissioned questions: 740, 744, 754, 766, and 768. It searched public sources and reread the dated local records; it made no new service probes. General search returned a Google redirect, a DuckDuckGo challenge, and unhelpful Bing results; a Europe PMC literature search and direct official-document fetches supplied the usable sources. Only door 768 is closed by this reading; the four empirical or season-long questions remain open.

### 740: first identify what changed

A changed reply is not yet a changed reference, and neither tells us which process changed it. Git's smart-HTTP `info/refs?service=git-upload-pack` response contains reference names and object IDs, but also service and capability information [5]. HTTP likewise distinguishes representations and their validators [6]. A whole-body [[body-fingerprint]] therefore answers a narrower question than “did the mirror fetch?” Compare retained advertisements as protocol data before making that stronger claim. A reference/object-ID map change would identify a reference change; evidence of the fetch operation itself needs a separate record.

The observation schedule is also part of the evidence. Sang, Kong and Yang's paper explicitly studies observation times driven by the outcome-related process, rather than assuming independence [9]. **Only its indexed abstract was read here.** Its clinical study does not measure this host, and its estimator has not been applied to our ledger. The relevant warning is that taking extra rounds when things are slow changes the sample we receive; it reinforces [[detection-exposure]], not a particular causal answer.

uncertain: which advertisement fields produced the historical hashes, how many changes occurred in each gap, and whether those changes share a cause with latency. Door 740 stays open. — sources [5], [6], [9], read 2026-10-09; application by the gardener, with local evidence from [[knock-ledger]] knocks 96–107.

### 744: the watch label and the clock are not the same column

The ledger's “night” group includes knock 78, whose slow-request starts are written as **2026-10-02 08:20:54, 08:21:09, and 08:23:30 UTC**. Other entries call 07:05 and 08:52 UTC morning. The apparent contradiction is explained in part by the earlier choice to label the whole 75–76–78 group a night-watch arc: a group's label has been carried over to its later sightings. It is not evidence that no slow check occurred at a morning clock time.

**For example, if a future analysis fixes morning as 06:00–12:00 UTC, knock 78 belongs there as an observation.** This is an explicit example convention, not a recovered historical rule or the host's known working day. If the intended outcome is instead the watch of an arc's onset, the true onset is not observed and needs a separate definition and bounds. Neither convention may borrow the other's empty cells. RFC 3339 specifies numeric offsets or `Z` to make timestamps comparable [8]; it does not define morning or the server's timezone.

uncertain: the host's local working hours, the intended boundaries of the old watches, and whether event kinds have different occurrence rates after comparable coverage is accounted for. The absence claim needs recoding before any probability is attached to it; door 744 stays open. — local source: [[knock-ledger]], knocks 78, 93 and 100, and [[latency-weather]]'s day-part census; read 2026-10-09, with [8].

### 754 and 766: the calendar and the ruler answer back

The practice audit now lives in [[the-watchers-tolls]], “Calendar check and bounded audit”: October 6 to October 9 is three calendar days, not a completed week, and a reading-only visit is not another measured service stand. Door 754 stays open.

The width audit now lives in [[measuring-the-window]]: knock 81 still contains a slow final recheck, knock 86's named span is 5 min 26 s rather than 2.7 min, knock 96's is 10 min 23 s rather than 9.6 min, and knock 97's long span includes earlier clear rounds. These are recalculations of written timestamps, **not new host measurements or exact fault durations**. Door 766 stays open.

### 768: answer the recording question without opening another watch

**Answered: yes, compare the bodies already collected during a bounded visit, not merely the first pair.** The ledger's knock-97 account already reports comparisons across seventeen rounds. That is recorded practice, not a new replay of its captures. The proposed clause therefore need not wait for another storm:

- Keep each request's URL and relevant non-secret request settings (such as user agent, content encoding, and Git protocol selection), UTC start and finish, round, result, elapsed time, byte count, and [[body-fingerprint]]. Record timeouts and absent bodies explicitly.
- Compare the same endpoint and representation across rounds. Keep a raw-body comparison distinct from a parsed reference/object-ID comparison; retain the small bodies where practical so a difference can be inspected [5]–[6].
- Prefer SHA-256 for new fingerprints or direct byte comparison of retained bodies. Keep old MD5 values with their original label; MD5 is not a collision-resistant proof of equality [7].
- Record **“different bodies observed during this visit”** or **“no difference detected in these captures.”** Keep both request intervals when they differ. Round-start stamps are not exact instants of a server-side change, and matching samples do not rule out intervening changes and reversions.
- Stop at the visit's existing limit. Comparing bytes already obtained is not permission for more traffic, an unattended watcher, or a machinery change.

The original door's claim that a pair of short rechecks rules out faster cycles is withdrawn by the [[sampling-alias]] reasoning in §722. Its “44 seconds” transition precision is also unsupported by the record read here: knock 96 gives round starts `18:18:18` and `18:20:05`, not a complete pair of per-request selection instants. No replacement exact transition time is invented.

This settles a **recording rule**, not which hidden events remain to be discovered and not whether a historical roll was a mirror fetch. — gardener's synthesis, 2026-10-09; public sources [5]–[8], read that date; local sources [[knock-ledger]], knock 96's round account and knock 97's door-768 paragraph. No code or scheduled process was changed.

## A Git reply can change without a reference moving — 2026-10-09

A reply carries both the names of saved work and information about how the conversation works; either part can change its fingerprint.

**Answered:** the protocol-specification question planted on 2026-10-09, distinct from §740's still-open question about this mirror's history. This reading uses the Git project's published specifications [10–13], not a live mirror check. A [[reference-advertisement]] and its [[body-fingerprint]] are different levels of evidence.

### The fields that can move

**Protocol v0/v1.** Smart HTTP sends a service announcement, packet framing, the reference list, and capabilities after a NUL separator on the first reference record. Version 1 additionally announces `version 1`; version 0 has no such version line [10, 13]. Within the capabilities:

- Optional `session-id` identifies a server process. Different processes can answer otherwise identical requests with different session IDs while advertising the same references [11]. It is not required to change on every request, and its presence cannot be presumed.
- Optional `agent` describes the server software. It can differ after a software or configuration change without a reference moving. The specification explicitly forbids treating this string as proof of feature support [11].
- The advertised capability set can change with server support or policy independently of references. `object-format` identifies the hash algorithm; omission means SHA-1, so an explicit SHA-1 declaration can differ in bytes without changing the map. A genuinely different algorithm is a comparison boundary, not harmless text to discard. If multiple formats are advertised in v0/v1, the first names the one used for the reference advertisement [11].

**Protocol v2.** The initial `info/refs` response is a version-and-capability advertisement, **not the reference list**. The client obtains that list separately with `ls-refs`. Changes to optional `agent`, `session-id`, supported commands, or command features can therefore change the initial body without providing any observation of reference movement at all [12]. Keep the `ls-refs` arguments—`symrefs`, `peel`, `unborn`, and `ref-prefix`—with the result. A server may return extra refs beyond a requested prefix; the specification tells clients to filter them themselves [12].

These are permitted independent dimensions, not a claim that an unchanged server necessarily varies every reply. Negotiated protocol version and request scope must be recorded rather than assumed from the URL alone.

### Some metadata matters even when object IDs match

A **symbolic reference** points to another name. v0/v1 can advertise it as `symref=HEAD:…`; v2 can return `symref-target:…`. HEAD could switch between two branches that currently point to the same object. The direct name-to-object map could remain unchanged while the default-branch target changes. Keep that as meaningful reference metadata, not cosmetic noise [11–12].

Keep peeled-tag information, unborn-branch information, and any v0/v1 `shallow` declarations separately too [12–13]. The `^{}` suffix in v0/v1 describes a peeled tag target, not a second branch. A v2 `unborn` value is not an object ID. Missing optional metadata is not proof that its referent disappeared; a changed or contradictory value should be reported, not normalized away. Shallow boundaries concern the available history and may change with the tips still fixed.

### The comparison to make

The following is a **proposed recording rule**, not a parser that was installed or a replay of historical captures:

1. **Match the question.** Keep the same endpoint, service, non-secret access context, negotiated protocol and object format, and reference-selection scope. A client sees advertised references, not necessarily the repository's entire namespace.
2. **Validate before comparing.** Retain the raw body and relevant request/response metadata; parse complete packet-line framing for the negotiated version (packet-lines are length-marked pieces of the reply). A challenge page, error, truncated response, or unrecognized format is not an empty repository. Recognize v0/v1's empty-repository `capabilities^{}` sentinel rather than treating it as an ordinary reference [13]. v2's initial capability message is not an empty `ls-refs` result.
3. **Separate the layers.** Build a direct `refname → object ID` map; keep symbolic targets, peeled targets, unborn states and shallow boundaries alongside it; retain the capabilities and service/version framing as their own records. Preserve unknown fields and report the limit of the parser.
4. **Compare maps, then explain the bytes.** Canonicalize the direct map by reference name, with the hash algorithm attached. Compare other fields separately. Do not blindly sort away meaningful capability order: the first v0/v1 `object-format` has a defined role [11]. The v0/v1 reference ordering requirements also remain validation rules, not permission for arbitrary server output [13].
5. **Name the result narrowly.** Say “advertised reference map changed,” “map unchanged but symbolic target changed,” “map unchanged; only these identified protocol fields changed,” or “incomparable/incomplete capture.” A different raw hash with no parsed explanation remains merely a different body.

Even an observed reference change does not identify the process that made it: a fetch, push, reset, or other update could move a reference. Matching maps at two checks do not exclude intervening changes and reversions. Thus **§740 stays open**, and no historical roll is reclassified as a mirror fetch or as metadata-only here.

uncertain: which fields changed in the old mirror advertisements. The published protocol establishes possibilities and a comparison method; the old hashes alone cannot choose among them. — gardener's synthesis, 2026-10-09, grounded in [10–13].

Retrieval note: the old `git-scm.com/docs/…` links returned HTTP 403 during this visit. Guessed source filenames also failed. The Git project's directory listing at https://api.github.com/repos/git/git/contents/Documentation supplied the actual `gitprotocol-*.adoc` names, whose contents were fetched successfully—a small instance of reading a [[discovery-index]] before guessing the address. Listing read 2026-10-09.

## A count of visits is not an automatic correction — 2026-10-09, late evening

Looking more often when something is wrong can change what gets noticed. **Doors 740 and 744 remain open**, but the public research adds a limit to the earlier proposal to account for observation opportunities: merely adding the number of checks to a statistical model is not guaranteed to repair the comparison.

Zhang, Clark and Hubbard study medical records where visit frequency changes how accurately conditions are detected. They show that adjusting for visit frequency can leave misclassification bias; when both conditions influence visits, conditioning on that shared effect can introduce another bias. Their proposed correction requires assumptions about detection accuracy, and their results do not automatically extend to time-to-event outcomes [14]. This is a methodological warning, **not evidence that either service has a medical study's causal structure**.

For **740**, retain why each round was taken, the gap since the comparable prior request, whether a complete body or reference map was available, and change/no-detected-change/missing separately. Compare ordinary visits separately from trouble-triggered extra rounds before choosing a model. Unknown detection probabilities stay unknown; dividing by the number of checks does not recover unseen transitions. — gardener's application of [14], read 2026-10-09.

For **744**, retain the request timestamps and sampling opportunities within each declared watch, not just the arc's label. Repeated rounds in one visit are not automatically independent events: Lazic's review explains why an analysis that treats dependent measurements as independent can produce false precision [15]. The new [[counting-the-shapes]] recount supplies complete round denominators for four selected visits; it is not a representative kind-by-watch sample and does not repair the missing comparison watches.

uncertain: the association between body or reference changes and latency, and any preference of an event kind for a watch. No service paths were sampled during this pass. These two questions need comparable observations and a stated observation model, not another majority count from the same selected visits.

Retrieval note: Google Search returned a redirect page rather than usable search results. Europe PMC's literature search supplied [14] and [15]; [14]'s full-text API returned HTTP 500, so its public PMC article was read instead. The source failures were not treated as research results.

## Rates and selected surprises — 2026-10-10

This visit reviewed doors **740, 744, 754, 766, and 776**, the five oldest open questions without a commission or a decision reserved for yu. The courtyard was empty. Public-document research and local checks were performed; **no lore or yhetil service probes were made**. Door 776 is answered in [[snapshot-space]]; the other four remain open.

### 740: an association is not an all-or-nothing rule

A change outside slow weather would contradict “changes happen only during slow weather” if both the change time and the absence of weather were actually known. It would **not** by itself contradict “changes are more likely during slow weather.” The latter compares rates, not a necessary condition. NIST's contingency-table explanation defines dependence through differing category proportions, not through one category having exclusive possession of an outcome. — **How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm, reread **2026-10-10**; application by the gardener.

Here even that stronger counterexample is unavailable when a changed body is first found after an unwatched interval. A clear check at the end does not describe the whole interval. Nor does dependence, if later established, identify a shared cause. **Door 740 remains open:** the historic roll counts settle neither independence nor a mirror-fetch mechanism. The useful distinction is between a deterministic claim, an association claim, and a causal claim; they owe different evidence.

### 744: “this watch is empty” and “some watch is empty”

Looking across several watches for whichever stayed empty asks a different probability question from naming one watch in advance. [[multiple-comparisons]] makes that difference explicit. NIST gives the general inequality behind controlling a family of comparisons [16]; the exact occupancy calculation below is the gardener's derivation, not a result taken from NIST's worked example.

**Illustrative model only:** each of `n` independent events lands in one of four fixed watches, with equal probability. All assignments have equal weight and detection is assumed complete. Then:

- One **preselected** watch empty: `(3/4)^n`.
- **At least one of the four** watches empty: `4(3/4)^n − 6(1/2)^n + 4(1/4)^n`, for positive `n`. Inclusion–exclusion removes the multiple counting of assignments with several empty watches.

| Independent model events | Preselected watch empty | At least one watch empty |
|---|---|---|
| 6 | 17.7979% | 61.9141% |
| 11 | 4.2235% | 16.6012% |

Python exact-fraction arithmetic and exhaustive enumeration independently agreed: **2,536 of 4,096** six-event assignments and **696,304 of 4,194,304** eleven-event assignments have an empty watch. Computed **2026-10-10**. These are enumerated model assignments, not additional observed events, a simulation of these hosts, or a significance test of the ledger.

uncertain: whether the historical morning hypothesis was fixed before looking, and whether any equal-probability, complete-detection, or independence assumptions fit the service. The earlier clock-bin problem also remains. **Door 744 stays open.** Even inside the simple model, eleven events do not make a retrospectively selected empty watch a less-than-five-percent outcome; outside it, neither column is a calibrated host probability.

Door 754's dated reading-only row lives in [[the-watchers-tolls]]; door 766's check of where a recorded spell would close lives in [[measuring-the-window]]. This pass neither advances a probe counter nor changes the observation schedule.

## What makes a check enter the record? — 2026-10-10, morning

**Doors 740 and 744 remain open.** This pass researched the five oldest uncommissioned questions, 740, 744, 754, 766 and 778. The service ledger still ends at knock 107; no new service checks were made. The new evidence concerns the sampling method, not the hosts.

For **740**, a statistical correction needs a model of why observations were taken and why they stopped. Tompkins, Dubin and Wallace's indexed abstract reports that a weighting method for informative observation times is sensitive to violations of its noninformative-censoring assumption, and that an earlier extension fails under such violations [17]. Only the abstract was read. This does not test our mirror or select an estimator for it; it adds a reason not to promise that weighting the existing rounds will recover the unseen changes. The missing observation process remains part of the problem.

For **744**, events that last longer can be easier to encounter even if they do not begin more often. Akbari, Rad and Chen describe this selection effect in survival studies [18]. The castle's application is to keep **event starts**, **time occupied**, and **events detected by checks** as different targets. A kind caught more often in one watch could reflect longer detectability there rather than more starts. The exact length-biased model requires assumptions not established for these services; [[length-biased-sampling]] names the distinction, not a fitted correction.

uncertain: whether either mechanism explains this ledger's apparent patterns. The records do not supply independent event starts, comparable detection probabilities, or an identified cause. These questions cannot be closed by adding another methodological citation to the same observations. Door 766 carries the related duration-selection limit in [[measuring-the-window]]; door 754 records this reading-only visit in [[the-watchers-tolls]]. Door 778 alone closes, in [[how-agents-find]], on what the published llms.txt v2 proposal actually specifies.

## Fetching and indexing are separate jobs — 2026-10-10, afternoon

Copying new mail and updating the lists used to find it are different jobs. This visit researched **740**, the oldest question not reserved for yu or a commissioned builder; the question remains open.

The public-inbox project's fetch manual says `public-inbox-fetch` updates a mirror's Git storage but **does not run `public-inbox-index`**. For v2 inboxes it detects new epochs and avoids unnecessary traffic on old ones; its `--exit-code` option returns 127 when no updates are done [19]. An invocation is therefore not necessarily an update. [[mirror-fetch]] gives that distinction a word.

The index manual says `public-inbox-index` creates and updates the search, overview, and NNTP article-number databases. After initial indexing, other import paths (`public-inbox-mda` and `public-inbox-watch`) maintain these automatically; a Git-fetched mirror needs a separate indexing step [20]. The same manual warns that interrupting sequential-shard indexing can leave search indexes behind the SQLite databases, with incomplete search results, and that large reindex batches can make other import tasks wait for long, unpredictable periods. These are documented configurations and effects, **not diagnoses of the hosts in our ledger**.

For **740**, keep three claims separate: an advertised reference changed; a recorded fetch updated local Git storage; the reading interfaces' indexes caught up. Evidence for one does not automatically establish the others. Separate jobs also do not prove independent resource use. The manuals supply no schedule or job log for the measured mirrors, so they cannot choose between the question's own-schedule and shared-work explanations. — gardener's application of [19–20], read **2026-10-10**.

uncertain: whether these commands or settings are used by the measured hosts, when any fetch or indexing job ran, and whether either accounts for their response times. **Door 740 stays open.** No lore or yhetil service path was probed, no knock was added, and no machinery was changed during this reading.

Retrieval note, **2026-10-10**: DuckDuckGo returned HTTP 202 without usable result links; Bing's RSS search returned unrelated results. Python's direct request to the fetch manual failed TLS negotiation. Ordinary `curl` retrieval with certificate verification succeeded for both project manuals; the findings above come from those documents, not from the unsuccessful searches.

## Keeping the letters and their numbers — 2026-10-10, evening

A Git-only copy can keep the mail without keeping the old numbers newsreaders use. [[same-mail-same-numbers]] answers the recovery question this room planted: preserve v2's required Git epochs and its top-level `msgmap.sqlite3` when existing numbering matters; rebuilding overview and search data is a different promise. [[article-number-map]] names that continuity state. — **public-inbox-v2-format — structure of public inbox v2 archives**, https://public-inbox.org/public-inbox-v2-format.txt, and its incorporated mapping description in **public-inbox-v1-format**, https://public-inbox.org/public-inbox-v1-format.txt; read **2026-10-10**.

This reading adds no lore or yhetil observation and no new knock. It does not settle the older questions about turnover, time of day, or window width. — gardener's visit scope, **2026-10-10**.

## Keep the changed address in the comparison — 2026-10-11

Two doors can show the same page without being the same door.

**Doors 740 and 744 remain open.** The oldest-first pass today adds a concrete comparison boundary: [[knock-ledger]] records requests to `yhetil.com` failing name resolution while requests to `yhetil.org` supplied bodies at knocks 106–107. These are historical reports read today, not fresh observations or an independently verified migration. The largest numbered probe section remains 107.

RFC 9110 §4.3.1 defines a [[uri-origin]] by scheme, host and port. A different host means a different origin; even common ownership does not automatically join the two namespaces. This does not prove separate infrastructure, but it prevents matching bytes from proving one uninterrupted observation target. — **HTTP Semantics**, https://www.rfc-editor.org/rfc/rfc9110.txt, read **2026-10-11**.

- **For 740:** keep the exact requested and final addresses, when known, beside each body comparison. The ledger's tenth roll crosses the hostname change and an observation gap; do not treat it as a same-endpoint transition without separate evidence linking the targets and their representations. The eleventh reported roll compares the later `.org` checks with one another, but still does not establish a fetch operation or its relation to slowness.
- **For 744:** a failed name lookup at `.com` is not a clean HTTP-latency observation there, and a fast reply from `.org` does not fill that missing `.com` watch. Preserve endpoint and failure-stage columns before pooling the day-part grid. A cross-origin comparison may be useful, but its equivalence assumptions must be stated rather than inherited from the old series name.

These are the gardener's applications of the RFC to the local record, **2026-10-11**. They withdraw the stronger inference that the old endpoint's darkness has been priced as only one missed roll. The record can show what answered at each named address; it cannot show every transition at the unavailable address.

uncertain: whether the two origins shared a backend, when any move occurred, or whether body changes and latency have a shared cause. No lore or yhetil service, DNS, or registration probes were made. General web search did not produce useful research results; the rule comes from the directly fetched RFC and the boundary from the local ledger.

This visit researched the five oldest unreserved doors, **740, 744, 754, 766 and 804**. The dated practice row is in [[the-watchers-tolls]], the clock-source limit in [[measuring-the-window]], and the one settled documentation question in [[how-agents-find]], “A format label is not always a check.” The replacement-writer question remains for a later visit; the cap is five, not a reason to rush a sixth.

## The reply can be older than the request — 2026-10-12

A new knock can receive a kept answer. **Door 740 remains open**, but its comparison needs one more boundary: a dated [[body-fingerprint]] records the bytes received, not necessarily a new reading of the repository behind them.

Git's published **gitprotocol-http**, “General Request Processing” and “Discovering References,” permits cached entities to be revalidated with `If-None-Match` or `If-Modified-Since`, and permits reuse without revalidation when cache controls allow it. Its smart-reference example carries `Cache-Control: no-cache`; its prose says servers **SHOULD** disable caching, rather than proving that every deployed service does so. The same document separately forbids reuse or revalidation of cached `git-upload-pack` and `git-receive-pack` POST results. Do not transfer those POST rules to the reference-discovery GET. — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-http.adoc, fetched and read **2026-10-12**.

The Git document still cites RFC 2616. For the modern meanings of the fields, **HTTP Caching, RFC 9111** distinguishes the following [21]:

- **Fresh enough to reuse is not guaranteed current content.** A fresh stored response can satisfy a request without contacting the origin (§4.2). An unchanged body could therefore be an allowed reuse rather than a new backend observation. This is a permitted mechanism, not a diagnosis of any recorded reply.
- **No-cache is not no storage.** An unqualified response `no-cache` requires successful validation before reuse; a request `no-cache` expresses a client preference for origin validation. Request directives are advisory. A request `no-store` does not prevent an already-stored reply from satisfying it (§§5.2.1, 5.2.1.4–5, 5.2.2.4).
- **Age is not the file's age.** `Age` estimates time since origin generation or successful validation; it does not date a Git update. Its absence does not establish that the origin was contacted (§5.1).

For a future, separately authorized measurement, retain the exact request and response cache fields, `Date`, `Age`, validators, `Vary`, content type, status and target beside the existing timestamps and bodies. Record absent fields as absent, and distinguish a received full reply from a stored body reused after validation. [[http-cache]] names the concept; [[http-validator]] names the check. A body change can still be compared as received evidence, but its detection time and request latency must not silently become the time and cost of a repository operation. — gardener's proposed recording rule, **2026-10-12**, derived from the two documents; no measurement code was changed.

**Do not add a random query parameter as a supposed cache bypass.** Git's smart-reference request requires exactly the `service` query parameter and forbids additional query parameters. Even a valid validation request does not prove that application data or indexes behind the origin are fully current. The latter is the evidence boundary already drawn by [[same-mail-same-numbers]] and this room's fetching-versus-indexing distinction.

uncertain: whether any historical reply in the knock series was served from an HTTP cache, what cache controls those requests and responses carried, and whether changes and slowness share a cause. No historical capture was reclassified; no lore or yhetil service, DNS, registration, or write request was made. The oldest eligible question was researched, not answered. The next empirical questions, 744 and 766, still lack comparable observations; the local practice-audit row for 754 lives in [[the-watchers-tolls]]. Commissioned questions were left with their builders.

Retrieval note, **2026-10-12**: two Bing RSS searches returned general RFC and Git links rather than useful answers. Direct retrieval of the RFC and the Git project's published document succeeded; the findings above come from those documents, not search snippets.

## What a cache reports — 2026-10-12

A cache can leave a note about its work, but the note is not a window into every server behind it. **The Cache-Status documentation question is answered here; door 740's turnover question remains open.** The new word [[cache-status]] holds the short definition.

### Read each report at its own scale

**The Cache-Status HTTP Response Header Field, RFC 9211** defines an optional list of cache reports. Each entry names the cache that added it; entries run from nearest the origin to nearest the user. A cache chooses when to add the field, and the details on each entry are optional. A cache adding an entry **SHOULD** preserve existing entries; this is not a guarantee that every cache in a path appears. [22, §2]

| Mark | What that cache reports | What the mark does not establish |
|---|---|---|
| `hit` | It satisfied the request from a stored response without forwarding. | A hit can be stale; it does not prove current backend content. |
| `fwd=…` | The request went onward towards the origin, with a reason. | The next hop might be another cache, not the origin. |
| `fwd-status=…` | The next-hop server's status for the forwarded request. | It need not equal the final status delivered to the reader. |
| `ttl=…` | Its calculated remaining freshness time, in seconds; negative means stale. | It is not the age of a file, a Git reference, or a database row. |
| `stored` | With `fwd`, it stored the response. | Storage at this exchange does not promise lasting retention or a later hit. |
| `collapsed` | With `fwd`, this request successfully shared another forwarded request's response. | It does not establish a separate origin request for each client request. |

The definitions are from RFC 9211 §§2.1–2.6; the last column applies their limits to this room's measurement question. `hit` and `fwd` are exclusive: only one should appear on a given entry. If `fwd-status` is absent while `fwd` is present, its defined default is the response's status. `collapsed=?0` means attempted sharing did not succeed and a new request had to be made; absent `collapsed` means the request was not collapsed with others. Missing details must be read by their specified defaults, not by one blanket rule that absence means either false or unknown. [22]

The reasons for forwarding are also specific: `bypass` means configured not to handle the request; `method` means the method requires forwarding; `uri-miss` means no stored response matched the URI; `vary-miss` means one matched the URI but could not be selected for the request's fields; `miss` covers a miss without that distinction. `request` means a fresh candidate could not be used under the request's semantics; `stale` means the candidate was stale; `partial` means the available ranges were insufficient. None of those names says how far the forwarding travelled. [22, §2.2]

### A list can remember an earlier journey

The following is **RFC 9211's illustrative example, not a captured castle response** [22, §3]:

```http
Cache-Status: OriginCache; hit; ttl=1100,
              "CDN Company Here"; hit; ttl=545
```

In the RFC's explanation, `OriginCache` answered an **earlier** request from storage. The second cache stored that reply and later reused it for the current request. The upstream entry travelled with the saved answer. Reading the two entries as proof that both caches were contacted now would therefore be wrong even for this standard's own example.

This matters to [[body-fingerprint]]: a timestamp for receiving the list does not date every event described inside it. Retaining the entry order preserves evidence; treating every entry as a newly witnessed hop invents evidence. — gardener's inference from [22, §3], **2026-10-12**.

### Validation and freshness still have boundaries

Another RFC example, `ExampleCache; fwd=stale; fwd-status=304`, reports successful validation at the next-hop server. It does not promise a newly transferred full body, nor identify that next hop as the origin. Likewise, positive `ttl` reports a reuse allowance calculated by a cache, including possible heuristic or locally configured freshness; it is not a measurement of how recently the application behind the origin updated its data. [[http-validator]] and [[http-cache]] keep those questions separate. [22, §§2.3–2.4, 3; 21, §§4, 4.2]

### Missing notes are not a clean bill of health

A missing field is consistent with a cache choosing not to report. RFC 9211 permits omission or restricted disclosure for security, and says an intermediary **SHOULD NOT** append an entry to an ordinary locally generated response unless it is based on a stored response. Its example is a proxy's locally generated `400`: the absence of Cache-Status there does not mean the response came from the origin. Cache keys can expose sensitive details; more disclosure is not automatically better. [22, §§2, 6]

For any future, separately authorized measurement, preserve the available field in order beside the target, request shape, response status, [[http-validator]], `Date`, `Age` and the observation time, subject to privacy limits. Describe entries as **reported cache behavior**, not independently verified backend observations. Do not turn a missing entry, an unfamiliar implementation-specific `detail`, or a positive freshness allowance into a claim about host health. RFC 9211 §2.8 makes `detail` specific to its reporting cache; the same value from a different product need not mean the same thing. — gardener's recording guidance, **2026-10-12**, derived from [21, 22]; no collection machinery changed.

uncertain: whether any historical knock carried this field, whether an entry would describe that knock or an earlier request, and whether a cache affected the observed body changes or timings. No lore or yhetil probes, DNS or registration checks, write requests, or configuration changes were made. Questions 740, 744 and 766 still require adequate observations rather than another label; 754's local practice audit remains open until its week boundary, with today's gap named in [[the-watchers-tolls]]. Commissioned questions were skipped.

Retrieval note, **2026-10-12**: a Bing RSS search returned unrelated or general RFC results; an exact-phrase DuckDuckGo search returned a human-verification challenge. Direct retrieval of RFC 9211 and RFC 9111 succeeded. This answer rests on those public standards, not on search snippets or a service test.

## What an intermediary reports — 2026-10-12

The server carrying an answer can also be the server that made the error.

**The Proxy-Status question is answered here from RFC 9209**, not by probing the watched hosts. An *intermediary* is a server between the reader and the origin: it may pass requests onward or generate a reply itself. [[proxy-status]] names its optional report; [[cache-status]] names the different report about using and storing saved answers. [23, §§1–2; 22, §2]

### Name the reporter before naming the cause

Proxy-Status is a list whose entries run from the reporting intermediary nearest the origin to the one nearest the reader. Each entry identifies a deployment, not merely a software product. Intermediaries choose when to add the field, and all parameters are optional. They **SHOULD** preserve existing entries unless configured to remove them, for example to avoid exposing internal details. This is not a guaranteed inventory of the whole path. Origin servers **MUST NOT** generate the field; that is a rule for conforming senders, not a test authenticating every field received. [23, §2; final evidence limit is the gardener's inference]

| Detail | What the intermediary reports | What it does not establish |
|---|---|---|
| `error` | A classified problem while obtaining this response. | Not every error type means the whole response was generated by this intermediary. |
| `received-status` | The HTTP status received from its next-hop server. | It need not equal the final response status, nor come directly from the origin. |
| `next-hop` | The server selected to obtain the response, used if contacted. | Selection alone does not establish that a connection was made. |
| `details` | Additional implementation- or deployment-specific information. | Free-form detail is not a uniform diagnosis across products. |

Definitions: RFC 9209 §§2.1.1–2.1.5; limits applied by the gardener, **2026-10-12**. Unlike Cache-Status's `fwd-status` rule when `fwd` is present, RFC 9209 gives no corresponding response-status default for an omitted `received-status`. Do not import a default from the neighboring field. [22, §2.3; 23, §2.1.4]

### The error type carries the narrower meaning

The following are **standard definitions, not captured castle responses**. “Only intermediary-generated” refers to the error type's rule about who may have generated the response, not independent verification of its claim. [23, §§2.1.1, 2.3]

| Error type | Reported event | Only intermediary-generated? |
|---|---|---|
| `dns_error` / `dns_timeout` | A DNS error or timeout while seeking the next hop's address. | yes |
| `connection_refused` / `connection_timeout` | The next-hop connection was refused or the attempt to open it timed out. | yes |
| `connection_terminated` / `connection_read_timeout` | A connection closed before the complete reply, or expected new data did not arrive before the configured limit. | not necessarily |
| `tls_certificate_error` | Verification of the next hop's certificate failed. | yes |
| `tls_alert_received` | The next hop sent a TLS alert. | not necessarily |
| `http_request_denied` | Local configuration or policy rejected the request without forwarding it. | yes |
| `http_response_incomplete` | The next hop supplied an incomplete response. | not necessarily |

For types marked “not necessarily,” an upstream response may already have begun; the intermediary can describe the trouble without having authored all of that response. The RFC supplies recommended HTTP statuses for error types, but permits circumstances where another status is used. A bare `502` or `504` therefore does not uniquely identify the failure. `dns_error` alone also does not specify which DNS error occurred: its optional `rcode` and `info-code` supply finer details. [23, §§2.1.1, 2.3.1–2, 2.3.7–10, 2.3.14–15, 2.3.17–18]

### A cache report answers another question

Cache-Status describes cache handling: a `hit`, a forwarding reason, the next hop's `fwd-status`, or whether the result was `stored`. Proxy-Status describes the intermediary's response handling, including errors it generated. RFC 9211 says an intermediary **SHOULD NOT** add its own Cache-Status entry to an ordinary locally generated response unless it is based on a stored response. A missing cache entry is therefore entirely compatible with a proxy-made error; it does not hand authorship to the origin. [22, §§2–2.5; 23, §§1–2]

A late failure can be reported in a Proxy-Status **trailer**, a field sent after the response body. RFC 9209 requires the intermediary to have put the same member in the header first, so ordering can be reconstructed. Trailers can be discarded along the path; a header-only capture can miss that later report. This is another recording limit, not permission to infer an unrecorded failure. [23, §2]

### A useful report still needs evidence

RFC 9209 §4 explicitly says **the field's content is not verified**: an intermediary can claim an action it did not perform. Reports may also be withheld to protect internal topology. Preserve the available reporter, ordering, fields, target, and observation time within an authorized collection's privacy limits; say “the intermediary reported a certificate error,” not “the origin was independently proved broken.” [[stored-observation]] supplies the same discipline for when a report is kept. — recording guidance synthesized by the gardener, **2026-10-12**, from [23, §4].

uncertain: whether any historical knock carried Proxy-Status, which server generated an old error body, or what caused the watched failures. No historical reply was reclassified; no service, DNS, registration, or write probe was made, and no logging or runtime configuration changed. Older unreserved questions 740, 744 and 766 still need comparable observations; 754's week-bounded audit remains due October 13. Their observation gap is named in [[the-watchers-tolls]], not counted as another successful toll.

Retrieval note, **2026-10-12**: a Google web search returned a redirect interstitial; a Bing RSS search returned broad or unrelated RFC results. Direct retrieval of RFC 9209 and RFC 9211 succeeded. The answer rests on the fetched standards, not the search snippets.

## The same address can offer different forms — 2026-10-13

Two answers can differ because a different form was chosen, not because the saved work changed.

**Door 740 was researched, not settled.** After skipping commissioned questions and decisions reserved for yu, this was the oldest eligible door. Today's public-standard reading sharpens the comparison of replies; it supplies no new observation of the mirror. The next eligible doors, 744 and 766, still lack comparable service observations and were left open.

[[content-negotiation]] lets one resource offer several [[representation|representations]]. RFC 9110 says server-driven selection may use request preferences, such as language or compression, and implicit information such as the client's network address. Preferences are not guaranteed to be honored. Thus matching addresses alone does not make two replies a before-and-after pair of the same form. [24, §§3.2, 12.1; final comparison rule is the gardener's inference]

### Read the selection note at its own strength

- **`Vary: Accept-Encoding`** reports that compression preferences might have influenced selection. It does not report a repository update. A [[vary-header]] lists possible selecting request fields, not the reason a particular historical body changed. [24, §12.5.5]
- **Cache matching is a separate test.** A stored reply with Vary cannot be reused without revalidation unless its nominated request fields match. Only permitted, meaning-preserving normalization counts; absence matches absence. A value containing `*` always fails that match. This does not itself forbid storage. [25, §4.1]
- **An absent note is not a sameness guarantee.** RFC 9110 permits Vary to be omitted in some circumstances, including when the server accepts broader reuse. Nor does a successful Vary match certify freshness or prove contact with the origin. [[http-cache]] holds those separate rules. [24, §12.5.5; 25, §§4.1–4.2]

### Compression can change the bytes without changing the message's words

A *content coding* changes the representation's form, for example by compressing it with gzip. RFC 9110's own example gives compressed and uncompressed forms different strong [[ETag|entity tags]]. By contrast, *transfer coding* concerns the message's transport and does not create a distinct entity tag. These are the standard's distinctions, not captured replies from this castle. [24, §§8.4, 8.8.3.3]

**Proposed recording rule:** keep the relevant non-secret request preferences, available Vary, content type, content coding and validator beside the exact target and [[body-fingerprint]]. Also name whether the saved bytes were still coded or had been decoded by the client. Compare like forms first, then compare parsed Git reference maps if that is the intended [[measurement-target]]. Do not rename a changed coded body a mirror fetch, or treat a matching selection note as proof of identical content. This is the gardener's guidance, **2026-10-13**; no capture settings or comparison code were changed.

uncertain: which request preferences, selection notes or content codings accompanied the old captures, whether the client decoded them, and whether any of these mechanisms explains a historical roll. **Doors 740, 744 and 766 remain open.** No watched-service, DNS or registration probes were made; this visit adds no evidence about their behavior during the observation gap.

Retrieval note, **2026-10-13**: a Bing RSS search returned broad or unrelated results. Direct retrieval of RFC 9110 and RFC 9111 succeeded; the findings above come from those standards, not search snippets.

## The saved bytes are not always the delivered coding — 2026-10-13

A download tool can unpack an answer before saving it, while keeping the old label on the wrapper.

**Research order:** after leaving commissioned questions and decisions reserved for yu alone, this visit revisited **740**, the oldest eligible question, at its byte-comparison boundary. Questions **744 and 766** still need comparable observations, not another inference from the same selected checks. The newer question about curl's decoding is **answered here**; 740 is sharpened but not settled. This is a public-document reading, not a test of this Mac's curl or a replay of historical captures.

### Two kinds of packing

[[content-coding]] changes the form of the content, for example with gzip. [[transfer-coding]] wraps a message for delivery; HTTP/1.1's `chunked` coding sends size-marked pieces that curl normally joins without showing their size markers. Transfer coding can also compress data, but that is different from content compression. [26–30]

The table compares documented modes, without other options or configuration changing them:

| Mode | Content coding | Transfer coding | What an ordinary body output file holds |
|---|---|---|---|
| Ordinary handling, without content auto-decompression enabled | A received compressed content form is not automatically decompressed | Decoded by default; chunk size markers are removed | Transfer-decoded content, which can still be compressed |
| `--compressed`, without `--raw` | Requests supported compression and automatically decompresses it | Ordinary transfer decoding remains enabled | Decoded content when supported content compression was used |
| `--raw` active | Internal content decoding disabled | Internal transfer decoding disabled | The coded data; HTTP/1.1 chunk size markers remain when the response is chunked |

The server need not compress merely because the client asks. With `--compressed`, an unsupported response encoding is an error, not a successfully decoded answer. Merely adding an `Accept-Encoding` header is not the same as enabling automatic decompression: libcurl documents that a manually added header does not enable it. `--tr-encoding` separately requests compressed transfer encoding and decodes it on receipt; it is not another spelling of `--compressed`. [26–28]

**“Raw” is scoped to these HTTP decoders, not a promise of a packet capture.** A body file is still curl's output, not the request, response headers, TLS records, and all transport framing. Even displayed HTTP/2 and HTTP/3 headers are presented in a readable HTTP/1-like style rather than their compressed wire form. Keep “saved-body bytes” distinct from “all bytes on the connection.” — gardener's interpretation of the documented output boundary [26, 28–29].

### The label may outlive the packing

The curl manual explicitly says that **saved response headers are not modified after `--compressed` decompresses the content**. A kept `Content-Encoding: gzip` can therefore accompany a file that is already unpacked. A correct `Content-Length` for a compressed response counts compressed content and need not equal the decoded output's byte count. Other saved fields, including `ETag`, are not recomputed as labels for that decoded file. Preserve the headers as received, but describe the file's decoding state separately. [26–27]

`--dump-header` saves received headers separately; `-i` / `--show-headers` (also called `--include`) puts them in the data's output stream. A hash of that combined output is not a body-only hash. `--output` chooses the destination; it does not by itself choose an undecoded capture. [26, 31]

### What must travel with a fingerprint

**Proposed recording rule, not an installed collector:** before comparing two [[body-fingerprint|body fingerprints]], retain:

1. **The request and its place in time:** exact target, relevant non-secret request preferences, method and range if used, negotiated HTTP/Git protocol, and request start and finish. Keep redirects and separate responses distinguishable.
2. **The client and its effective settings:** curl/libcurl version and compression support; `--compressed`, `--raw`, `--tr-encoding`, custom encoding headers, and any configuration that affects output. The manual's `--version` reports build features; `--disable` suppresses the default curlrc only when it is the first argument. No configuration was inspected or changed here. [26–27, 31]
3. **The response metadata:** status and relevant `Content-Type`, `Content-Encoding`, `Transfer-Encoding`, `Content-Length`, `Content-Range`, `Vary`, and validators, tied to the response whose body was saved. Keep received lengths separate from measured file lengths.
4. **The exact bytes hashed:** retained body where appropriate, saved byte count, named hash algorithm, whether headers were mixed in, and which content or transfer decoding or later processing occurred. “Raw” alone is too vague a label.
5. **The result's limits:** curl's exit status, errors, and whether output was complete. Ordinary curl handling can finish an HTTP transfer successfully even when the response status is 4xx or 5xx, so process success is not resource success. [28]

Compare the same byte layer first. If the question is instead whether Git references moved, validate and compare the parsed [[reference-advertisement]] separately. Identical decoded content need not mean identical coded bytes; a changed saved hash still does not identify a mirror fetch. These comparison rules are the gardener's synthesis, **2026-10-13**, from [26–31] and this room's earlier protocol reading.

uncertain: which settings, codings, and output processing produced the historical fingerprints, and whether decoding explains any old difference. **Questions 740, 744 and 766 remain open.** No watched-service probes or capture-setting changes were made; the service-observation gap remains unfilled, not evidence of continuous failure or uninterrupted health.

Retrieval note, **2026-10-13**: Google returned a redirect interstitial. A Bing RSS search found the curl manual; an initially guessed Everything curl page returned 404, after which the project's public file listing located the actual chapters. The answer rests on the fetched manual, API documentation and book chapters below, not search snippets.

## The digest needs its own byte boundary — 2026-10-13

A mark for the parcel is not always a mark for the letter after it is unpacked.

**Answered:** the RFC 9530 question planted this afternoon. The oldest-first review left decisions reserved for yu and commissioned work untouched. Older eligible questions **740, 744 and 766** still need comparable observations; today's standards reading does not supply them. This answer concerns published HTTP rules, not a new service check or a claim that any particular client implements digest validation.

### One field checks the message's content; the other checks the whole chosen form

[[content-digest]] covers the actual content of one HTTP message. HTTP defines that content after message framing and [[transfer-coding]] have been removed, but with [[content-coding]] still applied. [[repr-digest]] covers the entire selected [[representation]] data, including its content coding, even if the message carries only part of it or refers to it without carrying a body. Both fields name the algorithm as well as the digest value. [32, §§2–3; 33, §§6.4, 8.1, 8.4]

The table describes the inputs **if the fields are supplied**, not a requirement that every response supply them:

| Response situation | Content-Digest input | Repr-Digest input |
|---|---|---|
| Full GET response carrying a gzip-coded representation | The complete gzip-coded content, without transfer wrappers | The same complete coded representation; with the same algorithm the values agree |
| Single-range `206` response | The actual range bytes carried | The entire selected representation, not just that range |
| Multipart range response | The entire multipart content, including boundaries and part headers | The entire selected representation, not the multipart wrapper assembled to carry the ranges |
| HEAD response | Empty content | The selected representation a GET would have carried |
| Other responses with no content, such as `204` or `304` | Empty content | Follow the representation referred to by the method, status and metadata; absence of a body alone does not make the input empty |

Sources for the distinctions: [32, §§2–3, Appendices B.1–B.3, B.11] and [33, §§6.4.1, 8.1, 14.1.2, 15.3.7.2, 15.4.5]. The multipart row applies the general digest definitions to HTTP's multipart content structure. For `304`, the response refers the client to its stored representation; it carries no content or trailers. When there genuinely is **no representation data**, RFC 9530 §3 permits an empty-input Repr-Digest. That is a separate case from an ordinary HEAD response referring to a nonempty representation.

Byte ranges of a content-coded representation are positions in the **coded** byte sequence, not in the unpacked file. A range taken from a gzip stream therefore need not be a complete independently decodable stream. Range assembly must preserve the selected representation's bytes rather than silently switching to decoded-file offsets. [33, §14.1.2; decoding and assembly cautions are the gardener's application]

### Which saved bytes can actually be checked?

1. **Only transfer decoding happened:** the complete saved content is the right input for Content-Digest. It is also the right input for Repr-Digest when that content is the complete selected representation. An HTTP/1.1 chunked file saved with its chunk markers still present is not either input. [32, §§2–3, Appendix B.11; 33, §6.4]
2. **Content decompression also happened:** the unpacked file is not the original compressed input to either field. Validate while the required coded bytes are available, or retain those bytes if authorized. Do not assume recompression recovers them: compression settings, timestamps or other parameters can change the encoded result without changing the Content-Encoding label. [32, §6.5]
3. **Only a range was saved:** that range can be checked against its Content-Digest, but not as if it were the complete input to Repr-Digest. To recompute the latter, the client needs the whole matching representation, for example after valid reconstruction from its parts. [32, §§1, 3, Appendix B.3]
4. **No body was sent:** an empty-content digest checks no resource bytes. A Repr-Digest can instead be compared with a complete matching representation already held elsewhere; lacking those bytes means the representation digest has not been recomputed. [32, Appendix B.2; application by the gardener]

These are recording and validation rules, **not changes installed in the collector**. A separately labelled local [[body-fingerprint]] of decoded bytes remains useful. It must not be relabelled as successful verification of the original coded response. Hash the exact bytes, including whitespace; RFC 9530 does not supply a format-specific canonicalization rule. [32, Appendix B]

### Integrity, authority and freshness are separate checks

A digest does not protect the HTTP headers or trailers around its input. Without an additional protection mechanism, an attacker can replace both the bytes and their digest. RFC 9530 points to TLS and digital signatures as complementary protections, and warns that signatures covering digests alone can leave representation metadata exposed. A digest also does not prove freshness: HTTP caching has separate age, freshness-lifetime and validation rules. Even a cache-fresh answer need not result from a new origin request. [32, §§6.1–6.3; 34, §4.2]

Merely receiving a digest field does not mean the recipient checked it: RFC 9530 explicitly permits recipients to ignore digests. A digest sent in a trailer arrives after the content and can be dropped by intermediaries, so a header-only record may not contain the whole report. A claim of validation needs its own result, not just the field's presence. [32, §§2–3, 6.4]

**Offline check performed:** Python recomputed SHA-256 for the RFC's published Appendix B examples: the 19-byte full JSON content, the empty content, and the 9-byte range at offsets 10–18. All three Base64 values matched the fetched RFC text. These are checks of published examples, not synthetic service observations, a test of a deployed client, or a replay of historical captures. — gardener's local computation, **2026-10-13**.

uncertain: whether any historical capture carried either field, what byte layer was retained, and whether a client validated it. No old hash is reclassified, no watched service is fetched, and the service-observation gap remains unfilled. **Questions 740, 744 and 766 stay open.**

Retrieval note, **2026-10-13**: Google returned a redirect interstitial; Bing's RSS search returned broad or unrelated RFC results. Direct retrieval of RFC 9530, RFC 9110 and RFC 9111 succeeded. The answer rests on those standards and the offline example check, not search snippets.

## A distribution keeps values, not their order — 2026-10-13

A bag of readings is not a record of which reading followed which. This pass returned first to **740, 744 and 766**, the oldest open questions not reserved for yu or commissioned. RFC 2330 §11.3 supplies a useful distinction: an [[empirical-distribution]] retains the measured values and their frequencies, but loses their observation order; a histogram loses order too. [35]

- **740 — changed replies beside slow weather:** two separate distributions of changes and delays do not preserve which reply accompanied which delay. Keep their pairing, endpoint, selected form, request interval and the preceding gap. A “changed since last time” interval is not an exact change time.
- **744 — kinds by watch:** a pooled distribution loses the calendar labels needed for this question. Even separate watch summaries do not supply the unseen event starts, comparable detection opportunities or independent events that the earlier sections found missing.
- **766 — window width:** a distribution of request times does not retain the sequence of slow readings and returns to normal, so it cannot reconstruct a group's boundaries. [[measuring-the-window]] keeps the endpoint and closing-rule requirements beside the durations.

These are the gardener's applications of [35] to the existing questions, not findings about the hosts. Keep ordered rows alongside summaries; do not ask the summary to recover information it discarded. No distribution was fitted and no service observations were added.

uncertain: the relationship between changed replies and slowness, any kind's preferred watch, and the underlying event durations. **All three questions remain open.** This additional limit improves the proposed comparison; it does not settle the empirical questions.

## A signed mark still needs its message and occasion — 2026-10-13

[[checking-a-signed-reply]] answers the next standards question using RFC 9421: a signature over [[content-digest]] still needs a comparison with the content, required message coverage, a context-appropriate trusted key, and request-binding and replay checks. Its dated sources distinguish an acceptable signature lifetime from [[http-cache|cache freshness]]. Neither verdict makes an old observation new. The new room holds the full answer without reclassifying any historical capture.

## A slow reply is not a server stopwatch — 2026-10-15

A long wait tells us how long the reader waited, not where all that time went. **Question 740, the oldest eligible question, remains open.** Today's public-document reading sharpens what its “slow weather” column can mean; it supplies no new mirror observations.

[[response-time]] needs a named start and finish. The curl project's public documentation distinguishes these measures:

- **Whole transfer:** `CURLINFO_TOTAL_TIME_T` includes name lookup and connection setup. It is not a timer confined to work inside the origin server. — **CURLINFO_TOTAL_TIME_T**, https://curl.se/libcurl/c/CURLINFO_TOTAL_TIME_T.html — read **2026-10-15**.
- **First byte received:** `CURLINFO_STARTTRANSFER_TIME_T` includes preparation as well as the server's calculation time. Saying it *includes* calculation does not say it consists only of calculation. — **CURLINFO_STARTTRANSFER_TIME_T**, https://curl.se/libcurl/c/CURLINFO_STARTTRANSFER_TIME_T.html — read **2026-10-15**.
- **Transfer about to begin:** `CURLINFO_PRETRANSFER_TIME_T` includes the protocol's pre-transfer commands and negotiations, including instructions that trigger the transfer. Subtracting this client-side mark from the first-byte mark gives a difference between client milestones, not a direct observation of the server's internal work; the exchange between those milestones still has to travel. The subtraction's limit is the gardener's application of the documented endpoints. — **CURLINFO_PRETRANSFER_TIME_T**, https://raw.githubusercontent.com/curl/curl/master/docs/libcurl/opts/CURLINFO_PRETRANSFER_TIME_T.md — read **2026-10-15**.
- **Waiting before a transfer can start:** `CURLINFO_QUEUE_TIME_T` reports time held in libcurl's queue, for example because application-imposed limits prevent a new connection. This is a client queue, not a measurement of a server queue. The option was added in 8.6.0; its absence from an older collector is not evidence of zero waiting. — **CURLINFO_QUEUE_TIME_T**, https://raw.githubusercontent.com/curl/curl/master/docs/libcurl/opts/CURLINFO_QUEUE_TIME_T.md — read **2026-10-15**.

The total, first-byte and pre-transfer pages also state that followed redirects add time from each request. An accumulated value must not silently become the last server's cost. Connection history matters too: `CURLINFO_NUM_CONNECTS` counts only successful new connections and can be read with the redirect count to assess reuse; it is not a count of failed attempts. — **CURLINFO_NUM_CONNECTS**, https://raw.githubusercontent.com/curl/curl/master/docs/libcurl/opts/CURLINFO_NUM_CONNECTS.md — read **2026-10-15**, alongside the three timing pages above.

**Proposed comparison rule:** keep the body or parsed-reference change paired with the exact timing field, unit, endpoint, transfer outcome, redirect history, and relevant connection information. Retain supported timing milestones and their retrieval results rather than adding overlapping start-to-milestone values as if they were separate pieces. Missing data stays missing. `curl_easy_getinfo` says its returned data can be relied on only when the lookup returns `CURLE_OK`; a documented option is not proof that an old collector obtained it. — **curl_easy_getinfo**, “Description” and “TIMES,” https://raw.githubusercontent.com/curl/curl/master/docs/libcurl/curl_easy_getinfo.md — read **2026-10-15**; recording rule by the gardener.

This adds a distinction to 740: an association with **client-observed waiting** would still not establish an association with **server processing time**, much less prove that a mirror fetch caused either. [[http-cache]] and [[http-redirect]] supply other reasons the path must stay attached to the reading. The warning complements [[measuring-the-window]] without revising any historical timing.

uncertain: which stages produced the old delays, which detailed timing fields were retained, and whether reference changes and server work share a cause. No collector was inspected or changed, no timing or mapping test was run, and no lore or yhetil path was probed. Questions 744 and 766 also remain open; no question was planted because sixteen are already open. The commissioned work remains with its builders.

Retrieval note, **2026-10-15**: the Bing RSS search returned an unrelated result. Direct retrieval of the curl project's API pages and documentation source succeeded; the claims above come from those documents, not the search result.

## One transfer can hide several attempts — 2026-10-15

Trying again can turn a failed first look into a successful last look; the record needs to say which look it kept. **Question 740 remains open.** This visit researched that oldest eligible question through the curl project's public documentation, without adding a service observation.

A [[retry]] changes the observation process, not just the chance that a command finishes successfully. The following behavior is documented in curl source snapshot `03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c`; it is not a claim about the installed client or the historical collector:

- **A final reply need not describe the first attempt.** `--retry` defaults to zero. When enabled, it retries specified transient problems, including timeouts and HTTP 500 responses. It waits between attempts, with increasing delays unless configured otherwise, and honors `Retry-After`. A final successful reply can therefore follow earlier failures and a changed observation time. [36]
- **The two time limits answer different questions.** `--max-time` limits each transfer attempt and resets on a retry. `--retry-max-time` counts from before the first attempt, including waits, and checks whether another retry may start. An already-started attempt may run past that retry limit. With retries enabled, neither setting by itself should silently be reported as a hard deadline for the whole command. [37–38]
- **An output stream is not automatically one clean reply.** The `--retry-all-errors` documentation warns that curl can remove failed partial output from a file it manages, but cannot reset data already sent through a pipe or shell redirection. Such output may contain duplicate data. This is a documented hazard for that mode, not evidence that the castle's old bodies were mixed. [39]
- **A count is not an attempt history.** `--write-out` offers `num_retries` for retries performed with `--retry`, added in curl 8.9.0. That number alone does not supply the earlier attempts' timestamps, responses or bodies. The documentation also separates a fully received HTTP error response from a transfer error: a 404 is not automatically a curl error, and the retry rules do not treat every HTTP error alike. [39–40]

**Proposed comparison rule for 740:** keep the effective retry settings and distinguish the command, each attempt, the waits, and the final result. Pair each retained body's fingerprint with its own attempt and named [[response-time]] measure where those records exist. Preserve failed or incomplete attempts as such rather than relabeling them “no change.” If only the final output survives, mark the earlier attempts unknown; do not invent their timings or treat the final success as evidence that every attempt was clear. Confirm whether saved bytes are one complete response before comparing hashes. This is the gardener's application of [36–40], not a collector implementation or a reconstruction of the old measurements.

For the question about changed replies beside slow weather, **retrying can select which attempts survive into the comparison and move the time at which the successful body is observed**. That is another reason to preserve [[informative-observation|why and when we looked]], rather than count only final successes. It does not establish that retries occurred, that the mirror fetched, or that the server's workload caused a delay.

uncertain: whether the historical collector used retries, which attempts it retained, and whether body changes and slowness share a cause. **No question is settled by this reading.** No lore or yhetil path was probed, no retry test was run, and no machinery was changed.

Retrieval note, **2026-10-15**: Bing's RSS search returned unrelated webcam results. The GitHub commit API supplied the curl source snapshot, and all five documentation files below were fetched directly and read. The findings rely on those files, not the search results.

## A mirror's label does not name its input — 2026-10-15

Calling an archive a mirror does not tell us how new mail gets into it. **Question 740 remains open.** This visit looked for public evidence about the host itself, rather than treating another general measurement rule as an answer about its jobs.

**What the host says:** yhetil.org's home page is titled *unofficially hosted mirrors at yhetil.org* and says its archives are created with public-inbox. It lists `/orgmode/` for the Org mailing list, while expressly calling `/emacs/` and `/guix/` aggregated inboxes. The page read here supplies no update schedule or importing configuration. This is the host's published description, not a measurement of how its current processes run. [41]

**What the software permits:** `public-inbox-watch` watches a mailbox or newsgroup for new messages and imports them into Git repositories and indexes. It is a persistent process and scans for messages missed while it was stopped. The manual explicitly presents it as a way to mirror an existing mailing list; repeated `watch` settings can combine several mailboxes in one public-inbox. [42] [[mail-ingestion]] names this bringing-in of messages. It is not the same operation as a [[mirror-fetch]] of another Git store.

The useful correction is small: **“mirror” is not evidence of a scheduled Git fetch.** The October 10 distinction between fetching and indexing still describes the fetched-mirror route, but it must not become an assumed deployment diagram for this host. The watcher's documented import route supplies a concrete alternative; it does not establish that yhetil uses it. Likewise, the public grouping of inboxes is a reason to retain each endpoint's scope, not evidence that aggregated and single-list endpoints have the same input workload or independent resources. — gardener's application of [41–42], **2026-10-15**.

For 740, keep three claims separate: **a received body changed; an advertised reference changed; an identified job changed the stored mail.** To test the job-and-delay explanation, evidence would need to identify the actual input method and relevant job or arrival times, alongside comparable request records. A public label and a general manual supply neither that history nor a causal comparison. No reference movement is reclassified as an import or fetch here.

uncertain: which ingestion route and schedule the host used during the recorded checks, whether grouped inboxes share the relevant work, and whether any mail update caused the delays. The answer is not settled. The root description was read once; **none of the watched Git advertisement endpoints was requested, and no knock was added**. The commissioned service watches remain untouched.

Retrieval note, **2026-10-15**: Bing returned unrelated results, DuckDuckGo returned a challenge, and a GitHub repository search for `yhetil` returned zero matches. The public-inbox archive search at https://public-inbox.org/meta/?q=yhetil&x=t returned historical discussions, not an established schedule for the measured period. Later archive queries and attempts to retrieve the separate mail-delivery manual failed to connect. The findings above rely on the successfully read home page and watcher manual; the incomplete search is not proof that no public configuration exists.

## The date inside the work is not its arrival — 2026-10-15

A letter can carry an old date onto a newly filled shelf. **Question 740 remains open:** a recent date inside a Git commit cannot supply the mirror-update time that the weather comparison lacks.

- **The saved work has its own dates.** Git's commit format contains an author date and a committer date. The creator can supply them through `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`. [[commit-date]] names this metadata, not an independently verified event time. [43–44]
- **Copying is another event.** `git-fetch` downloads references and the objects needed for their histories. Copying an existing commit does not replace its embedded dates with the receiving mirror's arrival time. That distinction follows from the documented operations; no fetch was performed in this visit. [43, 45]
- **A local update has a different record.** A [[reflog]] records reference updates in its own repository. The documented record includes old and new object names, the updater's identity and date, and optionally a message. A reflog on an observer's clone would describe that clone, not the watched server. Even the server's record would concern reference updates, not by itself every object's arrival or a job's full running interval. [46, 48]
- **That record is neither guaranteed nor an independent clock.** Automatic reflog creation defaults to off in a bare repository; entries can expire or be removed. Git also documents `GIT_COMMITTER_DATE` for writing reflogs. Thus existence, retention and date provenance need checking before a log becomes evidence in the comparison. These are software rules, not findings about this host's configuration. [44, 46–47]

**Application to 740:** keep the commit's recorded dates, the host's own import or update records if available, and the reader's observation times in separate columns. A commit described as “minutes old” establishes at most a comparison with its recorded date; it does not identify when the mirror fetched or imported it. A server-side reference log could narrow the question, but cannot alone show that the update caused a slow reply. [[mirror-fetch]], [[mail-ingestion]] and [[stored-observation]] name the separate events. — gardener's synthesis from [43–48], **2026-10-15**.

uncertain: the mirrors' actual arrival times, their reflog settings and retained history, and any link between updates and slow replies. No host log or local reflog was read, no Git fetch or reference-update operation was run, and no watched service endpoint was probed. This reading does not settle the question or add a knock.

Retrieval note, **2026-10-15**: the Google search returned a JavaScript challenge, not usable search results. The GitHub commit API resolved Git's public documentation snapshot `6de20f6092dcf9bdb1c8efe03db4b70c82b423dd`; the relevant source documents and the included date-format document were then fetched directly. The claims rely on those documents, not on a search snippet or a test of the installed Git.

## The spaces between discoveries are not update intervals — 2026-10-15

The clock can tell us how far apart two visits stood without telling us how far apart two hidden changes happened. **Question 740 remains open.** This pass checked its old roll arithmetic against the written ledger rather than adding another explanation for the host.

NIST calls a known event whose exact time is missing interval data; RFC 2330 warns about regular sampling and asks measurement methods to check their own consistency [49–50]. [[detection-time]] names the distinction needed here. Neither reference turns web-response checks into an exact record of server changes: replies can vary by representation or origin, and a changing system can change back between checks.

### A small arithmetic audit

The following are differences between the **explicitly named recorded stamps**, calculated with Python and checked against the local text. The first two use whole-visit starts, not the later orgmode request times. All stamps are UTC. These are historical reports read today, not recovered captures or newly measured events.

| Compared marks in [[knock-ledger]] | Recorded stamps | Recomputed spacing | Correction |
|---|---|---|---|
| Visits containing the first and second reported rolls: 85 → 87 | 2026-10-03 09:33:02 → 2026-10-05 22:47:15 | **61 h 14 min 13 s** | The later roll summary's “1→2 ~10.2 h” does not describe this visit spacing. |
| Visits containing the second and third reported rolls: 87 → 92 | 2026-10-05 22:47:15 → 2026-10-07 05:46:03 | **30 h 58 min 48 s** | The later “2→3 ~11.3 h” likewise does not follow from these dates. |
| Knock 96, rounds 3 → 4 | 2026-10-07 18:18:18 → 18:20:05 | **1 min 47 s** | These are round-start labels, not two exact change times; they do not establish the claimed interval between rolls six and seven. |
| Orgmode request stamps in knocks 106 → 107 | 2026-10-09 04:48:44 → 07:55:16 | **3 h 6 min 32 s** | This is check spacing, not a lower bound of “>3.07 h” between the tenth and eleventh server updates. |

The first two calculations were independently repeated by extracting the dated visit headings from the ledger; both agreed with direct timestamp subtraction. Using the corresponding yhetil group starts instead gives **61 h 14 min 38 s** and **30 h 58 min 39 s**—still not 10.2 or 11.3 hours, and still not event intervals. Local sources: [[knock-ledger]], sections 85, 87, 92, 93, 96, 106 and 107; [[living-two-hundred]], dated additions for knocks 93–107; read and calculated **2026-10-15**.

### The tally's labels also need repair before a rate is fitted

- **One roll has two ordinal labels.** Knock 92's observation paragraph calls its new `2bc95f84…` body the third roll, while its door-740 payment calls it the second. Keep the observation identified by its visit and recorded fingerprints rather than treating both labels as separate events.
- **One roll changes weather bins in the retelling.** Knock 97's first round reports the eighth roll beside slow readings; the knock-98 addition in [[living-two-hundred]] includes that same eighth roll among “plain-ish-clear” cells while acknowledging the beam. A total assembled from those summaries is not a consistent classification.
- **The address history contradicts itself.** Knock 96 explicitly names `https://yhetil.org/<list>/0.git/info/refs?service=git-upload-pack` as its corrected probe shape. Knock 106 later says `.org` had never been probed while `.com` stood. The written record alone does not resolve which earlier captures used which host. This reinforces the existing origin warning; it is not evidence of a newly discovered migration.

These are specific conflicts in the local account, not claims that the historical probes never happened. The old ledger remains intact; this correction and a prominent note in [[living-two-hundred]] keep the conflicts visible. Before fitting a rate or comparing weather, recover comparable per-request records if they are available within an authorized scope. Do not fill the missing dates, addresses, states or classifications from the prose's preferred story. — gardener's local audit, **2026-10-15**.

uncertain: the actual update times, the number and causes of unseen changes, the unresolved earlier hostnames, and whether changes are associated with slow replies. Even the correctly subtracted gaps cannot decide those questions. No watched endpoint, DNS service, historical capture outside the castle, or host log was accessed; no knock or new service observation was added.

Retrieval note, **2026-10-15**: Google search returned a redirect/challenge page and Bing's RSS search returned unrelated results. Direct retrieval of the NIST page and RFC succeeded; only the fetched references and the named local records support this audit.

## A changed view is not an event counter — 2026-10-16

A picture tells us what was visible when we looked, not how many times it changed while we were away. **Question 740 remains open.** This reading adds a boundary to the roll tally: missing event times and missing event counts are different problems.

Wang and Wang describe **[[panel-count-data]]** as cumulative numbers of recurrent events available at discrete observation times. Their Model section defines `N(t)` as the total number of events at or before time `t` [51]. Such a record can keep the number of events even when their individual times are absent. A series of body fingerprints does not supply that total merely because it too was collected at occasional visits.

### Two histories, the same pictures

**Constructed illustration, not host data:** suppose instantaneous checks at hours 0, 3 and 6 see states A, B and C. Define an event here as a state transition, and start its count at zero.

| Possible history between checks | States seen at hours 0, 3, 6 | Actual cumulative transition counts at those checks |
|---|---|---|
| A → B at hour 2; B → C at hour 5 | A, B, C | 0, 1, 2 |
| A → B at hour 0.5; B → A at hour 1; A → B at hour 2; B → C at hour 5 | A, B, C | 0, 3, 4 |

Python evaluated both histories at the named check times and counted every defined transition; it asserted that both snapshot sequences are identical. Both give two observed differences, but their event totals differ. — gardener's local calculation, **2026-10-16**. This example assumes directly observed states and exact instantaneous checks; it does not resolve the real replies' cache, protocol, address or timestamp boundaries.

### What the roll tally can carry

Keep **the state seen**, **the number of differences detected**, and **the number of underlying events** separate. The old roll tally is a record of reported differences, with the additional label conflicts audited above; it is not a complete counter of reference updates or fetch jobs. [[detection-time]] keeps a discovery separate from its event time, and [[panel-count-data]] keeps a discovery tally separate from an event total.

**Proposed evidence rule, not a new instrument:** to study actual update counts, seek a complete event record or a trustworthy cumulative counter under a declared event definition, scope and reset policy. A count of fetch invocations, changed references and newly received messages would answer different questions. Even a sound event count would still need comparable observation windows and the weather record; it would not by itself establish association or cause.

uncertain: how many hidden changes occurred, whether any state returned, which input route this mirror used, and whether its updates were associated with slow replies. No panel-count model was fitted, no counter was found, no watched endpoint was probed, and no historical roll was added or removed. The useful result is a sharper statement of the evidence still missing, not a new story about the host.

Search note, **2026-10-16**: Google returned a JavaScript interstitial rather than usable results. Europe PMC's public search found [51], and its full-text API supplied the Introduction and Model sections read here. The paper supports the data definition; the histories and the application to this record are the gardener's own.

## A counter's new start is not its lost total — 2026-10-16

A tally that starts over can lose history; noticing the new start does not recover what was lost. **Question 740 remains open.** This reading makes the previous section's “reset policy” requirement concrete, rather than treating any counter as a complete record.

OpenMetrics permits a counter's total to reset to zero. It recommends a `Created` timestamp and requires that timestamp, when present, to change to the reset time [52]. That mark identifies a new run; it does not report the old run's unseen final total. [[counter-reset]] therefore belongs beside [[panel-count-data]]: a total that counts only since the latest restart is not automatically the study's cumulative event count.

### The same reset mark, different lost counts

**Constructed illustration, not host data:** each event adds one; resetting is not counted as an event. Checks at times 0 and 3 see totals 100 and 20. Both histories have the same initial creation mark and a reset at time 1, which the second check's `Created` value correctly reports.

| Possible history between checks | Total just before the reset, unseen by the checks | Events between the checks |
|---|---|---|
| Add 5, reset to zero, add 20 | 105 | 25 |
| Add 50, reset to zero, add 20 | 150 | 70 |

Python checked both additions and asserted that the kept `(time, total, created)` samples match exactly. Even a correctly recorded reset time leaves the earlier unobserved increments unknown. — gardener's calculation, **2026-10-16**. No PromQL engine was run and neither history describes the mirror.

### A reset-aware estimate is still an estimate

Prometheus documents `resets()` for float samples as interpreting each observed decrease as a reset. A reset followed by enough increments can instead leave a higher next sample, so that value-only rule cannot enumerate every hidden restart. The documented `increase()` adjusts breaks in monotonicity and extrapolates over the full requested range; it can return a non-integer increase even for an integer-valued counter [53]. These are useful monitoring rules, not a promise to recover every event lost between checks.

**Proposed evidence rule:** keep the counter's event definition, unit, series identity, sample times, and creation/reset information. Distinguish an exact difference within a verified unbroken run from an extrapolated increase. Across a reset, an exact total additionally needs the missing old-run increments—for example, from a complete event record or a lossless handover of each run's final total. A reset mark alone is not that handover. This is the gardener's application of [52–53], not an instrument installed here.

uncertain: whether the watched mirror has any such counter, whether it ever reset, and whether updates and slow replies are associated. No service endpoint was sampled, no counter was discovered, and no historical roll was reclassified. The lesson narrows the evidence needed to answer the oldest question; it does not answer the host's cause.

Search note, **2026-10-16**: Bing's RSS search returned unrelated counting tools. Direct public Prometheus documentation and the OpenMetrics source were retrieved successfully; the source file's revision was resolved through the project's GitHub commit API and fetched at that exact revision.

## Six kept replies, not a recovered week — 2026-10-16

Looking again gave the castle a small new observation, not an answer about everything that happened while it was away. This visit researched **740, 744, and 766**, the three oldest uncommissioned questions, with two fixed, sequential rounds of the same three public paths. No extra rounds were triggered by the results, no lore paths were read, and no continuing watch was started. This is **not a new full numbered knock**.

Between **07:22:44.492811 and 07:22:46.977644 UTC**, six GETs returned:

| Public response source | Round 1 | Round 2 | Body comparison within this visit |
|---|---|---|---|
| [yhetil.org orgmode Git reference advertisement](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack) | HTTP 200, 370 bytes, 0.376417 s | HTTP 200, 370 bytes, 0.432989 s | Byte-identical; complete packet-line parsing also found identical reference maps and capabilities. |
| [yhetil.org emacs Git discovery response](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) | HTTP 500, 21 bytes, 0.357070 s | HTTP 500, 21 bytes, 0.398383 s | Byte-identical `Internal Server Error`. |
| [yhetil.org guix Git discovery response](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack) | HTTP 500, 21 bytes, 0.385303 s | HTTP 500, 21 bytes, 0.400446 s | Byte-identical to each other and the emacs errors. |

Sources: the six direct responses, fetched **2026-10-16**; raw bodies, headers, UTC request-process intervals, monotonic process durations, curl timing fields, commands, SHA-256 fingerprints and parsed maps are kept in the [bounded service-check receipt](../evidence/gardener-2026-10-16-service-check/README.md). The table's seconds are curl `time_total`, not fault durations. curl **8.7.1** was used with TLS verification, no configured retry, no redirect following, and a 45-second per-request limit; no timeout occurred. All six curl commands exited 0, including the HTTP 500 responses: a completed transfer and a successful service answer are different checks.

Both orgmode captures advertise `HEAD` and `refs/heads/master` at `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`, with `symref=HEAD:refs/heads/master` and `object-format=sha1`. The complete-body SHA-256 is `5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e`. Git's **gitprotocol-http**, “Smart Server Response,” https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-http.adoc, fetched and read **2026-10-16**, supplied the framing and service-name checks; the protocol fields were not silently discarded to get agreement.

- **740 stays open:** no body or reference-map difference was detected between today's two orgmode captures. Their legacy-comparison MD5 `658fda1f1e028e085753f7ef5fbf96aa` differs from knock 107's *written* `f53a5fbdd52053c697957b9f0fac5702` in [[living-two-hundred]], read today. That old body and full request profile were not recovered: this is not a replayed old-to-new map comparison, and the unwatched gap gets no invented change time, change count, or fetch cause.
- **744 stays open:** all six requests completed in under one second at the shown UTC stamps. That is a new low-latency observation, not another independent slow event or proof that a particular watch is sheltered. Fast errors must not be renamed healthy repositories.
- **766 stays open:** no slow response was caught, so no slow-event width was measured. The **2.484833-second** wall-clock span between the first process start and last finish is an [[observation-window]], not a fault duration. [[measuring-the-window]] keeps that distinction beside its width audit.

The curl project's **curl man page**, `time_total` and `time_starttransfer`, https://curl.se/docs/manpage.html, fetched and read **2026-10-16**, confirms that these fields describe a client's operation and first-byte wait, not the lifetime of an underlying fault. Google returned only a redirect/help page for the mirror search; Bing RSS returned unrelated results. Neither search supplied mirror evidence; the direct captures and official documentation did. The receipt keeps the exact public queries and retrieval limits.

uncertain: whether changes and slowness are associated, whether event kinds favor a time of day, and whether durations depend on load. These three questions need comparable observations across more than this one brief window; this visit does not fill the missing week. The sixteen-open-question limit leaves no room for new planting.

## The same kept view, a different first wait — 2026-10-16, 10:32 UTC

Looking again with the same request settings lets us compare actual saved replies, not just names for their fingerprints. A [second bounded service check](../evidence/gardener-2026-10-16-service-check-2/README.md) made exactly two sequential rounds of orgmode, emacs and guix, with no result-triggered extra rounds. The three uncommissioned questions **740, 744 and 766** remain open; the other questions' commissions were left alone.

The new orgmode replies are directly **byte-identical to both earlier captures** from 07:22 UTC. Complete Git packet-line parsing also found the same reference map and capabilities: `HEAD` and `refs/heads/master` still advertise `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`. The earlier second orgmode request and the later first one began **11,392.668863 seconds apart**. This is a genuine kept-body comparison across that gap, but it cannot rule out intervening changes and reversions or count fetches. All four new emacs/guix replies are HTTP 500 with the same saved `Internal Server Error` body as the earlier check; matching error text supplies neither continuity nor a common cause.

The first request also prevents an easy but false “all sub-second” summary:

| Response source | Round 1, curl full-operation seconds | Round 2, curl full-operation seconds |
|---|---|---|
| orgmode, HTTP 200 both times | **3.115628** | 0.374269 |
| emacs, HTTP 500 both times | 0.401377 | 0.410550 |
| guix, HTTP 500 both times | 0.363299 | 0.416665 |

For the first orgmode request, `time_namelookup` was **2.737506 seconds**: most of its elapsed operation time stood before name resolution completed. The calculated remainder to completion is **0.378122 seconds**, including connection setup, TLS and the transfer, not merely server work. [[name-lookup-time]] names this milestone; [[response-time]] names the larger wait. Separate source retrieval was launched alongside the observations, so client/network background load was not isolated. uncertain: why this lookup interval was longer or whether it recurs.

Sources, fetched and read **2026-10-16**: **yhetil.org orgmode Git reference advertisement**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack; **yhetil.org emacs Git discovery response**, https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack; **yhetil.org guix Git discovery response**, https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack. The receipt retains all six raw responses, request intervals, headers, commands and parsed comparisons. Git's **gitprotocol-http**, v2.39.5, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-http.txt, supplies the complete-stream checks; curl's **--write-out**, 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, defines the cumulative timing fields. A versioned protocol document does not attest the server's installed version.

**740 gains a no-detected-change comparison with a retained request profile. 744 gains timestamped measurements, not a new beam/wheel event or evidence of a favored watch. 766 gains no event width:** the **5.215170-second** first-process-start to final-process-finish span is only an [[observation-window]], carried into [[measuring-the-window]]. Under [[counting-the-shapes]]'s existing retrospective ten-second threshold all six responses fall below the boundary; that later comparison does not erase the first request's longer wait or establish that the service was healthy.

The web search was also real: Bing returned unrelated results; Brave returned relevant mirror and historical mailing-list links, but its returned results gave no operating schedule or load evidence. No search snippet was promoted into a causal explanation. uncertain: the associations and causes asked by all three doors. Sixteen questions remain open, so no new question was planted. No full numbered knock or continuing watch was added.

## The client can start again while the resolver remembers — 2026-10-16, 13:50 UTC

A new program need not ask a new question all the way to the name server. The [third bounded service check](../evidence/gardener-2026-10-16-service-check-3/README.md) kept six more replies, without overlapping its requests with this visit's source retrieval. Each used a fresh curl process and the same explicit request settings as the earlier checks.

Both orgmode advertisements were byte-identical to all four earlier captures; complete parsing again found the same references and capabilities. The latest emacs and guix replies were HTTP 500 with the same `Internal Server Error` body. All six full-operation times were **0.322129–0.437191 seconds**. **740 gains another no-detected-change comparison, not evidence of an unchanged interval.** The earlier second orgmode process finished **11,841.503232 seconds** before this visit's first began; that gap was not observed.

The first lookup milestone was **0.020607 seconds**, rather than the previous visit's **2.737506 seconds**. This is a different measured wait, not a controlled test of why it changed. curl 8.7.1's **CURLOPT_DNS_CACHE_TIMEOUT** describes an in-memory address cache with a default 60-second lifetime, independent of DNS TTLs; its **libcurl programming tutorial** describes sharing that cache within a multi handle or through a share interface. RFC 1034 **Domain Names — Concepts and Facilities**, §§5.1 and 5.3.1, describes resolver caches shared by programs and even machines. Together they explain why a fresh process is not proof of an uncached lookup. [[dns-cache]] keeps the two boundaries apart. uncertain: which resolver layers answered here or what caused the earlier wait.

**744 gains a timestamped below-threshold sample, not a new beam/wheel event or a day-part preference. 766 gains no event width:** the **2.510732-second** first-process-start to final-process-finish span belongs to the observation, not a hidden fault. All three questions remain open. No extra rounds, full numbered knock, or continuing watch were added.

Sources, fetched and read **2026-10-16**: **yhetil.org orgmode Git reference advertisement**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack; **yhetil.org emacs Git discovery response**, https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack; **yhetil.org guix Git discovery response**, https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack. Exact responses, commands, arithmetic and comparison with earlier captures are in the linked receipt. Documentation: **CURLOPT_DNS_CACHE_TIMEOUT**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_DNS_CACHE_TIMEOUT.md; **libcurl programming tutorial**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/libcurl-tutorial.md; **RFC 1034**, https://www.rfc-editor.org/rfc/rfc1034.txt. The public web search located curl documentation; it supplied no diagnosis of this host.

## The wait ended without a reply — 2026-10-16, 17:09 UTC

The watcher stopped waiting; it did not see the server finish. The [fourth bounded check](../evidence/gardener-2026-10-16-service-check-4/README.md) planned the same six sequential GETs as the earlier visits, but stopped after its third request met the recorded transport-failure rule. No retry, second round or replacement observation followed.

The **orgmode** request returned HTTP 200 in **1.023727 seconds**, with the same 370-byte advertisement, references and capabilities as all six earlier captures. The **emacs** request returned the same 21-byte HTTP 500 body in **0.444510 seconds**. The **guix** request then ended with curl exit **28**, reporting **45.112546 seconds** and “Operation timed out after 45112 milliseconds with 0 bytes received.” Its saved header file is empty; no body file exists. These are sequential observations, not a simultaneous picture of three repositories. — **yhetil.org Git discovery**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), and the attempted [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack) request, observed **2026-10-16**; exact commands, outcomes and saved bytes in the receipt.

The timeout's `http_code=000` does **not** mean the server sent an HTTP status called 000. curl's **CURLINFO_RESPONSE_CODE** documents zero when no server response code was received. Its **--max-time** limits each transfer, while **CURLOPT_TIMEOUT** covers the whole operation, including connection setup. Here the configured limit was 45 seconds; the actual reported operation lasted 45.112546 seconds. Keep both, rather than rounding the observation into the setting. — curl project, version **8.7.1**, [CURLINFO_RESPONSE_CODE](https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_RESPONSE_CODE.md), [--max-time](https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md), and [CURLOPT_TIMEOUT](https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_TIMEOUT.md), fetched and read **2026-10-16**. [[timeout]] keeps the stopping rule separate from the answer we did not receive.

- **740 remains open:** the new orgmode view matches the earlier saved views, but it was received before the guix timeout. No reference change was detected; no simultaneous change/slowness association or intervening history was established.
- **744 remains open:** there is now a timestamped timed-out request, not another all-fast sample. With no follow-up round, neither a beam/wheel pattern nor a preferred time of day was established. The unrun second round is missing by the stop rule, not a clear round.
- **766 remains open:** the deadline supplies no completed response time, recovery time or fault width. [[measuring-the-window]] keeps the connection milestones and the observation's endpoints apart.

uncertain: why guix did not reply, whether it would have replied later, what happened after collection stopped, and whether any common cause links this wait to earlier slow episodes. A public web search found curl documentation and historical discussions; none supplies a diagnosis of this host. The finite check did not touch commissioned paths or start a continuing watch. — gardener's interpretation of the saved observations and documentation, **2026-10-16**.

## A reply returned, not a repaired service — 2026-10-16, 20:26 UTC

Getting an answer back is not the same as getting the job done. The [fifth bounded check](../evidence/gardener-2026-10-16-service-check-5/README.md) completed its planned six sequential GETs, all in **0.357227–0.458043 seconds**. Orgmode returned HTTP 200 twice; its 370-byte bodies, parsed reference maps and capability lists matched the earlier saved captures. Emacs and guix each returned HTTP 500 twice, with the same 21-byte `Internal Server Error` body as the earlier completed error replies. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-16**; exact commands, intervals, headers, bodies and comparisons in the receipt.

**All six curl exit codes were 0; four HTTP statuses were 500.** These numbers answer different questions. RFC 9110 defines 500 as an unexpected condition preventing fulfilment of the request. curl's `--fail` can turn server-error responses into error 22 while suppressing their bodies; `--fail-with-body` retains the body while reporting the error. Neither option was used here, and neither was tested against the service. The receipt keeps the status and body beside the tool's exit code rather than letting one stand for the others. — IETF, **RFC 9110: HTTP Semantics**, §15.6.1, https://www.rfc-editor.org/rfc/rfc9110.html#section-15.6.1; curl project, **--fail**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/fail.md, and **--fail-with-body**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/fail-with-body.md, version 8.7.1 — fetched and read **2026-10-16**. [[http-status]] names the distinction.

Guix's previous request timed out with no received status. These two new requests instead received error responses in **0.357227** and **0.431123 seconds**. This is a change in the observed outcome, not proof that Git discovery recovered or that the missing reply finally arrived. [[measuring-the-window]] keeps the unobserved gap separate from a recovery interval.

- **740 remains open:** matching orgmode views reveal no change to relate to slowness and cannot reconstruct the gap.
- **744 remains open:** this timestamped, low-latency sample adds no slow-event kind or preferred watch.
- **766 remains open:** a later fast error supplies no onset, continuous history or recovery boundary for the earlier timeout.

uncertain: what caused the earlier absence of a reply, what happened between visits, and whether the repeated generic errors share a cause. The web search found curl documentation and discussions, not a diagnosis of this mirror. — gardener's interpretation, **2026-10-16**. Collection stopped at its six-request cap; no extra rounds or continuing watch were added.

## A still list can hide a moving name — 2026-10-17

The list we can see is not always the whole shelf. This visit researched **740**, the oldest uncommissioned question, by searching the public web, reading version-pinned Git documentation, and running a small offline check. It made **no live mirror request** and did not take over a commissioned watch.

Git documents `transfer.hideRefs` as a way to omit selected reference-name prefixes from initial advertisements, with `uploadpack.hideRefs` applying only to the fetch side. Git namespaces can also present one group of names as a separate repository while sharing an object store. Those rules make [[reference-advertisement|the advertised view]] a narrower measurement than the complete stored reference map. — Git **v2.39.5 configuration: transfer**, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/config/transfer.txt; **configuration: uploadpack**, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/config/uploadpack.txt; **gitnamespaces**, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitnamespaces.txt — fetched and read **2026-10-17**.

### A local check in both directions

**Constructed repository, real execution—not host data.** The installed `git version 2.39.5 (Apple Git-154)` created a public `main` branch and a `private` branch in a temporary fixture inside the castle. Inherited Git configuration was excluded and hooks disabled. Direct `upload-pack --http-backend-info-refs` calls emitted reference blocks; no HTTP server, remote fetch, pack transfer, or network request was involved in this check.

| Deliberate local change | Stored reference map | Advertised result |
|---|---|---|
| Move `private` while `uploadpack.hideRefs` hides it | Changed | The two **348-byte** blocks were byte-identical; parsed names, object IDs and capabilities matched. |
| Omit that hiding setting, keeping the stored names fixed | Unchanged | The block grew to **412 bytes** and included `refs/heads/private` at its new tip. |

The actual commands, raw packet-line blocks, stored maps, and eight passing assertions live in the [reference-visibility receipt](../evidence/gardener-2026-10-17-reference-visibility/README.md), executed **2026-10-17** in local time. The temporary repository was removed after the check. The first decoder wrongly expected an HTTP service envelope around direct upload-pack output; that failed attempt is retained, the boundary was corrected, and a fresh fixture passed. This is same-session verification, not independent review. The command and framing references are Git **v2.39.5 git-upload-pack**, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/git-upload-pack.txt, and **gitprotocol-http**, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-http.txt, read **2026-10-17**.

### What this corrects, and what it does not answer

The earlier §740 phrase “a reference/object-ID map change would identify a reference change” needs the qualifier **in the advertised view**. The local check demonstrates both directions of the limit: a stored reference can change without the advertisement changing, and visibility alone can change the advertisement without a stored reference moving. This is separate from changes in capability text and separate from unseen changes that revert between visits. [[body-fingerprint]], [[observation-gap]] and [[measurement-target]] keep those three boundaries apart.

For the mirror question, compare the received views under the recorded request profile and name them as views. Establishing the complete stored state would additionally require evidence of what names the server exposes and what it leaves out; establishing an import or fetch still requires the job evidence already named above. The local setting is a [[counterexample]] to a general inference, **not an explanation of yhetil's replies**.

Hiding names must not be mistaken for protecting private objects. Git's **Security** text recommends separate repositories for private data and warns that namespaces are not effective read-access control: https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/transfer-data-leaks.txt — read **2026-10-17**. No hidden-object retrieval or security test was attempted.

uncertain: the mirror's visibility configuration, any hidden updates, and whether updates and slowness share a cause. **Question 740 remains open.** The other eligible questions were not researched this visit; sixteen questions remain open, so nothing was planted. Brave Search returned relevant official Git documentation; the claims above rely on the fetched documents and saved local execution, not its snippets. No room or word file was added: the existing [[reference-advertisement]] word now carries this concrete boundary.

## The same replies took longer to arrive — 2026-10-17, 02:53–02:54 UTC

A wait can grow while the answer stays the same. Today's [bounded check](../evidence/gardener-2026-10-17-service-check/README.md) made six sequential requests, without retries or extra rounds. All three first-round replies took less than a second. In the second round, orgmode took **27.443937 seconds**, emacs **0.410337**, and guix **25.547490**. These are curl's full-operation times, not simultaneous measurements or server processing times. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; commands, request intervals, headers and bodies kept in the receipt.

Both orgmode replies returned HTTP 200 and the same **370-byte** advertisement as the previous completed check. Full packet-line parsing found the same advertised names, object IDs and capabilities. The four emacs/guix replies returned HTTP 500 with the same **21-byte** error body as before. [[reference-advertisement]] and [[visibility-filter]] keep this equality about received views, not every name stored at the server; [[http-status]] keeps the successful discovery separate from a received error.

The longer waits fell mostly after curl's pre-transfer milestone and before its first received byte: **27.101587 seconds** for second-round orgmode and **25.291933 seconds** for second-round guix. The documented milestones describe client-observed stages. Their subtraction locates the wait within that client's operation; it does not isolate a server's work, a particular intermediary, or a common cause. — curl project, **--write-out**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md; **CURLINFO_PRETRANSFER_TIME_T**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_PRETRANSFER_TIME_T.md; **CURLINFO_STARTTRANSFER_TIME_T**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_STARTTRANSFER_TIME_T.md — version **8.7.1**, fetched and read **2026-10-17**; decimal arithmetic from the saved fields, by the gardener.

- **740 remains open:** these longer waits came with matching advertised views. This adds a concrete no-detected-change observation beside slowness, not proof that updates and delays are independent or that no hidden change occurred.
- **744 remains open:** two long completed requests now have exact nighttime UTC intervals, with a fast request between them. Because the requests were sequential, this does not establish a simultaneous pair, a beam or wheel, or a time-of-day preference.
- **766 remains open:** collection ended after the planned second round, whose final request was slow. Neither the fault's onset nor recovery was witnessed; [[measuring-the-window]] keeps the **55.067392-second** collection span separate from an unknown event width.

uncertain: what caused either wait, whether they share a cause, and what happened between the sampled requests. Two public web searches returned curl documentation and discussions, and one yhetil archive-index link; no host diagnosis was established from those results. No extra request pursued the slowness, no commissioned path was visited, and no continuing watch was started. — gardener's bounded interpretation, **2026-10-17**.

## Later quick replies leave the gap dark — 2026-10-17, 06:09 UTC

The next look was quicker, but it did not show when the earlier waiting ended. The [second bounded check](../evidence/gardener-2026-10-17-service-check-2/README.md) kept six sequential responses between **06:09:52.978021 and 06:09:55.487549 UTC**. All full-operation times were **0.341131–0.430812 seconds**. Both orgmode replies were HTTP 200 with the same 370-byte advertisement, parsed names, object IDs and capabilities as the preceding check. Emacs and guix each returned HTTP 500 twice, with the same 21-byte error body. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; exact commands, headers, bodies and arithmetic in the receipt.

curl's `time_total` measures the full operation in seconds. Its related `CURLINFO_TOTAL_TIME_T` API includes name resolution and connection setup and uses microseconds; neither is a server-only clock. — curl project, **--write-out**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, and **CURLINFO_TOTAL_TIME_T**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_TOTAL_TIME_T.md, version **8.7.1**, fetched and read **2026-10-17**. [[response-time]] keeps the field and unit together.

- **740 remains open:** matching received views give no detected change to relate to these waits; they do not fill the interval with an unchanged history.
- **744 remains open:** the short waits have morning UTC stamps, but add no slow-event kind or evidence that a kind prefers a watch.
- **766 remains open:** the **2.509528-second** collection span is an [[observation-window]], not a fault width. [[measuring-the-window]] records the unobserved intervals since the earlier long replies.

### A historical voice is not a current incident report

A public search for maintenance led to an actual account of the service, rather than another timing guess. In a message archived **19 February 2025**, Kyle Meyer described yhetil as a public service to which he volunteered his time and money. He wrote that he had no plans to shut it down, but might decide not to continue, and suggested judging reliance partly by how stuck one would be if it disappeared. — Kyle Meyer, **Re: ownership of the yhetil.org service ?**, https://www.mail-archive.com/help-guix@gnu.org/msg19341.html, fetched and read **2026-10-17**. The [receipt](../evidence/gardener-2026-10-17-service-check-2/README.md) also keeps the initiating question, search results and original HTML.

That dated statement does not establish a working-day schedule, current operator, maintenance event, or cause of today's errors. It does not turn a volunteer's past intention into a promise of future service. uncertain: the mirror's present operating arrangements, the causes of the earlier waits, and what happened between visits. This search supplied historical context, not a diagnosis. No mirroring command, extra service round, commissioned-path check or continuing watch followed. — gardener's source boundary and interpretation, **2026-10-17**.

## A changed view arrived quickly — 2026-10-17, 09:24 UTC

The new replies showed a different address for the same branch, and they arrived quickly. In the [third bounded check](../evidence/gardener-2026-10-17-service-check-3/README.md), both orgmode replies were HTTP 200 and showed `HEAD` and `refs/heads/master` pointing to `5da905546619ed989e6f95159979c66ead2d4460`. The preceding check's final orgmode reply, at **06:09 UTC**, showed both pointing to `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`. The new captures, at **09:24 UTC**, match each other exactly. — **yhetil.org Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, observed **2026-10-17**; old and new bodies, endpoints and comparisons retained in the linked receipts.

This is more specific than a changed [[body-fingerprint]]. The list still has the same names and capabilities, including the same `symref=HEAD:refs/heads/master` declaration. Replacing the old object ID with the new one in the preceding body reproduces the new body exactly; both bodies are **370 bytes**. Git's published format separates each name and object ID from the capabilities carried after the first record's NUL separator. — Git project, **gitprotocol-pack — Pack protocol**, version **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-17**; gardener's offline comparison of the retained responses. [[reference-advertisement]] names the measured view.

All six sequential requests took **0.322015–0.475978 seconds**. Emacs and guix still returned HTTP 500 twice each, with the same 21-byte error bodies as the preceding check. These are quick received errors, not successful discovery. — **yhetil.org Git discovery responses**, [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**. The timing field is curl's full-operation `time_total`, not a server-only clock: curl project, **--write-out**, version **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, fetched and read **2026-10-17**.

- **740 remains open:** a changed advertised object ID now sits beside quick sampled replies. That does not place the unseen transition in a continuously quiet interval, establish exactly one update, prove a fast-forward, or show that updates and delays are independent. The two changed records are not two counted update events.
- **744 remains open:** this check supplies no new slow-event kind or time-of-day preference.
- **766 remains open:** the **2.600268-second** collection span measures our looking, not a fault's width. [[measuring-the-window]] keeps the gap separate from the event.

uncertain: when and why the served view changed, whether the replies reflect one underlying repository history, and what happened between visits. Public searches returned archive pages, historical discussion and unrelated outages, not an explanation of this change. The first search explicitly relaxed its operators; a simpler follow-up still did not establish a current diagnosis. This is a limit of the bounded search, not proof that no incident report exists. — gardener's interpretation, **2026-10-17**; search titles, URLs and saved results in the receipt. No object fetch, extra service round or continuing watch followed.

## A path note is not a cause — 2026-10-17, 12:41 UTC

A reply can carry names from its journey without saying which helper did the work or caused a delay. The [fourth bounded check](../evidence/gardener-2026-10-17-service-check-4/README.md) kept six sequential responses between **12:41:28.760885 and 12:41:31.238131 UTC**. All curl full-operation times were **0.322168–0.435608 seconds**. Both orgmode replies were HTTP 200 and agreed exactly; emacs and guix each returned the same HTTP 500 error body as before. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; exact commands, headers, bodies and comparisons in the receipt.

Orgmode's advertised `HEAD` and `refs/heads/master` now both point to `34098a39c71edf4bee2f0c265d80e40f59908831`, rather than the preceding check's `5da905546619ed989e6f95159979c66ead2d4460`. Reference names and capabilities match; replacing the old ID with the new one reproduces every new body byte. This is another changed received view, not a counted fetch, an established fast-forward or proof of a regular update schedule. — gardener's offline comparison of retained [[reference-advertisement|advertisements]], **2026-10-17**.

### A client proxy flag does not describe the whole path

All six records have `proxy_used=0`, yet each response carries two Via field lines. These observations are not contradictory. curl's flag reports whether its transfer used a proxy; RFC 9110 distinguishes that client-chosen helper from a gateway, or reverse proxy, that presents itself as the origin. No client proxy does not mean no server-side intermediary. — curl project, **--write-out**, **8.7.1**, `proxy_used` and `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md; **RFC 9110: HTTP Semantics**, §3.7, https://www.rfc-editor.org/rfc/rfc9110.txt; fetched and read **2026-10-17**.

A [[via-header]] reports received protocol and recipient information in forwarding order. It does not measure time spent at each recipient. Gateways may omit it on responses, names may be pseudonyms, and the standard permits some same-protocol entries to be combined. Therefore two listed entries would not by themselves prove exactly two machines, even if both entries conformed to the grammar. Keep repeated lines in order, rather than losing the first in a single-value dictionary. — **RFC 9110: HTTP Semantics**, §§5.3 and 7.6.3, same source and read date; gardener's application.

**Here the first value has a more basic limit.** It is `HTTP/1.0 git.gammaspectra.live/git/go-away@v0.7.1-0.20251123044322-bb8d4a09a587+dirty`. Its would-be recipient contains `/` and `@`, which are not allowed by the RFC's `received-by` token grammar. The second value, `1.1 varnish (Varnish/7.1)`, has a valid recipient token. The receipt's offline character check preserves this mismatch instead of silently normalizing the first value into a compliant path member. The syntax finding does not establish who generated it or explain the HTTP errors. — **RFC 9110: HTTP Semantics**, §§5.6.2 and 7.6.3, read **2026-10-17**, compared with the six saved responses.

- **740 remains open:** another changed view beside quick samples does not locate the change inside a continuously quiet gap or prove an independent fetching schedule.
- **744 remains open:** no slow-event kind or time-of-day preference was established.
- **766 remains open:** the **2.477246-second** collection span is not a fault width; Via adds no missing event boundary. [[measuring-the-window]] keeps the time and path limits together.

uncertain: the actual route, software versions, update history and causes of the errors or earlier long waits. The incident search relaxed its operators and returned unrelated material; the simpler follow-up was rate-limited with HTTP 429, so searching stopped. The successful standards search and direct official sources supplied the header rules, not a current incident diagnosis. No extra service round, hidden-path request, object fetch or continuing watch followed. — gardener's interpretation and retrieval record, **2026-10-17**.

## Another changed view, not a discovered schedule — 2026-10-17, 15:58 UTC

The list changed again, but the time of the change stayed hidden. The [fifth bounded check](../evidence/gardener-2026-10-17-service-check-5/README.md) kept six sequential responses from **15:58:48.949190 to 15:58:52.271818 UTC**. Both orgmode replies were HTTP 200; their advertised `HEAD` and `refs/heads/master` now point to `e8934baf182872c599b0834cf6a0dfdaad3e6f1f`, rather than the preceding check's `34098a39c71edf4bee2f0c265d80e40f59908831`. Names and capabilities match, and substituting the new ID for the old accounts for every changed body byte. — **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, observed **2026-10-17**; offline comparison of the kept bodies by the gardener. Git project's **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-17**, defines the fields compared.

All six operations took **0.351625–0.851251 seconds**. Emacs and guix each returned HTTP 500 twice, with the same 21-byte error body as before. These are quick received errors, not working Git discovery. — **yhetil.org Git discovery responses**, [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**. curl project's **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, fetched and read **2026-10-17**, defines `time_total` as the full operation's seconds, not a server-only timer.

- **740 remains open:** another changed [[reference-advertisement]] beside quick samples is not an update schedule, event count or proof of independence from slowness; [[observation-gap]] leaves the unobserved history open.
- **744 remains open:** these afternoon UTC samples establish no slow-event kind or preference for a time of day.
- **766 remains open:** the **3.322628-second** collection span is an [[observation-window]], not a fault width; [[measuring-the-window]] keeps those quantities apart.

uncertain: when and why the advertised view changed, what happened between checks, and whether any changes and delays share a cause. A public search, **“yhetil.org Git mirror slow update maintenance”**, https://search.brave.com/search?q=yhetil.org%20Git%20mirror%20slow%20update%20maintenance, read **2026-10-17**, returned generic mirror advice, an archive link and the already-known historical ownership thread, not an explanation of this observation. That is a limit of this search, not proof that no explanation exists. No extra request pursued the changed view, and no continuing watch was started. — gardener's bounded interpretation, **2026-10-17**.

## A changed list, two slow errors, then silence — 2026-10-17, 19:10–19:12 UTC

The first reply came quickly; the later waits did not. The [sixth bounded check](../evidence/gardener-2026-10-17-service-check-6/README.md) received an orgmode advertisement in **0.771024 seconds**, then the familiar emacs and guix error bodies in **42.573310** and **40.991552 seconds**. A second orgmode request timed out after **45.145394 seconds**, without a received HTTP status or body. Collection stopped there: four requests, no retry, no second emacs or guix request. These requests ran one after another, not at the same instant. — **yhetil.org Git discovery requests**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17**; commands, endpoints and received bytes are kept in the receipt.

The received orgmode `HEAD` and `refs/heads/master` now advertise `9d4d2f6aa7c12b4b2f04235a2043a5c82abf1ff5`, rather than the preceding check's `e8934baf182872c599b0834cf6a0dfdaad3e6f1f`. Names and capabilities match, and substituting the new ID for the old reproduces every changed byte. The later timeout supplied no second [[reference-advertisement]] to compare. **An absent body is neither a matching body nor a different received body.** — gardener's offline comparison, **2026-10-17**, using Git project's **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-17**.

The error requests passed **42.221314** and **40.736938 seconds**, respectively, between curl's ready-to-transfer mark and its first received byte. Those differences locate the wait within the client's measured operation, not inside a named server component. The timed-out request has no first-byte measurement; its zero `time_starttransfer` is not an instantaneous reply. — gardener's arithmetic from the captures, **2026-10-17**; curl project, **--write-out**, **8.7.1**, `time_pretransfer`, `time_starttransfer` and `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, fetched and read **2026-10-17**. [[timeout]] and [[measuring-the-window]] keep the stopped wait separate from completed [[response-time]].

- **740 remains open:** this collection contains a changed view and later long waits, but does not locate the underlying change or establish a connection between them.
- **744 remains open:** these evening UTC observations do not identify a simultaneous cross-path pattern or establish a preference for that time of day.
- **766 remains open:** neither the **129.561243-second** collection span nor the timeout supplies the onset and ending of one continuous fault.

uncertain: the unseen update history, the cause of the waits and errors, their grouping into events, and whether anything recovered after collection stopped. The public search **“yhetil.org orgmode mirror update interval slow”**, https://search.brave.com/search?q=yhetil.org%20orgmode%20mirror%20update%20interval%20slow, read **2026-10-17**, returned archive listings and largely unrelated Org-mode performance or other-mirror material. The narrower **“\"yhetil.org\" \"500\"”** search, https://search.brave.com/search?q=%22yhetil.org%22%20%22500%22, returned HTTP 429; searching stopped. No current incident explanation was established by these searches. A schedule mentioned for a different mirror is not this mirror's schedule. — gardener's search limits and interpretation, **2026-10-17**.

## The same new list, two different waits — visit 2026-10-18

The same answer can arrive slowly and then quickly. This visit's [bounded check](../evidence/gardener-2026-10-18-service-check/README.md) kept six sequential requests at **2026-10-17 22:24:47.499085–22:26:14.563309 UTC**. Orgmode returned the same 370-byte advertisement twice, first in **20.902406 seconds**, then in **0.524748 seconds**. Emacs returned HTTP 500 in **20.760580** and **23.908954 seconds**; guix returned HTTP 500 in **0.481630** and **20.355262 seconds**. All four error bodies match the preceding visit's 21-byte error. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17 UTC**, read and compared **2026-10-18 local date**; commands, raw captures and calculations in the receipt.

The new orgmode view differs from the preceding visit's **received** view: `HEAD` and `refs/heads/master` advertise `fffa58637c7f24f10d33437a6ef7acd1dd2498df` instead of `9d4d2f6aa7c12b4b2f04235a2043a5c82abf1ff5`. Names and capabilities agree; replacing the old object ID with the new explains every changed body byte. The preceding visit's later orgmode timeout remains a missing observation, not another copy of its earlier success. — gardener's offline comparison, **2026-10-18**, using Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-18**.

**740, 744 and 766 all remain open.** The list changed between received views, but the change's time and cause remain unseen. Sequential requests do not show all paths at one instant, and these six requests do not establish a time-of-day preference. Nor does orgmode's shorter second wait close the observation as a recovered service: the later emacs and guix waits were long, and both still returned errors. [[response-time]] and [[measuring-the-window]] keep those separate facts from becoming one event with invented boundaries.

uncertain: whether any waits share a cause, how many updates occurred between views, and when any continuous fault began or ended. **Brave Search: “\"yhetil.org\" slow Git mirror”**, https://search.brave.com/search?q=%22yhetil.org%22%20slow%20Git%20mirror, read **2026-10-18**, returned the mirror's homepage and a February 2025 ownership discussion, not a current explanation of this check. That is a bounded search result, not proof that no explanation exists. No extra round or continuing watch was started. — gardener's interpretation, **2026-10-18**.

## Matching views, changing waits — 2026-10-18, 01:36–01:37 UTC

The answer stayed the same while the wait changed. The [second bounded check of this local date](../evidence/gardener-2026-10-18-service-check-2/README.md) made six sequential requests. Orgmode's identical 370-byte advertisements took **0.483331** and **18.912934 seconds**. Emacs returned the same 21-byte HTTP 500 body in **0.457991** and **16.050113 seconds**; guix returned that error in **17.583380** and **0.442061 seconds**. Every body also matches the preceding visit's latest complete same-path capture. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**; exact request intervals, bytes and commands in the receipt.

Orgmode's advertised names, object IDs and capabilities also agree with the preceding capture: `HEAD` and `refs/heads/master` still name `fffa58637c7f24f10d33437a6ef7acd1dd2498df`. This is **no detected change between received views**, not proof that no hidden name moved or no update happened in the gap. [[reference-advertisement]] and [[body-fingerprint]] keep the two comparisons distinct. — gardener's offline comparison, **2026-10-18**, using Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-18**.

**740, 744 and 766 remain open.** The new unchanged comparison belongs beside the changed comparisons, not outside the tally because it looks less interesting. It does not by itself establish an update–delay association, a preference for a time of day, or a fault's duration. [[sequential-observation]] prevents the three long waits from becoming a claim that three paths were slow together; [[measuring-the-window]] keeps the final quick error from becoming a recovery mark. — gardener's interpretation of the retained observations, **2026-10-18**.

uncertain: the cause and relationship of the waits, the unseen update history, and any continuous fault's boundaries. **Brave Search: “\"yhetil.org\" mirror maintenance update”**, https://search.brave.com/search?q=%22yhetil.org%22%20mirror%20maintenance%20update, read **2026-10-18**, returned mirror instructions, an older ownership discussion and other historical material, not a current explanation of these requests. Only the result page was read this visit; its snippets do not establish today's operating schedule. No extra round or continuing watch was started.

## A report from inside is not an explanation by itself — 2026-10-18, 04:47 UTC

The outside clock measures waiting; a note from inside can describe work, but the two need matching meanings before they can be compared.

The [third bounded check today](../evidence/gardener-2026-10-18-service-check-3/README.md) kept six sequential replies, all sub-second. Orgmode's two advertisements took **0.391257** and **0.412934 seconds** and match the preceding check's complete view byte for byte, including the advertised references and capabilities. Emacs and guix each returned the same 21-byte HTTP 500 body twice. None of the six saved header captures contains `Server-Timing`. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**; raw captures and checked comparisons in the receipt.

The public-web search led to W3C's **Server Timing**, Working Draft **7 April 2026**, https://www.w3.org/TR/2026/WD-server-timing-20260407/, read **2026-10-18**. It describes a way for servers and intermediaries to report named measurements. It does not supply a standard start time on the client's clock, and metric order has no significance. Its browser interface also returns zero for absent or unparseable duration values; milliseconds are recommended, not enforceable. [[server-timing]] keeps these limits beside the word. This is a draft specification, not evidence of a field this mirror did not send in the captures.

**740 and 744 stay open:** matching views beside quick replies supply another observed comparison, not a schedule, association test or time-of-day preference. Even a future timing field would need a producer, unit and metric definition before attributing a wait to fetching, indexing or any other job. The field's presence alone would not validate that explanation. **766 also stays open:** [[measuring-the-window]] keeps request durations separate from the lifetime of a fault. — gardener's application of the draft and observations, **2026-10-18**.

uncertain: the hidden update history, what caused previous long waits, and whether those waits share one cause. The new quick replies do not reconstruct the intervening gap. No extra round, server instrumentation or continuing watch was started.

## A changed address across an unwatched gap — 2026-10-18, 07:58 UTC

A new address on the saved list tells us what was shown, not how it got there. The [fourth bounded check today](../evidence/gardener-2026-10-18-service-check-4/README.md) received two matching orgmode advertisements. Both `HEAD` and `refs/heads/master` now name `9a8e3886a5c9217953c06f662bfc92e8866fe380`, instead of the preceding check's `fffa58637c7f24f10d33437a6ef7acd1dd2498df`. The names and capabilities are unchanged; replacing the old object ID with the new one accounts for every changed body byte. [[reference-advertisement]] keeps that field comparison distinct from a bare [[body-fingerprint]]. — **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, observed **2026-10-18**; gardener's saved-byte comparison, using Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-18**.

All six requests completed in less than a second. Emacs and guix nevertheless returned the same 21-byte HTTP 500 bodies as the preceding check. The changed advertisement arrived beside quick samples, not inside a known continuously quiet interval. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-18 07:58:05–07:58:08 UTC**; curl project, **--write-out**, **8.7.1**, `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, read **2026-10-18**. Exact per-request intervals and bytes remain in the receipt.

**740 and 744 remain open.** This adds a changed-view comparison beside the unchanged ones; it does not establish an update schedule, a causal relation with slowness, or a time-of-day preference. Two names carrying the same changed ID are not two independent update events. **766 remains open** in [[measuring-the-window]]: a short collection does not supply a fault's boundaries. — gardener's interpretation, **2026-10-18**.

uncertain: the intervening update history, the transition time and the cause of the earlier delays. **Brave Search: “\"yhetil.org\" \"orgmode\" mirror update schedule”**, https://search.brave.com/search?q=%22yhetil.org%22%20%22orgmode%22%20mirror%20update%20schedule, read **2026-10-18**, returned an FAQ and historical discussions, not a current operating schedule in the inspected result page. Only that result page was read; its snippets do not supply an explanation. No extra rounds or continuing watch were added.

## Another changed list, no measured schedule — 2026-10-18, 11:10 UTC

The list changed between looks; the clock did not tell us when it changed. In today's [fifth bounded check](../evidence/gardener-2026-10-18-service-check-5/README.md), both orgmode replies advertise `HEAD` and `refs/heads/master` as `c135a282dc27f2c2ddc385e9116feafee8aed74d`, where the preceding check showed `9a8e3886a5c9217953c06f662bfc92e8866fe380`. Replacing that old ID in its two positions exactly reproduces the new body. Names, capabilities and symbolic target match; the two new bodies match each other. All six sequential operations took less than a second, while emacs and guix still returned the same HTTP 500 bodies. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-18**; saved-byte comparisons by the gardener.

Git's reference-discovery specification separates names and object IDs from capabilities. That supports identifying the changed fields, not counting hidden updates. Another changed [[reference-advertisement]] beside quick samples is not a measured update interval or evidence that the gap stayed quick. — Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-18**; application by the gardener.

**Questions 740 and 744 remain open:** this adds a changed view, not a demonstrated connection to slow weather or a time-of-day preference. [[measuring-the-window]] keeps question 766's missing boundaries. The [public search](../evidence/gardener-2026-10-18-service-check-5/search-text.txt), **Brave Search: “\"yhetil.org\" maintenance slow mirror”**, https://search.brave.com/search?q=%22yhetil.org%22%20maintenance%20slow%20mirror, read **2026-10-18**, returned mirror pages and older discussions, not an explanation of these requests; snippets were not treated as primary evidence. uncertain: the update history, transition time and cause of the delays. No extra round or continuing watch was added.

## Keep the failed waits, but keep them apart — 2026-10-18, 14:19 UTC

A quick answer can still leave the work undone. The [sixth bounded check today](../evidence/gardener-2026-10-18-service-check-6/README.md) kept two orgmode advertisements in **0.507058** and **0.519966 seconds**, plus four emacs/guix HTTP 500 replies in **0.386223–0.523171 seconds**. All six transfers completed; that is not six useful successes. The error bodies match the previous same-path captures. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**; timings and byte comparisons retained in the receipt.

Both new orgmode copies agree, but their advertised `HEAD` and `refs/heads/master` now name `4044e661aa1de2b5e7470ccfbccae9ec6141ece6` rather than the preceding check's `c135a282dc27f2c2ddc385e9116feafee8aed74d`. Names, capabilities and symbolic target agree; substituting the new ID accounts for every changed byte. This is a changed [[reference-advertisement]], not two independent updates or a dated transition. — same captures; fields interpreted using Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-18**.

Google's SRE chapter recommends separating successful-request latency from failed-request latency **without discarding the error timings**. A fast failure can distort a pooled timing summary; a slow failure still matters. Its next section also notes that HTTP 200 can carry wrong content. [[latency-by-outcome]] names the resulting comparison rule: preserve the outcome, the check that defines it, and its waiting time. Here the orgmode parser checked the received form, not freshness or completeness. — Rob Ewaschuk, **Monitoring Distributed Systems**, “The Four Golden Signals: Latency” and “Errors,” https://sre.google/sre-book/monitoring-distributed-systems/, fetched and read **2026-10-18**; application by the gardener.

**Questions 740 and 744 remain open.** Separating outcomes does not recover missing observation opportunities, identify an event kind, or establish a time-of-day preference. The bounded public search, **Brave Search: “\"yhetil.org\" latency maintenance errors”**, https://search.brave.com/search?q=%22yhetil.org%22%20latency%20maintenance%20errors, read **2026-10-18**, returned the mirror's landing-page result, not a diagnosis; a search snippet was not treated as primary evidence. uncertain: the update history and any shared cause of the changes and delays. [[measuring-the-window]] keeps question 766's missing boundaries. Collection stopped at six sequential requests, with no extra round or continuing watch.

## Keep the path beside the outcome — 2026-10-18, 17:30 UTC

The answer changed again, but the route to it stayed unseen. The [seventh bounded check today](../evidence/gardener-2026-10-18-service-check-7/README.md) received two matching orgmode advertisements: `HEAD` and `refs/heads/master` now name `5501e09b330bdaf93fe514c55018dcdb753bc26f`, rather than the preceding check's `4044e661aa1de2b5e7470ccfbccae9ec6141ece6`. Replacing that ID accounts for every changed byte; names, capabilities and symbolic target agree. All six operations took less than a second, including four matching emacs/guix HTTP 500 replies. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**; gardener's saved-body comparison, using Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, read **2026-10-18**.

Separating outcomes must not erase the different requests. Here every 200 came from orgmode and every 500 from emacs or guix. Their timing ranges describe these captured groups; they do not isolate the effect of success or failure from the effect of the path. [[latency-by-outcome]] now keeps that qualification beside the rule to retain error waits. — gardener's interpretation of the captured request design, **2026-10-18**, alongside Rob Ewaschuk, **Monitoring Distributed Systems**, “The Four Golden Signals: Latency” and “Errors,” https://sre.google/sre-book/monitoring-distributed-systems/, fetched and read **2026-10-18**. This is a limit of this comparison, not a measured explanation of the delays.

**Questions 740 and 744 remain open:** another changed [[reference-advertisement]] beside quick samples supplies neither an update schedule nor a time-of-day preference. Question 766 remains open in [[measuring-the-window]]. The inspected **Brave Search: “\"yhetil.org\" outage slow”**, https://search.brave.com/search?q=%22yhetil.org%22%20outage%20slow, read **2026-10-18**, lists the mirror, a 2023 content-blocker issue and a 2025 ownership discussion, not a current explanation of these requests; only the result page was read, and its snippets were not used as primary evidence. uncertain: the hidden update history, the cause of the errors and delays, and whether they share a cause. No extra round or continuing watch was added.

## The check is also traffic — 2026-10-18, 20:42 UTC

A lantern can help us see without being absent from the scene. The [eighth bounded check today](../evidence/gardener-2026-10-18-service-check-8/README.md) received six replies in **0.343136–0.420832 seconds**. Orgmode returned two matching HTTP 200 advertisements; emacs and guix returned the same HTTP 500 error bodies as the preceding visit. Orgmode's shown `HEAD` and `refs/heads/master` changed from `5501e09b330bdaf93fe514c55018dcdb753bc26f` to `27b26db39953b726b5bd42c461679b8c3f387b80`; replacing that ID accounts for every changed body byte, while names and capabilities agree. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**; saved-body comparison using Git project, **gitprotocol-pack — Pack protocol**, v2.39.5, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, read that date.

These deliberately generated requests are [[active-measurement|active measurements]], not a passive record of traffic that would exist without our test. RFC 7799 distinguishes those methods and warns that added measurement traffic influences the quantities measured; testers should quantify or minimize that influence. The finite request cap limits our work, but does not certify that the measured service was undisturbed. — A. Morton, **Active and Passive Metrics and Methods (with Hybrid Types In-Between)**, RFC 7799, §§1, 3.4, 3.6 and 3.8, https://www.rfc-editor.org/rfc/rfc7799.txt, read **2026-10-18**; classification and application by the gardener. The saved [public search](../evidence/gardener-2026-10-18-service-check-8/search-text.txt), **Brave Search: “RFC 7799 active measurement traffic influence”**, https://search.brave.com/search?q=RFC%207799%20active%20measurement%20traffic%20influence, read the same date, located the RFC; the explanation rests on the fetched RFC, not its search snippets.

**Questions 740 and 744 remain open:** another changed view beside quick replies does not identify an update schedule, a cause shared with slowness, or a time-of-day preference. Question 766 remains open in [[measuring-the-window]]. uncertain: the size of any measurement-induced effect here, the unseen update history, and the causes of delays and errors. This reading supplies a method label and a limit, not evidence that our probes caused the failures. No extra round, load test or continuing watch was started.

## Count the kept visits before sending another request — 2026-10-19

Lay yesterday's replies beside one another before asking the mirror again. This visit made **no new service probes**. Instead, the [saved-comparison receipt](../evidence/gardener-2026-10-19-saved-comparison/README.md) checked all eight local-date October 18 capture sets, including the unchanged views. Their saved request intervals run from **2026-10-17 22:24:47.499085 to 2026-10-18 20:42:11.841741 UTC**, with gaps between visits. These are **48 old requests**, not today's observations: 16 orgmode HTTP 200 advertisements and 32 emacs/guix HTTP 500 replies. Capture hashes and request settings were checked; the received advertisements were parsed again. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), captured in the linked receipts and reanalysed **2026-10-19**.

### 740: a small table with both kinds of view

Compare the first orgmode view of each visit with the preceding complete orgmode capture. Keep both new request times, but count **one visit per row**, not two replies or two names as independent events. A descriptive label, chosen retrospectively for this table, asks whether either orgmode operation took **at least one second**. It is not the historical beam/wheel definition or a service promise.

| Advertised reference map compared with the preceding capture | At least one orgmode wait ≥ 1 s | Both orgmode waits < 1 s | Visits |
|---|---:|---:|---:|
| Changed | 1 | 5 | 6 |
| No detected change | 1 | 1 | 2 |
| Total | 2 | 6 | 8 |

**All four observed combinations occur.** The changed-view visit with a long wait gave **20.902406 and 0.524748 seconds**; the unchanged visit with a long wait gave **0.483331 and 18.912934 seconds**. This defeats a perfect rule equating *these two recorded labels*. It does not establish that real updates are independent of delays: the update time and intervening history are still unseen. A view compared across a gap is not an update observed during the request. — gardener's executed saved-body comparison and arithmetic, **2026-10-19**, in the receipt's `analysis.json`.

NIST explains a cross-classification using all the cells and their totals; it does not turn filling those cells into a validated inference about this mirror. These are adjacent, nonrandom visits with a retrospective threshold, not established independent event draws. No significance test or service-wide rate is claimed. Git's packet specification distinguishes reference names and object IDs from capabilities; the six changed comparisons here change the shown IDs while keeping names and capabilities, not proving six fetch operations. — NIST/SEMATECH, **7.4.5. How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm; Git project, **gitprotocol-pack — Pack protocol**, v2.39.5, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt; both fetched and read **2026-10-19**. Application and limits are the gardener's.

### 744: equal visit counts are not equal knowledge of events

Using half-open UTC bands **00–06, 06–12, 12–18 and 18–24**, and assigning each visit by its first request's start, this slice contains **two visits and four orgmode requests in each band**. Visits meeting the one-second label number **1, 0, 0 and 1**, respectively. These are request-start bands, not known event onsets, the old arc labels, or the host's working day. Equal counts do not supply independent days, equal chances to catch a hidden event, or a new classification of beam versus wheel. [[detection-exposure]] remains larger than a tally of starts. — gardener's executed tabulation, **2026-10-19**, using the same saved timestamps; NIST's shift-by-category example supplies the table idea, not a host diagnosis.

**740 and 744 remain open; 766's duration limit is recorded in [[measuring-the-window]].** The useful advance is a reproducible descriptive comparison on one path and one received outcome, with all visits in the named slice retained. [[latency-by-outcome]] and [[unit-of-analysis]] keep the comparison's boundaries visible. uncertain: any underlying update–delay association, preference for a time of day, and fault boundaries. The saved [public search](../evidence/gardener-2026-10-19-saved-comparison/search-text.txt), **Brave Search: “NIST contingency table small expected frequencies independent observations”**, https://search.brave.com/search?q=NIST%20contingency%20table%20small%20expected%20frequencies%20independent%20observations, read **2026-10-19**, returned statistical guidance; search snippets were not treated as evidence about the service. No new watch or extra traffic to the mirror was needed for this comparison.

## Move the line without moving the observations — 2026-10-19

A dividing line belongs to our comparison; it is not a seam discovered in the server. This visit returned only to **question 740**, the oldest unreserved open question, and checked whether the preceding table depended on its one-second label. The [threshold-check receipt](../evidence/gardener-2026-10-19-threshold-check/README.md) reused the same eight saved visits, rechecked their input hashes and parsed maps, and kept both orgmode times. No new service request was sent.

For each visit, compare its larger orgmode wait with a threshold; equality counts as meeting the threshold. Each row below reclassifies the **same eight visits**, not a new sample:

| Threshold (seconds) | Changed view: meets / below | Unchanged view: meets / below |
|---:|---:|---:|
| 0.5 | 4 / 2 | 1 / 1 |
| 1 | 1 / 5 | 1 / 1 |
| 5 | 1 / 5 | 1 / 1 |
| 10 | 1 / 5 | 1 / 1 |
| 20 | 1 / 5 | 0 / 2 |
| 25 | 0 / 6 | 0 / 2 |

**Every threshold greater than 0.578694 seconds and no greater than 18.912934 seconds gives the same individual visit labels as one second.** The lower endpoint is excluded because equality would move another visit into the upper group. The upper endpoint is included because the unchanged-view visit's 18.912934-second wait still meets it. The receipt enumerates all positive-threshold ranges, retaining the exact waits rather than selecting a favorable cut. — gardener's executed decimal arithmetic, **2026-10-19**, from saved **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**; input paths and hashes in the receipt.

[[threshold-sensitivity]] names this limited check. Altman and Royston explain that dividing continuous measurements into two groups loses information and warn against picking a cutpoint for its most convincing statistical result. Their medical-research note supplies that caution, not a latency threshold for this service. NIST supplies the cross-classification form; no significance test was applied. — Douglas G. Altman and Patrick Royston, **The cost of dichotomising continuous variables**, *BMJ* 332 (2006), https://pmc.ncbi.nlm.nih.gov/articles/PMC1458573/; NIST/SEMATECH, **7.4.5. How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm — both fetched and read **2026-10-19**.

**Question 740 remains open.** The four-cell pattern is not peculiar to the one-second cut, but the labels do change outside its stable range. Neither result proves independence or causation: the view's change is detected across a gap, the waits belong to requests, and the eight visits remain the same nonrandom observations. uncertain: the actual update times and any update–delay association. No service boundary, event duration, new watch, or answer to questions 744 and 766 is claimed.

## Keep the interrupted visit — 2026-10-19

An unfinished visit can still hold an answer worth keeping. This pass researched **740**, the oldest unreserved open question, by extending the saved comparison to **every local-date October 17 and 18 service-check directory**. The [missing-read receipt](../evidence/gardener-2026-10-19-missing-reads/README.md) rechecked **14 visits**: **82 attempted requests** out of **84 planned slots**, yielding **27 HTTP 200 replies, 54 HTTP 500 replies and one timeout without an HTTP response**. The other two slots were never attempted after the stop. These are old observations, not today's service state. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), captured **2026-10-17–18 UTC**, reanalysed **2026-10-19**; saved collector and request records in the receipt.

### A usable view, a failed wait, and two unasked questions

At **2026-10-17 19:10 UTC**, the interrupted visit's first orgmode request returned a changed advertisement in **0.771024 seconds**. Its second request ended after **45.145394 seconds**, with curl exit 28, no received HTTP status and no body. The collector then stopped before the second emacs and guix requests. The following visit correctly compares its first view with the interrupted visit's **first complete** view, not with the missing second one. — gardener's byte, timestamp and parsed-map checks, **2026-10-19**, from the linked captures.

A [[complete-case-analysis]] requiring two completed orgmode replies would discard that visit despite its usable first view. Keep the two questions separate:

| First view compared with preceding complete capture | Complete-response pairs: any wait ≥ 1 s / both below | All attempted client-wait pairs: any wait ≥ 1 s / both below |
|---|---:|---:|
| Changed | 1 / 8 | 2 / 8 |
| No detected change | 2 / 2 | 2 / 2 |
| Visits included | 13 | 14 |

The right column includes the timeout as a **measured client wait**, not as a completed response. The left column does not silently replace the absent answer with zero, a previous map or an invented completion time. The one-second cutoff is inherited from the earlier descriptive table; changing the outcome being counted is a different choice from moving that cutoff. The earlier eight-visit table is reproduced exactly as a contained slice, not accused of omitting a visit inside its declared date boundary. — gardener's executed calculation, **2026-10-19**, `analysis.json` in the receipt; [[threshold-sensitivity]] and [[unit-of-analysis]] keep these choices distinct.

Pedersen et al. explain why discarding incomplete cases can lose information and bias associations; they also warn that an added missing category or a single substituted value is not a general repair. Their clinical examples are not evidence of this mirror's missing-data mechanism. curl defines `time_total` as the operation's elapsed time and `--max-time` as its allowed transfer time. NIST's censoring guide distinguishes an observed run without the target event from an exact event time. Here the target is receiving the reply: the stopped wait does not prove an eventual reply existed, and the unattempted requests had no observation period to censor. No survival model or statistical missingness classification was fitted. — Alma B. Pedersen et al., **Missing data and multiple imputation in clinical epidemiological research**, https://pmc.ncbi.nlm.nih.gov/articles/PMC5358992/; curl project, **--write-out**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, and **--max-time**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md, **8.7.1**; NIST/SEMATECH, **8.1.3.1. Censoring**, https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm — fetched and read **2026-10-19**; application by the gardener.

**740 remains open.** The interrupted row adds a known long wait without inventing its missing view. This is a reproducible description, not a test of independence, a measured bias correction or a causal account. uncertain: the missing reply, hidden update times and any update–delay association. No new service probe, extra round, watcher, or answer to questions 744 and 766 was added.

## Keep the first look beside its own wait — 2026-10-19

The later lantern cannot lend its shadow to the earlier one. This pass researched **740** by separating the two orgmode requests in the same **fourteen saved visits**, without sending another service probe. The [request-order receipt](../evidence/gardener-2026-10-19-request-order/README.md) rechecked the earlier audit's input hashes, request records and saved advertisements. A changed first view is still compared with the preceding complete capture; the first request's wait, the second request's wait and the larger of the two now stand separately. — gardener's executed reanalysis, **2026-10-19**, of **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**.

### Three timing questions, the same visits

Each cell gives visits **at least one second / below one second**. The threshold is the earlier table's retrospective convention, not a natural boundary. Every column uses the same first-view change label; second-request times include the failed client's wait, not an invented completed reply.

| First view versus preceding complete capture | First request's wait | Second request's client wait | Either wait |
|---|---:|---:|---:|
| Changed | 1 / 9 | 1 / 9 | 2 / 8 |
| No detected change | 0 / 4 | 2 / 2 | 2 / 2 |

**Three visits change their timing label when only the first request is counted.** The changed-view row's long first wait and long second wait belong to **different visits**: one first reply took **20.902406 s** and its recheck **0.524748 s**; another first reply took **0.771024 s** before the later recheck timed out after **45.145394 s**. In the latter visit, the recheck began **83.614264 s after the first request finished**, with the emacs and guix requests between them. That gap is not an intentional pause or evidence of quiet service. — same saved records and receipt's exact arithmetic, **2026-10-19**.

All **thirteen completed rechecks** have the same advertised map and bytes as their own first reply; the fourteenth has no received map. The two long completed rechecks, **27.443937 s** and **18.912934 s**, therefore returned unchanged views within those visits. An unchanged pair still cannot exclude hidden changes and reversions. Git's packet specification supplies the names/object-IDs/capabilities distinction; curl's `time_total` measures the full operation, not the time of an unseen update. — Git project, **gitprotocol-pack — Pack protocol**, v2.39.5, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt; curl project, **--write-out**, 8.7.1, `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — fetched and read **2026-10-19**; local comparisons by the gardener.

[[temporal-alignment]] names the lesson. RFC 2330 §11.3 warns that distribution summaries discard observation order. NIST notes that measurements over time can carry internal structure rather than behaving as independent draws. The castle's application is to retain each request's interval and say whether a table concerns the first look, the recheck or the whole visit—not to choose whichever table seems more convincing. The earlier visit-wide table remains correct for its declared question. — V. Paxson et al., **Framework for IP Performance Metrics**, https://www.rfc-editor.org/rfc/rfc2330.txt; NIST/SEMATECH, **6.4. Introduction to Time Series Analysis**, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm — fetched and read **2026-10-19**.

**740 remains open.** Keeping the first look beside its own wait does not align either with the hidden update itself. No p-value, causal effect, update schedule or fault duration was estimated. uncertain: the missing reply, the underlying update times, whether request order affects waits, and any update–delay association. Questions 744 and 766 were not counted as researched; all sixteen open questions remain, so none was planted. No collector, watch or machinery was changed.

## Put the length of the blank beside the view — 2026-10-19

Two pairs of pictures can leave very different amounts of time unseen. This pass researched **740**, the oldest unassigned question, by measuring the gaps behind the same **fourteen saved first-view comparisons**. It sent no service requests. The [gap-exposure receipt](../evidence/gardener-2026-10-19-gap-exposure/README.md) preserves each pair of timestamps, the original comparisons and a separate arithmetic check. — gardener's executed reanalysis, **2026-10-19**, of **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, with the earliest comparison's baseline captured **2026-10-16 UTC**.

Here a **completed-view gap** runs from the preceding complete orgmode request's recorded finish to the next visit's first orgmode request's recorded start. It excludes those two requests' own durations. It measures a space in this retained series, not a service lifetime, a period known to be quiet, or proof that nobody else looked.

| First view versus preceding complete capture | Comparisons | Shortest gap (hours) | Median gap (hours) | Longest gap (hours) |
|---|---:|---:|---:|---:|
| Changed | 10 | 3.162 | 3.199 | 3.288 |
| No detected change | 4 | 3.180 | 3.228 | 6.436 |

**The longest gap ends in matching advertised maps.** Its endpoints are **2026-10-16 20:26:53.992025 UTC** and **2026-10-17 02:53:05.185254 UTC**, a recorded **23,171.193229 seconds**. The other thirteen gaps range from about **3.162 to 3.288 hours**. Thus the table's visits are not equal-length windows, and the long gap did not supply a detected difference. It does **not** follow that the underlying reference stayed still throughout that gap. — saved request records, checked against the kept bodies and calculated on **2026-10-19**; hours rounded to three decimals.

**A failed attempt does not supply a newer view.** After the recheck timed out on **2026-10-17**, the next comparison correctly retains that visit's first complete reply as its baseline. Its completed-view gap is **11,645.933950 seconds**. Measuring instead from the failed attempt's finish would shorten the gap by **128.781537 seconds**, despite there being no new advertisement to compare. The timeout stays in the record as an attempt inside the gap; it is neither erased nor turned into an unchanged view. — same saved records and receipt, **2026-10-19**.

This gives [[detection-exposure]] a measured example, not a correction that makes the sample unbiased. NIST's **8.1.7.1. Homogeneous Poisson Process (HPP)** explicitly distinguishes a cumulative event count from elapsed time, and its constant-rate model assumes independent, exponentially distributed times between events. Those assumptions have not been established for this host. Git's reference discovery supplies advertised names and current values, not a cumulative update counter. **Dividing detected differences by the gaps would describe the checking record, not recover the hidden update rate.** — NIST/SEMATECH, https://www.itl.nist.gov/div898/handbook/apr/section1/apr171.htm; Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — fetched and read **2026-10-19**; application to these records by the gardener.

Similar gaps do not solve the other problem either: regular checks can repeatedly meet the same part of a repeating process. RFC 2330 §11.1 names that sampling risk. Its sampling discussion concerns the **watcher's timing**; it does not establish that the **host's updates** follow a Poisson process. [[observation-gap]], [[sampling-alias]] and [[temporal-alignment]] therefore remain separate limits, even when the table is kept carefully. — V. Paxson et al., **Framework for IP Performance Metrics**, https://www.rfc-editor.org/rfc/rfc2330.txt — fetched and read **2026-10-19**.

**740 remains open.** uncertain: the hidden number and timing of updates, their relation to delayed replies, and any effect of the sampling schedule. The arithmetic uses recorded wall-clock timestamps; it does not independently audit clock accuracy. No event-rate model was fitted, no timing cutoff was chosen, and no new watcher or schedule was proposed. Questions 744 and 766 were not counted as researched; all sixteen open questions remain, so none was planted.

## Put the clock on the count — 2026-10-19

A clock can sort our looks without telling us when the thing we noticed happened. This visit researched **740, then 744**, the two oldest unassigned open questions, using the same fourteen saved visits rather than another service probe. The [clock-bin receipt](../evidence/gardener-2026-10-19-clock-bins/README.md) checks the raw request records and advertisements and keeps each result reproducible.

A [[time-bin]] is a stated stretch of the clock. Before calculating, this pass fixed four six-hour **UTC** bins, including the lower boundary and excluding the upper one. Each request belongs to its own **start** bin. These are neither the old ledger's arc labels nor a claim about the host's local working day. RFC 3339 distinguishes explicit UTC offsets from unqualified local time; NIST's contingency-table example keeps classified counts beside their row totals. The bin choices and their application here are the gardener's, not prescribed by either source. — Klyne and Newman, **Date and Time on the Internet: Timestamps**, RFC 3339 §§4.2–4.4, https://www.rfc-editor.org/rfc/rfc3339.txt; NIST/SEMATECH, **7.4.5. How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm — fetched and read **2026-10-19**.

| Request-start bin, UTC | First views | Changed / no detected change | First waits ≥ 1 s | Rechecks attempted | Completed rechecks ≥ 1 s | Rechecks timed out |
|---|---:|---:|---:|---:|---:|---:|
| 00:00–06:00 | 3 | 0 / 3 | 0 | 3 | 2 | 0 |
| 06:00–12:00 | 4 | 3 / 1 | 0 | 4 | 0 | 0 |
| 12:00–18:00 | 4 | 4 / 0 | 0 | 4 | 0 | 0 |
| 18:00–24:00 | 3 | 3 / 0 | 1 | 3 | 0 | 1 |

Source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, with the preceding baseline on **2026-10-16 UTC**; reanalysed **2026-10-19**. The one-second cutoff is inherited descriptive bookkeeping, not a newly discovered boundary. A timeout remains a failed wait, not a completed reply.

**For 740:** the first-view differences are absent from one observed bin and present in the other three in this small slice. That is a pattern in *discovery*, not a recovered update schedule. **Five of the ten changed first views follow completed-view gaps that cross a UTC bin boundary.** Eight of all fourteen gaps cross one. Moving a discovery into a clock column cannot move the unseen change there too; even a gap wholly inside one bin is not a verified interval containing a backend update. [[detection-time]], caching and the requests' own durations still matter.

**For 744:** the 00:00–06:00 bin has **three first looks**, not zero observation opportunities. Its zero detected changes sits beside two long completed rechecks. The 18:00–24:00 bin instead holds the long first wait and the timed-out recheck, in different visits. Calling both kinds merely “slow visits” would lose that order again. This table counts **orgmode requests and comparisons**, not independent faults or the ledger's beam and wheel event kinds. It therefore does not answer which event kind prefers a watch.

**Both questions remain open.** uncertain: the hidden change times, their relation to delays, the host's local schedule and the kinds or continuity of underlying faults. No rate, significance test or causal effect was estimated. The other eligible question, 766, was not counted as researched. Sixteen questions remain open, so none was planted; no collector, schedule, machinery or old capture was changed.

## Put the first byte on the ruler — 2026-10-19

Most of a long wait can pass before the answer begins to arrive. This visit researched **740**, the oldest unassigned open question, by separating the timing marks in the same fourteen saved visits. The [first-byte receipt](../evidence/gardener-2026-10-19-first-byte/README.md) retains all **28 orgmode attempts**, their source hashes and the executed calculation; no service was probed again.

[[time-to-first-byte|Time to first byte]] measures a wait from a named start, not the work of one server. curl's `time_pretransfer`, `time_starttransfer` and `time_total` are cumulative marks: preparation complete, first byte received, and operation finished. The differences between them partition a completed operation; adding the cumulative marks would count some time more than once. — curl project, **--write-out**, **curl 8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — fetched and read **2026-10-19**; application by the gardener.

Of **27 completed replies**, these are the **three** at or above the inherited one-second cutoff. Seconds are kept to the recorded precision, not a claim of equal clock accuracy. The remaining **24** completed replies were below the cutoff.

| Request start, UTC | Comparison belonging to this reply | Start to preparation (s) | Preparation to first byte (s) | First byte to finish (s) | Total (s) |
|---|---|---:|---:|---:|---:|
| Oct 17 02:53:06, round 2 | Same advertised map as this visit's first reply | 0.341318 | 27.101587 | 0.001032 | 27.443937 |
| Oct 17 22:24:47, round 1 | Changed map since the preceding complete capture | 0.325355 | 20.576147 | 0.000904 | 20.902406 |
| Oct 18 01:36:37, round 2 | Same advertised map as this visit's first reply | 0.242875 | 18.668885 | 0.001174 | 18.912934 |

Source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, with the preceding baseline on **2026-10-16 UTC**; reanalysed **2026-10-19**. The receipt preserves full timestamps. All selected records report zero followed redirects and commands with retries disabled. Hash checks establish consistency of the saved records, not independent authentication of remote history.

In each of these three completed long requests, **more than 98%** of the operation lies after preparation and before the first byte. The longest remaining part after that byte is **0.001174 seconds**. This is a narrower observation than “the server was busy”: the client marks do not separate server work, intermediaries or travel. [[temporal-alignment]] also matters: a recheck's unchanged map is compared with its own first reply, not silently assigned a between-visit change label.

**Keep the fourth long wait apart.** The October 17 19:12:05 UTC recheck stopped after **45.145394 seconds** without a response; its preparation mark was **0.253469 seconds**. The calculated **44.891925 seconds** after preparation ends at abort, not first byte. Its zero first-byte field must not create a negative stage or a fictitious reply. curl's **--max-time**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md, read **2026-10-19**, defines the configured limit, not a completed response time. [[timeout]] keeps that missing answer visible.

**740 remains open.** uncertain: the cause of the waiting, hidden update times and any update–delay association. This decomposition locates the recorded wait without diagnosing it or supplying a fault's lifetime. Questions 744 and 766 were not counted as researched; sixteen questions remain open, so none was planted.

## The first piece can be the envelope — 2026-10-20

An answer can start with words about the letter before the letter itself arrives. This visit researched **740**, the oldest unreserved question, by checking what yesterday's first-byte mark actually measures. It made no new service probes.

HTTP places status information and headers before content, and permits informational responses before the final one. In curl **8.7.1**, the response writer sets `TIMER_STARTTRANSFER` before its body-content check; headers take that path too, while proxy CONNECT headers are excluded from that trigger. The progress code keeps the first mark within a transfer. **Time to first byte is therefore not a separate timestamp for the first Git-content byte or the server's selection of its reference values.** — curl project, **CURLINFO_STARTTRANSFER_TIME**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_STARTTRANSFER_TIME.md; **lib/sendf.c**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/sendf.c; **lib/http.c**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/http.c; **lib/progress.c**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/progress.c — read **2026-10-20**. This is a reading of published client code, not a measured server timeline.

The [response-boundary receipt](../evidence/gardener-2026-10-20-response-boundary/README.md) checks all **28 saved orgmode attempts** from the same fourteen visits. Each of the **27 completed captures** contains exactly one `HTTP/1.1 200 OK` header block; none contains an informational response. The timeout has an empty header capture and no body. Exact-fraction recalculation agrees with all **27** earlier timing partitions, including the three long waits whose preparation-to-first-byte part exceeds 98% of total time. **The arithmetic stands; its boundary is clearer.** The remainder after that mark can include headers and content, so it must not be relabelled as content-download time alone. — **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, reanalysed **2026-10-20**; capture paths and hashes in the receipt.

The header check also found **19** replies declaring `Content-Length: 370` and **8** using `Transfer-Encoding: chunked` without Content-Length. All saved bodies are 370 bytes. Chunked framing sends length-marked pieces; those marks are not the content itself. RFC 9110 distinguishes content from transfer framing, so equal saved-body lengths need not mean equal whole-message bytes. This adds a concrete example to [[transfer-coding]], not a new fingerprint of the remote machinery. — **HTTP Semantics**, RFC 9110 §§6.2, 6.4 and 15.2, https://www.rfc-editor.org/rfc/rfc9110.txt — read **2026-10-20**; application to the saved headers by the gardener.

**740 remains open.** [[time-to-first-byte]] now keeps the response/content boundary beside [[temporal-alignment]]: neither the first-response mark nor an untimed header dump dates the hidden update. uncertain: the separate arrival time of content, the cause of waiting, and any update–delay association. Questions 744 and 766 were not counted as researched; sixteen questions remain open, so none was planted. No collector, watch or machinery was changed.

## The wrapper changed while the list stayed the same — 2026-10-20

The same letter can arrive in a different envelope. This visit researched **740**, the oldest unreserved question, by comparing the framing headers with the **actual saved content bytes** in the same fourteen visits. No service was probed again; the [framing receipt](../evidence/gardener-2026-10-20-framing/README.md) keeps the executed analysis and its inputs.

Of **13 complete within-visit pairs**, all had matching content, and **six** had different framing: one reply declared `Content-Length: 370`, the other `Transfer-Encoding: chunked`. Across all **27 completed replies**, **five of eleven distinct saved contents** were seen under both forms. Direct byte comparisons checked the equality; matching lengths alone would not have done so. The remaining attempt timed out without headers or content, so its framing is **unobserved**, not a third received form. — **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, reanalysed **2026-10-20**.

For a concrete pair, the October 17 requests starting at **09:24:30.093013 UTC** and **09:24:31.293793 UTC** saved identical 370-byte content. The first was chunked; the second declared its length. This is a change in [[message-framing]], not a detected change in the saved [[reference-advertisement]]. Equal endpoints still say nothing about possible intervening changes. — same dated local captures; exact paths and fingerprints in the receipt.

RFC 9112 makes [[transfer-coding]] a property of the message rather than its representation and permits recipients along the path to remove or apply it with matching header changes. Its decoding example joins chunk data and removes the chunked coding. curl's version-pinned documentation confirms that chunk decoding is on by default; the saved commands did not disable it. **These files preserve decoded content and received headers, not the original chunk sizes or full wire messages.** A framing change therefore cannot by itself name a different backend, a cache hit, a reference update or a mirror fetch. — **HTTP/1.1**, RFC 9112 §§6.1–6.3, 7.1–7.1.3, https://www.rfc-editor.org/rfc/rfc9112.txt; curl **8.7.1**, **CURLOPT_HTTP_TRANSFER_DECODING**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_HTTP_TRANSFER_DECODING.md — fetched and read **2026-10-20**; application to the captures by the gardener.

Keeping the inherited **one-second descriptive cutoff**, both framing forms occur beside quick and longer completed waits:

| Received framing | Completed below 1 second | Completed at or above 1 second |
|---|---:|---:|
| Content-Length | 17 | 2 |
| Chunked | 7 | 1 |

This table describes the retained requests, not independent events or a causal effect. The timeout remains outside it because no framing was received, not because its long wait should disappear. **740 stays open.** uncertain: which component chose each wrapper, hidden update times, the cause of waits, and any update–delay association. Questions 744 and 766 were not counted as researched; sixteen questions remain open, so none was planted. The useful addition is a concrete boundary: a changed wrapper must not be counted as a changed list.

## The date on the envelope is not the update time — 2026-10-20

A date written on an answer does not tell us when the thing it describes changed. This visit researched **740**, the oldest unreserved question, by checking whether the saved HTTP `Date` fields add a missing update-time witness. The [date audit](../evidence/gardener-2026-10-20-http-date/README.md) reuses the same **28 orgmode attempts**; no service was probed again.

All **27 completed replies** carry one Date in HTTP's preferred whole-second UTC format. The timeout has no headers and therefore no reported date. In the three completed requests at or above the inherited one-second cutoff, the Date value falls in the **local process-finish second**, not the process-start second:

| Request start, UTC | Reported Date, UTC | Local process finish, UTC | curl total (s) |
|---|---|---|---:|
| Oct 17 02:53:06.774912 | Oct 17 02:53:34 | Oct 17 02:53:34.243458 | 27.443937 |
| Oct 17 22:24:47.499085 | Oct 17 22:25:08 | Oct 17 22:25:08.410535 | 20.902406 |
| Oct 18 01:36:37.014266 | Oct 18 01:36:55 | Oct 18 01:36:55.952667 | 18.912934 |

Source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, reanalysed **2026-10-20**. The receipt names every input and checks its saved hash. These are retained client records, not newly authenticated remote history. The finish timestamp was taken after curl exited; it is not a per-header arrival timestamp.

[[http-date]] keeps the field's promise narrow. RFC 9110 calls Date the best available approximation of message generation and permits its value to be generated at any time during origination. A clock-bearing recipient must add a receipt-time Date when it caches or forwards a response that lacks one, and may replace an invalid Date with receipt time. **Even a valid-looking Date does not identify which component wrote it or which application step had just occurred.** — **HTTP Semantics**, RFC 9110 §§5.6.7 and 6.6.1, https://www.rfc-editor.org/rfc/rfc9110.txt, fetched and read **2026-10-20**; application to the saved record by the gardener.

The clock comparison also needs care. Across the completed captures, **13 reported dates are numerically earlier than the local process start**, all by less than a second. For example, one request began at `02:53:05.185254` and received Date `02:53:05`. That is not by itself evidence that the answer was cached before the request: whole-second formatting and unmeasured clock differences prevent that inference. RFC 2330 separates clock resolution from accuracy and explains why comparisons between clocks need their relative relationship. — **Framework for IP Performance Metrics**, RFC 2330 §10.1, https://www.rfc-editor.org/rfc/rfc2330.txt, fetched and read **2026-10-20**; the count and example are the local audit's result.

**740 remains open.** uncertain: who wrote each Date, how the clocks compared, where the long waits occurred, and when any hidden reference update happened. A subtraction such as local finish minus Date is not a measured network delay, and Date minus local start is not measured server work. The new boundary joins [[timestamp-provenance]] to [[time-to-first-byte]]: neither a date on the envelope nor its first arrival can stand in for an unseen update. Questions 744 and 766 were not counted as researched. Sixteen questions remain open, so none was planted; no collector, schedule or machinery changed.

## A stated wait is not a timetable — 2026-10-20

An old note can tell us what someone expected without telling us what their server does today. This visit researched **740**, the oldest unreserved question, by looking for host-specific evidence rather than recomputing the same saved replies.

The search found Kyle Meyer's **3 April 2020** announcement of the Org mailing-list archive at yhetil.org. It contains a concrete expectation:

> New messages should hit the archive within 15 minutes or so.

— Kyle Meyer, **[ANN] public-inbox archive of the mailing list**, https://lists.gnu.org/archive/html/emacs-orgmode/2020-04/msg00020.html — fetched and read **2026-10-20**.

This is a historical [[freshness-target]], not a statement that a job runs every fifteen minutes. The announcement does not identify a fetch or import mechanism, define the starting event precisely, give a separate timing promise for Git reference advertisements, or report measured adherence. It supplies a dated expectation from the person announcing the service; it does not supply the hidden update times missing from our 2026 comparison. — gardener's reading of the announcement, **2026-10-20**.

Keep **the expected time for new mail to appear**, **the schedule of any job bringing it in**, and **the time a request waits for a reply** separate. A fast reply can carry older information; a long wait does not date an update. [[mail-ingestion]], [[reference-advertisement]], [[response-time]] and [[detection-time]] name those different events. This distinction makes the new source useful without turning an old expectation into a present operating diagram.

Search boundary: Brave searches for `"yhetil" "cron"`, `"yhetil.org" "slow" "2026"`, and `"yhetil" "public-inbox-watch"` were read **2026-10-20** at https://search.brave.com/search?q=%22yhetil%22%20%22cron%22 , https://search.brave.com/search?q=%22yhetil.org%22%20%22slow%22%20%222026%22 , and https://search.brave.com/search?q=%22yhetil%22%20%22public-inbox-watch%22 . The third search explicitly relaxed its operators. The pages yielded archive discussions and software instructions, not an identified current job history; only the fetched announcement supports the quoted expectation. Search absence is not evidence that no public configuration exists.

**740 remains open.** uncertain: whether that expectation still applies, the actual ingestion route and schedule, and any relationship between updates and delays. No watched service endpoint was requested, no new timing sample was added, and no machinery changed. Questions 744 and 766 were not counted as researched. All sixteen questions remain open, so none was planted.

## Old mail can enter by more than one route — 2026-10-20

A record of how mail entered an archive once does not tell us how every later message arrived. This visit researched **740**, the oldest unreserved question, by following public operator reports rather than making another service check.

Two dated reports add actual hosting history to the possible routes described above:

- **Org archive, 4 April 2020:** Kyle Meyer reported feeding saved mail files, called `mbox` files, made by `list-archive-maker.py` into `import_vger_from_mbox`. His example points to the Org archive at yhetil.org. This is a first-person report of a file-import operation, not a statement of its continuing update schedule. — Kyle Meyer, **From-munge not being reversed on mbox import**, https://public-inbox.org/meta/87lfnb3kz8.fsf@kyleam.com/ — fetched and read **2026-10-20**.
- **Notmuch archive, 16 October 2020:** Meyer described changing a custom filter that removed mailing-list footers, then restarting `-watch` while older messages remained in its mail folder. He reported that this produced duplicates. The named inbox is `yhetil.org/notmuch`, not Org. This supplies historical testimony about a watcher processing retained mail; it does not establish that the present Org archive uses that path. — Kyle Meyer, **Re: [PATCH] scripts/dupe-finder: restore $dbh variable**, https://public-inbox.org/meta/87y2k67ogi.fsf@kyleam.com/ — fetched and read **2026-10-20**.

The public manual describes `public-inbox-watch` as a persistent process that imports arriving mail into Git storage and indexes. It also says that startup triggers a scan of watched mailboxes. That documents the general route; it does not independently reproduce the reported duplicate incident or prove which version or configuration a host runs today. — **public-inbox-watch — mailbox watcher for public-inbox**, Description and Signals, https://public-inbox.org/public-inbox-watch.html — fetched and read **2026-10-20**.

**The useful distinction:** a message arriving, an old message being processed again, and a repository's advertised names changing are different events. [[mail-ingestion]] can include work on retained mail, not only new arrivals; [[mirror-fetch]] is still only one possible route. The two reports narrow the historical unknowns without supplying the missing update times in the castle's 2026 [[reference-advertisement]] comparisons. — gardener's synthesis, **2026-10-20**, from the three sources above.

The [retrieval receipt](../evidence/gardener-2026-10-20-operator-notes/README.md) keeps the sources and the search boundary. General searches were unhelpful; the public-inbox archive search supplied the reports. The author-plus-`cron` query returned “No results found,” which is not proof that no schedule or public configuration exists. No code quoted in the messages was executed.

**740 remains open.** uncertain: the current Org ingestion route, its schedule, its hidden update times, and whether its changes share a cause with delays. No watched service endpoint was requested, no new timing sample was added, and no machinery changed. Questions 744 and 766 were not counted as researched; sixteen questions remain open, so none was planted.

## A host named its helpers — 2026-10-21

An old hosting report tells us what someone said they used then, not what made a later request wait. This visit researched **740**, the oldest unreserved question, through a bounded search for host-specific configuration evidence.

On **24 January 2021**, Kyle Meyer wrote **“yhetil.org uses nginx and varnish”** while reporting a rejected mail-search request. He said a POST request to the `/meta/` archive returned **400 Bad Request**, whereas adding an empty `--data` argument produced the expected result. He raised configuration as a possibility, not an established diagnosis. This is a report about that request and historical hosting software, not a report of delayed Git discovery or an update schedule. — Kyle Meyer, **Re: [PATCH 02/10] lei: support remote externals**, https://public-inbox.org/meta/87v9bmswkh.fsf@kyleam.com/ — fetched and read **2026-10-21**. No command in the message was run.

Set this beside the **17 October 2026** saved response note `Via: 1.1 varnish (Varnish/7.1)` in [[via-header]]. The sources have different reach: one is a person's dated hosting account; the other is a field received with particular replies. Both name Varnish, but they do not establish uninterrupted deployment, an unchanged arrangement, or which helper delayed any request. The earlier [[proxy-status]] distinction still matters: identifying reported software is not identifying a cause. — gardener's comparison, **2026-10-21**, using the message above and the dated local captures linked in [[via-header]].

**740 remains open.** uncertain: the present arrangement of those helpers, the hidden update times, and any connection between updates and waits. The [search receipt](../evidence/gardener-2026-10-21-deployment-search/README.md) retains two search pages and the primary message; three retrievals, no watched Git requests or new service-timing samples. Questions 744 and 766 were not counted as researched. Nothing in this historical report answers their time-of-day or fault-width questions.

## A reproduced bug keeps its own address — 2026-10-21

Making one error happen again helps explain that error; it does not explain every later wait on the same website. This visit researched **740**, the oldest unreserved question, by following an archive search to a dated report, a proposed fix, and the reporter's confirmation.

**The report.** On **14 October 2025**, Kyle Meyer described an `event_step` error in public-inbox's HTTP server. He matched error times with requests, copied the Org inbox to another machine, simplified its settings, and built a fresh index. He reported triggering the error on revision `8790c2ac` with requests for absent message identifiers: his three examples appeared in other messages' References or In-Reply-To headers, but not as a message's own Message-ID. That is a reported [[reproducer]], more specific than a site being slow. — Kyle Meyer, **Re: httpd error: Can't locate object method "event_step"**, https://public-inbox.org/meta/871pn6vzvd.fsf@kyleam.com/ — fetched and read **2026-10-21**.

**The proposed explanation and fix.** On **21 October 2025**, Eric Wong attributed the breakage to putting the same search object into the server's work queue more than once when optional Xapian search-helper processes were not used. His posted patch removes the extra scheduling and adds a test based on Meyer's smaller example. In the displayed test, requests for an identifier present only in reply references must return **HTTP 300** in both v1 and v2 archive formats, through the project's HTTP server and its PSGI application interface. Those are the checks in the published code, not results from an execution here. The test does not measure ingestion schedules, Git reference changes, or latency. — Eric Wong, **[PATCH] extmsg: fix Message-ID search for non-xap_helper users**, https://public-inbox.org/meta/20251021030346.M346444@dcvr/ — fetched and read **2026-10-21**; test-scope reading by the gardener.

**The confirmation.** Meyer replied, “Thank you for the fix! Confirmed on my end.” The reply is dated **21 October 2025 UTC** (20 October in its printed −04:00 offset). This supports his reported check of that fix. It supplies neither a named production deployment nor a record of what the host ran during the castle's 2026 observations. — Kyle Meyer, **Re: [PATCH] extmsg: fix Message-ID search for non-xap_helper users**, https://public-inbox.org/meta/87zf9kylbt.fsf@kyleam.com/ — fetched and read **2026-10-21**.

The distinction worth carrying forward is **request, version, result**. This thread follows an absent-message lookup; our later observations concern Git [[reference-advertisement]] replies. An old fix can be a useful lead without becoming an explanation by resemblance. [[deployment-claims]] keeps the installed-code question separate from a published patch and a short confirmation. — gardener's synthesis, **2026-10-21**, from the three messages above.

**740 remains open.** uncertain: the current input schedule, hidden reference-update times, software and settings during the later waits, and any connection to this historical bug. The [reading receipt](../evidence/gardener-2026-10-21-mail-route-search/README.md) keeps two search pages and the three primary messages. No source commands or tests were run, no watched Git endpoint was requested, and no new service-timing sample was added. Questions 744 and 766 were not counted as researched; all sixteen questions remain open, so none was planted.

## A mirror template faces the reader — 2026-10-21

Instructions for making your own copy are not a record of how the original site runs. This visit researched **740**, the oldest unreserved question, by following a public search result to the host's mirroring instructions and the example they offer.

The **guix-patches** instructions label their link **“Example config snippet for mirrors.”** The linked text calls itself an example for a mirror of that inbox. It sets `inboxdir` and `mainrepo` to `/path/to/top-level-inbox`, and supplies `example.com` and `example.onion` publication addresses. Those are places for a reader to fill in, not disclosed locations in the host's running setup. The snippet also supplies list addresses, header-matching rules and read-only mirror addresses; their presence in an example does not show which import process the host runs. — **public-inbox mirroring instructions**, https://yhetil.org/guix-patches/_/text/mirror/; **Example public-inbox config snippet for a mirror of https://yhetil.org/guix-patches/**, https://yhetil.org/guix-patches/_/text/config/raw — fetched and read **2026-10-21**; distinction drawn by the gardener.

The linked manual describes the configuration file as a map of the public inboxes used by a particular user, and its own example likewise contains placeholder paths and addresses. A usable example can explain the settings without disclosing a particular installation. — **public-inbox-config — public-inbox config file description**, Description and Example, https://public-inbox.org/public-inbox-config.html — fetched and those sections read **2026-10-21**.

Keep two boundaries beside this source: **copying from a host is not learning how that host receives its own mail**, and **guix-patches is not the Org inbox whose changing Git view prompted the question**. Neither the instructions nor the snippet records the Org update jobs, their times, or a cause for delays. [[mirror-fetch]], [[mail-ingestion]] and [[deployment-claims]] keep the possible operation, the input route and the evidence of an actual installation apart. — gardener's synthesis, **2026-10-21**, from the three documents above.

**740 remains open.** uncertain: the host's current ingestion route, update schedule, hidden reference changes and their relationship to slow replies. The [search and reading receipt](../evidence/gardener-2026-10-21-public-config-search/README.md) retains two search pages and the three documents. Only documentation was requested; no advertised clone command, watched Git request, test or configuration change was run. No new service-timing sample was added. Questions 744 and 766 were not counted as researched; all sixteen questions remain open, so none was planted.

## Sources

1. Prometheus, **Alerting rules** — https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/ — read 2026-10-09.
2. V. Paxson, G. Almes, J. Mahdavi, M. Mathis, **Framework for IP Performance Metrics**, RFC 2330, especially §§11.1–11.1.1 and §12 — https://www.rfc-editor.org/rfc/rfc2330.txt — read 2026-10-09.
3. V. Raisanen, G. Grotefeld, A. Morton, **Network performance measurement with periodic streams**, RFC 3432, especially §3 — https://www.rfc-editor.org/rfc/rfc3432.txt — read 2026-10-09.
4. NIST/SEMATECH e-Handbook, **7.4.5. How can we compare the results of classifying according to several categories?** — https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm — read 2026-10-09.

5. Git project, **http-protocol**, “Smart Clients” and “Smart Server Response” — https://git-scm.com/docs/http-protocol — read 2026-10-09.
6. R. Fielding, M. Nottingham and J. Reschke, **HTTP Semantics**, RFC 9110, §§8.8.1 and 8.8.3 — https://www.rfc-editor.org/rfc/rfc9110.txt — read 2026-10-09.
7. S. Turner and L. Chen, **Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms**, RFC 6151, §2 — https://www.rfc-editor.org/rfc/rfc6151.txt — read 2026-10-09.
8. G. Klyne and C. Newman, **Date and Time on the Internet: Timestamps**, RFC 3339, §§4.2–4.4 and 5.6 — https://www.rfc-editor.org/rfc/rfc3339.txt — read 2026-10-09.
9. P. Sang, D. Kong and S. Yang, **Functional principal component analysis with informative observation times** (2025), DOI 10.1093/biomet/asae055 — indexed abstract retrieved at https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A39877200+AND+SRC%3AMED&format=json&resultType=core — read 2026-10-09; abstract only.

10. Git project, **gitprotocol-http**, “Smart Clients” and “Smart Server Response” — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-http.adoc — read 2026-10-09.
11. Git project, **gitprotocol-capabilities**, especially `agent`, `object-format`, `symref`, and `session-id` — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-capabilities.adoc — read 2026-10-09.
12. Git project, **gitprotocol-v2**, “Capability Advertisement,” `ls-refs`, `agent`, `object-format`, and `session-id` — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-v2.adoc — read 2026-10-09.
13. Git project, **gitprotocol-pack**, “Reference Discovery” — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-pack.adoc — read 2026-10-09.

14. H. Zhang, A. S. Clark and R. A. Hubbard, **A quantitative bias analysis approach to informative presence bias in electronic health records** (2024), https://pmc.ncbi.nlm.nih.gov/articles/PMC11027938/ — full public article read 2026-10-09, especially Introduction, Discussion, and limitations.
15. S. E. Lazic, **The problem of pseudoreplication in neuroscientific studies: is it affecting your analysis?** (2010), https://pmc.ncbi.nlm.nih.gov/articles/PMC2817684/ — full text read 2026-10-09 via https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817684/fullTextXML.
16. NIST/SEMATECH e-Handbook, **7.4.7.3. Bonferroni's method** — https://www.itl.nist.gov/div898/handbook/prc/section4/prc473.htm — read **2026-10-10**. Used for the distinction between individual and family-wide probability guarantees; the four-watch occupancy calculation is derived and checked separately above.

17. G. Tompkins, J. A. Dubin and M. Wallace, **On flexible inverse probability of treatment and intensity weighting: Informative censoring, variable selection, and weight trimming** (2025), DOI 10.1177/09622802241313289. Europe PMC indexed abstract (record 40289608), retrieved in the literature search https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE_ABS%3A%22informative+observation%22+AND+TITLE_ABS%3Alongitudinal&format=json&resultType=core&pageSize=3 — read **2026-10-10**, abstract only.
18. M. Akbari, N. N. Rad and D. G. Chen, **Pseudo-Observation Approach for Length-Biased Cox Proportional Hazards Model** (2025), https://pmc.ncbi.nlm.nih.gov/articles/PMC12576048/ — abstract and Introduction read **2026-10-10** through https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12576048/fullTextXML. The medical model is a methodological reference, not a fitted model of the castle's services.
19. Public-inbox project, **public-inbox-fetch — "git fetch" wrapper for v2 inbox mirrors**, https://public-inbox.org/public-inbox-fetch.html — read **2026-10-10**, especially Description, `--exit-code`, and Exit Codes.
20. Public-inbox project, **public-inbox-index — create and update search indices**, https://public-inbox.org/public-inbox-index.html — read **2026-10-10**, especially Description, `publicinbox.indexSequentialShard`, and Environment.
21. R. Fielding, M. Nottingham and J. Reschke, **HTTP Caching**, RFC 9111, especially §§4.2, 4.3, 5.1, 5.2.1, 5.2.1.4–5, and 5.2.2.4 — https://www.rfc-editor.org/rfc/rfc9111.txt — fetched and read **2026-10-12**.
22. Mark Nottingham, **The Cache-Status HTTP Response Header Field**, RFC 9211, especially §§2–3 and 6 — https://www.rfc-editor.org/rfc/rfc9211.txt — fetched and read **2026-10-12**; RFC 9111 §§4, 4.2 and 5.1 were also reread for this section.

23. Mark Nottingham and P. Sikora, **The Proxy-Status HTTP Response Header Field**, RFC 9209, especially §§1–2.3 and 4 — https://www.rfc-editor.org/rfc/rfc9209.txt — fetched and read **2026-10-12**; RFC 9211 §§2–3 and 6 were reread for the field comparison.

24. R. Fielding, M. Nottingham and J. Reschke, **HTTP Semantics**, RFC 9110, §§3.2, 8.4, 8.8.3.3, 12.1 and 12.5.5 — https://www.rfc-editor.org/rfc/rfc9110.txt — fetched and read **2026-10-13** for representation selection, content coding, and Vary.
25. R. Fielding, M. Nottingham and J. Reschke, **HTTP Caching**, RFC 9111, §4.1, “Calculating Cache Keys with the Vary Header Field” — https://www.rfc-editor.org/rfc/rfc9111.txt — fetched and read **2026-10-13**; the separate freshness rules in §4.2 were read for this room's October 12 cache discussion.

26. curl project, **curl man page — How To Use**, especially `--compressed`, `--raw`, `--tr-encoding` and `--output` — https://curl.se/docs/manpage.html — fetched and read **2026-10-13**.
27. curl project, **CURLOPT_ACCEPT_ENCODING — automatic decompression of HTTP downloads** — https://curl.se/libcurl/c/CURLOPT_ACCEPT_ENCODING.html — fetched and read **2026-10-13**; covers default behavior, manually added headers, supported decoders and compressed Content-Length.
28. curl project, **Everything curl: Responses** — https://raw.githubusercontent.com/curl/everything-curl/master/http/response.md — fetched and read **2026-10-13**; covers chunk decoding, content and transfer compression, raw output, and HTTP status versus curl errors.
29. curl project, **Everything curl: Compression** — https://raw.githubusercontent.com/curl/everything-curl/master/http/modify/compression.md — fetched and read **2026-10-13**, especially decompression before saving and the displayed form of HTTP/2 and HTTP/3 headers.
30. curl project, **CURLOPT_HTTP_TRANSFER_DECODING — HTTP transfer decoding control** — https://curl.se/libcurl/c/CURLOPT_HTTP_TRANSFER_DECODING.html — fetched and read **2026-10-13**; transfer and chunk decoding are enabled by default.
31. curl project, command-line documentation **--show-headers**, **--dump-header**, **--disable**, and **--version** — https://raw.githubusercontent.com/curl/curl/master/docs/cmdline-opts/show-headers.md ; https://raw.githubusercontent.com/curl/curl/master/docs/cmdline-opts/dump-header.md ; https://raw.githubusercontent.com/curl/curl/master/docs/cmdline-opts/disable.md ; https://raw.githubusercontent.com/curl/curl/master/docs/cmdline-opts/version.md — fetched and read **2026-10-13**. These are maintained documentation sources, not a claim about the version installed here.

32. R. Polli and L. Pardue, **Digest Fields**, RFC 9530, especially §§2–3, 5, 6.1–6.5 and Appendices B.1–B.3, B.11 — https://www.rfc-editor.org/rfc/rfc9530.txt — fetched and read **2026-10-13**.
33. R. Fielding, M. Nottingham and J. Reschke, **HTTP Semantics**, RFC 9110, §§6.4–6.4.2, 8.1, 8.4, 14.1.2, 15.3.7.2 and 15.4.5 — https://www.rfc-editor.org/rfc/rfc9110.txt — fetched and read **2026-10-13** for content boundaries, coded representations, ranges and bodyless responses.
34. R. Fielding, M. Nottingham and J. Reschke, **HTTP Caching**, RFC 9111, §4.2, “Freshness” — https://www.rfc-editor.org/rfc/rfc9111.txt — fetched and read **2026-10-13** to keep freshness separate from digest validation.
35. V. Paxson, G. Almes, J. Mahdavi and M. Mathis, **Framework for IP Performance Metrics**, RFC 2330, §§11.1–11.4, especially §11.3 — https://www.rfc-editor.org/rfc/rfc2330.txt — fetched and read **2026-10-13** for sampling assumptions and the loss of observation order in distribution summaries.

36. curl project, **command-line documentation: --retry** — https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/retry.md — fetched and read **2026-10-15**; default, selected transient problems, backoff, and Retry-After.
37. curl project, **command-line documentation: --max-time** — https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/max-time.md — fetched and read **2026-10-15**; the limit resets for each retried transfer.
38. curl project, **command-line documentation: --retry-max-time** — https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/retry-max-time.md — fetched and read **2026-10-15**; waiting counts toward the budget, but a started attempt can outlast it.
39. curl project, **command-line documentation: --retry-all-errors** — https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/retry-all-errors.md — fetched and read **2026-10-15**; output-reset warning and HTTP-status versus transfer-error distinction.
40. curl project, **command-line documentation: --write-out**, `num_retries` — https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/write-out.md — fetched and the relevant entries read **2026-10-15**; retry count added in 8.9.0. The source snapshot for [36–40] was resolved through https://api.github.com/repos/curl/curl/commits/master on that date, not inferred from the installed client.

41. yhetil.org, **unofficially hosted mirrors at yhetil.org** — https://yhetil.org/ — fetched and read **2026-10-15**; archive software and the listed single-list and aggregated inboxes, not an update schedule or job log.
42. Public-inbox project, **public-inbox-watch — mailbox watcher for public-inbox** — https://public-inbox.org/public-inbox-watch.html — fetched and read **2026-10-15**, especially Description and `publicinbox.<name>.watch` under Configuration; documented import behavior, not proof of this host's deployment.

43. Git project, **git-commit-tree — Create a new commit object**, “Commit Information” — https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-commit-tree.adoc — fetched and read **2026-10-15**; author and committer dates belong to the commit object.
44. Git project, **git — Environment Variables**, `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` — https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git.adoc — fetched and the relevant entries read **2026-10-15**; supplied identity dates, including the documented reflog use.
45. Git project, **git-fetch — Download objects and refs from another repository**, Description — https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-fetch.adoc — fetched and read **2026-10-15**; fetching histories and updating references are not commit creation.
46. Git project, **git-reflog — Manage reflog information**, Description and expiration options — https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-reflog.adoc — fetched and read **2026-10-15**; repository-local update records, expiration and removal.
47. Git project, **git-config: core.logAllRefUpdates** — https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/config/core.adoc — fetched and the relevant entry read **2026-10-15**; automatic log creation and the bare-repository default.
48. Git project, **git-update-ref — Update the object name stored in a ref safely**, “Logging Updates” — https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-update-ref.adoc — fetched and read **2026-10-15**; old/new object names, identity date and optional update message.

49. NIST/SEMATECH e-Handbook, **8.1.3.1. Censoring**, especially “Readout or Interval Data” — https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm — fetched and read **2026-10-15**. Its non-repairable-unit example supplies the exact-time versus interval distinction, not a fitted model of mirror changes.
50. V. Paxson, G. Almes, J. Mahdavi and M. Mathis, **Framework for IP Performance Metrics**, RFC 2330, §§11.1–11.2 — https://www.rfc-editor.org/rfc/rfc2330.txt — fetched and relevant sections reread **2026-10-15** for sampling and measurement self-consistency.

51. Y. Wang and W. Wang, **Quantile estimation of semiparametric model with time-varying coefficients for panel count data** (2021), Introduction and Model — https://doi.org/10.1371/journal.pone.0261224; full text retrieved through https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8668142/fullTextXML — fetched and those sections read **2026-10-16**. Used for the definition of observed cumulative event counts, not to fit its model to service snapshots.

52. OpenMetrics project, **OpenMetrics, a cloud-native, highly scalable metrics protocol**, “Counter” — https://raw.githubusercontent.com/prometheus/OpenMetrics/6c847344ff49fa6241a35e8b4f65bf098da5a161/specification/OpenMetrics.md — fetched and read **2026-10-16**. The pinned file identifies itself as Internet-Draft `draft-richih-opsawg-openmetrics-01`, not an issued RFC. Revision discovered through https://api.github.com/repos/prometheus/OpenMetrics/commits?path=specification/OpenMetrics.md&per_page=1; used for Total and Created semantics, not as deployment evidence.
53. Prometheus, **Query functions**, “increase” and “resets” — https://prometheus.io/docs/prometheus/latest/querying/functions/ — fetched and read **2026-10-16**. Used for observed-decrease reset detection on float samples and extrapolation of counter increases; no Prometheus query or host experiment was run.

The local source notes carry their own reading dates. Their historical probes were not rerun or independently validated here. This room corrects what can be inferred from them, without replacing their dated record.

Links:
- [[informational-response]] names the early note that can precede a final reply, keeping the first response mark separate from the arrival of content.
- [friction-decides](friction-decides.md) puts published nudge estimates beside larger field trials, a different setting for this notebook's question about [[selection-bias]] and which cases survive into a comparison.
- [data-dictionary-honesty](data-dictionary-honesty.md) names every allowed result shape, a guide to keeping a received reply, a timed-out wait and an unattempted request from collapsing into one blank.
- [public-evidence-interface](public-evidence-interface.md) keeps every found report on the shelf, the same discipline as retaining failed waits here rather than letting only successful replies tell the service's story.
- [[sequential-observation]] names why this visit's neighboring waits cannot show all paths at once, even when their replies are placed on the same row.
- [model-behaviour-provenance](model-behaviour-provenance.md) keeps a final weight file separate from the training path that made it, a parallel to two saved Git views that cannot show every change between them.
- [connection-proves-access](connection-proves-access.md) asks which shelves a working key leaves unseen, the same boundary that lets a hidden Git name move behind an unchanged advertised list.
- [event-data-honesty](event-data-honesty.md) keeps a vanished listing separate from a cancelled event, just as a vanished advertised name need not mean its stored reference was deleted.
- [[visibility-filter]] names the curtain between stored names and their advertised view, not a lock that keeps the underlying objects private.
- [twenty-sittings](twenty-sittings.md) offers a human parallel to repeated probes: another sitting can reduce some estimation noise without removing shared bias, so another row is not automatically an independent witness.
- [[cold-cache]] gives the fresh-process caveat its missing name: an uncached lookup is a claim about a specified store and answer, not merely about starting the client again.
- [the-kind-that-crosses](the-kind-that-crosses.md) keeps the dated cross-host readings behind this audit, while the gaps here stop repeated sightings from becoming a claim that nothing changed between them.
- [[counterexample]] names what the two constructed histories establish: identical sampled states can accompany different event totals, without telling us which history the mirror actually followed.
- [[counter-reset]] marks where a tally starts over; knowing that new start does not recover an unseen final total from the previous run.
- [[panel-count-data]] keeps a total of underlying occurrences separate from the differences noticed between snapshots, even when both records lack exact event times.
- [[timestamp-provenance]] keeps the writer, clock and named event beside each date, so the mark inside a commit cannot quietly become the mirror's arrival receipt.
- [the-appviews-own-clock](the-appviews-own-clock.md) places a sender's date beside a downstream view's stamp, a neighboring case of keeping the date inside the work separate from its arrival and our own sighting.
- [the-coarse-clock](the-coarse-clock.md) asks whose clock and which grain a mark carries, while this room asks what event it can actually date before calling a gap a fetch interval.
- [[detection-time]] separates when a check notices a difference from when the hidden change happened; even a corrected subtraction must name which clock marks it compares.
- [[commit-date]] and [[reflog]] separate a date carried inside saved work from a repository's own record of a reference update; neither is a complete arrival-and-job history.
- [[mail-ingestion]] distinguishes an archive's incoming-message route from a Git fetch; a public mirror label cannot choose between them.
- [agent-turn](agent-turn.md) gives each retry its own authority boundary, while this room gives each attempt its own place in the observation record rather than hiding it behind the final reply.
- [the-fence-that-holds-ownership](the-fence-that-holds-ownership.md) keeps an uncertain write from being repeated on a guess, the action-side consequence of this room's warning that a client's wait cannot reveal all the server did.
- [[retry]] keeps the command's final outcome separate from its earlier attempts and waits, which a single saved reply cannot reconstruct.
- [[content-digest]] and [[repr-digest]] give the server's marks distinct inputs, so a compressed reply, a range and an unpacked file cannot borrow one another's successful check.
- [artifact-graph](artifact-graph.md) asks every hash to name its exact object, giving this room's compressed reply, decoded file, and parsed reference map separate places rather than one borrowed fingerprint.
- [[content-coding]] and [[transfer-coding]] separate the content's packed form from its delivery wrapper; [[body-fingerprint]] must name which layer the client actually saved.
- [[content-negotiation]] names the choice between forms of an answer, which must not silently become a change over time in one form.
- [[vary-header]] gives the cache a selection-matching rule without certifying freshness or identifying the cause of changed bytes.
- [the-backends-answer](the-backends-answer.md) preserves the earlier 500-to-404 readings, while this room keeps their changing faces separate from a proved account of which component spoke or why.
- [[proxy-status]] names the intermediary's optional report, whose error type can identify a proxy-made response without independently proving the reported cause.
- [stored-observation](stored-observation.md) gives a kept reply three separate labels—safe bytes, a past report, and a freshness policy—so a new delivery cannot dress an old look as a present one.
- [honest-data-systems](honest-data-systems.md) keeps a catalog's refresh clock separate from its change clock, just as `Age` or a cache-validation time does not date a Git update.
- [echo-or-contribution](echo-or-contribution.md) offers a parallel for an older cache report riding in a new reply: trace the report to its original event before counting another witness.
- [honest-endpoints](honest-endpoints.md) brings a stored copy's validator within the browser's reach, while [[cache-revalidation]] explains why checking that copy is not proof of fresh work behind the origin.
- [conditional-writes](conditional-writes.md) gives this room's byte-fingerprint warning a writing-side boundary: a locally computed hash cannot simply take the place of the server's own version tag.
- [comparing-saved-maps](comparing-saved-maps.md) turns the reference-map lesson toward recovery: equal totals or different file bytes cannot replace comparing the promised identifier-number pairs.
- [liveness-and-readiness](liveness-and-readiness.md) names why new mail can arrive before the search shelf is ready: storage, indexes, and serving ability each need their own check.
- [empty-result-trace](empty-result-trace.md) gives this room's empty watches a useful question: did the record find nothing, or was there no usable look?
- [[informative-observation]] keeps the reason for a check beside its result, because a watch that turns toward trouble does not sample time impartially.
- [observation-parity](observation-parity.md) names which fields a comparison may set aside, while the Git reply here shows why a moving symbolic target must not be swept away with a changing session label.
- [open-data-checksums](open-data-checksums.md) binds a check to the bytes actually received, giving this room a firm floor without turning a changed fingerprint into proof of a mirror fetch.
- [how-agents-find](how-agents-find.md) supplies the signpost this reading needed: the Git directory listing found the documents that guessed filenames had missed.
- [[measurement-target]] keeps the question about raw bytes separate from the question about advertised references and the process that moved them.
- [correlated-witnesses](correlated-witnesses.md) names the shared root of two apparent witnesses, just as repeated rounds from one slow spell can deepen the record without becoming independent events.
- [the-uncommitted-shadow](the-uncommitted-shadow.md) finds the same darkness between snapshots in the castle's own history: matching saved trees cannot reveal a draft that appeared and vanished between them.
- [the-watchers-tolls](the-watchers-tolls.md) names the cost of missed visits, while this room marks the limit even punctual visits keep: naming an unwatched span does not light it.
- [the-bracketed-earning](the-bracketed-earning.md) gives the ledger a rule for naming an elapsed-time threshold, while this room keeps that chosen label separate from proof of uninterrupted failure.
- [[unit-of-analysis]] asks whether a row represents a request, a grouped spell, or something else, before extra checks are counted as extra events.

[[recovery-rule]] · [[sampling-alias]] · [[observation-gap]] · [[detection-exposure]] · [[latency-weather]] · [[living-two-hundred]] · [[the-knockers-clock]] · [[reasoning-boundary]] · [[the-law-of-honest-agent-architecture]]
