# Observability

Observability follows authoritative owners rather than creating a synthetic global state.
## Ecosystem diagnostic and documentary observability

**kOADiag** provides opt-in, scope-limited cross-repository observations (static boundaries, API routes, events, IK and C0 port checks, and owner-provided E2E evidence). **kOA Doc Server** presents documents, independent wiki checkouts, RepoSurveyor profiles and provenance-aware exports. Neither application owns product state or qualifies a release. See the [companion-tool and hinge-repository map](../inventory/ECOSYSTEM_TOOLING.md).

## Runtime Pack

Observe `kristal_runtime` verification, active Runtime Pack identity, activation/rollback receipts and runtime health. Observe kOA Node Agent receipts separately when a privileged host transition occurs.

## Release

Observe Release Set/channel compatibility independently from Runtime Pack verification/activation.

## Koali Spaces

Observe Space activation, runtime registration, readiness and presentation state separately from product business state and Kristal Runtime Pack state.

## Cross-system protocol

Where Interaction Kernel Profiles are adopted, observe delivery/retry/idempotency/reconciliation independently from target-domain completion. Until product/platform adoption is explicit, do not label all kOA-Linux internal interactions as IK traffic.
