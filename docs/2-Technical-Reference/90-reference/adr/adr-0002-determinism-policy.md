# ADR-0002: Determinism Policy

- **Status:** Accepted, amended by ADR-0008
- **Decision:** retain deterministic artifact production and reproducible evidence; remove the historical universal validation-before-compile gate.

## Context

Determinism is required for content addressing, signatures, reproducible builds, reliable compatibility checks and idempotent cross-system operations. Kristal v5, however, separates deterministic compilation from validation and authority recognition.

## Decision

kOA requires deterministic behavior where a contract defines canonicalization, hashing, serialization, ordering, identity derivation or idempotency fingerprints.

For Kristal:

1. exact Kristal version/tag/commit and canonicalization profile are pinned;
2. a deterministic compile may create a Working Exchange;
3. validation/review and authority recognition are recorded independently;
4. stricter production policies may gate Reference status, publication, distribution or activation;
5. Build Record v2 records these statuses independently.

## Consequences

The earlier formulation “compile must not run unless validation PASS” is superseded by ADR-0008. Historical records remain interpretable, but new implementations and docs use stage-specific eligibility gates.
