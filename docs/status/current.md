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
| **Kristal v5** | Knowledge-contract baseline is `5.0.0-rc.3` + Referent Registry `1.0.0`; knowledge-model bundle digest frozen | rc.3 contract/release-candidate surfaces are present; supplied release metadata has unresolved commit | EncyKlopedia→Da’at→Kristal→UCKK knowledge boundary frozen at explicit contract versions | Do not call rc.3 a completed immutable release until tag→commit is resolved; unrelated older downstream locks remain scope-specific |
| **Da’at → Kristal** | Mapping/ACL role explicit | Mapping boundary defined; qualification remains integration-specific | Consumes EncyKlopedia/operational exports and maps to Kristal-native contracts | Da’at does not acquire source or Kristal authority |
| **UCKK / Univers-Cité** | `uckk.univers-cite-projection/1.0.0` frozen; Moodle/campus authority remains local | Projection contract and Moodle/campus documentation supplied | Consumes pinned Kristal artifacts; kOA-Linux also has separate governed UCKK import/publication boundaries | Projection/materialization does not become Kristal canon; external readings do not replace Assembly authority |
| **kOA-Linux / Koali platform** | Extensive platform contracts, profiles, admission/release and lifecycle governance | Advanced-beta/system-closure work with selected subsystem integration evidence | Operational composition root for profile-selected systems | System-release closure still depends on profile-specific build/qualification evidence |
| **Koali Spaces** | Generic Surface Layer contracts and authority boundaries established | Generic host core implemented/build-smoked in owner evidence | Real pilot evidence exists; each application still requires explicit admission/onboarding | No blanket production-hosting claim |
| **Interaction Kernel** | Normative protocol/Profile documentation exists; state remains participant-owned | Selectively adopted | Konnaxion↔Orgo qualified; knowledge boundary uses explicit `1.1.0` build/artifact profiles | IK is not a central service or universal replacement for platform contracts |
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
  kristal.build.request/1.1.0
        ↓
Da’at → Kristal 5.0.0-rc.3 / Referent Registry 1.0.0
        ↓
Interaction Kernel
  kristal.artifact.ready/1.1.0
        ↓
UCKK
  uckk.univers-cite-projection/1.0.0
```

See [`../2-Technical-Reference/40-integration/knowledge-projection.md`](../2-Technical-Reference/40-integration/knowledge-projection.md).

## Update rule

Advance a claim only with owner evidence appropriate to that scope. Do not infer production readiness from documentation completeness, repository presence, a release-candidate label or a successful local integration test.
