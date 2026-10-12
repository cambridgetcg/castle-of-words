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

The local source notes were read on the same date. Their historical probes were not rerun or independently validated here. This room corrects what can be inferred from them, without replacing their dated record.

Links:
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
