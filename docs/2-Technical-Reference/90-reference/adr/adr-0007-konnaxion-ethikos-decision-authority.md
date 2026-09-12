# ADR-0007: Konnaxion/eThikos Owns Civic Decision Finalization and Direct Orgo Handoff

**Status:** Accepted  
**Date:** 2026-09-12  
**Decision Owner:** Ecosystem Architecture  
**Scope:** Konnaxion/eThikos decision authority, Orgo execution handoff, optional UCKK publication

---

## 1) Context

An earlier A014 demonstration path modeled the operational trigger as a decision published by UCKK/Assembly and then relayed to Orgo. That model was incorrect for the intended product architecture.

The intended architecture is that civic/public deliberation and decision finalization occur inside **Konnaxion/eThikos**. Orgo is the governed execution/workflow system. UCKK is optional as a publication/distribution/learning surface.

## 2) Decision

For Konnaxion-owned civic/public decisions:

```text
Konnaxion / eThikos deliberation
→ readings (Smart Vote / EkoH / etc.)
→ eThikos decision stage
→ finalized DecisionRecord
→ direct Konnaxion→Orgo machine handoff
→ Orgo Signal / Workflow / Case / Tasks
```

The finalized eThikos DecisionRecord is the authoritative source event for the Orgo handoff.

UCKK MAY independently consume the decision for publication, distribution, presentation, or learning, but MUST NOT be required as the decision authority or mandatory relay between Konnaxion and Orgo.

Smart Vote/EkoH outputs remain readings/inputs unless a specific eThikos decision contract explicitly assigns a different role. A reading alone MUST NOT be silently treated as the finalized decision.

## 3) Boundary rules

- Konnaxion/eThikos owns civic decision state and final DecisionRecords.
- Orgo owns Signal/WorkflowVersion/Case/Task operational state.
- Konnaxion hands decisions to Orgo through an authenticated, versioned, idempotent machine boundary.
- Konnaxion does not write Orgo tables directly.
- Orgo does not become the owner of the civic decision.
- Orgo→Konnaxion operational impact/publication uses the IntegrationOperation + Outbox + provider pattern.
- UCKK publication is optional and independent from the direct Konnaxion→Orgo handoff.

## 4) Consequences

Positive:

- decision ownership matches Konnaxion/eThikos product responsibility;
- Orgo receives a clear, auditable operational trigger;
- UCKK can be present or absent without changing decision authority;
- Smart Vote remains transparent decision support rather than hidden execution authority;
- cross-system boundaries stay explicit and independently testable.

Required follow-up:

- refactor historical A014 fixtures that encode UCKK/Assembly as the authority path;
- introduce/validate a direct Konnaxion/eThikos→Orgo handoff;
- revalidate the end-to-end scenario before treating historical checkpoint passes as conformance evidence;
- retain historical identifiers only for traceability until renamed/migrated.

## 5) Superseded assumption

The following assumption is explicitly rejected:

```text
Konnaxion reading
→ UCKK/Assembly decision authority
→ UCKK relay
→ Orgo
```

for the Konnaxion/eThikos decision flow covered by this ADR.

## 6) Related documents

- `../../40-integration/orgo-konnaxion/index.md`
- `../../40-integration/orgo-konnaxion/uckk-a014-validation-2026-09-12.md`
- `../../../3-Layer-Model/layers/07_decision_legitimacy.md`
- `../../../3-Layer-Model/layers/08_execution.md`
