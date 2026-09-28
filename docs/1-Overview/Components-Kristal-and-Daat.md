# Kristal, Da’at and the knowledge boundary

Kristal is the ecosystem's structured epistemic/reference system. Da’at is the anti-corruption/mapping boundary used to enter Kristal-native contracts. EncyKlopedia and UCKK sit on opposite sides of this boundary with different responsibilities.

## Current authority flow

```text
source/provider discovery
    ↓
EncyKlopedia
    acquisition evidence + referent candidates
    ↓ encyklopedia.corpus-harvest-handoff/1.0.0
Da’at
    mapping / ACL / contract adaptation
    ↓
Kristal
    Referent Registry + epistemic artifacts
    ↓ kristal.artifact.ready/1.1.0
UCKK / Univers-Cité
    rebuildable scoped projection / Moodle / glossary / media view
```

## Kristal v5 lifecycle

```text
Structured Epistemic State
    ↓ compile
Working Exchange
    ↓ review / validation / authority recognition
Reference Exchange (when recognized for a declared scope)
    ↓ policy-dependent derivation
Runtime Pack / consumer projection
```

Claim-IR and Resolved Claim-IR may exist in extraction/resolution profiles, but they are not universal mandatory stages.

## Referent identity

The current knowledge-contract baseline adds **Referent Registry `1.0.0`** as a domain-neutral identity layer. External identifiers such as Wikidata, Gutenberg or VIAF may support matching/provenance; they do not become the authority for Kristal referent identity or assertion status.

## EncyKlopedia responsibilities

EncyKlopedia owns:

- source discovery and provider resolution;
- lossless acquisition evidence and provenance;
- source snapshots/exports;
- referent candidates;
- the immutable corpus-harvest handoff.

It does **not** validate epistemic truth or create authority recognition merely by acquiring evidence.

## Da’at responsibilities

Da’at:

- maps source/IK-facing payloads into Kristal-native contracts;
- enforces the declared mapping/ACL boundary;
- preserves source identity, provenance and epistemic labels;
- does not become owner of source operational state or Kristal authority semantics.

## UCKK / Univers-Cité responsibilities

UCKK owns consumer projection choices such as scope membership, primary view, derived glossary, Moodle materialization and media-library presentation. The projection is rebuildable from a pinned Kristal state and does not become the Kristal source of truth.

## Current Kristal baseline

The knowledge-contract set targets:

```text
Kristal                  5.0.0-rc.3 (release-candidate)
Referent Registry        1.0.0
knowledge-model bundle   sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98
```

The supplied rc.3 release metadata declares `v5.0.0-rc.3` but has no resolved commit SHA yet. Treat this as a frozen contract baseline, not as proof of a completed immutable release.

See [knowledge-projection.md](../2-Technical-Reference/40-integration/knowledge-projection.md).
