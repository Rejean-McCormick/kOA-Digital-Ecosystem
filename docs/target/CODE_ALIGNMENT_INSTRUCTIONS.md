# Implementation instructions for the final-system architecture

**Type:** engineering backlog / actionable alignment instructions. **Goal:** make the code and source contracts implement the [final-system architecture](architecture.md); not a retrospective list of mistakes. **Authority:** instructions for owner review, **not** permission to modify a remote repository, merge, publish, or deploy.

## How to execute

For each work item: inspect the **real full repository checkout at a pinned commit**; confirm the owner and schema; implement and test the smallest non-breaking change; produce signed/hashed receipts as required by that owner; update this C0 map only with real evidence. The supplied `repos(1).zip` is predominantly README/docs/wiki content, **not the complete implementation code**, so the instructions below are intentionally path-scoped to known documentation and named subsystems rather than pretending to provide untested source patches.

Statuses: `READY_C0` means central coordination changes can be made and validated within this repository; `OWNER_IMPLEMENTATION_REQUIRED` means full owner checkout and owner approval are required; `SPEC_DECISION_REQUIRED` means the interface/authority decision has not yet been bilaterally approved. Priorities emphasize final user-visible functionality.

## Workstream I — Final knowledge and source pipeline

### I01 · Skope / integrated EncyK to Médiathèque (P0; `OWNER_IMPLEMENTATION_REQUIRED`)

**Owner sources inspected:** `repos/Skope/README.md`, `repos/Skope/docs/UNIFIED_1_0_OPERATIONS.md`, `repos/mediatheque/README.md`, `repos/Mediatheque-blank/README.md` in `repos(1).zip`.

**Target code changes:** inspect the actual Skope `skope/` and integrated `encyk/` modules and Médiathèque engine/adapters in full checkouts. Define the source package and receiving contract with exact version, source/preservation IDs, digest, provider provenance and receipt. Ensure candidate QID inventories are never misrepresented as verified raw evidence. Implement persistent, idempotent acceptance plus divergent-replay rejection, malformed-package denial, safe reprocessing and an operator review pathway. No automatic Framework authority transfer.

**Acceptance:** a fixture source is accepted once, replay returns the same receipt, payload corruption is rejected, a conflicting replay is rejected, an absent or unapproved source cannot be promoted, and a separate receiver verifies the pinned producer package. Include real-data compatibility evaluation before broad use. **Do not** assume the historical `encyklopedia.corpus-harvest-handoff/1.0.0` is the current contract.

### I02 · Framework v11 / Kit v4 / Integration Pack version lock (P0; `SPEC_DECISION_REQUIRED`)

**Owner sources:** `repos/Kristal-Framework-c325f677/README.md`, `repos/Kristal-Authoring-Kit/README.md`, `repos/Kristal-Integration-Pack/README.md`.

**Target code changes:** pin the final approved Framework/KQ-KP-KA-KS profile, Kit-compatible graph/registry/dictionary schema and Integration Pack read-view API to exact immutable commits and checksums. Define compatibility failure response and explicit opt-in upgrade for old workspaces; reject silent namespace rewriting or a Wikidata Q/P substitution for KQ/KP. Keep semantic labels outside canonical identity. The observed candidate set is Framework `11.0.0-draft.4`, Kit `4.0.0-draft.4`, Integration Pack `0.3.0-alpha.1`; **do not relabel drafts as a final qualified release**.

**Acceptance:** producer/consumer fixture matrix of at least: known KQ/KP/KA/KS, locale direct/fallback/missing, crosswalk Q/P, invalid namespace, invalid lexical binding, old-profile opt-in denial, mismatched checksum. Validate both accepted and intentionally rejected versions.

### I03 · diK / Kristalizer into controlled Kit authoring (P0; `OWNER_IMPLEMENTATION_REQUIRED`)

**Owner sources:** `repos/diK/README.md`, `repos/Kristalizer/README.md`, `repos/Kristal-Integration-Pack/README.md`.

**Target code changes:** reconcile diK's described `11.0.0-draft.3` target with Framework/Pack `draft.4` by tested compatibility rather than string comparison. Add/read exact catalog import receipt, review identity, namespace and source hash; require explicit approval before the Kit modifies an author's workspace. Preserve separation between external Wikidata matching and canonical semantic identity; no implicit application to all Kristals.

**Acceptance:** both approved and rejected candidate crosswalks, missing locale, namesake collision, digest mismatch and non-approved catalog import are exercised on pinned test fixtures. Every approved write has an audit/rollback artifact.

### I04 · Published read surfaces to Konstellation, Kompiler and EncyKlopedia (P0; `SPEC_DECISION_REQUIRED`)

**Owner sources:** `repos/Kristal-Integration-Pack/README.md`, `repos/Kompiler/README.md`, `repos/Konstellation/README.md`, `repos/EncyKlopedia/README.md`, `repos/kristal-public/README.md`.

**Target code changes:** define a release-index/read-view contract with stable semantic identity, canonical revision and derived-view digest, language fallback flags, external crosswalk trace, authorization classification, source references and schema version. Consumers validate the pinned release and reject unapproved, stale or malformed views. EncyKlopedia remains a *read-only encyclopedia*; its public API must never trigger acquisition, authoring, or release approval.

**Acceptance:** independent import tests for the three consuming products; an approved synthetic release reads identically by semantics, a missing translation is visibly marked, and unapproved/private content cannot leak into public endpoints. A repository snapshot is not evidence of real public publication.

## Workstream II — Operational/educational/security boundaries

### II01 · Orgo as the sole authority for real educational work (P0; `OWNER_IMPLEMENTATION_REQUIRED`)

**Owner sources:** `repos/Orgo-a6379623/README.md`, `repos/Kontexte/README.md`, `repos/Kompose/README.md`, `repos/Akor/README.md`, `repos/Ekole/README.md`.

**Target code changes:** cross-check the real launch/operation paths for classroom capsules and missions. Kontexte/Kompose/Akor submit versioned, reviewable *intents or designs*; Orgo is the only owner of Cases/Tasks and durable transitions. Ensure tenant/teacher role enforcement, bounded practice/synthetic mode and retries. The educational apps must not write Orgo tables directly.

**Acceptance:** exact owner permission/denial tests, duplicate intent replay, teacher cancellation, partial-group participation, and Orgo terminal receipt reconciliation. An educational simulation must not create a real task unless explicitly authorized.

### II02 · UCKK / Ékole learning and Moodle projections (P1; `OWNER_IMPLEMENTATION_REQUIRED`)

**Owner sources:** `repos/Ekole/README.md`, `repos/Ekole-Pastorale/README.md`, `repos/UCKK-Assets/README.md`, `repos/UCKK-Ops-Console/README.md`, `repos/mediatheque/README.md`.

**Target code changes:** preserve neutral Ékole Core and independent content packs. Specify authorized UCKK import and Moodle acceptance receipts, resource/course mappings, rebuildability and supervised write approvals. Keep institution decisions, educational provenance and Moodle enrollment authority outside Framework; include durable media/version references from Médiathèque where necessary.

**Acceptance:** idempotent content-pack import, dry-run vs live-write enforcement, explicit teacher/institution authorization, locale fallback display, source traceability and rollback/rebuild of a projection without altering semantic canon.

### II03 · Security admission / actual enforcement (P0; `OWNER_IMPLEMENTATION_REQUIRED`)

**Owner sources:** `repos/Konfid/README.md`, `repos/Daat/README.md`, `repos/KonnaxionDiag/README.md`, `repos/Konnaxion-Capsule-Manager/README.md`.

**Target code changes:** establish signed/bound principal and resource identifiers, short-lived decisions, trusted Konfid policy transport and app-local authorization checks. Diagnostic or approval evidence must be checked at the actual enforcing PEP; no detector/service directly acquires unrestricted host credentials. Require denial for missing policy, stale digest and mismatched actor/tenant.

**Acceptance:** deny-by-default, expired approval, replay, mismatched tenant and conflicting delegation all fail closed; allowed operations produce owner and enforcement receipts without leaking secrets.

### II04 · Runtime / platform / presentation lifecycles (P1; `OWNER_IMPLEMENTATION_REQUIRED`)

**Owner sources:** `repos/kOA-Linux-Koali/README.md`, `repos/Koali-Control-Panel/README.md`, `repos/Koali-Spaces/README.md`, `repos/Konstellation-Publisher/README.md`.

**Target code changes:** validate release admission against exact artifact/version, manifest and execution privileges; make build, qualification, approved publication, runtime activation and Koali Space activation separately observable. Ensure an independently runnable product has no hard dependency on Koali Spaces; Control Panel orchestrates dev workflows without bypassing platform policy.

**Acceptance:** controlled rollback at each lifecycle, attempted activation before authorization is denied, no privately sourced bytes published, clean-build preflight fails on a dirty worktree, and loss of Koali shell does not corrupt application business state.

### II05 · Agentic and language products (P2; `OWNER_IMPLEMENTATION_REQUIRED`)

**Owner sources:** `repos/Konductor/README.md`, `repos/SemantiK-Architect-a60c12de/README.md`, `repos/SemantiK_Runtime_Orchestrator/README.md`, `repos/Spek/README.md`.

**Target code changes:** keep Konductor's agentic job state separate from Orgo Cases/Tasks. Require explicit brokered intents when an agent requests an owner action. In SemantiK, enforce exact lexical/runtime version compatibility and faithful meaning realization; the Runtime Orchestrator changes RuntimeSets, not semantic truth. Spek consumes reviewed short realizations without asserting conformance automatically.

**Acceptance:** blocked unsafe tool request, reproducible language fallback, immutable RuntimeSet promotion/rollback, documented mismatch failure, and an editorial publication that exposes its review state.

## Workstream III — Central repository code (this delivery)

### III01 · Machine-readable final portfolio and validator (P0; `READY_C0`)

**53-owner source reconciliation:** before modifying product implementations, use [`SNAPSHOT_RECONCILIATION.md`](SNAPSHOT_RECONCILIATION.md) and the [`code snapshot ledger`](../inventory/code-snapshots-53.v1.json) to pin an exact owner artifact and separate unverified source observations from executed tests. `Kolor` and `Karacter` are now in the primary portfolio; their cross-owner contracts remain to be qualified. The 53 supplied branch kits are instructions, not completed audits.

**Code implemented in the accompanying refactor:** `docs/target/portfolio.v1.json`, `docs/target/boundaries.v1.json`, `scripts/validate_target_architecture.py`, `scripts/render_target_portfolio.py`, `scripts/render_target_boundaries.py`, `tests/test_target_architecture.py`. Preserve all 53 canonical identities from `docs/inventory/repositories.json`, distinguish absent sources, require SHA-256 for archive-backed roles, and refuse contradictory authority assignments for core owner names.

**Acceptance:** `python scripts/validate_target_architecture.py`, `python scripts/render_target_portfolio.py --check`, `python scripts/render_target_boundaries.py --check`, `python -m unittest discover -s tests -v` all pass. Deliberately damaged role/source tests must fail.

### III02 · Make the final architecture the discovery entry point (P0; `READY_C0`)

**Files:** `README.md`, `docs/index.md`, `docs/inventory/README.md`, `docs/target/README.md`, `docs/target/architecture.md`, `docs/target/journeys.md`, `docs/target/PORTFOLIO.md`.

**Acceptance:** readers can move from the project README to final architecture, to a specific repository role, to code instructions in at most three clicks. Existing legacy links remain intact during this increment.

### III03 · Reconcile legacy graph and status/publication views (P1; `SPEC_DECISION_REQUIRED`)

**Files:** `docs/inventory/graph-registry.v1.json`, `docs/inventory/graph-focus.v1.json`, `docs/2-Technical-Reference/10-system/authority-map.md`, `docs/2-Technical-Reference/40-integration/contract-map.md`, `docs/status/current.md`, and the downstream `kOA-D-E-GitHub-Audit` dated renderer.

**Target code changes:** decide versioned migration from the old EncyKlopedia-as-acquirer graph to distinct Skope/EncyK, Médiathèque and EncyKlopedia read-only identities. Do **not** silently redirect an historical v6 contract ID or label an untested graph link as qualified. Re-run the downstream graph publisher's independent schema/route tests on a preview before promoting the new view.

**Acceptance:** graph metadata, owner roles and paths agree; no misleading source-acquisition edge ends at modern EncyKlopedia; previously published graph snapshots remain reproducible; wiki and audit navigation remain stable. This separate work item is deliberately **not auto-applied** to the consumed graph registry in the current increment.

### III04 · Audit reproducible target docs and CI (P0; `READY_C0`)

**Files:** `.github/workflows/c0-coordination.yml`, `AGENTS.md`, new target scripts and tests.

**Acceptance:** PRs touching the target pages/registry must trigger checks; invalid portfolio fields, missing inventory members, absent evidence hashes, unrendered Markdown or unauthorized status markers fail the build. No CI job performs Git push or product deployment.

### III05 · Classify relevant neighboring repositories (P1; `SPEC_DECISION_REQUIRED`)

**Files:** [24-project survey](adjacent-projects.md), `docs/inventory/repositories.json` (only after owner approval), any designated adjacent-source contract mapping.

**Target code changes:** examine which of GF Wordbench/Observatory, `uckk-moodle`, `kOA-D-E-GitHub-Audit`, Kolor, Karacter, Kin-City and other neighbors participate in the final system and which remain external. Model dependency/consumer edges explicitly without adding non-canonical projects as automatic peers. Preserve the distinction between real owner repositories, GitHub discovery, source snapshots and generated publication archives.

**Acceptance:** each candidate has a documented owner identity, explicit `core / dependency / external / research` placement, actual code/evidence source, adopted contract where applicable and a reasoned inclusion decision. No dependency edge inferred merely from a folder name.

## Decision gates before a multi-repository code migration

| Gate | Required result |
|---|---|
| G1 — Target owner agreement | Each producer/consumer accepts its own scope and explicitly says which contract/profile revision it adopts. |
| G2 — Exact compatibility | Immutable commits, dependency locks, schema fixtures and reproducible build/test commands. |
| G3 — Independent qualification | A separate consumer or diagnostic tool validates real producer output and failure cases. |
| G4 — Release safety | Human/owner-approved publication target, privacy review, denial path, receipts, reversible activation. |
| G5 — Navigation & content | C0's final architecture docs, canonical code and read consumers report consistent roles and versions. |

**Do not expand this backlog into an automatic cross-repository rewrite.** Changes to full owner code require the missing source tree, producer/consumer review and exact tests. The status ledger should report only completed gates, not intended ones.
