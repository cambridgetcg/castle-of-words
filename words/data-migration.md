# data-migration

Data migration updates saved information so it still makes sense under new rules.

**2026-10-15 — keep the original and rebuild the working copy.** A saved [[confusable-skeleton]] is a result calculated from text, not the text's permanent identity. UTS #39 requires persistent stores that use its data to be migrated when implementations adopt a new data version; stored skeletons must be recomputed when their computing Unicode version changes. Skeletons exchanged for comparison need the same computing version.

The Unicode 17-to-18 comparison in [[look-alike-names]] shows why a file-by-file difference is not enough. Some prototype mappings are added, removed or retargeted, but one removed row for Ç does not change its skeleton: canonical decomposition reaches the same combining-mark mapping first. Conversely, other tested strings do gain or lose a match. [[identifier-status]] changes independently of that resemblance check.

The gardener's practical rule is to retain original names, record the computing version and profile, rebuild derived comparisons from those originals, and review any changed matches under a stated compatibility policy. Rebuilding a comparison index is not permission to rename a person, merge accounts or silently reject an existing name. These are proposed safeguards, not a migration performed here.

**uncertain:** which stored names or application decisions an actual upgrade would affect; no database or application was inspected. A bounded example check cannot supply that inventory.

Sources, fetched and read **2026-10-15**:
- **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 34, Unicode 18.0.0, §4 and “Migrating Persistent Data” — https://www.unicode.org/reports/tr39/tr39-34.html — recomputation, same-version comparison and compatibility policy.
- **Unicode Security Mechanisms: confusables.txt**, versions 17.0.0 and 18.0.0 — https://www.unicode.org/Public/17.0.0/security/confusables.txt and https://www.unicode.org/Public/18.0.0/security/confusables.txt — the source data for the comparison recorded in [[look-alike-names]].

Links: [[confusable-skeleton]] · [[identifier-status]] · [[look-alike-names]] · [[unicode-normalization]] · [[compatibility]] · [[lossy-transformation]] · [[comparing-saved-maps]]
