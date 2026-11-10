# 53-source snapshot reconciliation and branch-10 evidence

**Status:** `OBSERVED_SNAPSHOT` (offline file provenance) and `TARGET_DESIGN` (functional responsibilities). Supplied date: 2026-11-09. This ledger does not certify GitHub HEAD, deployment, all owner tests or cross-owner qualification.

The 53 members from `SmartDump_20261109_113255(2).zip` were checked against their supplied audit register SHA-256. See the machine-readable [53-snapshot ledger](../inventory/code-snapshots-53.v1.json), the [portfolio roles](portfolio.v1.json) and [inventory](../inventory/repositories.json). All 53 owner-code entries are intentionally `NOT_EVALUATED` for doc-code conformity and `NOT_RUN` for tests in this *source-intake* ledger.

## Newer branch-10 owner snapshots

Four additional owner snapshots were uploaded at 16:35 local time: `kOA_Digital_Ecosystem_Code_snapshot(7).zip`, `docs-initkoa-org_Code_snapshot(1).zip`, `HomePage_Code_snapshot(1).zip`, and `Koali_Scenario_Mosaic_Code_snapshot(1).zip`. They are used as the **current branch-10 code baselines**. Their fingerprints and exact source-size observations are recorded in [the branch-10 source manifest](../integration/branch10-inputs.v1.json). They do not replace the 53-owner intake evidence for unrelated repositories.

The central ZIP's README, tests and scripts referenced `docs/target/` but the ZIP did **not** contain that directory. This branch has recreated a working target-design corpus against the currently available 53 owner sources, preserving the original central non-target code. **It is a reconstruction**, not a byte-for-byte recovery of earlier unmounted generated artifacts. Product owners must still qualify exact contracts and applications.

## Source classes and limits

| Evidence | Permitted claim | Forbidden extrapolation |
|---|---|---|
| File/ZIP SHA-256 | Exact captured bytes from an offline snapshot | Actual GitHub revision, successful build or deployment |
| Local build/validation result | Named test ran in named local environment | Every branch integration works |
| Bilateral contract test | Exact pinned sender and receiver handled fixtures | Other consumers or public release permission |
| Owner release permission | Named content and destination approved | Host activation or clinical use |
| Measured host receipt | Exact target environment reached a reported state | Universal production maturity |

The final functional architecture is summarized in [its index](functional-chains/README.md). Historical dated versions of contract material remain preserved under `docs/2-Technical-Reference/40-integration/` and are not silently reclassified as final standard.
