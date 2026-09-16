# kOA Digital Ecosystem

> System-of-systems documentation for the kOA ecosystem. This repository describes cross-system ownership, integration contracts, release/activation boundaries, and implementation-status evidence. Product repositories remain authoritative for their internal models and implementation status.

**Alignment baseline:** 2026-09-16  
**Kristal baseline:** `5.0.0-rc.1` / tag `v5.0.0-rc.1` / commit `af703bf02ee04a69a5f2ad6694fa8b8e56ae2b19`  
**kOA-Linux baseline:** current supplied docs/contracts snapshot generated 2026-09-16  
**Koali Spaces baseline:** current supplied docs snapshot generated 2026-09-16

## Purpose

kOA is a system of independently owned systems. This documentation answers:

1. Which system owns each authoritative state?
2. What crosses a system boundary, under which contract?
3. Which transition is occurring: workflow, epistemic compilation/validation/recognition, release-channel activation, Runtime Pack activation, or UI/Space activation?
4. What is implemented now versus defined as a target integration?

## Ownership map

| System / boundary | Primary ownership |
|---|---|
| **Konnaxion** | civic/public domain state, deliberation, consultations, readings, DecisionRecord and product surfaces |
| **Orgo** | Signal, Workflow, Case, Task, IntegrationOperation, outbox and operational reconciliation |
| **Kristal** | Structured Epistemic State, Working/Reference Exchanges, validation, authority recognition, Reader Policy and Runtime Pack semantics |
| **kOA-Linux** | host/platform contracts: profiles, trust, policy, resources, artifact admission, release channels, privileged lifecycle operations |
| **kristal_runtime** | kOA-Linux native runtime component owning Runtime Pack verification/compatibility state, active Runtime Pack state, activation/rollback receipts and runtime health |
| **kOA Node Agent** | narrow node-local privileged lifecycle/activation/recovery operations under authorization |
| **Koali Spaces** | optional global experience/presentation composition; Space activation, routing, shell and admitted application surfaces |
| **Interaction Kernel (IK)** | target cross-system interoperability protocol/Profile layer; not participant state |
| **Da’at** | mapping/ACL boundary between ecosystem/IK-facing requests and Kristal-native contracts |

## Core rules

- **One authoritative owner per state.** Hosting, rendering, transport or projection does not transfer ownership.
- **No cross-system database writes.** Receivers mutate only their own authoritative state.
- **Kristal v5 compilation is distinct from validation and recognition.** A Working Exchange can exist before final validation/recognition where policy permits.
- **Release channels are distinct.** kOA-Linux separates `system`, `services`, `governance` and `knowledge` channels and binds compatible versions through a Release Set.
- **Runtime Pack activation state is not a new Digital Ecosystem artifact.** In kOA-Linux deployments, `kristal_runtime` owns Runtime Pack verification/active-state/rollback records; kOA Node Agent can execute the narrow privileged host transition where required.
- **Space activation is not Runtime Pack activation.** Koali Spaces activates presentation/application composition, not Kristal knowledge state.
- **Interaction Kernel is the target system-of-systems protocol.** It must not be presented as already replacing kOA-Linux's canonical internal/component communication contracts until those contracts explicitly adopt it.
- **`accepted` is not `succeeded`.** Durable asynchronous effects require terminal reconciliation.

## Principal flows

```text
Konnaxion finalized DecisionRecord
        │
        │ target IK profile: governance.decision.execute
        ▼
Orgo Signal → WorkflowVersion → Case / Tasks
        │
        │ target IK profile: accountability.impact.publish
        ▼
Konnaxion-owned accountability / impact state
```

```text
source / dataset / proposal
        ▼
Structured Epistemic State
        ▼
Working Exchange
        ▼
validation / review / authority recognition as applicable
        ▼
Reference Exchange when recognized
        ▼
Runtime Pack
        ▼
kOA-Linux knowledge channel + Release Set compatibility
        ▼
kristal_runtime verification / active state
        ▼
kOA Node Agent privileged transition when required
```

```text
admitted product/application
        ▼
Koali Spaces registry / Space configuration
        ▼
Space activation / routing / presentation

This is presentation state, not Kristal Runtime Pack activation.
```

## Current status

The architecture and documentation are aligned, but target protocol adoption and product integration maturity are not uniform. Koali Spaces has later evidence for a real Konnaxion pilot, while some current Koali reference pages still describe that pilot as pending and therefore need product-side refresh. Interaction Kernel remains a target system-of-systems integration layer until explicit product/platform contract adoption is published.

See [`docs/status/2026-09-16.md`](docs/status/2026-09-16.md).
