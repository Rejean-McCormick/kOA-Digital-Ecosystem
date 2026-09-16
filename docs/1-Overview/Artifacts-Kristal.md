# Kristal v5 artifacts

The kOA ecosystem consumes Kristal v5 artifacts without collapsing their epistemic distinctions.

| Artifact | Purpose |
|---|---|
| Structured Epistemic State | structured input/state with provenance and epistemic labels |
| Claim-IR / Resolved Claim-IR | optional extractor/resolution profiles |
| Working Exchange | deterministic compiled Exchange; not necessarily validated/recognized |
| Validation Report | scoped validation decision/findings |
| Authority Recognition | scoped authority recognition decision |
| Reference Exchange | authority-recognized reference artifact for declared scope |
| Reader Policy | controls which labeled material a consumer may read |
| Runtime Pack | offline/runtime projection with explicit source artifact status |

Validation, recognition, publication and activation are separate transitions. A failed or incomplete validation does not universally mean that no Working Exchange may exist.

## What belongs in Kristal

Kristal is the ecosystem's portable epistemic/knowledge artifact layer, not a shared application database. Kristal artifacts are appropriate for knowledge that needs explicit provenance, assertion status, certainty, validation/recognition state, authority scope, reader policy, conflicts/revocations or reproducible content addressing.

Mutable product state remains with its product owner. Orgo Cases/Tasks/Workflow state and Konnaxion consultations/participants/votes/DecisionRecords do not move into Kristal merely because a knowledge artifact is produced from them. The source owner exports an immutable snapshot or referenced artifact; Da’at maps that input to Kristal-native semantics.

## Derived query materializations

A Runtime Pack may contain deterministic structures optimized for local reading/querying, including tables, dictionaries, indexes, columnar data and, when an adopted profile defines it, a read-only database representation. Such structures are **derived and non-authoritative**:

- they are tied to a source Exchange/content digest;
- they must not be a writable operational store;
- they must not redefine epistemic status;
- they must be rebuildable deterministically from the referenced Kristal artifact and declared build inputs.

For production deployment, the kOA Profile may impose stricter eligibility rules (for example recognized/reference material only). Those rules must be declared as kOA deployment policy rather than attributed to Kristal's universal compile semantics.
