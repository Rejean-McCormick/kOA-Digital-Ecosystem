# FC-18 — Independent qualification, exact evidence and C0 audit publication

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-14](FC-14-identity-and-policy.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An owner or independent reviewer chooses an exact product revision, target profile, risk level and diagnostic campaign.

**Expected final outcome:** A scoped, reproducible qualification verdict with complete evidence links and explicit negative findings; optionally a public-safe dated audit projection.

**Owner(s) of state and decisions:** KristalDiag, KonnaxionDiag, LevelUpDiag-kOA-Linux, LevelUpDiag-Orgo, LevelUpDiag_SemantiK-Architect, MediKristal-LevelUpDiag-; kOA Digital Ecosystem C0 and GitHub Audit as consumers.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Pin target | Diagnostic caller | exact source revision, profile and dependency locks → test subject | Target cannot silently change mid-campaign |
| 2 | Run independent checks | Diagnostic owner | pinned subject → checks, logs and fixtures | Verifier revision, isolated environment and synthetic/real distinction recorded |
| 3 | Issue evidence | Diagnostic engine | results → signed/hashed report and failures | Verdict always scoped to subject and campaign |
| 4 | Review gaps | Owner/security | diagnostic evidence → remediation/admission recommendation | Green check is neither publication approval nor production evidence |
| 5 | Coordinate | C0 | safe evidence metadata → portfolio/maturity/contract map | No copy of private subject data and no blind completion of branch kits |
| 6 | Publish audit view | GitHub Audit / docs portal | selected C0 projection → dated public report | Public-safe, pinned source and interpretation |

## Interfaces and authority gates

The 53 branch kits are **work instructions**, not finished diagnostic reports. The 53 matching SHA-256 snapshot records prove capture identity only; they do not prove successful code tests or integrated release.

## Failure, privacy and forbidden shortcuts

Never issue a global green status from partial campaign, use synthetic tests as real-world proof, or expose source bytes or sensitive logs through the public dashboard.

## Definition of done — acceptance and negative tests

Test verifier independence, tampered subject/reports, negative fixtures, data classification filtering, stale evidence invalidation, Git commit pin mismatch and proof-to-claim scope consistency.

## Required code and contract alignment

Owner implementation: expand diagnostic suites per product and have C0 ingest only explicitly qualified, source-pinned and classified results. Enforce publication signoff of audit projections.

## Product-specific notes

The audit system may reveal uncertainty and blockers. It must not manufacture confidence by filling empty template fields or counting files as capabilities.

## Source anchors and verification boundary

Owner diagnostic READMEs, C0 snapshots-53 ledger and KITS_BRANCHE_53_REPOS; central tests/validation scripts; B-KNOW-07.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
