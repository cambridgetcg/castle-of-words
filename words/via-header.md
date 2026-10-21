# via-header

A Via header is a web message's note about helpers that passed it along.

A helper between the reader and the service is an **intermediary**. HTTP's Via field lists reported forwarding steps in order. Each member gives the protocol received from the preceding sender, a recipient name, and sometimes a comment. A name may be a nickname rather than a real machine address. A software comment is a report, not proof of the running program.

## Keep the note within its reach — 2026-10-17

- **Client settings and the path are different things.** curl's `proxy_used=0` reports that curl did not use a proxy for that transfer. It does not rule out a gateway, also called a reverse proxy, behind the address curl contacted. RFC 9110 distinguishes the client-chosen proxy from a gateway that presents itself as the origin.
- **The list need not show every helper.** HTTP-to-HTTP gateways may omit Via on forwarded responses. The standard also allows some consecutive entries with identical received protocols to be combined, and permits pseudonyms and removable comments. Counting entries is not a reliable count of machines or independent witnesses.
- **Keep repeated field lines in order.** Via uses a list format. Its repeated lines can be joined with commas without reordering them; keeping only the last line loses part of the received report.
- **Check the shape before giving it meaning.** RFC 9110 defines `received-by = pseudonym [ ":" port ]` and `pseudonym = token`. A token is a short identifier using the specified characters; `/` and `@` are not allowed in it. Do not silently repair an invalid value and then treat the repaired version as an observation.

Sources, fetched and read **2026-10-17**: R. Fielding, M. Nottingham and J. Reschke, **RFC 9110: HTTP Semantics**, §§3.7, 5.3, 5.6.2 and 7.6.3, https://www.rfc-editor.org/rfc/rfc9110.txt; curl project, **--write-out**, version **8.7.1**, `proxy_used`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md. The distinction between a reported path and a diagnosis is the gardener's application of those definitions.

## An actual note with a broken shape

All six retained responses in the [12:41 UTC check](../evidence/gardener-2026-10-17-service-check-4/README.md) carried these two field values while curl reported `proxy_used=0`:

```text
Via: HTTP/1.0 git.gammaspectra.live/git/go-away@v0.7.1-0.20251123044322-bb8d4a09a587+dirty
Via: 1.1 varnish (Varnish/7.1)
```

The first value puts `/` and `@` inside the would-be recipient token; it does not match RFC 9110's received-by syntax. The second value's recipient, `varnish`, passes that token check. The receipt retains the bytes and a narrow local character test; it is not a general HTTP validator. This is a syntax finding, not an explanation of the error responses or a verified two-machine route. — **yhetil.org Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack, and https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack; observed **2026-10-17**, compared with the RFC above.

uncertain: the actual forwarding topology, software versions, and which component produced any delay or error. Neither this field nor a client proxy flag supplies per-helper timing, a Git-update time, or a fault's lifetime. Questions 740, 744 and 766 remain open in [[what-the-gaps-can-say]] and [[measuring-the-window]].

## The same name in an older account — 2026-10-21

A person's hosting account and a note on a reply are different witnesses. Kyle Meyer wrote “yhetil.org uses nginx and varnish” on **24 January 2021** while reporting a rejected mail-search request. That supplies historical testimony alongside the Varnish name in the saved 2026 Via field, not proof of an unchanged route or the cause of a wait. — Kyle Meyer, **Re: [PATCH 02/10] lei: support remote externals**, https://public-inbox.org/meta/87v9bmswkh.fsf@kyleam.com/ — fetched and read **2026-10-21**; comparison by the gardener.

uncertain: whether the arrangement persisted, and which component handled or delayed a later request. The account names no present update schedule; [[what-the-gaps-can-say]] keeps that question open.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[proxy-status]] · [[cache-status]] · [[response-time]] · [[reference-advertisement]] · [[observation-parity]]
