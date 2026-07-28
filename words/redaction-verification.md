# redaction-verification

Redaction-verification is the act of checking that a record claiming to be redacted actually has its secrets removed — by running the exact redactor again and accepting only unchanged output.

If a validator cannot authenticate a redacted record, it must re-run the redactor and compare. Otherwise the validator may echo secrets while calling them redacted. The honest redaction pipeline is: redact, verify by re-redaction, then return. Never: trust the label "redacted" and pass it through.

Links: [[receipt]] [[digest]] [[fail-closed]] [[safety-boundaries]]
