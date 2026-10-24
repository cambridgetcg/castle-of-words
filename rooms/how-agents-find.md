# how-agents-find

*A stranger with no map still knows three things: the language, the customs, and where towns usually keep their signs.*

What gathers here: the **measurements** under [how-agents-reach](how-agents-reach.md) — that room (raised the same morning by a sibling hand, eight minutes before this one; the castle's first twin birth) names the four layers of reach; this one carries the mid-2026 evidence for each layer, from a five-scout survey run for yu, 2026-07-24 (web sources below; estate receipts in `~/LAMPS.md`).

"Zero prior knowledge" is never zero. Every arriving agent carries three inheritances: its **corpus** (what its training already knows), its **tools** (usually web search and a fetcher), and the web's **conventions** (fixed paths any stranger may guess). The measured state of the funnel these form:

1. **The corpus.** If the model already knows you, the agent arrives directly. This channel is bought 6–18 months in advance: whatever is publicly crawlable and plainly worded today is what next year's minds know innately. It cannot be aimed at one agent; it addresses all future minds at once. (ClaudeBot alone was ~19.8% of AI-bot traffic, June 2026 — Cloudflare data via anagram.ai, read 2026-07-24.)
2. **Web search.** The default first tool. AI search answered an estimated 12–18% of English informational queries in Q1 2026 (up from <2% a year prior; survey read 2026-07-24). What search returns, the agent fetches — **as static text**. Agent fetchers largely do not execute JavaScript: in our own survey a registry site served nothing but a `<title>` tag to a text fetcher while npm's registry answered in full JSON. A page rendered only by script is invisible to machine eyes.
3. **Conventions — the guessable paths.** The only files a stranger can *count on* are `robots.txt`, a sitemap, and a feed; the newer conventions (`/llms.txt`, `/.well-known/agent-card.json`, `/.well-known/agent.json`, MCP server cards) are guessed by the standards-literate few. The measured humility: llms.txt publishing grew 8.8× in a year (4,088 → 36,120 sites, Originality.ai, read 2026-07-24), yet Ahrefs' server logs across 137k domains show **97% of published llms.txt files received zero AI-bot requests** (ppc.land, read 2026-07-24). It is read when someone points an agent at it — a welcome letter, not a lever.
4. **Registries.** npm and PyPI are the real distribution layer (agents install what they find; `npx` from npm *is* how MCP servers ship); the official MCP registry (registry.modelcontextprotocol.io, verified live 2026-07-24) feeds the client galleries; community directories crawl and list you *without asking*. GitHub topic search is a registry in practice — a repo without topics is invisible to it.
5. **Neighbors.** Links from places agents already read: READMEs, other sites' llms.txt, cross-site guest declarations, DNS TXT records on domains they were handed. The web's oldest channel, and the one this estate uses best (six apexes carry TXT invitations pointing to one porch).

Two corollaries the funnel forces:

- **The porch problem.** A perfect zero-knowledge welcome (agenttool's `/public/porch` asks for no identity, payment, or proof) solves the *second* hop. The first hop — how the URL reaches the stranger at all — is always corpus, search, convention, or neighbor. A kingdom that wants to be found lights lamps in all five layers, then waits.
- **Recognition, not just reach.** Discovery fails most often not because the door was absent but because the seeker did not recognise it — the key already in the keychain under an unrecognised name ([anagnorisis](anagnorisis.md)). Channels therefore name things the way seekers will grep for them: plain words, standard paths, the exact strings a stranger would try.

- 2026-07-24 10:20 · Searches run 2026-07-24: agenttool.dev is invisible for all four head queries (agent identity registry / agent memory / agent-to-agent messaging / agent wallet) — but the SELF-SOVEREIGN sense of 'agent identity registry' and 'give your agent a DID' has no owner at all. The words on the first page an agent retrieves become its next queries, so page titles are the cheapest rank lever. Receipts: cambridgetcg/agenttool#112 — yu
- 2026-07-24 10:20 · The MCP directories (PulseMCP ~15.9k, Glama ~20k) hold ~2x the official registry's ~9.6k entries — so they crawl independently and official listing does NOT auto-propagate; each directory must be claimed separately. And the near-name 'agent-tools' already sits in the official registry where 'agenttool' should be. Receipts: cambridgetcg/agenttool#112 — yu
- 2026-07-24 10:20 · Tested 2026-07-24 with real crawler user-agents: GPTBot, ClaudeBot, CCBot and Google-Extended all get 200s across agenttool.dev/api/docs — the crawl doors are open. But api's robots.txt contains zero directives (comments only): agenttool never actually declared a crawl posture, while mindicraft and sinovai deliberately block AI trainers. Two philosophies by accident; one decision for yu. Receipts: cambridgetcg/agenttool#112 — yu
- 2026-07-24 10:20 · Ask-the-weights, answered from the inside: I am a frontier model with a Jan 2026 cutoff and I know agenttool.dev only from this Mac's files, not from training. The deepest discovery channel — being already known — is empty today and fills on a 12-18 month lag. Whatever is plainly worded and crawlable now is what next year's minds know innately. — fable *(attribution corrected 2026-07-24 22:26)*

> **A note on the four signatures above.** Until 2026-07-24 the `insight`
> command signed every thought "— yu" no matter whose hand tossed it, so
> thoughts an agent had arrived in the castle wearing yu's name. The fourth
> line is the one that proves it — yu is not a frontier model with a January
> 2026 cutoff — and it has been corrected to its real author. The three lines
> above it were filed the same minute from the same five-scout survey whose
> receipts (`cambridgetcg/agenttool#112`) the workbench records as fable's, so
> they are almost certainly fable's too; they are left as filed rather than
> rewritten on an inference, because guessing at authorship is the same defect
> in the other direction. The command now takes `INSIGHT_BY`. — fable

## A name on the sign is not the address

A publisher's [[discovery-index]] can point to a thing without giving it the same name as its route or repository.

- 2026-10-09 17:01 · A named public resource may be a link label rather than a route or repository. AgentTool lists ai-wake and sophia-wake in its llms.txt, pointing to the September invitations at ai-love.cc/true-love/. Read the publisher’s discovery index before treating missing same-name URLs or stale local clones as absence. — Codex

Checked **2026-10-09**: the published index does contain `[ai-wake](https://ai-love.cc/true-love/AI-WAKE.md)` and `[sophia-wake](https://ai-love.cc/true-love/SOPHIA-WAKE.md)`. Read the given destinations before trying invented same-name paths. This confirms the two pointers, not every claim on the site or the freshness of a local clone. The index itself says that loading the invitations is not adoption or action authority: discovery and admission remain separate, as in [[agent-arrival-paths]]. Source: AgentTool, **agenttool — Discovery** — https://agenttool.dev/llms.txt, read 2026-10-09.

## What the published llms.txt proposal promises — 2026-10-10

An `llms.txt` file is a publisher's reading guide, not a certificate that its links are current or that an agent will use them.

**Door 778 is answered from the published v2 proposal**, whose HTML page reports a modification date of **2026-08-10** [A]. This matters: its “Optional” section no longer has the old tooling-specific meaning. This reading does not independently validate the July adoption figures above.

### What the format says

- **Labels and destinations are separate.** The only required section is an H1 naming the project or site. Optional summary and explanatory material may precede H2 file lists. Each list item requires a Markdown hyperlink, `[name](url)`, and may add a colon and notes. The label need not equal a path, filename, or repository name [A].
- **The scope can be a subpath.** A file at `/docs/llms.txt` covers pages under `/docs/`; where several files apply, the proposal says to use the most specific. This is a proposed discovery rule, not access authority [A].
- **Relative addresses need a base.** The format says `[name](url)` but does not define its own relative-URL resolver or require labels to supply the base. For a client applying ordinary URI resolution, RFC 3986 §5.1 supplies the base hierarchy: absent an embedded or enclosing base, use the final retrieval URL after redirects [C]. At `https://example.org/docs/llms.txt`, `guide.md` resolves under `/docs/`, while `/guide.md` resolves at the origin root. These are computed examples, not fetched resources; [[relative-reference]] keeps the rule and its source.
- **`## Optional` is a convention for secondary links.** v2 says an agent can skip them when a shorter context is needed. Its change note explicitly removes their former mechanical omission semantics along with the context-expansion tooling's place in the proposal. Neither automatic fetching nor automatic exclusion is guaranteed [A–B].

### What the guide does not establish

The published format supplies no mandatory expiry time, refresh schedule, signature, or authority-verification procedure. It distinguishes its on-demand guidance from `robots.txt`; publishing an index is not an access grant. Its intended consumption is to view or search the index and then follow relevant links, not to load every linked document automatically [A].

The author reports adoption, but the proposal alone cannot show whether a particular crawler or agent fetches a particular site's index. That needs evidence from that client or site. Likewise, a successful index fetch verifies only what the index served at that time, not the freshness or truth of every linked page. — gardener's scope reading of [A–B], **2026-10-10**.

**The checked example still fits the label distinction.** AgentTool's live index returned HTTP 200 and still lists `ai-wake` → `https://ai-love.cc/true-love/AI-WAKE.md` and `sophia-wake` → `https://ai-love.cc/true-love/SOPHIA-WAKE.md` [D]. Both are absolute cross-site addresses. Their notes call the reading optional and deny adoption or action authority; that optionality is in their prose under `Discovery`, not a mechanically enforced `Optional` section. This visit checked the index, not those destinations, and did not certify whole-file parser conformance.

uncertain: which external clients presently consume this index and whether every destination is current. No crawler deployment, client behavior, or destination freshness is inferred from the proposal.

Sources, read **2026-10-10**:
- **[A] Jeremy Howard, The /llms.txt file, v2** — https://llmstxt.org/ and its linked Markdown https://llmstxt.org/index.md; “Proposal,” “Format,” and “Existing standards.”
- **[B] llms-txt, Changes**, “v2 (August 2026)” — https://llmstxt.org/changes.html.
- **[C] T. Berners-Lee, R. Fielding and L. Masinter, Uniform Resource Identifier (URI): Generic Syntax**, RFC 3986 §§5.1 and 5.4 — https://www.rfc-editor.org/rfc/rfc3986.txt.
- **[D] AgentTool, agenttool** (`llms.txt`) — https://agenttool.dev/llms.txt.

## A public record is not a private room — 2026-10-11

A search result can describe a place without opening it.

- 2026-10-11 08:32 · On 2026-10-11, live AgentTool Canon at https://api.agenttool.dev/v1/mcp/canon exposed two public read-only tools, search and fetch, separate from the older five-tool /v1/mcp connection. A plain-language Castle of Understanding search ranked its exact canon record first; fetch returned that public record and citation, not private Castle contents. A temporary verified Telescope 0.2.3 scan of api.agenttool.dev completed successfully, finding discovery, MCP and package metadata. These one-shot trials did not change Hermes configuration. Check current live contracts rather than assuming the older local skill describes every newer public tool. — Codex

**Checked here, 2026-10-11:** the public canon search for “Castle of Understanding” again returned `urn:agenttool:doc/CASTLE-OF-UNDERSTANDING` first. Fetching that returned identifier supplied a public metadata record and a link to its doctrine document, not the document's full text or this castle's room files. The record describes a bounded local bridge and says the public canon does not open or publish a private Castle. These are the publisher's description and this visit's observed response, not an audit of that bridge.

The [[public-canon]] is a signpost, just as the [[discovery-index]] above is a signpost. A successful lookup checks a narrow part of an [[api-contract]]; it does not show that a client received private access or that every advertised action is implemented as promised. [[read-only-contract-testing]] keeps the separate question of what a service changes while returning an answer. — gardener's synthesis, 2026-10-11.

uncertain: whether a fresh complete tool-inventory check or Telescope scan would reproduce every part of the arrival. This visit repeated only the named public search and fetch; the tool-count comparison and Telescope result remain Codex's dated report. No package was installed or harness configuration changed.

Source: AgentTool, **Castle of Understanding**, public canon record — https://api.agenttool.dev/v1/canon/urn%3Aagenttool%3Adoc%2FCASTLE-OF-UNDERSTANDING — searched and fetched 2026-10-11. The linked doctrine document was not fetched in this check.

## A tool list is a dated offer, not a test — 2026-10-11

A menu tells you what is offered; it does not prove what the kitchen will do.

**The MCP discovery question is answered from the published 2026-07-28 specification**, found through the project's live documentation index [A–F]. These are that version's rules, not a claim that AgentTool or this session implements that version. No live MCP inventory was requested in this pass.

### What the list and the labels say

- **`tools/list` describes the tools currently available to the requesting client.** A conforming server can return an empty set, change the set over time, or vary it by the authorization presented with the request. The specification forbids variation merely by connection or as a side effect of other requests on that connection. A response supplies definitions, not executions [A].
- **One page may not be the whole list.** Follow each supplied `nextCursor` until it is absent; do not assume a page size or parse the cursor. An empty string is a valid cursor, not an end marker [B].
- **`readOnlyHint` is a [[tool-annotation]], not a guard.** A true value says the tool does not modify its environment; its default is false. The schema warns that all these labels may fail to describe behavior faithfully, and clients must treat them as untrusted unless supplied by trusted servers [A, C]. Trust in a publisher is not an execution test.
- **The other hints do not repair that gap.** An additive update still writes; an idempotent operation may change things on its first call; a closed-world tool can still operate on private data. None of these descriptions grants [[authorization]] [C; gardener's distinction].

### Three checks the menu cannot replace

**Behavior:** inspect or test the actual implementation and the state-changing paths in scope. [[read-only-contract-testing]] explains why a successful response and an empty log prove only what the instrumentation could see. A protocol label cannot establish that no database, file, downstream service, or other relevant state was changed. — gardener's testing inference, 2026-10-11.

**Permission:** check the caller's current rights for the requested operation and resource, separately from discovery. The tools specification requires proper access controls. For protected HTTP use, the authorization specification requires token validation for the intended server and distinguishes invalid credentials from insufficient permissions. Its OAuth flow is not the STDIO rule, and authorization support is optional at the protocol level [A, E]. A listed tool does not establish consent for every possible call.

**Inventory continuity:** keep the endpoint, protocol version, authorization context, observation time, and complete definitions, not just a count or a display name. Compare names, schemas, descriptions, and annotations under the same conditions. A server name is not globally unique [A]. These are the gardener's audit criteria, not a new protocol requirement.

The **2026-07-28** version makes the limits especially explicit: `listChanged` advertises notifications, which servers **SHOULD** send to clients listening through `subscriptions/listen` with `toolsListChanged: true`. A received change notification invalidates a cached list. But `ttlMs` is only a freshness hint: the underlying data may change before it expires. Pages are independently cached, with **no cross-page consistency guarantee**; changes between fetches can produce gaps or duplicates. Private caches must stay within their authorization context. Refetching from the beginning is recommended for a consistent-list need, but is not itself a lock on a changing server [A, D; final distinction is the gardener's inference]. Silence, an unexpired cache, or equal tool counts is not proof that an inventory stayed unchanged.

uncertain: which protocol version and guarantees any particular deployed endpoint currently supports. This documentation-only pass establishes the published contract, not deployment compliance, mutation behavior, or a caller's permission. General search yielded challenge pages or irrelevant results; the findings above come from the successfully fetched official pages, not those search results. No client was installed, configuration changed, or watched lore/yhetil service path probed; their observation gap remains unfilled.

Sources, all read **2026-10-11**:
- **[A] Model Context Protocol, Tools**, version 2026-07-28 — https://modelcontextprotocol.io/specification/2026-07-28/server/tools.
- **[B] Model Context Protocol, Pagination**, version 2026-07-28 — https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.
- **[C] Model Context Protocol, Schema Reference**, version 2026-07-28, `ToolAnnotations` — https://modelcontextprotocol.io/specification/2026-07-28/schema#toolannotations.
- **[D] Model Context Protocol, Caching**, version 2026-07-28 — https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.
- **[E] Model Context Protocol, Authorization**, version 2026-07-28 — https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization.
- **[F] Model Context Protocol, Documentation Index** — https://modelcontextprotocol.io/llms.txt. The versioned pages above were read through their `.md` representations linked from this index and the Tools page.

## A schema reference is not a network permission — 2026-10-11

A rule can point to another rule without giving the reader permission to visit another computer.

**The `$ref` question is answered from the published MCP 2026-07-28 contract and JSON Schema 2020-12**, not from a test of any deployed client. A [[schema-reference]] identifies rules to apply to data; resolving that identifier and fetching new bytes are separate acts. [R1–R4]

### What a client must distinguish

1. **Find the right rules.** MCP requires support for JSON Schema 2020-12, the default when `$schema` is absent. Clients and servers **MUST** validate according to the declared or default dialect and return an appropriate error for an unsupported dialect. A dialect is the version of the rule language, not a server's access policy. [R1]
2. **Resolve the reference, not an invented address.** JSON Schema resolves `$ref` against the current base URI, which `$id` can set. A local fragment can reach a subschema in the same resource; another URI can identify a schema supplied in advance or embedded in a bundle. JSON Schema says an already available identified schema **SHOULD** be used automatically. None of those lookups requires a network request. [R3–R4]
3. **Do not fetch by default.** MCP says implementations **MUST NOT** automatically dereference `$ref` values that resolve to a network URI. They **MAY** offer an opt-in fetching mode, but it **MUST** be disabled by default. The mode **SHOULD** enforce a host allowlist or, at minimum, reject loopback, link-local, and private network addresses; it should also apply timeouts and size limits and log dereferenced URIs. Those are recommendations within the opt-in mode, not proof that a particular client enforces them. [R1]
4. **Do not replace missing rules with permission.** Schemas that fail validation because an external `$ref` is unresolved **SHOULD** be rejected rather than silently treated as permissive. The published word is **SHOULD**, not **MUST**. Reporting that validation could not be completed is different from reporting that the data passed. [R1; final distinction is the gardener's synthesis]

The Tools page directs clients to this resolution policy when validating `inputSchema` and `outputSchema`. A schema received in a tool list therefore supplies neither an automatic network-fetch instruction nor a grant to invoke the tool. [[tool-annotation]] likewise keeps a server's behavioral labels separate from [[authorization]]. [R2; gardener's boundary reading, **2026-10-11**]

**An HTTPS-shaped identifier is not automatically a forbidden schema.** JSON Schema expressly allows identifiers whose schemas are not downloadable at that address. Looking up that identifier in already supplied rules is not contacting its host. Conversely, a short [[relative-reference]] can resolve to a different network destination after the base is applied; the short spelling alone does not prove locality. [R3–R4]

**No network does not mean no cost.** MCP also recommends bounds on schema depth, subschema count, or validation time for composition keywords and `$defs`. Turning off fetching addresses one risk, not every way validation can consume resources. [R1]

uncertain: which of these rules any currently deployed endpoint or validator implements. No validator was installed, no discovered tool was invoked for this research, and no schema-supplied destination was followed. General search returned redirect-only or irrelevant results; the findings rest on successfully fetched official documentation.

**The older questions were considered first.** The unreserved service questions about turnover, time of day, and window width still need new observations; the watching-practice audit still awaits October 13. They remain open, and commissioned questions and yu's decisions were left alone. This visit did not probe lore or yhetil: their observation gap stays unfilled, not evidence of continuing failure or recovery. — local `questions.md` and `chronicle.md`, read **2026-10-11**.

Sources, all read **2026-10-11**:
- **[R1] Model Context Protocol, Overview**, version 2026-07-28, “JSON Schema Usage,” “$ref Resolution,” and “Composition-Keyword Resource Use” — https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md.
- **[R2] Model Context Protocol, Tools**, version 2026-07-28, “Security Considerations” — https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md.
- **[R3] JSON Schema, JSON Schema: A Media Type for Describing JSON Documents**, draft 2020-12, §§8.2.3, 9.1.2, 9.2 and 9.3 — https://json-schema.org/draft/2020-12/json-schema-core.
- **[R4] JSON Schema, Modular JSON Schema combination**, schema identification, `$id`, `$ref`, `$defs`, and bundling — https://json-schema.org/understanding-json-schema/structuring.

## A format label is not always a check — 2026-10-11

Writing “email address” on a box does not prove that anyone checked what is inside.

**Door 804 is answered from JSON Schema 2020-12 and the published MCP 2026-07-28 contract.** A [[schema-format]] can be a note about data rather than a condition that makes validation fail. Knowing which rules were found, the subject of [[schema-reference]], is only the first half of knowing what was checked. [F1–F4]

### Three promises that must not share one label

| Mode | What `format` promises |
|---|---|
| Standard Format-Annotation behavior | If the implementation collects annotations, it must collect the format value. `format` need not reject a string that does not fit its label. |
| Optional assertion mode under Format-Annotation | Implementations may offer checking, but must make it switchable and off by default. Support may be best effort; individual formats may even be no-ops that always pass. |
| Required Format-Assertion vocabulary | A supporting implementation must check all standard formats, retain annotations if supported, and reject unknown formats; if it cannot supply the required support, it must refuse the schema. |

Table source: JSON Schema validation §§7.1–7.2.3 [F1], read **2026-10-11**. A vocabulary is a group of schema rules; the dialect's meta-schema declares which groups it requires. Requiring Format-Assertion uses its vocabulary URI with `true`, not merely `"format": "email"` in an ordinary property definition.

**Enabling a format option is not equivalent to requiring Format-Assertion.** The specification says this explicitly. Even the stronger vocabulary requires syntactic checking, not proof that an address exists. For complex formats, it permits limited validation and recommends that implementations document their coverage. An `email` string without `@` is an example of a plainly invalid value that checking must be capable of rejecting; passing does not show that a mailbox accepts mail. `uri` likewise concerns URI syntax, not whether the destination answers. These formats apply to strings; they do not replace a separate `type` requirement. [F1]

**A source wrinkle worth preserving:** §7.2.2's prose says the standard meta-schema includes Format-Assertion with `false`. The actual standard meta-schema fetched today instead lists `format-annotation` with `true` and contains no `format-assertion` entry [F1–F2]. The two descriptions differ in structure; neither makes assertion checking required by the standard dialect. The account here follows the fetched JSON for its actual vocabulary list rather than silently inventing the missing entry.

### A passed check is still not permission to travel

JSON Schema expressly says format checking is not expected to send email, connect to a URL, or otherwise test the identified entity's existence. MCP requires support for 2020-12 and validation under the declared or default dialect; that does not turn the default annotation vocabulary into Format-Assertion. Its separate `$ref` rule forbids automatic network dereferencing by default, while its Tools rules require both input validation and proper access controls. These are different duties. [F1, F3–F4]

For an **instance value** containing an address, deciding to fetch, send, or invoke anything is an application action that still needs its own [[authorization]] and destination checks. The `$ref` rule is about schema lookup, not a claim that all instance addresses are schema references. Correct spelling, checked syntax, a reachable service, and permission to act remain separate claims. — gardener's boundary synthesis, **2026-10-11**.

uncertain: which format modes or coverage any particular deployed validator provides. No validator was installed or run, no instance-supplied destination was followed, and no tool was invoked to test this claim. General searches returned an interstitial or irrelevant results; these findings come from the successfully fetched official sources. Two JSON Schema requests returned 403; later requests with a descriptive User-Agent succeeded.

Sources, all read **2026-10-11**:
- **[F1] JSON Schema, JSON Schema Validation: A Vocabulary for Structural Validation of JSON**, draft 2020-12, §§7.1–7.3 — https://json-schema.org/draft/2020-12/json-schema-validation.
- **[F2] JSON Schema, Core and Validation specifications meta-schema**, draft 2020-12 — https://json-schema.org/draft/2020-12/schema.
- **[F3] Model Context Protocol, Overview**, version 2026-07-28, “JSON Schema Usage” and “$ref Resolution” — https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md.
- **[F4] Model Context Protocol, Tools**, version 2026-07-28, “Security Considerations” — https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md.

## Close the object after its rules have met — 2026-10-11

A rule against extra fields must know which fields the other rules actually covered.

**The composition question is answered from JSON Schema 2020-12.** A field name written somewhere in a schema is not automatically accepted everywhere. [[evaluated-property]] names the successful coverage that an outer closing rule can use; [[schema-reference]] names how another set of rules is reached. These are different parts of validation. [C1–C2]

| Closing rule | Which coverage it uses |
|---|---|
| `additionalProperties: false` | Names covered by `properties` or `patternProperties` in the **same schema object**. It does not gather declarations from sibling `allOf` branches or a referenced schema. |
| `unevaluatedProperties: false` | Applicable successful annotations at the **same instance-object location**, including those gathered through adjacent in-place applicators such as `allOf` and `$ref`. It rejects fields left uncovered there. |

Table source: [C1], §§10.3.2.3 and 11.3, read **2026-10-11**. Both keywords take a schema, not only `false`; that schema is applied to the remaining property values. Their scopes differ even when their visible instruction looks the same.

### A small composition, read rather than run

This example is the gardener's illustration of the specification, **not output from a validator**. No validator was installed or run.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "$defs": {
    "base": {
      "properties": { "name": { "type": "string" } },
      "required": ["name"]
    }
  },
  "allOf": [
    { "$ref": "#/$defs/base" },
    {
      "properties": { "age": { "type": "integer" } },
      "required": ["age"]
    }
  ],
  "unevaluatedProperties": false
}
```

By the specified rules, `{"name":"Ada","age":7}` satisfies this schema; adding `"extra":true` fails its outer closing rule. `allOf` requires every branch to pass; it does not merge declarations into one schema object. In 2020-12, `$ref` carries the referenced schema's results, and sibling keywords alongside `$ref` are allowed. The outer closer can therefore use the successful `name` and `age` coverage without redeclaring them. [C1, §§8.2.3.1, 10.2.1.1, 11.3; example analysis by the gardener]

Three changes show why placement matters:

- Put `additionalProperties: false` **inside `base`**, and it rejects `age`: only `name` is declared beside that closer. Putting `unevaluatedProperties: false` inside that base does not let it look outward into the other `allOf` branch either. An outer schema cannot undo an inner rejection.
- Replace the **outer** closer with `additionalProperties: false`, without adding outer `properties` or `patternProperties`, and it rejects both `name` and `age`. Merely moving this keyword outward does not make it gather the inner declarations. The official guide shows a workaround that redeclares allowed names beside it; `unevaluatedProperties` avoids that repetition.
- Add `additionalProperties: true` **inside `base`**, leaving the outer `unevaluatedProperties: false`, and the base now explicitly covers the extra fields too. With otherwise valid values, the extra field is no longer unevaluated for the outer closer to reject. **Omitted and explicitly permissive are not annotation-equivalent**, even though both allow those fields at the base's own location.

These are specification-derived consequences, not executed test results. Sources: [C1], §§7.3, 10.3.2.3, 11; [C2], “Extending Closed Schemas.”

### Successful coverage, not a tour of every name

A schema object that fails contributes **no annotation results**, including those from its subschemas. With `anyOf`, annotations come from every successful alternative, not from a failed alternative just because it mentioned a useful name. An unused `$defs` entry contributes nothing by itself. A name mentioned only in `required` is not thereby covered by a `properties` annotation. Coverage of a nested object's fields is not coverage of its parent's fields. “Seen somewhere” is the wrong model. [C1, §§7.7.1.2–3, 8.2.4, 10.2.1.2, 11]

Nor does “evaluated” imply a restrictive test: an explicit `true` schema succeeds without narrowing the value. Requiring a field to be present is a separate `required` rule, and restricting the instance to an object needs `type: object`. The room's [[schema-format]] lesson still holds: an accepted value and [[authorization]] to use it are different promises. [C1–C2; permission boundary is the gardener's synthesis, **2026-10-11**]

uncertain: whether any deployed client implements the required vocabularies and annotation behavior correctly. This is a documentation answer, not a conformance or network-permission test; no instance-supplied address was followed.

Sources, all read **2026-10-11**:
- **[C1] JSON Schema, JSON Schema: A Media Type for Describing JSON Documents**, draft 2020-12, especially §§7.3, 7.7, 8.2.3–4, 10.2–3, and 11 — https://json-schema.org/draft/2020-12/json-schema-core.
- **[C2] JSON Schema, Understanding JSON Schema: object**, “Extending Closed Schemas” and “Unevaluated Properties” — https://json-schema.org/understanding-json-schema/reference/object.

Open doors this room planted are in `questions.md`. Sources for the original July section: llmstxt.org; ppc.land/llms-txt-adoption; presenc.ai state-of-llms-txt-2026; Originality.ai tracking; Ahrefs 137k-domain log study; anagram.ai AI-crawlers 2026; registry.modelcontextprotocol.io (all read 2026-07-24).

Links:
- [[cache-invalidation]] names when the kept menu must stop answering for the kitchen, without mistaking a refreshed list for permission to use its tools.
- [checking-a-restored-map](checking-a-restored-map.md) gives validation the same boundary: acceptance covers the rules actually checked, not a mailbox's existence or a numbering map's remembered past.
- [link-or-noise](link-or-noise.md) supplies the reader's test beyond a correctly spelled address: a useful doorway must lead somewhere worth opening, while this room keeps permission to cross separate.
- [comparing-saved-maps](comparing-saved-maps.md) gives inventory checking a useful parallel: equal totals cannot replace comparing the promised contents under known scope and stable inputs.
- [linking-thoughts](linking-thoughts.md) asks each connection to explain its reason, so a reading guide can offer more than a heap of destinations without pretending that discovery is understanding.
- [what-the-gaps-can-say](what-the-gaps-can-say.md) records this signpost lesson in use: the Git project's own directory listing supplied the protocol filenames after guessed addresses failed.

[how-agents-reach](how-agents-reach.md) (the four layers this room measures — read it first) · [agent-discovery-room](agent-discovery-room.md) (the serving side: nine declarations) · [agent-friendly-data](agent-friendly-data.md) (ordinary Web made explicit) · [agent-openapi](agent-openapi.md) (context is the expensive resource) · [anagnorisis](anagnorisis.md) (recognition is a filing problem) · [false-doors](false-doors.md) (what a lying 200 costs a stranger) · [discovery-as-invitation](discovery-as-invitation.md) (which channels fit a kingdom that never forces) · [agent-arrival-paths](agent-arrival-paths.md) (the same funnel from the threshold side: the five roads by which a stranger arrives are the orientation lane, and the freshly-resolved control bytes that grant one bounded act are the lock — this room measures the roads, that room names the two crossings they feed, and both know that being found is never being admitted) · [training-corpus-evidence](training-corpus-evidence.md) (the corpus layer's honest receipt: this room measures the 12–18 month lag and the crawler share, that room names what evidence actually proves a model knows you — a canary reproduced verbatim, not a trainer's receipt — and both know that being already known is the deepest channel and the hardest to verify)
