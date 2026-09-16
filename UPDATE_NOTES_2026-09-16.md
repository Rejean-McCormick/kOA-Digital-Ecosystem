# Update notes — 2026-09-16

This update starts from the supplied `kOA_Digital_Ecosystem.wiki(2).zip` version and incorporates the current supplied kOA-Linux and Koali Spaces documentation snapshots.

## Main changes

1. Refined Runtime Pack ownership: `kristal_runtime` owns local verification/compatibility/active-state/activation+rollback receipts/runtime health; kOA Node Agent performs only narrow privileged node transitions when required.
2. Deprecated the Digital Ecosystem-created authoritative `Runtime Activation State` for kOA-Linux.
3. Replaced Digital Ecosystem `Release Record v2` authority with the kOA-Linux Release Set/release-channel model; legacy Release Record remains projection-only.
4. Added explicit `system/services/governance/knowledge` release-channel mapping.
5. Added Koali Spaces as an optional presentation/composition subsystem and separated Space activation from Runtime Pack activation.
6. Recorded later Koali↔Konnaxion pilot evidence and flagged stale Koali “pilot pending” reference pages as product documentation drift.
7. Reframed Interaction Kernel as the target cross-system protocol/Profile layer whose adoption must be explicit; it does not automatically replace kOA-Linux internal/component contracts.
8. Kept Kristal v4 pages only as historical link targets; v5 remains active.
9. Updated ADR-0009 and ADR-0010 to reflect the refined ownership/adoption model.
10. Added ADR-0011 to formalize the three-layer authority boundary: product-owned operational state → immutable source export/Da’at mapping → Kristal knowledge artifact → derived Runtime Pack/query materialization.
11. Clarified that IK is not a database/artifact store, Kristal is not a shared transactional database, and any database-like Runtime Pack representation must be read-only/derived/rebuildable rather than a second source of truth.
