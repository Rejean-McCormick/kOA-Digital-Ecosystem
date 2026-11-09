# kOA Digital Ecosystem — diK / Kristalizer C0 update (2026-11-06)

**Scope:** documentation, source-root repository inventory, C0 candidate handoff coordination and regression tests **only**. No canonical Kristal, dictionary, deployment, release, GitHub workflow or private Médiathèque data is modified.

## Apply the overlay to the local repository

Target repository root:

`C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem`

Unzip the supplied `OVERLAY_kOA_Digital_Ecosystem_diK_Kristalizer_20261106.zip` **into that directory**, preserving its relative paths and allowing replacement of the listed documentation and validator files. Do not extract into the parent `C:\mycode` directory. All files not listed in the overlay are untouched by the overlay.

To run a local confirmation from **PowerShell 7**:

```powershell
Set-Location 'C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem'
python scripts/validate_c0_coordination.py
python -m unittest discover -s tests -v
```

This update was constructed against `znapshot_kOA_Digital_Ecosystem_11061318.zip` and uses the source-root and version information in `SmartDump_20261106_131708.zip` (its nested diK/Kristalizer code snapshots). If your local checkout has diverged, **review the file diff before extraction** rather than overwriting newer changes.

## Confirmed additions

| Repository | Exact SmartDump source root | Version observed in the source snapshot |
| --- | --- | --- |
| `Rejean-McCormick/diK` | `C:\mycode\diK\diK` | `1.0.0-alpha.7` |
| `Rejean-McCormick/Kristalizer` | `C:\mycode\Kristal\Kristalizer` | `1.2.2` |

The canonical `docs/inventory/repositories.json` grows **49 → 51**; matching human inventory and graph indexes updated. New non-normative C0 documentation lives in `docs/2-Technical-Reference/40-integration/dik-kristalizer/`.

## Important unresolved gate

`diK 1.0.0-alpha.7` targets Framework `11.0.0-draft.3`; `Kristalizer 1.2.2` requires a separately installed Authoring Kit `4.0.0-draft.4` pinned to Framework `11.0.0-draft.4`. The versions were read from the uploaded sources; a real end-to-end interoperability test is **not done**. Both maintain the distinction between candidate lexical/identity observations and approved canonical KQ/KP/KA/KS.

The existing historical v6 knowledge contract is **unchanged**, and no user-supplied Wikimedia dump or SQLite index is published. No public GitHub push, PR, or release has been made by applying this local overlay.

## Validation evidence

- `python scripts/validate_c0_coordination.py` passes on the assembled snapshot.
- `python -m unittest discover -s tests -v` passes on the assembled snapshot.
- Updated C0 validation rejects false promotion of SmartDump paths to verified Git remotes, and rejects claims of public-release permission or certified interoperation.

## Next phase (separate repository corrections)

After the local registry update, review the other owner repositories one at a time. First resolve the draft.3/draft.4 compatibility, then qualify lexical candidate handoffs and the 41-concept UNESCO branch projection. Do not treat target 14 locales as 14 independently qualified SemantiK/GF runtime channels without a coverage/conformance report.
