# Architecture

## Architectural thesis

kOA is a system of independently owned systems and platform components. Integration coordinates them without collapsing their authoritative states.

## Owner map

| Responsibility | Owner |
|---|---|
| civic/public state and DecisionRecord | Konnaxion |
| workflow/work state and durable external operations | Orgo |
| epistemic artifact semantics | Kristal |
| platform profiles/trust/policy/resources/release channels | kOA-Linux |
| Runtime Pack verification/compatibility/active state/receipts/runtime health | `kristal_runtime` |
| narrow privileged node-local lifecycle transition | kOA Node Agent |
| presentation composition and Space lifecycle | Koali Spaces |
| target cross-system protocol/Profile semantics | Interaction Kernel, where explicitly adopted |
| ecosystem-to-Kristal mapping/ACL | Da’at |

## Release architecture

kOA-Linux separates `system`, `services`, `governance` and `knowledge` release channels. A Release Set binds tested-compatible versions across channels.

Kristal Runtime Packs are platform artifacts in the `knowledge` channel. The kOA-Linux artifact classification (`artifact_class = runtime_pack`) is distinct from Kristal's own scoped manifest discriminator.

## Runtime Pack activation architecture

```text
Runtime Pack candidate
  -> kOA-Linux artifact / knowledge-channel admission
  -> kristal_runtime verification + compatibility + activation eligibility
  -> active_runtime_pack_record transition
  -> activation/rollback receipt

when privileged host mutation is required:
  -> kOA Node Agent executes the narrow authorized node-local transition
```

`kristal_runtime` does not own governance policy, resource scheduling, host privilege or workflow state. kOA Node Agent does not own release authority or epistemic semantics.

## Koali Spaces placement

Koali Spaces sits above admitted applications as optional presentation infrastructure. It owns shell/routing/presentation/Space lifecycle only. Removing Koali must not transfer or delete owner-system business state.

## Interaction Kernel placement

IK is a target system-of-systems protocol/Profile layer for selected cross-product boundaries. kOA-Linux already has canonical internal/component communication contracts; Digital Ecosystem must not claim those have been replaced by IK until explicit adoption/mapping is published.
