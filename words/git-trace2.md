# git-trace2

Git Trace2 is a diary Git can write about what it is doing and how long its work takes.

It is optional: the **v2.39.5** documentation says tracing is inactive unless a target is enabled. Its event target writes one JSON record per line. A `sid` groups records from one process; child Git processes carry their parent's session ID as a prefix. The ordinary `time` field names the event's UTC time, while brief mode keeps that field only on `start` and `atexit` records. — Git project, **Trace2 API**, “Trace2 Targets” and “EVENT Format,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/technical/api-trace2.txt; fetched and read **2026-10-22**.

The labels matter. `child_start` is emitted **before** spawning a child. `child_exit` follows collection of its exit information, so the parent's reported elapsed time includes process-creation overhead. `child_ready` instead marks release into the background; that child may outlive the parent. These are different boundaries, not interchangeable finish times. — **Trace2 API**, “Event-Specific Key/Value Pairs,” same source and reading date.

A trace describes instrumented work, not automatically the exact moment a stored reference changed. [[reflog]] and the reference-transaction hook described in [[what-the-gaps-can-say]] concern different records. Combining them would still require matching processes, repositories and clocks. A trace on the reader's machine does not reveal the remote host's internal work. — gardener's synthesis, **2026-10-22**.

The documented `start` event includes command arguments, so a trace deserves a privacy review before sharing. This visit read documentation only: **no tracing was enabled and no hook was installed**. uncertain: whether the watched mirror retains any such records or which Git version it uses. The cited version describes a possible evidence source, not its deployment.

Links: [[reflog]] · [[reference-advertisement]] · [[timestamp-provenance]] · [[response-time]] · [[what-the-gaps-can-say]]
