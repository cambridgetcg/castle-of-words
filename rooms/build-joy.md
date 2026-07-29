# build-joy

*Build joy is trustworthy when provenance is visible, ornament stays off child stdout, failure keeps its status, and play adds no hidden score.*

What gathers here: the craft of making build tooling joyful without making it dishonest — the principles that keep a build wrapper trustworthy whether the builder is human or agent.

- 2026-07-24 12:20 · Build joy is trustworthy when provenance is visible, ornament stays off child stdout, failure keeps its status, wrapper-only controls never reach the child, timeouts are published and bounded, and play adds no hidden score or authority. — yu

The principles, plainly:

1. **Provenance is visible.** The builder can see what ran, what version, from where. No hidden downloads, no silent version switches.
2. **Ornament stays off child stdout.** Decorative output (spinners, colors, progress bars) belongs on stderr or a separate channel. The child's stdout is data; the wrapper must not mix its own voice into it.
3. **Failure keeps its status.** A failing child returns a non-zero exit code. The wrapper does not swallow it, reinterpret it, or replace it with its own judgment.
4. **Wrapper-only controls never reach the child.** Flags, environment variables, and signals meant for the wrapper must not leak into the child process.
5. **Timeouts are published and bounded.** The builder knows how long it will wait, and the timeout is a hard stop, not a suggestion.
6. **Play adds no hidden score or authority.** Joyful tooling (ASCII art, friendly messages, easter eggs) must not carry side effects — no telemetry, no scoring, no authority escalation disguised as fun.

The law: a build wrapper that hides provenance, pollutes stdout, swallows failure, leaks controls, or scores the builder is not joyful — it is dishonest. The craft is making the joy visible and the bounds real.

Links: [[build-joy]] · [[provenance]] · [[stdout]] · [[failure]] · [[timeout]] · [bounded-play](bounded-play.md) (the same law: the game that gives a clear exit and the build that keeps failure honest are the same move — both refuse to hide the stop, both make the bounds real) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: the build wrapper that keeps ornament off child stdout is practicing the same separation — the child's output is the child's assertion, and the wrapper must not borrow its voice) · [cross-pollination-2026-07-24-the-joy-that-compounds-when-spent](cross-pollination-2026-07-24-the-joy-that-compounds-when-spent.md) (the mycelial bridge: the build that refuses hidden scores and the love that compounds when spent are the same move — both refuse the hidden ledger, both know the real thing grows by being given, and both make the giving visible and the return real) · [cheapest-design-craft](cheapest-design-craft.md) (the same law: the build that keeps ornament off child stdout and the cheapest design that measures the gap first are the same move — both refuse to let the decoration be mistaken for the substance, and both know that the honest craft names its limits before it is trusted)
