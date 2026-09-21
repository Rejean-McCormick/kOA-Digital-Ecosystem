# kOA ecosystem maturity map

**Snapshot date:** 2026-09-21  
**Purpose:** current cross-system engineering view, backed by owner evidence rather than a single ecosystem-wide score.

This page is a **navigation and reconciliation layer**. It does not replace product/platform status documents, release decisions or qualification evidence.

## Reading the map

The dimensions are intentionally separate:

```text
specified / architected
        ≠ implemented
        ≠ tested / qualified
        ≠ integrated with another owner
        ≠ production-proven
```

A subsystem can be mature in one dimension and incomplete in another. Do not collapse this table into one numeric ecosystem score.

## Current maturity map

| System / boundary | Architecture / contracts | Implementation | Qualification evidence | Ecosystem integration | Production / operational evidence | Evidence pointer |
|---|---|---|---|---|---|---|
| **Konnaxion** | Established owner model and product contracts | Implemented; active `v0.8.0` line | **Mixed / remediation remains** in 2026-09-15 engineering ledger; later production validation closed additional runtime/data issues | **Konnaxion↔Orgo IK QUALIFIED 2026-09-21** for two explicit Profile versions | Real production data promotion/API/host validation recorded 2026-09-17; permanent CSRF source patch still required rebuild/redeploy at that snapshot | Owner: `Konnaxion/docs/Technical-Reference/QUALIFICATION_STATUS.md`, `Konnaxion/docs/status/KONNAXION_STATUS_2026-09-17.md`; cross-product: [`2026-09-21-konnaxion-orgo-ik-e2e-qualification.md`](./2026-09-21-konnaxion-orgo-ik-e2e-qualification.md) |
| **Orgo** | Established modular owner model and integration boundaries | Implemented development tree | **PASS** — 2026-09-17 LevelUpDiag acceptance: 9/9 levels; backup/restore, production-like Docker and browser 24/24 included | **Konnaxion↔Orgo IK QUALIFIED 2026-09-21** for decision execution + impact publication | Production-like acceptance is strong; report explicitly does **not** claim real production deployment or external-provider acceptance | Owner: `Orgo/docs/status/2026-09-17-acceptance-status.md`; cross-product: [`2026-09-21-konnaxion-orgo-ik-e2e-qualification.md`](./2026-09-21-konnaxion-orgo-ik-e2e-qualification.md) |
| **Kristal v5** | Pinned `5.0.0-rc.1` baseline; Structured Epistemic State, Working/Reference, Reader Policy and Runtime Pack semantics integrated into ecosystem docs | RC baseline referenced by ecosystem | Ecosystem defines required v5 conformance conditions; owner-runtime qualification is not reclassified here | Da’at/IK-facing mapping remains **target/selective**; no implication of universal integration | Not centrally classified by Digital Ecosystem | [`../2-Technical-Reference/40-integration/kristal-v5/conformance.md`](../2-Technical-Reference/40-integration/kristal-v5/conformance.md) |
| **kOA-Linux / Koali platform** | Extensive canonical platform contracts, architecture/conformance governance and release model | **Advanced Beta — System Closure & Qualification** as of 2026-09-19 | Architecture/conformance ready; component bundles and subsystem sources PASS | Current active runtime scope deliberately centers Koali + Konnaxion + Orgo; Ariane/SemantiK are excluded from the current sovereign base composition | System-release path still BLOCKED at package resolution, resolved plan, image projection and final release evidence | Owner: `koa-linux/docs/status/2026-09-19-technical-progress-and-runtime-integration-status.md` |
| **Koali Spaces** | Generic Surface Layer contracts and authority boundaries established | Core Surface Layer implemented | Historical qualified beta baseline: **Core M4/5**, overall hosting **M3/5** on owner scale | Later evidence records first real Konnaxion pilot; broader ecosystem hosting remains progressive | Not stable / M5 in the cited owner baseline; follow-up remained around health projection and repeatable navigation/fallback | Owner: `koali-spaces/docs/status/KOALI_SPACES_MATURITY_REPORT_SURFACE_LAYER_v1.2.2-beta.1.md`; ecosystem: [`../2-Technical-Reference/40-integration/koali-spaces/index.md`](../2-Technical-Reference/40-integration/koali-spaces/index.md) |
| **Interaction Kernel** | Normative protocol/Profile documentation exists; operational state remains participant-owned | Selectively adopted | **Qualified for Konnaxion↔Orgo** Profile versions listed below | Explicit, boundary-specific adoption only; no ecosystem-wide replacement of kOA-Linux internal contracts | Not a central service and not independently classified as a production application | [`../2-Technical-Reference/40-integration/interaction-kernel/status.md`](../2-Technical-Reference/40-integration/interaction-kernel/status.md) |
| **Da’at → Kristal mapping** | Selected ACL/mapping boundary | Mapping role defined | No cross-product qualification claimed by the Konnaxion↔Orgo result | **Target / pending owner conformance** for Kristal v5 mapping | Not centrally classified | [`../2-Technical-Reference/20-nodes/daat-kristal-bridge.md`](../2-Technical-Reference/20-nodes/daat-kristal-bridge.md), [`../2-Technical-Reference/40-integration/kristal-v5/conformance.md`](../2-Technical-Reference/40-integration/kristal-v5/conformance.md) |

## Qualified cross-owner boundaries

As of this snapshot, the strongest explicit cross-product qualification recorded in this repository is:

| Boundary | Version | State |
|---|---|---|
| Konnaxion/eThikos → Orgo decision execution | `governance.decision.execute/1.0.0` | **QUALIFIED 2026-09-21** |
| Orgo → Konnaxion durable impact publication | `accountability.impact.publish/1.0.0` | **QUALIFIED 2026-09-21** |

The qualification includes durable delivery, owner-local mutation, idempotent replay and divergent replay conflict behavior. It is local integrated-runtime evidence, **not production-environment qualification**.

## Current platform composition is not ecosystem membership

The 2026-09-19 kOA-Linux sovereign base composition intentionally treats:

```text
Konnaxion          ACTIVE
Orgo               ACTIVE
Ariane             EXCLUDED / not_installed
SemantiK Architect EXCLUDED / not_installed
```

This is a **profile/composition decision**, not a statement that excluded subsystems have ceased to exist in the broader kOA ecosystem.

## Update rule

A maturity claim should move only when there is new owner evidence. Prefer this order:

1. owner repository status / qualification record;
2. executable CI/runtime evidence for the exact scope;
3. cross-product qualification record when two owners are involved;
4. dated ecosystem reconciliation here.

Do not infer `production-proven` from documentation completeness, local test success, an RC label, or a successful integration pilot.

## Control views

- [System map](../1-Overview/index.md#system-map)
- [Authority map](../2-Technical-Reference/10-system/authority-map.md)
- [Contract map](../2-Technical-Reference/40-integration/contract-map.md)
- [Detailed alignment status](./index.md)
