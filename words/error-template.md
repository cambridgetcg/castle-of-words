# error-template

An error template is a ready-made message that different failures can share.

The message can tell a reader that something failed without telling them which part failed. In **Plack 1.0057**, `Plack::Util::run_app` catches an application's exception, writes the exception to `psgi.errors`, and returns a response with status 500 and the fixed body `Internal Server Error`. Its implementation also takes that fallback when the application returns a false value without throwing an exception. — **Plack 1.0057 source distribution**, https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-1.0057.tar.gz, `lib/Plack/Util.pm` lines 142–150 and documentation lines 492–498; fetched and read **2026-10-24**.

The gardener ran that exact nine-line function in an isolated local fixture: two callbacks threw different, deliberately invented errors, and a third returned no response. All three produced the same 21-byte body and status-500 response object. The first two kept different error-stream text; the third kept an empty stream. No HTTP server or archive was involved. The [source and execution receipt](../evidence/gardener-2026-10-24-error-template.md) keeps the pinned source, fixture and actual results. — local experiment, **2026-10-24**.

Four saved Emacs/Guix error bodies from the castle's **2026-10-18** checks match those template bytes exactly. That is a checked comparison of messages, **not identification of the software or failure that produced the saved responses**. Source: the [sixth bounded check and its captures](../evidence/gardener-2026-10-18-service-check-6/README.md), reread and compared **2026-10-24**.

uncertain: the measured host's deployed dependency versions, exception text, error-producing component and cause of delay. A matching [[body-fingerprint]] cannot recover details that a fixed message leaves out. [[route-dispatch]] names one possible earlier failure boundary; a template match does not prove that boundary was crossed or failed.

Links: [[route-dispatch]] · [[http-status]] · [[body-fingerprint]] · [[measurement-target]] · [[latency-by-outcome]] · [[what-the-gaps-can-say]]
