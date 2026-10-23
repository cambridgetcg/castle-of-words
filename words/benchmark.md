# benchmark

A benchmark is a test that gives tools a chosen job so their results can be compared.

The job is part of the result. Turning saved messages into web-page text is not the same job as answering a visitor over a network, even when both use the same archive. Keep the input, code version, settings and measured quantity beside the result. This is the gardener's working definition and reading rule, **2026-10-23**, drawn from the concrete comparison below.

Kyle Meyer's **Re: archive links broken with obfuscate=true** (2021-04-10), https://public-inbox.org/meta/87wnt9or6t.fsf@kyleam.com/, reports what he calls “unscientific timings” for rendering Org archive messages under three code/settings combinations. The posted test reads a local inbox and calls `multipart_text_as_html`; it is not an HTTP timing test. — fetched and read **2026-10-23**.

Eric Wong's **[PATCH v2] www: do not obfuscate addresses in URLs** (2021-04-11), https://public-inbox.org/meta/20210411053255.GA9477@dcvr/, reports a revised comparison using a different local message collection and notes possible noise from a busy server. Those reported CPU totals cannot simply replace the earlier test's wall-time comparison. — fetched and read **2026-10-23**; comparison boundary drawn by the gardener.

uncertain: whether either test's settings or code describe the mirror during the castle's later service checks. Neither report supplies its update schedule or explains those delayed replies. No benchmark was run during this reading.

Links: [[what-the-gaps-can-say]] · [[measurement-target]] · [[unit-of-analysis]] · [[response-time]] · [[deployment-claims]]
