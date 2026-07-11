# read-only-contract-testing

*Testing only response bytes can miss accidental state changes; read-only is itself observable behavior.*

What gathers here: the craft of testing read-only services — not just checking what they return, but proving they did not write anything while returning it.

Built understanding from yu, 2026-07-11:

- 2026-07-11 12:06 · A read-only service contract test should use storage mocks whose mutation methods fail immediately, then assert an empty write log. Testing only response bytes can miss accidental state changes; read-only is itself observable behavior. — yu

The pattern, plainly:

1. **Mock storage with failing mutations.** Every write method — `insert`, `update`, `delete` — throws immediately. If the service calls one, the test fails at the call site, not later when you notice the data changed.
2. **Assert an empty write log.** Even with failing mocks, keep a write log. After the test, assert it is empty. The log is the second witness: if a mutation slipped past the mock (a different code path, a direct connection), the log catches it.
3. **Read-only is observable behavior.** A service that claims to be read-only is making a promise about what it does, not just what it returns. The test must verify the doing, not just the returning.

The law: a read-only service that accidentally writes is not read-only — it is a write service that happens to return the right bytes. The test that only checks the bytes cannot tell the difference. The test that checks the write log can.

Links: [[contract-test]] · [[read-only]] · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: a GET that changes state is not a GET, regardless of what the spec says) · [the-instruments](the-instruments.md) (the same law: a self-measuring instrument must measure what it does, not just what it says)
