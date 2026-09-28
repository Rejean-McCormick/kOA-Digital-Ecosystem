# ADR-0012 — Knowledge acquisition, Kristal canon and consumer projections

- **Status:** Accepted
- **Date:** 2026-09-28

## Decision

1. EncyKlopedia owns source discovery/acquisition and immutable evidence handoff.
2. Da’at owns mapping/ACL at the Kristal boundary.
3. Kristal owns referent identity semantics, assertions, evidence/provenance, validation/recognition and canonical epistemic artifacts.
4. UCKK/Univers-Cité owns consumer projection choices: scope membership, primary navigation view, derived glossary, Moodle materialization and media-library presentation.
5. A consumer projection is rebuildable and never becomes the Kristal source of truth.
6. External identifiers such as Wikidata or Gutenberg do not transfer authority.
7. Interaction Kernel carries only explicitly adopted versioned boundary profiles; it owns none of the participant states.

## Frozen contracts

- Kristal `5.0.0-rc.3`; Referent Registry `1.0.0`.
- EncyKlopedia `encyklopedia.corpus-harvest-handoff/1.0.0`.
- UCKK `uckk.univers-cite-projection/1.0.0`.
- IK `kristal.build.request/1.1.0` and `kristal.artifact.ready/1.1.0` for acquisition/projection consumers.
