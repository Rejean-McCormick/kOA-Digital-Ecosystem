# Semantic-stack local checkout roots (24 November 2026)

> **Generated file:** edit `semantic-stack-local-roots.v1.json` and run `python scripts/render_semantic_stack_local_roots.py`.
> Reported Windows paths are offline coordination evidence, not live Git, HEAD, origin, qualification, or publication authorization.

This operational list identifies the 14 repositories or local worktrees selected for the diK/EncyK/Kristal semantic-alignment overlay. Thirteen entries mirror [the existing 55-repository C0 identity inventory](repositories.md); `GF_Wordbench` is tracked **only in this workstream list**, without an unverified GitHub identity or a change in the C0 perimeter.

| Component | Reported Windows checkout root | Evidence |
|---|---|---|
| `Kristal-Framework` | `C:\mycode\Kristal\Kristal-Framework` | User-provided directory scan |
| `Kristal-Authoring-Kit` | `C:\mycode\Kristal\Kristal-Authoring-Kit` | User-provided directory scan |
| `Kristal-Manager` | `C:\mycode\Kristal\Kristal-Manager` | User-provided directory scan |
| `KristalDiag` | `C:\mycode\Kristal\KristalDiag` | User-provided directory scan |
| `Kristal-Integration-Pack` | `C:\mycode\Kristal\Kristal-Integration-Pack` | User-provided directory scan |
| `kristal-public` | `C:\mycode\Kristal\kristal-public` | User-provided directory scan |
| `diK` | `C:\mycode\diK\diK` | Supplied code snapshot index (`source_root`) |
| `EncyKlopedia` | `C:\mycode\EncyKlopedia\EncyKlopedia` | User-provided directory scan |
| `SemantiK-Architect` | `C:\mycode\SemantiK_Architect\SemantiK_Architect` | Supplied code snapshot index (`source_root`) |
| `SemantiK_Runtime_Orchestrator` | `C:\mycode\SemantiK_Architect\SemantiK_Runtime_Orchestrator` | User-provided directory scan |
| `Spek` | `C:\mycode\Spek_Semantic-publishing\Spek` | User-provided directory scan |
| `Konstellation` | `C:\mycode\Konstellation\Konstellation` | User-provided directory scan |
| `Kristalizer` | `C:\mycode\Kristal\Kristalizer` | User-provided directory scan |
| `GF_Wordbench` | `C:\mycode\Grammatical-Framework\GF_Wordbench` | User-reported `.git` directory |

## Interpretation

- `diK` and `SemantiK-Architect` roots were confirmed in the supplied 24 November code snapshot indexes. The project name `SemantiK-Architect` uses a hyphen in the GitHub identity, while the local folder uses underscores.
- The operator reported moving `GF_Wordbench` up one directory: the Git metadata is now at `C:\mycode\Grammatical-Framework\GF_Wordbench\.git`. The checkout root excludes `.git`.
- The other roots were reported in the operator's recursive directory scan. Duplicate names inside `DocServer`, backups, vendor copies, `src/` and archives are **not** selected checkout roots.
- The historical snapshot indexes and prior audit records remain unchanged; moving a checkout does not retroactively change archival evidence.
- This list does not approve an overlay, canonical Kristal writes, Wikidata crosswalk promotion, GitSink enrollment, or public deployment.

## Read-only Windows verification

Run from the C0 checkout root:

```powershell
pwsh -NoProfile -File .\scripts\check_semantic_stack_local_roots.ps1 | Format-Table -AutoSize
```

Use `-RequireAll` to fail if any checkout is missing or the discovered Git root does not exactly match the reported path. This check never modifies repositories.
