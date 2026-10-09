# Reconciliation findings (October 9, 2026)

Sources: supplied `mycode_arborescence_git.txt`, previous `KOA_repo_locations_20261009_1151.csv`, and the `kOA_Digital_Ecosystem(2).zip` inventory. This report does not claim a live Windows or GitHub integrity test.

## Summary

- Lines in tree: **5197**; `.git` markers: **100** unique local paths.
- Previous GUI inventory: **66 public** and **49 local/other** entries, with 107 reported marker-positive rows (one duplicate path and six nested wiki paths account for the difference from 100 in the new tree).
- Draft inventory: **115** records (100 marker-observed, 6 previously observed nested, 3 legacy missing paths, 3 unknown paths, 2 excluded, 1 ambiguous mapping).

## Important corrections

- `kOA-Digital-Ecosystem`: `C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem`, not `C:\mycode\kOA\kOA_Digital_Ecosystem`.
- `Interaction-Kernel`: `C:\mycode\Interaction-Kernel\interaction_kernel` (the parent folder alone is not the Git root).
- `Konstellation`: Git identity `Rejean-McCormick/Konstellation`, **not** `knstl/konstellation`.
- `Kristal-Framework`: `C:\mycode\Kristal\Kristal-Framework`, not the old lowercase path.
- `MediKristal` and `MediKristal-LevelUpDiag-`: underneath `C:\mycode\Kristal\MediKristal\`, **not** under `Kristal-Kollection`.
- `VotingMachine`: `C:\mycode\02-Experimental\VotingMachine\VotingMachine`.
- `KeyFlow`: `C:\mycode\UCKK\KeyFlow(formulaires)`.
- `Rejean-McCormick/UCKK` cannot be mapped to `C:\mycode\UCKK\uckk-moodle`, because previous GitSink origin points that checkout to `Rejean-McCormick/UCKK-Moodle`.

## Six unresolved repos, excluding the two user-ignored repos

- `Rejean-McCormick/Grammatical-Framework-audit` — `local_root_unknown`; candidate: `C:\mycode\Grammatical_Framework\gf-audit`
- `Rejean-McCormick/Konnaxion-LevelUpDiag` — `local_root_unknown`; no candidate
- `Rejean-McCormick/Konnaxion-SecurityDiag` — `local_root_unknown`; no candidate
- `Rejean-McCormick/Kristal-Reference` — `legacy_path_not_found`; old path: `C:\mycode\Kristal\kristal-reference`
- `Rejean-McCormick/KristalV10` — `legacy_path_not_found`; old path: `C:\mycode\Kristal\KristalV10`
- `Rejean-McCormick/LevelUpDiag-Kristal` — `legacy_path_not_found`; old path: `C:\mycode\Kristal\levelupdiag_kristal`

## Prior mappings not carried forward as current repo ownership

- `knstl/konstellation` — legacy `C:\mycode\Konstellation\Konstellation`; not confirmed as current identity in the new inventory.
- `opentapioca/opentapioca` — legacy `C:\mycode\SenTient\SenTient\opentapioca`; not confirmed as current identity in the new inventory.
- `senigami/audiobook-studio` — legacy `C:\mycode\Voxtral_Audiobook_Studio\Voxtral_Audiobook_Studio`; not confirmed as current identity in the new inventory.

## Notes

- `Grammatical_Framework\gf-audit` exists as a **directory without a `[GIT]` marker**; it is not equated to the `Grammatical-Framework-audit` clone.
- The submitted tree intentionally stops at each Git root, so nested `.wiki-cache` Git checkouts are not rediscovered. Their earlier log evidence is preserved separately.
- `Kristal-Kollection` has a local `.git` marker even though the GitHub repo was empty at the earlier remote check; these are compatible facts.
- No file writes to a Windows checkout or GitHub were performed. The replacement files are **proposals**, not automatically applied changes.
