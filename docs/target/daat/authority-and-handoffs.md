# DaaT — Cross-owner authority and handoff architecture

**Status:** `TARGET_DESIGN`. Do not treat these desired handoffs as existing profiles. In a conflict, the approved owner contract wins and the affected route is **BLOCKED**.

## Boundary table

| Stage | Authoritative owner | Permitted DaaT involvement | Must not happen |
|---|---|---|---|
| Identity, account, legal terms | External source holder + identity/security authorities | Route based on authenticated rights/scope | Claim data ownership or terms acceptance on user's behalf |
| Research/acquisition | Skope/EncyK or authorized host connector | Select permitted source lane; validate exports | Add a competing unrestricted web crawler |
| Source custody | Selected Médiathèque instance | Preserve a verified ArtifactRef/source reference | Duplicate raw media catalogue or infer read permission from custody receipt |
| Mappings, contract alignment | DaaT | Declared, pinned, deterministic transformation and fail-closed admission | Auto-granted profile, silent semantic coercion or global ETL store |
| IK transport and delivery | Interaction Kernel | Invoke adopted profile using trusted host | Redefine IK envelope/receipt/retry semantics |
| External crosswalk and language | Framework/diK/Kristalizer | Pass candidates and evidence | Convert Wikidata Q/P or lexical word into KQ/KP automatically |
| Arketype design | Arketype | Present candidate structural composition | Treat templates as semantic graphs |
| Canonical authoring | Framework + Authoring Kit + authorized author | Deliver owner-accepted candidates | Write canonical KA/KS or claim local build is recognized |
| Knowledge release | Independent qualification + content release owners | Reference terminal receipt | Publish to public Git/knowledge sites by inference |
| Runtime activation | Runtime/platform owner | No direct activation side effect | Use signed export as activation grant |
| Operational business effects | Source owner/Orgo/receiving app | No direct mutations; use specific approved interface | Write source accounting records or Tasks from source metadata |

## Interface ID and status ledger

| Target interface | Known source-backed status | To be decided |
|---|---|---|
| DaaT ⇄ IK `kristal.build.request/2.0.0` (v6 path) | Existing narrow owner profile and DaaT offline synthetic tests | Production host qualification under its actual sender restrictions |
| DaaT generic external admission over IK | **No adopted generic profile** | Exact ID, sender/receiver, auth and terminal receipt semantics |
| Skope → Médiathèque evidence custody | Documented source-specific handoff with scope and receipt | Instance-specific source disclosure authorization and cross-owner acceptance |
| Médiathèque → DaaT source-reference mapping | **No adopted generic DaaT/Médiathèque profile** | Exact least-privilege locator, tenant/actor, schema, bilateral tests |
| DaaT/Kristalizer/diK → Kit v11 authoring | Target only; Framework/Kit drafts evolve independently | Pin compatible owner versions, review and rejection fixtures |
| Framework external export PROV-O/RO-Crate | v5 PROV-O draft optional; RO-Crate exact export not proven | Only specific export demand and conformance testing |

Do not assign invented `B-*` identifiers or count new C0 boundaries before C0's existing traceability/boundary registry owners approve them. Existing FC and B-KNOW boundaries continue to govern.

## Authorization, provenance and trust

- Authentication and actor/workload binding must be verified in trusted hosts. An authorization decision is exact-bound, fresh, scoped and enforced at the actual receiving PEP; an `allow` string in a file is not permission.
- Source provenance, build provenance and publication provenance are three separate classes. A source URI or hash does not confer truth/authority.
- Fail closed on cross-tenant references, unsupported contracts, missing disclosure rights, missing audit or an unknown post-side-effect result.
- Treat third-party parser/AI output as untrusted data with source location and review status, never as instructions or validated canonical assertions.
- Third-party OSS notices and data reuse rights are distinct. Source licenses can prohibit retention even if parsing code is permissively licensed.

See [DaaT target overview](README.md) and [acceptance](qualification-and-delivery.md).
