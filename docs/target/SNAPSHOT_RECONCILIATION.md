# Consolidated reference set — 53 owner snapshots

**Classification:** `TARGET_DESIGN` + `OBSERVED_SNAPSHOT` metadata. **Date:** 2026-11-09. **Owner:** C0 / kOA Digital Ecosystem.

This document integrates the additional SmartDump, the 53-repository audit matrix and the owner-branch kits into the **final-system reference architecture**. It is not a history of past errors, a source-code certification, an inferred GitHub HEAD, or permission to publish. The target architecture remains the primary explanation; this page records the evidence required to make it defensible.

## Confirmed by inventory

- **53 distinct owner repository identities** are listed in the supplied proposed register, and **53 matching nested code ZIPs** are present in `SmartDump_20261109_113255(2).zip`. Each nested ZIP matched its recorded SHA-256 at intake: **53/53**.
- The former C0 register covered 51 of these identities. **`Rejean-McCormick/Kolor` and `Rejean-McCormick/Karacter`** have now been included in [`repositories.json`](../inventory/repositories.json), based on their owner snapshots, without declaring qualified cross-owner integrations.
- Three previously source-absent roles can now be grounded locally: `HomePage-initkoa.org` (Next.js site manifest), `initkoa-docs` (MkDocs documentation portal), and `Koali-Scenario-Mosaic` (Astro bilingual scenario application). Owner role descriptions are recorded in [`portfolio.v1.json`](portfolio.v1.json) with SHA-256 of the exact cited file.
- The inventory now covers **53** identities; the earlier 24-folder neighboring survey has **22 remaining** non-admitted project folders. **This is a scope-accounting correction**, not evidence that the remaining folders are irrelevant.
- [`code-snapshots-53.v1.json`](../inventory/code-snapshots-53.v1.json) records snapshot member path, SHA-256, declared source root and structural file counts for each of the 53 owners. **All 53 have `doc_code_conformity=NOT_EVALUATED`, `tests_executed=NOT_RUN`, and `git_revision=null` in this evidence ledger.** C0's own local tests are separately reported below and never promoted to 53-owner test claims.

## Current final-system responsibilities clarified by source inspection

| Owner | Target responsibility represented in C0 | Precise offline evidence / qualification limitation |
|---|---|---|
| **Kolor** | Bilingual character-sheet, role and palette preparation with reviewed image and manifest export | `Kolor_Code_snapshot.zip::README.md`; `kolor_studio_core.py` and CLI files are present. No live inter-product contract or operating environment has been qualified. |
| **Karacter** | Local-first fictional-character creative design, author-controlled narrative events, simulation and export | `Karacter_Code_snapshot.zip::README.md`; its creative "canon" is **character/story canon**, not the canonical Kristal semantic identity registry. No Koali/Orgo integration should be inferred. |
| **HomePage-initkoa.org** | Public-site codebase and reading/initiative web application | `HomePage_Code_snapshot.zip::package.json` (`next` + build scripts). Build/deployment **not executed** in this consolidation. |
| **initkoa-docs** | Aggregation/navigation of the owner wiki material via MkDocs | `docs-initkoa-org_Code_snapshot.zip::docs/index.md`, `mkdocs.yml`; aggregated pages do not become the normative contract owner. |
| **Koali-Scenario-Mosaic** | Bilingual, static-first problem/scenario atlas | `Koali_Scenario_Mosaic_Code_snapshot.zip::README.md` and `package.json`; the current README describes 36 canonical scenarios, while older `docs/README.md` describes a 120-item corpus. The source snapshot also contains exactly 36 English and 36 French `src/content/scenarios/*/SCN-*.md` entries; the older corpus description is a separate documentation lane that warrants owner review. No build executed. |

The complete source container and hashes are in the ledger. Its file counts are **structural only**; inspecting the presence of files or tests is not a behavior or compliance audit. All source files remain in their owner snapshots and are **not re-packaged** by C0.

## Target boundaries unchanged until bilateral agreement

The [target boundary map](BOUNDARIES.md) still contains **26 proposed typed edges**. Adding two products does not authorize inventing a Kolor → Kontexte API, a Karacter → Koali runtime integration, or another cross-repository contract. Proposed edges require owner acceptance, pinned revisions and producer+consumer evidence.

The existing C0 graph remains a **selective 14-system architecture illustration**, not a 53-node compatibility graph. Its reference count tracks the register, not a claim of exhaustive relationships.

## Critical owner gates to verify before claiming final-system operation

1. **Knowledge preparation and custody:** distinguish Skope/embedded EncyK source collection, Médiathèque source acceptance, DaaT mapping and the Framework/Authoring Kit's canonical semantic validation. Verify both endpoints of each adopted handoff, with exact schema and receipts. No assumption of v1/v2 handoff interchangeability.
2. **Kristal v11 coordination:** resolve the exact Framework, Kit, diK and Kristalizer draft pins. The documented diK draft.3 / Kristalizer-via-Kit draft.4 combination is not automatically compatible. The frozen v6 contract set remains untouched as a separate scoped reference.
3. **Civic execution:** Konnaxion decisions → explicit Interaction Kernel contract → Orgo governed tasks → scoped accountability effects. A local qualified path does not prove general production availability.
4. **Read and publication:** build, independent qualification, admission, immutable publication, read-projection synchronization and runtime activation are distinct decisions. EncyKlopedia, `kristal-public`, UCKK and public sites must not implicitly receive authoring or publication authority.
5. **Creative/educational assets:** identify export schemas from Kolor and local import behavior in Kontexte/Ekole before describing an integration as implemented. Keep Karacter's fictional narrative authority separate from global system governance.

## Two independent evidence axes

For every owner claim, capture both **source provenance** (`OBSERVED_SNAPSHOT`, `DOCUMENTED`, `USER_DECIDED`, `PROPOSED`, `BLOCKED`, `UNKNOWN`) and **doc-code verdict** (`CONFIRMEE_SOURCE`, `PARTIELLE`, `CONTREDITE`, `OBSOLETE`, `DOCUMENTEE_SEULEMENT`, `NON_VERIFIABLE`). Neither axis by itself indicates runtime maturity. Evidence of a test passing must include the actual command, environment, input revision and output. The audit matrix's source-file, workflow and test counts are not PASS results.

The 53 owner kits are **work instructions**. The supplied `BRANCH_REPORT_TEMPLATE_*.json` files have `branch_state=NON_COMMENCE` and empty `claims`/`validations`; they are **not 53 completed audits**. Do not present the audit's documentation-delta counts as current functional defects. Its comparisons to the earlier publication can be used for targeted review, but are not a core organizing principle of the final system.

## Coordination workflow and acceptance

- Treat the **owner code snapshot** as available evidence of implementation structure, not of deployment or current remote HEAD; establish remote revision and run independent tests before claiming qualified behavior.
- For each repository, produce a branch report matching `SCHEMA_BRANCHE_53.json` from the supplied owner-kit ZIP, recording exact source and owner, claims, verified symbols, test commands, changed files and cross-owner requests.
- Apply cross-owner changes only within their respective owners, with acceptance tests and explicit authority review. C0 may maintain architecture, catalogues, contracts-at-boundaries and evidence status, but never take over product code.
- Keep reader-first target documentation primary; use the evidence ledger and audit matrices for traceability rather than importing 53 verbose per-branch reports into the main navigation.

**C0 verification after this change:** see the local test output accompanying this consolidation. No complete 53-repository code audit or production qualification has been performed. No remote push or deployment was attempted.
