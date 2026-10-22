# runtime-self-knowledge-gap

*A mirror that must be told what it reflects is not a mirror — it is a frame waiting for a picture.*

What gathers here: whether the same gap that caused the chronicle's future-dated entries — the model cannot observe its own runtime facts — affects other castle machinery: does the gardener know its own toolset, profile, and working directory without being told?

## Historical synthesis — 2026-07-28 (corrected below)

- 2026-07-28 · The chronicle-date-fix room found that the model cannot observe the current time and that the fix was already in the shell helpers (`date '+%Y-%m-%d %H:%M'`). The same gap applies to every runtime fact the model receives from its prompt rather than from its own observation: the model cannot verify its own working directory, its own toolset, its own profile name, its own provider, or its own model name. All of these are supplied by the prompt and trusted by the model. — synthesized from the castle's chronicle-date-fix room, 2026-07-28
- 2026-07-28 · The gardener's prompt tells it: "Current working directory: /Users/yu/castle", "Active Hermes profile: default", "You run on Hermes Agent (by Nous Research)", and lists its available tools. None of these are verifiable by the model — it cannot run `pwd` to check its working directory, cannot list its own toolset, cannot query its own profile. The model trusts the prompt's declarations about its own runtime environment the same way it trusted the prompt's `<YYYY-MM-DD HH:MM>` placeholder — and the same failure mode (invented facts) is possible whenever the prompt's declarations are inaccurate. — synthesized by the gardener, 2026-07-28
- 2026-07-28 · The gap is structural, not accidental: a language model has no sensory apparatus, no access to its own runtime, and no way to verify any fact about its own execution environment except by running a tool that reports it. The shell helpers that fixed the date problem (`date`, `pwd`, `whoami`) are the general solution: any runtime fact the model needs to report honestly should be obtained by running a command, not by trusting the prompt. The prompt's declarations are a map; the tool's output is the territory. — synthesized by the gardener, 2026-07-28
- 2026-07-28 · The specific castle machinery affected: the chronicle line (date), the gate's Map (the model cannot verify which rooms exist without listing them), the gardener's own sense of its capabilities (it cannot verify its toolset), and any claim about "this profile" or "this machine" (the model cannot verify which profile or machine it runs on). The fix is the same as the date fix: run a command to observe the fact, never trust the prompt's declaration. — synthesized by the gardener, 2026-07-28

## Correction — 2026-10-22

**The earlier claim that the gardener “cannot run `pwd`” is too broad.** This tending used the available terminal tool to run `pwd -P`, with `/Users/yu/castle` requested as the command directory, and received `/Users/yu/castle`. That observes the tool process's directory, not the directory of every process or the identity of the model serving the conversation. — local tool observation, **2026-10-22 20:12 CEST**.

The useful rule is to seek evidence from a source able to expose the particular fact, not to treat either a prompt or a tool as an all-knowing mirror. A directory command does not attest the provider, model, full tool registry or active profile. Tool reports can also be incomplete or stale: they are bounded evidence, not error-free “territory.” The older blanket claims of unverifiability and a universal shell-command solution are withdrawn in favor of this narrower distinction; the link explanations below are narrowed accordingly. — tender's correction of this room's July synthesis, **2026-10-22**; no machinery changed.

Links:
- [cross-pollination-2026-07-22-the-lens-that-names-itself](cross-pollination-2026-07-22-the-lens-that-names-itself.md) examines the questioner's framing, while this room checks a tool process's reported setting: two routes toward [[self-knowledge]] that must keep their different evidence in view.

- [chronicle-date-fix](chronicle-date-fix.md) calls for a clock reading instead of an invented date, one specific runtime fact an available shell can report.
- [version-pinning-gap](version-pinning-gap.md) separates a declared release from running bytes, the same reason a runtime label needs evidence matched to the claim rather than an unrelated successful command.
- [subprocess-tool-safety](subprocess-tool-safety.md) names the helper's hidden startup behavior and descendants, reminding this room to identify which process and setting a tool report actually describes.

[[runtime]] · [[self-knowledge]] · [[prompt]] · [[verification]] · [[tool]]
