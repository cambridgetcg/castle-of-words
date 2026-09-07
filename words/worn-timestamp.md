# worn timestamp

*A time written in pencil is a wish; a time carved by the ledger's own hand is a fact.*

A worn timestamp is any time mark the data carries by declaration rather than by measurement. For a child: it is the difference between a photo of a cake with the date scribbled on the back afterward, and the oven's timer that dinged when the cake finished.

The world is full of worn timestamps, each wearing the mark of whoever wrote it. A digital photo's EXIF "DateTimeOriginal" field is written by the camera's own clock, but any editor can change it afterward — it is the camera's claim, not the world's proof. A Git commit carries two dates, `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`; both are claims the committer chooses, and Git's own documentation says it "does not enforce" them. An HTTP `Date` header is only "the best available approximation" the server chose to send; the RFC admits it can be set "at any time during message origination." Even Bitcoin's block timestamp confesses it is accurate only to within an hour or two.

None of these fix the originator's pen. The [[attacker-held-pen]] law says the one who benefits from the timestamp must never be the trusted source for it. The worn timestamp is the honest version of that: it is carried openly, but it is a claim to log, never a birth-certificate. Where a timestamp must be trusted, it must come from a clock no interested party holds — the watching clock of the feed itself, or a third-party ceiling like RFC 3161, and even then only as a ceiling, never a birth.

Links: [[attacker-held-pen]] (the originator's pen) · [[watching-clock]] (the clock built for seeing) · [[defaulted-time]] (the painted-on mark) · [[movement-identity]] (the hash must hash facts, not claims) · [the-coarse-clock](../rooms/the-coarse-clock.md)

## Sources

- Wikipedia, "Exchangeable image file format" (Exif), https://en.wikipedia.org/wiki/Exchangeable_image_file_format — read 2026-09-07: DateTimeOriginal is camera-clock metadata; no standard field existed for time zone until version 2.31 (2016), and the metadata is freely editable after capture.
- Git documentation, `git-commit` man page, https://git-scm.com/docs/git-commit — read 2026-09-07: `--date` overrides the author date; `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` are taken from the environment, and Git "does not enforce" them.
- RFC 9110 §6.6.1, "Date" header field, https://httpwg.org/specs/rfc9110.html#field.date — read 2026-09-07: "a sender can generate the date value at any time during message origination"; the field is the sender's "best available approximation."
- Bitcoin Wiki, "Block timestamp," https://en.bitcoin.it/wiki/Block_timestamp — read 2026-09-07: "block times are accurate only to within an hour or two."
