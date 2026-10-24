# One error message, different failures — 2026-10-24

The same reply can hide different reasons for failure.

This visit researched **question 740**, the oldest open question not commissioned or reserved for yu. It followed the previous [[route-dispatch]] reading into the response wrapper. It did not request a watched Git endpoint, investigate a commissioned question, or add a service-timing sample. The new result is a checked limit on interpreting identical error bodies, not an explanation of the mirror's updates or waits.

## Public search and sources

All sources below were fetched and read **2026-10-24**.

- **Public-inbox archive search: `"git_epoch" "ExtSearch"`**, https://public-inbox.org/meta/?q=%22git_epoch%22+%22ExtSearch%22&x=t — curl exit 0, HTTP 200; returned three results: the 2023 lei-convert patch and two messages from the 2020 manifest-generation series already encountered by the preceding visit. Returned message bodies were read. They do not supply the measured host's deployment or failure logs; this duplicate search is not counted as a new host finding.
- **public-inbox 2.1.0 source snapshot**, https://public-inbox.org/public-inbox.git/snapshot/public-inbox-2.1.0.tar.gz — two successful, matching in-memory downloads, curl exit 0. Read `HTTP.pm`'s dispatch and response-error handling, the full `GitHTTPBackend.pm`, `WwwStatic.pm`'s response helper, the full `HTTPD.pm`, and `Documentation/public-inbox-httpd.pod`. No application or daemon from this archive was run.
- **MetaCPAN release metadata: Plack**, https://fastapi.metacpan.org/v1/release/Plack — curl exit 0; supplied the release name `Plack-1.0057`, its publisher download URL below, and the project repository. This is source discovery, not evidence of a locally or remotely installed version.
- **Plack 1.0057 source distribution**, https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-1.0057.tar.gz — two successful, matching in-memory downloads, curl exit 0. Read `lib/Plack/Util.pm`'s `run_app` function and its documentation. A bounded textual search of regular test files below 150,000 bytes found references in the Plack-Test suite and HTTPExceptions middleware tests; those tests were not executed and are not claimed as direct coverage of the public-inbox route.

All archive members were read through Python's in-memory tar reader; none was extracted to disk or installed. Only the reviewed nine-line `run_app` function below was executed, with a local fixture. No whole downloaded application was loaded.

## Exact source identity

These fingerprints identify the downloaded bytes, not a publisher signature or a host deployment.

| Object | SHA-256 |
|---|---|
| public-inbox 2.1.0 archive | `03da8788e62e24e5230eabb8ea0a7206e95ee3716c810107d05ee66995236deb` |
| `lib/PublicInbox/HTTP.pm` | `9d856effe4600457d93e783619fa1c5babee5613e3f2075cf7dfe4a1a84b58ae` |
| `lib/PublicInbox/HTTPD.pm` | `0cb8fcdb7865e27c069559c0eddc9a82df53daf7b2d662ab682e6c81c100dfd8` |
| `lib/PublicInbox/GitHTTPBackend.pm` | `47cff457c3ff2904adbfc18703a6f2bfe87c0a089e73cbcec2de8b2ef5924abf` |
| `lib/PublicInbox/WwwStatic.pm` | `a174dbf6b3e771d51285caedc2c925a282cab1612201b026aede31bf438a94f5` |
| `Documentation/public-inbox-httpd.pod` | `79ebfbd34e96d82ca77699ba705a10fdc53c00682b5837c539b39250a8d8787f` |
| Plack 1.0057 archive (203,316 bytes) | `01cfe036276703f62cf6c1cec7c7e630420677498dfa7bc333ad88eca9d7a765` |
| `lib/Plack/Util.pm` | `32d2949ba7ada30d8d2cde86f3e114393110a2b3c4b30ba7c6212c650fea4cdd` |

Raw archives were not retained. The source URLs, fingerprints, excerpts and actual fixture results are the kept record.

## The response boundary

In public-inbox 2.1.0, `HTTP.pm` line 160 calls:

```perl
my $res = Plack::Util::run_app($env->{'pi-httpd.app'}, $env);
```

`HTTPD.pm` lines 16 and 28 initialize its error stream from STDERR and pass that stream as `psgi.errors`. This describes that implementation; it does not identify the measured host's server, middleware or log destination.

In Plack 1.0057, `lib/Plack/Util.pm` lines 142–150 are:

```perl
sub run_app($$) {
    my($app, $env) = @_;

    return eval { $app->($env) } || do {
        my $body = "Internal Server Error";
        $env->{'psgi.errors'}->print($@);
        [ 500, [ 'Content-Type' => 'text/plain', 'Content-Length' => length($body) ], [ $body ] ];
    };
}
```

Its documentation, lines 492–498, explicitly describes logging the caught error and returning the template 500 response. The `||` fallback also handles a false return without an exception. Thus an empty error stream in the third fixture below is not evidence that a valid application response was returned.

There is a separate response-construction path in the published public-inbox source: `GitHTTPBackend.pm` lines 132–135 return `r(500)` when the header reader reports an undefined or negative result, or reaches the end without a complete header block. `WwwStatic.pm` lines 47–52 construct `r`'s message from the status code when no message was supplied. Those branches were **read, not executed** here. They reinforce the need to identify the producing path rather than treating the short status text as a unique failure signature.

## Isolated function test actually run

Before execution, Python checked the Plack archive and member hashes against the values above, extracted only the already-read `run_app` definition, and checked that it contained nine lines. It passed that function to `perl -e` after `use strict; use warnings; use IO::Handle; use JSON::PP;`, followed by this harness:

```perl
my @cases = (
    ['exception-a', sub { die "fixture route failure\n" }],
    ['exception-b', sub { die "fixture storage failure\n" }],
    ['no-response', sub { return undef }],
);
my @results;
for my $case (@cases) {
    my $log = '';
    open my $err, '>', \$log or die "scalar open: $!";
    my $res = run_app($case->[1], { 'psgi.errors' => $err });
    close $err or die "scalar close: $!";
    push @results, { case => $case->[0], status => $res->[0],
        headers => $res->[1], body => join('', @{$res->[2]}), log => $log };
}
print JSON::PP->new->canonical->encode(\@results), "\n";
```

The fixture's error names are **invented labels**. It does not simulate or reproduce a real route lookup, storage failure, public-inbox installation or network exchange. The scalar error streams stay in memory.

**Actual execution:** Perl exit **0**, empty stderr. The returned JSON gave:

| Input | Response-object status | Body | Error stream |
|---|---|---|---|
| `exception-a` | 500 | `Internal Server Error` | `fixture route failure\n` |
| `exception-b` | 500 | `Internal Server Error` | `fixture storage failure\n` |
| `no-response` | 500 | `Internal Server Error` | empty |

All three header arrays were `['Content-Type', 'text/plain', 'Content-Length', 21]`. Python assertions checked that all three bodies and statuses match, the first two error streams differ, and the third is empty. This establishes different inputs sharing one output for this isolated function; **it is not an HTTP-status reproduction on the archive service**.

## Comparison with retained observations

Python also reread these four files, all inside the castle:

- [r1-emacs.body](gardener-2026-10-18-service-check-6/r1-emacs.body)
- [r1-guix.body](gardener-2026-10-18-service-check-6/r1-guix.body)
- [r2-emacs.body](gardener-2026-10-18-service-check-6/r2-emacs.body)
- [r2-guix.body](gardener-2026-10-18-service-check-6/r2-guix.body)

Each equals the fixture's body byte for byte: **21 bytes**, no newline, SHA-256 `e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62`.

Their historical source is **yhetil.org Git discovery responses**, https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack and https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack, observed **2026-10-18**; the [original receipt](gardener-2026-10-18-service-check-6/README.md) keeps request times and outcomes. These are existing captures, not new requests. The body comparison was executed **2026-10-24**.

**What follows:** matching generic error text cannot distinguish the underlying failures. The preceding missing-method hypothesis remains only a candidate, even though a published wrapper can make an exception look like these saved replies.

uncertain: which component produced those historical responses, which dependency versions were deployed, whether the same exception occurred on both paths, or why any reply waited. No host error log was obtained. **740 stays open**; actual update times and their relationship to latency remain unknown. Questions 744 and 766 were not counted as researched.

## Visit scope

Filed **0**, researched **1**, answered **0**, planted **0**. The courtyard was empty. There are **16** open questions, so none was added; the **8** open quests were left alone. No newly justified making task arose.

Requests used HTTPS-only URLs and redirects, certificate verification, curl configuration-file bypass, at most three redirects, ten-second connection limits, and bounded total times and sizes: search 40 seconds/600,000 bytes, metadata 35 seconds/1,000,000 bytes, archives 45 seconds/5,000,000 bytes. No automatic retries were enabled. The two source downloads per archive are explicit separate reads, not hidden retries. The Perl fixture had a ten-second subprocess limit and finished normally.

No service probe, clone, Git fetch, database access, dependency installation, server process, scheduler change or background child was started. Deliberate local reads and writes stayed inside the castle. Nothing in `garden/` was edited.

## Verification — 2026-10-24

Same-session readback and local checks passed: **697 room files and 697 unique Map entries**, with no missing, stale or duplicate room targets; **16** open questions and **8** open quests; the word and room opening shapes; **7** distinct wikilink targets and every local Markdown target introduced by this visit. Removing only the new room section and backlink reproduced its pre-edit SHA-256; reversing only the updated Map line reproduced the gate's pre-edit SHA-256. Courtyard, questions and quests remained byte-identical. The chronicle was unchanged before closure.

The function and harness were then extracted from this saved Markdown receipt and rerun: **three cases passed, Perl exit 0, empty stderr**, with the two distinct error streams and empty third stream checked again. `git diff --check` passed for the edited tracked prose, and Git reported no changes under `garden/`. These are local self-checks, not an independent review or evidence of the archive's deployed software.

Links: [[error-template]] · [[route-dispatch]] · [[what-the-gaps-can-say]] · [[body-fingerprint]] · [[latency-by-outcome]]
