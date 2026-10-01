# Ecosystem authority map

**Status:** current ecosystem-level reference map

This page answers one question: **where does authoritative state live?** It is an index, not a competing source of truth.

## Authority map

| State / decision | Authoritative owner | Allowed ecosystem role of others | Explicit non-authority |
|---|---|---|---|
| Civic/public domain state, participation, deliberation, finalized `DecisionRecord` | **Konnaxion** | Consumers may receive authenticated projections/events | Orgo, Kristal, Koali and IK do not become civic-state owners |
| Workflow, Signal, WorkflowVersion, Case, Task, IntegrationOperation, outbox/reconciliation | **Orgo** | Other systems may trigger work or consume durable results | Konnaxion/Koali do not write Orgo work tables |
| Source discovery, provider resolution, lossless acquisition evidence and immutable harvest handoff | **EncyKlopedia** | Da’at/Kristal consume pinned exports/evidence | Acquisition does not validate epistemic truth or own Moodle projections |
| Ecosystem/IK-facing mapping into Kristal-native contracts | **Da’at** | Maps/adapts payloads under ACL while preserving provenance | Da’at owns neither source state nor Kristal authority semantics |
| Referent Registry semantics, Kristal State, typed valuations/coordinates/applicability, validation/recognition, Reader Policy, record-role/actionability semantics and derived runtime projections | **Kristal** | Consumers derive read/projection/runtime materializations | Kristal is not source acquisition, a live app DB, or UCKK presentation state |
| Univers-Cité scope/projection configuration, Moodle/campus state, derived glossary/media presentation, local Assembly decisions | **UCKK / Univers-Cité** | Consumes pinned Kristal artifacts and optional external readings | UCKK does not own Kristal assertions/referents or Konnaxion civic decisions |
| Platform profiles, trust/policy/resources, artifact admission, release channels and Release Sets | **kOA-Linux** | Admits/co-ordinates product artifacts under platform policy | Product apps do not acquire platform release authority |
| Runtime Pack verification/compatibility, active Runtime Pack state, activation/rollback receipts, runtime health | **`kristal_runtime`** | Platform coordinates compatibility; Node Agent may execute narrow privilege | Digital Ecosystem does not create a parallel runtime-activation state |
| Narrow authorized node-local privileged lifecycle / activation / recovery operation | **kOA Node Agent** | Executes authorized host transitions and emits receipts | Node Agent does not own release or epistemic authority |
| Shell, routing, Space lifecycle and admitted application presentation | **Koali Spaces** | Composes owner surfaces | Rendering/routing does not transfer business/epistemic authority |
| Cross-system Profile/envelope semantics where explicitly adopted | **Interaction Kernel** | Carries commands, queries, events, receipts and ArtifactRefs | IK is not participant operational state and is not automatically universal |
| Human-readable communication planning/realization, SA↔GF bridge, RuntimeSet/capability/conformance semantics | **SemantiK Architect** | Realizes complete upstream meaning faithfully | Does not choose truth, civic outcomes or omit supplied facts |
| RuntimeSet release ordering, integrity transfer, promotion/rollback and activation sequencing | **SemantiK Runtime Orchestrator** | Coordinates independent GF/SA/diagnostic owners | Does not own grammar, semantic truth or diagnostic truth |
| Federated identity credentials/assertions | **Identity Provider** for IdP assertions | Apps map identity into local accounts | IdP identity does not imply cross-product roles |
| Local memberships, roles, permissions, sessions and app audit | **Each application** | OIDC may authenticate; app authorizes locally | No universal role table |

## Non-transfer rules

```text
integration              != ownership transfer
projection               != authority
acquisition evidence     != validation
external identifier      != authority
cache/read model         != source of truth
artifact                 != live operational state
transport                != business state
Space activation         != Runtime Pack activation
accepted                 != succeeded
```

## Authority-preserving knowledge flow

```text
source/provider
    → EncyKlopedia evidence + referent candidates
    → Da’at mapping/ACL
    → Kristal-owned referent/Kristal State artifact
    → derived Runtime Pack or UCKK projection
```

No step silently transfers ownership of the upstream state.

## Related references

- [`architecture.md`](./architecture.md)
- [`trust-boundaries.md`](./trust-boundaries.md)
- [`../40-integration/contract-map.md`](../40-integration/contract-map.md)
- [`../40-integration/knowledge-projection.md`](../40-integration/knowledge-projection.md)
- [`../../status/current.md`](../../status/current.md)

## Kristal v6 actionability invariant

Actionability classification is knowledge/policy metadata. It does not transfer execution authority from an operational owner to Kristal, Da’at or a consumer projection.
