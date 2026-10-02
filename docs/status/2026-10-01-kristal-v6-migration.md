# 2026-10-01 — Kristal v6 ecosystem migration

## Scope

This snapshot advances the active cross-system knowledge boundary from Kristal v5 RC assumptions to Kristal Standard `6.0.0`. Historical v4/v5 documentation remains for decision history but is explicitly non-current.

## Active contract changes

- canonical structured artifact: `kristal_state`;
- `certainty_level`/`uncertainty` → typed `valuations[]`;
- `qualifiers` → `coordinates`;
- `scope` → `applicability`;
- new generalized semantics: `record_role` and `actionability`;
- IK build/artifact/revision boundaries: `2.0.0`;
- canonicalization: `kristal.v6:jcs-rfc8785`.

## Ecosystem interpretation

Kristal can now preserve external constraints, observations, organizational rules, derived states, decisions and action candidates in one traceable model. This makes deterministic portions of existing processes directly actionable while preserving explicit human-review and human-decision boundaries.

The migration does **not** make Kristal an orchestrator or shared operational database. `actionability = automatic` is eligibility metadata; actual execution still crosses the target owner's contract/admission/authority boundary.

## Validation

The documentation snapshot parses all JSON documents and resolves all included relative Markdown links. Interaction Kernel validation is recorded in its companion snapshot `VALIDATION.md`.
## Post-migration documentation cleanup

The same snapshot cleanup also retires remaining active-doc v5 wording: the integrator guide, Konstellation integration, compatibility/pinning ADR, Architect ADR, ADR index and historical v5 integration pages now distinguish the v6 active baseline from v5 migration/history material.
