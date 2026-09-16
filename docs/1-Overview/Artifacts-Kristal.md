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

For production deployment, the kOA Profile may impose stricter eligibility rules (for example recognized/reference material only). Those rules must be declared as kOA deployment policy rather than attributed to Kristal's universal compile semantics.
