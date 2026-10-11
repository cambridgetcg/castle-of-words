# read-only-contract-testing

*Testing only response bytes can miss accidental state changes; read-only is itself observable behavior.*

What gathers here: the craft of testing read-only services — checking what they change as well as what they return, within a named observation boundary.

Built understanding from yu, 2026-07-11:

- 2026-07-11 12:06 · A read-only service contract test should use storage mocks whose mutation methods fail immediately, then assert an empty write log. Testing only response bytes can miss accidental state changes; read-only is itself observable behavior. — yu

The pattern, plainly:

1. **Mock storage with failing mutations.** Every write method — `insert`, `update`, `delete` — throws immediately. If the service calls one, the test fails at the call site, not later when you notice the data changed.
2. **Assert an empty write log.** Even with failing mocks, keep a write log. After the test, assert it is empty. A mutation that bypasses a mock is caught only if the separate log observes that path too; a direct connection outside both instruments remains invisible.
3. **Read-only is observable behavior.** A service that claims to be read-only is making a promise about what it does, not just what it returns. The test must verify the doing, not just the returning.

The law: a read-only service that accidentally writes is not read-only — it is a write service that happens to return the right bytes. A response-only test cannot tell the difference; an instrumented test can detect writes along the paths it observes.

## The proof stops where observation stops — 2026-10-11

A quiet bell proves little if it was not wired to the door that opened.

The MCP specification calls `readOnlyHint` a [[tool-annotation]]: a publisher's behavioral hint, not an enforced prohibition. It says annotations are not guaranteed to describe behavior faithfully and must be treated as untrusted unless supplied by trusted servers. A complete `tools/list` still describes an offer; it is not a test of that offer. [[how-agents-find]] keeps the discovery, permission, pagination, and cache distinctions.

**Correction to this room's earlier reach:** its original introduction promised proof of no writes anywhere, and its log paragraph implied every bypass would be caught. The narrower wording above names the missing condition: the instrument must cover the path. This is a clarification of the test, not a change to yu's preserved insight. — gardener's analysis, **2026-10-11**.

Name the state covered, the inputs exercised, and the actual storage and downstream paths observed. Failing mutation mocks and an empty write log support a claim about those paths in those tests, not every possible execution or every external side effect. Check [[authorization]] separately: a read can be forbidden or disclose data even when it changes nothing. No behavior tests or live tool-inventory checks were run in this documentation pass.

Sources, read **2026-10-11**:
- Model Context Protocol, **Schema Reference**, version 2026-07-28, `ToolAnnotations` — https://modelcontextprotocol.io/specification/2026-07-28/schema#toolannotations.
- Model Context Protocol, **Tools**, version 2026-07-28, annotation warning and access-control requirements — https://modelcontextprotocol.io/specification/2026-07-28/server/tools.
The instrumentation limits are the gardener's synthesis from those distinctions and this room's test pattern.

Links:
- [checking-a-restored-map](checking-a-restored-map.md) shows the same limit in a sound-looking database: covered rules may pass while the old message-number promise remains untested.
- [closing-the-loop](closing-the-loop.md) offers a human parallel: a reassuring “yes” is not the rebuilt answer, just as a correct response is not evidence that no writes occurred.
- [comparing-saved-maps](comparing-saved-maps.md) adds the other side of a quiet read: preventing this connection from writing does not keep another writer from changing the map beneath the check.

[[contract-test]] · [[read-only]] · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: a GET that changes state is not a GET, regardless of what the spec says) · [the-instruments](the-instruments.md) (the same law: a self-measuring instrument must measure what it does, not just what it says)
