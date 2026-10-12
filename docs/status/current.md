# kOA ecosystem maturity map

**Purpose:** current cross-system engineering view backed by owner evidence. This page does not replace owner status/release documents.

## Reading the map

```text
specified / architected
    ≠ implemented
    ≠ tested / qualified
    ≠ integrated with another owner
    ≠ production-proven
```

## Current maturity map

| System / boundary | Architecture / contracts | Implementation / qualification | Ecosystem integration | Production / operational caution |
|---|---|---|---|---|
| **Konnaxion** | Established owner model and product contracts | Implemented; qualification ledger still contains remediation items | Konnaxion↔Orgo IK boundary qualified for `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0` | Do not equate integrated qualification with complete production closure |
| **Orgo** | Established modular owner model and integration boundaries | Current owner evidence includes full local acceptance across database/deep/browser/acceptance campaigns | Konnaxion↔Orgo IK boundary qualified for decision execution + impact publication | Production-like acceptance is not a claim of real production deployment |
| **EncyKlopedia** | `encyklopedia.corpus-harvest-handoff/1.0.0` frozen; acquisition/provenance boundary explicit | Acquisition pipeline and handoff contracts are present in owner bundle | Feeds Da’at/Kristal through immutable evidence + referent candidates | Acquisition evidence is not epistemic validation |
| **Kristal v6** | Standard `6.0.0` + Referent Registry `1.0.0`; manifest and core-schema digests pinned | v6 state/reader contracts and migrated domain packages are available | EncyKlopedia→Da’at→Kristal→UCKK boundary aligned to IK v2 Kristal profiles | Actionability does not transfer execution authority; projections remain derived |
| **Da’at → Kristal** | Mapping/ACL role explicit | Mapping boundary defined; qualification remains integration-specific | Consumes EncyKlopedia/operational exports and maps to Kristal-native contracts | Da’at does not acquire source or Kristal authority |
| **UCKK / Univers-Cité** | `uckk.univers-cite-projection/1.0.0` frozen; Moodle/campus authority remains local | Projection contract and Moodle/campus documentation supplied | Consumes pinned Kristal artifacts; kOA-Linux also has separate governed UCKK import/publication boundaries | Projection/materialization does not become Kristal canon; external readings do not replace Assembly authority |
| **kOA-Linux / Koali platform** | Extensive platform contracts, profiles, admission/release and lifecycle governance | Advanced-beta/system-closure work with selected subsystem integration evidence | Operational composition root for profile-selected systems | System-release closure still depends on profile-specific build/qualification evidence |
| **Koali Spaces** | Generic Surface Layer contracts and authority boundaries established | Generic host core implemented/build-smoked in owner evidence | Real pilot evidence exists; each application still requires explicit admission/onboarding | No blanket production-hosting claim |
| **Interaction Kernel** | Normative protocol/Profile documentation exists; state remains participant-owned | Selectively adopted | Konnaxion↔Orgo qualified; knowledge boundary uses explicit `2.0.0` build/artifact profiles | IK is not a central service or universal replacement for platform contracts |
| **SemantiK Architect** | Planner-centered communication contracts + SA↔GF boundary | Owner status states canonical v1 core implemented | kOA-Linux admission is profile-specific | Production render requires admitted real RuntimeSet artifacts |
| **SemantiK Runtime Orchestrator** | Owner-preserving release-control boundary | Coordinates release/gates/promotion/rollback/activation | Integrates independent GF/SA/diagnostic authorities through external contracts | Sequencing is not grammar/semantic/diagnostic authority |

## Qualified Konnaxion ↔ Orgo boundary

| Boundary | Version | State |
|---|---|---|
| decision execution | `governance.decision.execute/1.0.0` | **QUALIFIED** integrated local runtime |
| durable impact publication | `accountability.impact.publish/1.0.0` | **QUALIFIED** with replay protections |

See [`../2-Technical-Reference/40-integration/orgo-konnaxion/index.md`](../2-Technical-Reference/40-integration/orgo-konnaxion/index.md).

## Frozen knowledge boundary

```text
EncyKlopedia
  encyklopedia.corpus-harvest-handoff/1.0.0
        ↓
Interaction Kernel
  kristal.build.request/2.0.0
        ↓
Da’at → Kristal Standard 6.0.0 / Referent Registry 1.0.0
        ↓
Interaction Kernel
  kristal.artifact.ready/2.0.0
        ↓
UCKK
  uckk.univers-cite-projection/1.0.0
```

See [`../2-Technical-Reference/40-integration/knowledge-projection.md`](../2-Technical-Reference/40-integration/knowledge-projection.md).

## Update rule

Advance a claim only with owner evidence appropriate to that scope. Do not infer production readiness from documentation completeness, repository presence, a release-candidate label or a successful local integration test.

## C0 parallel integration status (2026-10-08 snapshot evidence)

The qualified Konnaxion↔Orgo claims above remain in their existing scope. **The following are not new production claims**; they identify gaps between the frozen historical knowledge lane and the newer owner snapshots.

| Workstream | Observed here | NOT yet established |
|---|---|---|
| C0 integration reference | C0 registry/versions and ownership gates introduced | Current exact GitHub commit pins for all owners; all E2E proofs |
| C1 Zoology / Framework / Diag | v6 payload and v9 state available; local validation and build reproducible | Independent v10 qualified read surface with exact proof |
| C2 Manager / Bootstrap | Github sync/publish contract families exist | Per-Kristal authorization-gated publishing end-to-end |
| C3 `kristal-public` | Zoology v9 state present; root genesis state distinct | Valid v10 collection index and scoped qualified immutable Zoology publication |
| C4 Konstellation Light | Demo catalog exists (`demo-v9-small`); manual GitHub Pages workflow | Verified published Zoology import and automatic post-release rebuild |
| C5 Kompiler/Integration Pack | Reader and historical bridge tests available | Exact current Kompiler 0.8 bridge compatibility and Zoology Context Pack |
| C6 EncyK→Médiathèque | EncyK handoff v2 defined; Médiathèque Source/Snapshot/Representation model | Consumer handoff v2 receipt, idempotent replay/rejection and old v1 mapping |

**Global publication policy adopted:** first per-Kristal authorization, then optional automatic future qualified revisions *within unchanged scope*. Specific authorization for publishing Zoology content is still open. See [C0 register](../2-Technical-Reference/40-integration/orchestration-c0/README.md).

## Skope and Ékole (snapshot reconciliation, 2026-10-10)

| System | Documented implementation | Qualification / boundary | Local surface |
| --- | --- | --- | --- |
| Skope | Python/SQLite offline working-scope explorer, synthetic-demo-tested; export/branch/convergence preview | No real D: clone conformance established; no Framework-v5 normative subset-recipe identity; no v9/v10 canonical promotion or kOA handoff | `127.0.0.1:8767` in updated repo |
| Ékole | Core/Élève/Enseignant views, 202 authoring stubs, derived pedagogical graph, local OpsConsole, candidate Moodle-plan | No qualified 202 v9 states, no published v10 releases or confirmed Moodle write; no integrated Skope consumer | Core/Élève `8765`; Enseignant **or** OpsConsole `8766` by default |

The owner snapshots establish application features, not a qualified cross-product production deployment. [Evidence & contracts](../2-Technical-Reference/40-integration/skope-ekole/index.md).

## Kristal hosted v10 harmonization — evidence review (2026-10-12)

The earlier v6 table is a **frozen historical knowledge projection**, not a claim that Framework v6 is the latest release. Source snapshots identify Framework `10.0.0-draft.3.1` and Authoring Kit 3.2.4. They **do not establish end-to-end GitHub qualification**.

| Workstream | Verified snapshot fact | Open gate / status |
|---|---|---|
| Framework / Kit | v10 draft.3.1 and Kit 3.2.4 described; tools validated locally in prior audit | Exact approved remote pins unresolved |
| Manager / C2 | Manager files document sync/gating; snapshot lacks `kristal_manager` runtime | **BLOCKED** on complete checkout + authorized public gate |
| GitHub collection / C3 | `kristal-public` has Zoology state but no collection index and required manifest/read surface | **BLOCKED**, staging E2E only |
| Local workspaces | 126 distinct `state_ref` and 212 registered artifacts in snapshot | Per-workspace Kit/readiness review required |
| Global navigator | Konstellation v10 host adapter and Kristal selector exist; seven isolated adapter tests passed | **PROPOSED** My Kristals fleet integration |
| Templates | Arketype holds noncanonical structural types and neutral templates | Standalone software integration only; no publication authority |
| Historical register | Kollection has legacy registry and UCKK stubs | Crosswalk before deprecation, no data deletion |

Track the source facts and required receipts under the [C0 v10 readiness ledger](../2-Technical-Reference/40-integration/kristal-v10-alignment/readiness.md).
