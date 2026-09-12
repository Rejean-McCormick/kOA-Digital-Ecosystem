# kOA — Current Status

**Last updated:** 2026-09-12  
**Purpose:** concise operational/architecture status. This directory is descriptive, not normative; ADRs and technical contracts remain authoritative.

## Current headline

The ecosystem architecture has been corrected so that **Konnaxion/eThikos owns civic/public decision finalization and hands finalized decisions directly to Orgo**. UCKK is optional for publication/distribution and is not a mandatory relay.

The **outbound Orgo → Konnaxion durable publish path is now validated end-to-end** on the historical A014 fixture, including canonical recovery of a previously dead outbox delivery and exact-one provider effect.

The main remaining gap is the **direct Konnaxion/eThikos → Orgo decision handoff** and revalidation of the scenario against that corrected authority model.

## Status matrix

| Capability | Status | Evidence / note |
|---|---|---|
| Konnaxion/eThikos decision authority model | **DECIDED** | ADR-0007 accepted |
| UCKK optional publication/distribution role | **DECIDED** | Not mandatory in Konnaxion→Orgo path |
| Orgo Signal / Workflow / Case / Task mechanics | **VALIDATED (historical fixture)** | Mechanics pass; old authority path not final acceptance evidence |
| Konnaxion World `uckk-a014` / release 1 | **VALIDATED** | READY/CURRENT provider context |
| Orgo worker → Konnaxion provider | **VALIDATED** | Publish POST 200 |
| Canonical outbox redrive | **VALIDATED** | FAILED/DEAD historical delivery recovered through API |
| J30 IntegrationOperation terminal result | **VALIDATED** | `RUNNING → SUCCEEDED` |
| Konnaxion J30 provider effect | **VALIDATED** | `count = 1`, `receipt.status = succeeded` |
| Direct Konnaxion/eThikos → Orgo handoff | **OPEN** | Primary remaining integration task |
| Corrected inbound idempotency test | **OPEN** | Must prove replay creates no duplicate Orgo consequence |
| Corrected end-to-end scenario | **OPEN** | Must replace UCKK/Assembly mandatory authority path |
| Later follow-up / reconsideration (historical J90/R1) | **BLOCKED** | Wait until corrected inbound path is proven |

## Next actions

1. Define the smallest finalized eThikos DecisionRecord/handoff contract Orgo actually needs.
2. Implement or configure a dedicated authenticated Konnaxion/eThikos → Orgo machine adapter.
3. Map the decision handoff to an Orgo Signal with stable `decision_ref`, correlation and idempotency identity.
4. Refactor the historical A014 fixtures so UCKK is optional rather than the authority/relay.
5. Validate inbound replay/idempotency and expected Signal/Case/Task creation.
6. Re-run the already proven outbound Impact publication from the corrected scenario.
7. Then run the later observation/reconsideration checkpoints and freeze the final demo evidence.

## Do not regress

- No cross-system SQL business mutation.
- No hardcoded runtime UUIDs in reusable world/scenario packs.
- `accepted != succeeded` for asynchronous provider work.
- Redrive existing durable work; do not recreate it blindly.
- Bridge/database/application credentials are distinct and must not be persisted in docs.
- Smart Vote/EkoH readings are inputs to the eThikos decision process, not silent execution authority by themselves.

## Detailed status

See [`2026-09-12.md`](2026-09-12.md).

## Architecture references

- [`../2-Technical-Reference/90-reference/adr/adr-0007-konnaxion-ethikos-decision-authority.md`](../2-Technical-Reference/90-reference/adr/adr-0007-konnaxion-ethikos-decision-authority.md)
- [`../2-Technical-Reference/40-integration/orgo-konnaxion/index.md`](../2-Technical-Reference/40-integration/orgo-konnaxion/index.md)
- [`../2-Technical-Reference/40-integration/orgo-konnaxion/uckk-a014-validation-2026-09-12.md`](../2-Technical-Reference/40-integration/orgo-konnaxion/uckk-a014-validation-2026-09-12.md)
