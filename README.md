# kOA Digital Ecosystem

> **Current coordination update (2026-10-12):** Kristal v10 hosting alignment is tracked separately from the **frozen historical v6 knowledge-projection contract set**. This repository coordinates contracts and ownership; it does not own semantic canon, publish Kristals, or activate runtimes. Start at [Kristal v10 alignment](docs/2-Technical-Reference/40-integration/kristal-v10-alignment/README.md) and the [2026-10-12 change report](docs/status/2026-10-12-kristal-v10-harmonization.md). The older "Current baselines" section below documents the previously pinned projection lane; it is **not** a statement that Kristal v6 is the newest Framework architecture.

> Canonical system-of-systems map for kOA. This repository describes cross-system ownership, explicit integration contracts, release/activation boundaries and current maturity evidence. Product and platform repositories remain authoritative for their internal state, implementation and product-owned contracts.

## Historical pinned knowledge-projection baseline (2026-10-01)

- **Historical projection alignment:** 2026-10-01 architecture; see the 2026-10-12 v10 coordination overlay.
- **Knowledge-contract baseline:** Kristal Standard `6.0.0`, Referent Registry `1.0.0`, EncyKlopedia handoff `encyklopedia.corpus-harvest-handoff/1.0.0`, IK profiles `kristal.build.request/2.0.0` + `kristal.artifact.ready/2.0.0`, UCKK projection `uckk.univers-cite-projection/1.0.0`.
- **Kristal standard identity:** v6 is pinned by its published standard-manifest SHA-256 and core contract digests; canonicalization is `kristal.v6:jcs-rfc8785`.
- **kOA-Linux:** platform composition authority for profiles, admission, release channels and lifecycle; independent subsystem implementations remain owner-controlled.

## Control views

Use these views together:

- **System map** — what exists and how the major systems relate: [`docs/1-Overview/index.md`](docs/1-Overview/index.md)
- **Authority map** — who owns each authoritative state or decision: [`docs/2-Technical-Reference/10-system/authority-map.md`](docs/2-Technical-Reference/10-system/authority-map.md)
- **Contract map** — which explicit boundaries connect owners: [`docs/2-Technical-Reference/40-integration/contract-map.md`](docs/2-Technical-Reference/40-integration/contract-map.md)
- **Maturity map** — specified vs implemented vs qualified vs integrated vs production-proven: [`docs/status/current.md`](docs/status/current.md)
- **Layer model** — conceptual classification/orientation only: [`docs/3-Layer-Model/README.md`](docs/3-Layer-Model/README.md)
- **Repository inventory** — local/GitHub repository discovery map: [`docs/inventory/README.md`](docs/inventory/README.md)

## Purpose

The repository inventory additionally records where known repositories and documentation roots live; inventory membership is discovery metadata only.

This repository answers four questions without becoming a competing product authority:

1. Which system owns each authoritative state?
2. What crosses each system boundary, under which explicit contract/profile?
3. Which lifecycle is involved: operational workflow, epistemic compilation/recognition, release/activation, presentation, or projection?
4. What is actually implemented/qualified now versus merely specified?

## Ownership map

| System / boundary | Primary ownership |
|---|---|
| **Konnaxion** | civic/public domain state, deliberation, finalized `DecisionRecord`, civic/accountability state |
| **Orgo** | Signal, Workflow, Case, Task, IntegrationOperation, outbox and operational reconciliation |
| **EncyKlopedia** | source discovery/acquisition, provider resolution, lossless evidence and immutable corpus-harvest handoff |
| **Da’at** | mapping/ACL boundary into Kristal-native contracts |
| **Kristal** | referent identity semantics, Kristal State, typed valuations/coordinates/applicability, validation/recognition, Reader Policy, record-role/actionability semantics and knowledge-runtime projection semantics |
| **UCKK / Univers-Cité** | scoped consumer projections, Moodle materialization, derived glossaries, campus/learning state and institutional decisions |
| **kOA-Linux** | platform profiles, trust/policy/resources, artifact admission, release channels and Release Sets |
| **`kristal_runtime`** | Runtime Pack verification/compatibility, active Runtime Pack state, activation/rollback receipts and health |
| **kOA Node Agent** | narrow authorized node-local privileged lifecycle/activation/recovery operations |
| **Koali Spaces** | optional presentation composition, routing, shell and Space lifecycle |
| **Interaction Kernel** | versioned cross-system envelope/Profile semantics only where explicitly adopted |
| **SemantiK Architect** | faithful semantic-to-human communication planning/realization and SA↔GF boundary |
| **SemantiK Runtime Orchestrator** | RuntimeSet release sequencing, promotion/rollback and activation ordering |

## Core rules

- **One authoritative owner per state.** Hosting, transport, projection or rendering does not transfer ownership.
- **No cross-system database writes.** Receivers mutate only receiver-owned state.
- **Projection is rebuildable.** A UCKK/Univers-Cité projection does not become the Kristal canon.
- **Acquisition is not validation.** EncyKlopedia referent candidates and evidence do not become validated Kristal assertions merely by handoff.
- **External identifiers do not transfer authority.** Wikidata, Gutenberg, VIAF and similar identifiers remain references/providers.
- **Interaction Kernel carries contracts; it owns no participant state.** Adoption is explicit and boundary-specific.
- **Space activation is not Runtime Pack activation.** Presentation and knowledge-runtime state are separate lifecycles.
- **`accepted` is not `succeeded`.** Durable asynchronous effects require terminal reconciliation.
- **Historical RC records do not define the active standard.** Retained v5 release-candidate material is migration/history evidence only; the active Kristal v6 standard identity is the pinned manifest/core-contract digest set.

## Principal flows

### Civic decision → governed work

```text
Konnaxion finalized DecisionRecord
    → IK governance.decision.execute/1.0.0
    → Orgo Signal / Workflow / Case / Tasks
    → IK accountability.impact.publish/1.0.0
    → Konnaxion-owned accountability / impact state
```

### Knowledge acquisition → canon → Univers-Cité projection

```text
source discovery / acquisition
    → EncyKlopedia immutable evidence + referent candidates
    → encyklopedia.corpus-harvest-handoff/1.0.0
    → Da’at mapping / ACL
    → Kristal referent + v6 state contracts
    → Working / Reference artifacts as policy permits
    → kristal.artifact.ready/2.0.0
    → uckk.univers-cite-projection/1.0.0
    → rebuildable UCKK / Moodle / glossary / media presentation
```

### Knowledge runtime activation

```text
Kristal Runtime Pack
    → kOA-Linux knowledge channel / Release Set compatibility
    → kristal_runtime verification + active-state transition
    → kOA Node Agent privileged host transition only when required
```

### Presentation composition

```text
admitted application
    → Koali Spaces manifest / runtime registration
    → Space activation / routing / presentation
```

## Start here

- [`docs/index.md`](docs/index.md)
- [`docs/2-Technical-Reference/40-integration/knowledge-projection.md`](docs/2-Technical-Reference/40-integration/knowledge-projection.md)
- [`docs/status/current.md`](docs/status/current.md)

## Selected first tandem deployment profile (2026-10-18)

**User decision:** the first final Konnaxion + Orgo target is a **Linux VPS with Docker and the Konnaxion Capsule Agent**. [C0 profile / owner gates](docs/2-Technical-Reference/40-integration/tandem-vps-capsule-agent/README.md) records this *target*, not a deployment authorization. Local FakePlant IK E2E is verified; Agent signed ReleaseSet admission (**Lot 1C**) and real VPS deployment remain unqualified. kOA-Linux stays an optional separate platform profile.

## C0 — Parallel integration coordination (2026-10-08)

The **frozen Kristal v6/IK v2/UCKK baseline above is preserved**; it should not be read as a claim that the current EncyKlopedia 0.12.0 handoff still emits `encyklopedia.corpus-harvest-handoff/1.0.0`. Current owner contracts and the v10 GitHub publication route are tracked separately in the [C0 coordination register](docs/2-Technical-Reference/40-integration/orchestration-c0/README.md). The new handoff `encyk.source-evidence-handoff/2.0.0` is **not yet verified against a real Médiathèque receiver**.

C0 records cross-system dependencies and evidence; each application remains authoritative for its contracts and releases. Zoology's publication automation policy requires first per-Kristal permission and mandatory independent qualification on every new revision; **the Zoology-specific authorization is not yet established**.

## New mapped applications: Skope & Ékole (Oct 2026)

- **Skope** defines a Wikidata-based Kristal working scope, using local graph extraction, branch depth controls and convergence review. It does **not** publish validated Kristal canon.
- **Ékole** manages Québec primary-school educational workspaces and local student/teacher projections; 202 workspaces are authoring **stubs**, not 202 qualified semantic releases.

See [application ownership and maturity](docs/1-Overview/Components-Skope-and-Ekole.md), [integration boundaries](docs/2-Technical-Reference/40-integration/skope-ekole/index.md), [local ports](docs/2-Technical-Reference/40-integration/skope-ekole/local-ports.md), and [GitHub descriptions](docs/inventory/GITHUB_DESCRIPTIONS.md). These additions do not alter frozen Kristal v6 contracts or qualify new E2E handoffs.
