# Documentation/code alignment — C0 coordination (2026-11-23)

> **Historical baseline:** this document records the original audit. For post-installation SHA-256 verification from the 14:48 SmartDump, see [post-overlay validation](2026-11-23-post-overlay-validation.md). The original 17 findings and statuses remain unchanged for traceability.

> **Classification:** `OBSERVED_SNAPSHOT`, not an owner release, integration qualification, deployment status, or GitHub HEAD verification. This dated C0 coordination record does not supersede any owner contract.

## Evidence and scope

- **55** offline application snapshots with individual source indexes in `SmartDump_20261123_101022.zip`; see [the 23 November 55-repository digest ledger](../inventory/code-snapshots-55-2026-11-23.v1.json).
- C0 [canonical registry](../inventory/repositories.json) still contains **55** declared repository identities and Windows local roots. The [53-snapshot ledger](../inventory/code-snapshots-53.v1.json) is retained untouched as a **9 November historical baseline**; it is not mislabeled as current code.
- `kOA_contexte_20261123_145808_bf276628.zip` contains 57 documentary repository directories; its overlap with the code capture is not a proof of owner checkout identity. Findings below are scoped to the directly compared material.
- The two supplied C0 offline snapshots do **not** include `docs/target/`. However, **GitHub `main` was separately observed to contain `docs/target/`, `portfolio.v1.json` and all 24 named FC chain files**. Treat the ZIP omission as a packaging/source coverage gap, **not** a finding that the current C0 repository lacks its final-system corpus. Do not rebuild or overwrite that corpus from an incomplete ZIP.
- Archive contents and local source indexes do not attest Git revision, remote `origin`, executable behavior, integration tests, product release or production state.

## Owner coordination policy

1. **No owner-repository modification is authorized by this C0 report.** Owner code, documentation, pins and releases require owner review.
2. **diK is actively being updated by its owner; all diK findings are deferred.** Do not alter diK or silently advance any Framework compatibility pin.
3. Preserve distinct authority for civic decisions, operational tasks, knowledge validation, acquisition, source custody, release, publication, and runtime activation.
4. A link absent from a supplied archive is only a snapshot observation until the owning Git tree has been checked. Similarly, newer version numbers are not proof of cross-app compatibility.
5. Track the owner's exact commit and acceptance evidence before closing a finding. Avoid a global qualification claim based solely on documentation changes.

## Findings

The machine-readable [issue register](2026-11-23-documentation-drift.v1.json) contains the full source-file evidence, warnings, proposed owner actions, and coordination statuses. The table is a navigation summary, not independent proof.

| ID | Owner/repository | Priority | Observed issue | C0 status |
|---|---|---|---|---|
| `DOC-001` | `kOA_Digital_Ecosystem` | `P1` | Corpus docs/target absent dans les snapshots | `snapshot_gap_remote_tree_present` |
| `DOC-002` | `diK` | `P1` | Statut courant alpha.8 alors que le code est alpha.10 | `deferred_owner_updating` |
| `DOC-003` | `Daat` | `P1` | README et index technique figés sur 0.4.2 et 0.3.0 | `open_owner_documentation` |
| `DOC-004` | `Karacter` | `P1` | Index « Latest 7.0 » après livraison 7.4 | `open_owner_documentation` |
| `DOC-005` | `Koali_Scenario_Mosaic` | `P1` | Index documentaire 120 scénarios après bascule V2 vers 36 | `open_owner_documentation` |
| `DOC-006` | `Koali-Control-Panel` | `P2` | Index technique marqué 4.0.0 malgré code 4.1.1 | `open_owner_documentation` |
| `DOC-007` | `Kristal-Authoring-Kit` | `P2` | Version draft.4, changelog arrêté à draft.3 | `open_owner_documentation` |
| `DOC-008` | `SemantiK_Runtime_Orchestrator` | `P3` | Résumé README v1.2.0 et changelog 1.2.1 en fin | `open_owner_documentation` |
| `DOC-009` | `diK` | `P2` | Copie de l’inventaire C0 toujours à 49 dépôts | `deferred_owner_updating` |
| `DOC-010` | `Konstellation-Publisher` | `P2` | Copie de l’inventaire C0 toujours à 49 dépôts | `open_owner_documentation` |
| `DOC-011` | `LevelUpDiag-Orgo` | `P2` | Deux guides de validation annoncés manquent | `open_owner_documentation` |
| `DOC-012` | `Kristal-Manager` | `P2` | Plusieurs aides d’opérations du README manquent | `open_owner_documentation` |
| `DOC-013` | `SenTient` | `P3` | Docs/ai au lieu de docs/ai dans les liens | `open_owner_documentation` |
| `DOC-014` | `ecole-pastorale` | `P2` | 11 liens de README vers wiki/ sans fichiers correspondants | `open_owner_documentation` |
| `REL-001` | `Konstellation` | `P1` | Absence de package-lock.json — npm ci non reproductible depuis le snapshot | `owner_release_blocker_documented` |
| `VER-001` | `Koali-Control-Panel` | `P2` | Recommandation LevelUpDiag-Koali 2.2.0 vs code 3.0.0 | `compatibility_qualification_required` |
| `VER-002` | `diK` | `P2` | Pin Framework draft.3 vs écosystème Framework draft.4 | `deferred_owner_updating` |

## C0-specific decisions

- **C0-target ZIP coverage:** `DOC-001` is now classified `snapshot_gap_remote_tree_present`, not an active GitHub missing-corpus incident. Preserve the remote source; separately investigate snapshot include/exclude rules and whether a reproducible export contains all canonical target documents.
- **New structural baseline:** retain 9 November (53) and 23 November (55) ledgers side by side; do not rewrite the historical references inside the target portfolio without owner-source verification.
- **Inventory copies:** the 49-entry inventories observed in diK and Konstellation Publisher are separate owner-documentation copies. C0's canonical declared scope is 55; no C0-driven copying or mutation of those owner trees occurs here.
- **diK freeze:** `DOC-002`, `DOC-009`, and `VER-002` are `deferred_owner_updating`. No upgrade recommendation is issued for them while owner work is in progress.
- **Release and compatibility:** `REL-001` is a release reproducibility problem correctly disclosed by Konstellation, not a stale documentation claim. `VER-001` requires owner-level compatibility testing before changing a version recommendation.

## Suggested acceptance evidence per owner finding

- **Version/docs drift:** owner-reviewed documentation referencing exact version, build manifest and changelog; historic versions explicitly labeled.
- **Links and navigation:** resolved local Markdown links against an actual complete Git tree (including case-sensitive paths where relevant), with generated and external wiki surfaces marked separately.
- **Contract or release compatibility:** exact producer/consumer versions, real acceptance fixtures, repeatable build/test records, and owner approval before promotion.
- **Closure:** record owner commit/ref, files changed and verification report; C0 reclassifies only after this evidence, not from the present ZIP.

## Verification limitations

This record compiles static inspection and SHA-256 archive evidence. No production, compatibility or cross-system tests were run by the audit. C0 was not pushed or released by creating this report. The 24-chain target corpus exists on GitHub main but was omitted from the supplied archive; consequently a full snapshot-only C0 test suite cannot be certified against that incomplete export.
