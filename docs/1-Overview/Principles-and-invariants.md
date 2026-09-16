# Principles and invariants

1. **Unique authoritative owner.** Every authoritative state has one declared logical owner.
2. **No direct cross-system writes.** Integrations use explicit versioned contracts and owner APIs.
3. **Presentation is not authority.** Koali rendering, routing or Space activation does not transfer business, epistemic or host authority.
4. **Integrity is not authority.** Valid bytes/signatures do not imply validation, recognition or activation eligibility.
5. **Workflow state is not epistemic state.** Orgo statuses do not replace Kristal assertion/validation/recognition states.
6. **Compilation is not validation.** Kristal v5 may compile Working Exchanges before final validation/recognition where policy permits.
7. **Recognition is scoped.** Reference status is authority/scope-specific, not universal truth.
8. **Reader Policy does not rewrite underlying state.** Visibility preserves labels and lineage.
9. **Runtime Pack state has a precise owner.** On kOA-Linux, `kristal_runtime` owns verification/compatibility/active Runtime Pack state and activation/rollback receipts; Node Agent performs only the narrow privileged host transition when required.
10. **Release Set is not activation state.** It binds compatible release-channel versions; it does not replace component active-state records.
11. **Space activation is not Runtime Pack activation.** Koali Space lifecycle is presentation/application composition.
12. **`accepted != succeeded`.** Durable asynchronous operations require terminal reconciliation.
13. **Idempotency survives retry/redrive.** Same logical key with different semantic content is a conflict.
14. **IK adoption is explicit.** Interaction Kernel is the target cross-system Profile layer, but it does not silently replace kOA-Linux internal/component contracts.
15. **No forced Kristal hop.** Konnaxion↔Orgo remains direct unless an adopted Profile explicitly requires Kristal.
