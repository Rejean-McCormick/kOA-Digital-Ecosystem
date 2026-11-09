# FC-20 — Medical-domain knowledge and pathway application

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-02](FC-02-source-custody.md), [FC-04](FC-04-semantic-authoring.md), [FC-06](FC-06-knowledge-consumption.md), [FC-14](FC-14-identity-and-policy.md), [FC-18](FC-18-diagnostics-and-audit.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An authorized clinical/domain operator requests a scoped medical knowledge or pathway view from admitted sources and approved internal domain data.

**Expected final outcome:** An attributable, authorization-bound medical-domain feature, **not a clinical diagnosis or care authorization by virtue of this architecture**.

**Owner(s) of state and decisions:** MediKristal for its application/domain data and pathways; MediKristal-LevelUpDiag- for engineering checks; external qualified clinical/institutional authority for any medical deployment.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Admit context | MediKristal | authorized professional/tenant + use purpose → scoped session | No inference of medical qualification from login alone |
| 2 | Resolve material | MediKristal / read adapters | approved source and semantic references → traceable read set | Provenance, currency and uncertainty visible |
| 3 | Apply domain logic | MediKristal | local domain data/rules → proposed pathway or information view | Application remains owner of its decision support semantics |
| 4 | Review | Authorized domain actor | candidate output → accepted/rejected local action | High-risk medical actions require independent governance and human oversight |
| 5 | Record | MediKristal | approved event → minimal audit/domain receipt | Health data privacy and retention policy enforced |
| 6 | Diagnose software | MediKristal LevelUpDiag | pinned app revision → engineering checks | Software PASS is explicitly not clinical safety approval |

## Interfaces and authority gates

No general integrated medical→Orgo/UCKK/Framework publication contract is approved by these inputs. Any such handoff requires domain, privacy, safety and interface-specific owner decisions.

## Failure, privacy and forbidden shortcuts

Fail closed for unverified clinical status, stale or missing clinical evidence, cross-patient data, missing consent/role, model-produced unsupported advice and unsafe automated intervention.

## Definition of done — acceptance and negative tests

Test tenant/patient isolation, data minimization, audit, access revocation, clinical-domain unknowns, stale source warnings and negative engineering fixtures; a qualified clinical safety process is separately required before real-care use.

## Required code and contract alignment

Owner implementation: isolate health-data authority from C0 and public Git; establish clinical validation, privacy, incident and deployment governance before enabling real patient workflows.

## Product-specific notes

Neither semantic conformance nor an engineering diagnostic certifies medical efficacy, patient safety, regulatory compliance or suitability for care.

## Source anchors and verification boundary

MediKristal owner README and MediKristal LevelUpDiag owner documentation; snapshots do not establish clinical certification.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
