# Ecosystem authority map

**Status:** ecosystem-level reference map  
**As of:** 2026-09-21

This page answers one question: **where does authoritative state live?**

It is an index, not a competing source of truth. Product and platform repositories remain authoritative for their internal models, contracts and implementation state.

## Authority map

| State / decision | Authoritative owner | Allowed ecosystem role of others | Explicit non-authority |
|---|---|---|---|
| Civic/public domain state, participation, deliberation, finalized `DecisionRecord` | **Konnaxion** | Consumers may receive authenticated projections, events or references | Orgo, Kristal, Koali Spaces and IK do not become civic-state owners |
| Workflow, `Signal`, `WorkflowVersion`, `Case`, `Task`, `IntegrationOperation`, outbox/reconciliation | **Orgo** | Other systems may trigger work or consume durable results through contracts | Konnaxion and Koali Spaces do not write Orgo work tables |
| Structured Epistemic State, Working/Reference Exchanges, validation/recognition semantics, Reader Policy, Runtime Pack semantics | **Kristal** | Source systems export immutable snapshots/references; runtimes materialize derived views | Kristal is not the live transactional database for Orgo/Konnaxion |
| Ecosystem/IK-facing mapping into Kristal-native contracts | **Da’at** for mapping/ACL behavior | Translates between boundary contracts without taking source ownership | Da’at does not become owner of source operational state or Kristal authority semantics |
| Platform profiles, trust/policy/resources, artifact admission, release channels and Release Set contracts | **kOA-Linux** | Product artifacts are admitted and coordinated under platform policy | Product applications do not acquire platform release authority |
| Runtime Pack verification/compatibility, active Runtime Pack state, activation/rollback receipts, runtime health | **`kristal_runtime`** | kOA-Linux coordinates compatibility; Node Agent may execute narrow privileged mutation | Digital Ecosystem does not define a parallel runtime-activation record |
| Narrow authorized node-local privileged lifecycle / activation / recovery operation | **kOA Node Agent** | Executes an authorized host transition and emits receipts | Node Agent does not own release authority or epistemic state |
| Shell, routing, Space lifecycle and admitted application presentation | **Koali Spaces** | Composes owner surfaces and preserves owner labels/status | Rendering, routing or Space activation do not transfer business/epistemic authority |
| Cross-system Profile/envelope semantics where explicitly adopted | **Interaction Kernel** | Carries commands, queries, events, receipts and artifact references | IK is not participant operational state and is not automatically universal |
| Federated identity credentials/assertions, when OIDC is used | **Identity Provider** for IdP credentials/assertions | Applications map identity into local accounts according to local policy | IdP identity does not imply cross-product roles or authorization |
| Local accounts, memberships, roles, permissions, sessions and application audit | **Each application** | OIDC may authenticate the person; application evaluates local authorization | No shared user database or universal role table |

## Non-transfer rules

```text
integration      != ownership transfer
projection       != authority
cache/read model != source of truth
artifact         != live operational state
transport        != business state
Space activation != Runtime Pack activation
accepted         != succeeded
```

## Authority-preserving flow

```text
product-owned mutable state
        │
        │ immutable export / authenticated interaction
        ▼
contract boundary
        │
        ├── receiver mutates only receiver-owned state
        │
        └── artifact mapping may enter Da’at / Kristal
                    │
                    ▼
          Kristal-owned epistemic artifact
                    │ deterministic build
                    ▼
          derived Runtime Pack / read materialization
```

No step in the flow silently transfers ownership of the upstream source state.

## Related references

- [`architecture.md`](./architecture.md)
- [`trust-boundaries.md`](./trust-boundaries.md)
- [`../40-integration/contract-map.md`](../40-integration/contract-map.md)
- [`../../status/current.md`](../../status/current.md)
- [`../40-integration/identity-oidc/principles.md`](../40-integration/identity-oidc/principles.md)
- [`../40-integration/identity-oidc/local-authorization.md`](../40-integration/identity-oidc/local-authorization.md)
