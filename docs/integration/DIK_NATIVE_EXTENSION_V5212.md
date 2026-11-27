# V5.21.2 one-shot private workflow

Run the overlay installer with PowerShell 7. It checks the V5.21.1 baseline, pins previous components, installs additive files, records an overlay receipt, runs the regression suite, then generates a private `SEMANTIC_V5212_*` directory. Return the PowerShell log, `report.json` and `active.sqlite`. The expected status is `EXTENSION_AND_REGISTRATION_REHEARSAL_COMPLETE_EDITORIAL_PENDING`. No canon, public repository or network changes. Keep previous private generations and their candidate and editorial files intact; do not place approval edits inside an immutable generation.

The new generation holds `candidates/`, `editorial/`, `registration-plans/`, `approval-templates/`, `predicate-review/`, and `manifest.sha256.json`. The older candidate documents remain in their original generations; the new review packets/plans refer to their exact inventory. Approval checking is a declaration check only; production activation is not implemented.
