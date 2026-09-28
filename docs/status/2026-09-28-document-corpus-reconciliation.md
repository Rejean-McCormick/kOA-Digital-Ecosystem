# kOA Digital Ecosystem — document-corpus reconciliation

**Date:** 2026-09-28  
**Status:** reconciliation record  
**Authority:** non-authoritative; owner repositories remain authoritative for their own scope

## Inputs

This reconciliation was performed against the supplied documentation corpus rather than repository names alone.

Source artifacts:

```text
Rejean-McCormick.zip
sha256:f7966f5bcac72c14cd4be60d14e3d41676ccf42dd64e241f626574f6178aca44

github_repo_roots_final(1).json
sha256:7ecb5b2251e2d924bd5189294de48ed6bec8c4cbf05d2dd6cee2a6313d7e10cc
```

Observed discovery scope:

```text
documentation ZIP repositories/racines: 38
root-reference JSON repositories:        41
reference entries absent from ZIP:        3
```

The three root-reference entries not bundled in the ZIP are listed in the generated repository registry. Their absence from the ZIP is not interpreted as removal or deprecation.

See:

- [`../2-Technical-Reference/10-system/repository-corpus.md`](../2-Technical-Reference/10-system/repository-corpus.md)
- [`../generated/repository-corpus-2026-09-28.json`](../generated/repository-corpus-2026-09-28.json)

## Reconciliation rules

1. Owner repository authority beats ecosystem prose for owner-internal state/contracts.
2. A proposal is not promoted into adopted authority.
3. A candidate is not called a release until its release identity exists.
4. Local qualification is not silently promoted to cross-owner or production qualification.
5. Repository presence is not integration.
6. Copied reference documentation does not become a new contract owner.
7. Profile composition is not ecosystem membership.
8. Klassification/Layer Model is derived conceptual navigation and cannot override technical owner/contract maps.

## Corrections applied

### 1. Kristal: separate upstream candidate from adopted integration pin

The previous ecosystem summary could be read as if `5.0.0-rc.1` were also the latest owner candidate.

The supplied Kristal owner docs now show:

```text
upstream candidate:       5.0.0-rc.2
local conformance status: PASS (2026-09-17)
final local campaign:     22 PASS / 0 WARN / 0 BLOCKED / 0 FAIL / 0 ERROR
rc.2 Git tag:             pending in supplied owner docs
```

Interaction Kernel still pins Kristal `5.0.0-rc.1` through its accepted Kristal-pin ADR. Therefore the ecosystem integration pin remains rc.1 until an explicit downstream pin update occurs.

**Result:** maturity/status pages now show both facts instead of replacing one with the other.

### 2. SemantiK Architect: implementation state updated

The supplied owner `docs/22_IMPLEMENTATION_STATUS.md` states that the canonical SemantiK Architect v1 core is implemented.

The owner boundary remains narrow:

- communication planning and realization;
- lexical orchestration and exact binding;
- SA↔GF bridge contracts;
- RuntimeSet/capability/conformance semantics;
- deterministic faithful output.

It does not own upstream truth/content selection, civic decisions or business state.

Production rendering still requires admitted real RuntimeSet release artifacts.

### 3. SemantiK Runtime Orchestrator: explicit owner-preserving release boundary added

The supplied orchestrator architecture makes its ownership unusually clear:

- GF Wordbench owns GF compilation, language validation, PGF production and release evidence;
- SemantiK Architect owns SA↔GF, lexical, capability, conformance, RuntimeSet and semantic-faithfulness contracts;
- LevelUpDiag owns independent diagnostics;
- GF Observatory owns observation/evidence aggregation;
- the Runtime Orchestrator owns only sequencing, transactionality, integrity transfer, promotion, rollback and activation ordering.

Digital Ecosystem now records this as a boundary family without claiming ecosystem-wide qualification.

The supplied GF Observatory start-here snapshot marks implementation as **not implemented**, so no runtime Observatory claim is inferred.

### 4. UCKK-Moodle: authority and directional integration boundaries added

The supplied UCKK master doctrine defines:

```text
standalone_core
connected_konnaxion (optional)
```

Important authority locks now reflected in Digital Ecosystem:

- Moodle capabilities remain authoritative for UCKK permissions;
- UCKK-Moodle owns Assembly decisions;
- Konnaxion computes Smart Vote readings;
- Smart Vote is a non-sovereign reading, not the Assembly decision;
- external systems do not write Moodle source tables.

kOA-Linux separately owns canonical directional integration contracts for:

```text
publish_to_uckk
import_from_uckk
```

These are not bidirectional synchronization. Source and destination authorities remain separate and receipts/selection/acceptance are explicit.

### 5. UCKK current status added without overclaiming

The 2026-09-26 owner status reports a fresh Moodle 5.2.3+ local installation, multi-façade structure, course seeding and successful Mediatheque import. The same status still records a local HTTP-server conflict blocking final web validation.

The 2026-09-28 UCC refactor is an editorial/public-architecture change. It is not treated as a global UCKK engineering qualification.

### 6. kOA-Linux major-update package explicitly kept non-authoritative

`docs/KOALI_MAJOR_UPDATE_SPEC_2026-09/00-governance/00-status-and-authority.md` states that the package is a standalone major-update proposal that has not yet been merged into authoritative Koali/kOA documentation.

Digital Ecosystem now records this explicitly. Existing canonical kOA-Linux docs/contracts remain the authority until adoption.

### 7. Koali Spaces evidence kept split by scope

The generic Surface Layer has strong implementation/build/runtime evidence. The owner maturity report supports M4 for the generic host core.

However, the supplied current implementation snapshot still lists production onboarding of Konnaxion/Orgo/UCKK/SemantiK Architect as not implemented.

The existing real Konnaxion pilot evidence is therefore kept as pilot/integration evidence, not generalized into production multi-app hosting.

### 8. EncyKlopedia copied kOA references are not promoted to authority

The EncyKlopedia corpus explicitly says its `00_system/docs/kOA-reference/` subtree is a copied local reference subset and that the owner kOA/IK repositories remain authoritative.

The repository is catalogued for discovery, but its copied reference pages are not used to create a second IK/Kristal authority.

### 9. Repository inventory separated from system map

The supplied corpus includes many additional repositories: diagnostics, worlds/orchestration, domain applications, reference implementations, educational/operational tooling, language engineering and research/product work.

Digital Ecosystem now inventories those repositories, but does not automatically add them to the core system map.

A repository enters the authority or contract map only when an explicit owner boundary is supported by the supplied documentation.

## Claims intentionally preserved

The following previously established claims were not weakened by this reconciliation:

- Konnaxion↔Orgo IK `governance.decision.execute/1.0.0` qualification dated 2026-09-21;
- Orgo→Konnaxion `accountability.impact.publish/1.0.0` qualification dated 2026-09-21;
- kOA-Linux `kristal_runtime` ownership of Runtime Pack verification/active-state/activation+rollback receipts;
- kOA Node Agent's narrow privileged host-transition role;
- Koali Space activation is distinct from Runtime Pack activation;
- product-owned mutable state is not replaced by Kristal artifacts/materializations;
- current cited kOA-Linux sovereign base composition can exclude SemantiK Architect without removing it from ecosystem membership.

## Files updated by this reconciliation

- `README.md`
- `docs/index.md`
- `docs/1-Overview/index.md`
- `docs/2-Technical-Reference/00-overview/scope.md`
- `docs/2-Technical-Reference/10-system/authority-map.md`
- `docs/2-Technical-Reference/10-system/components.md`
- `docs/2-Technical-Reference/10-system/repository-corpus.md`
- `docs/2-Technical-Reference/40-integration/contract-map.md`
- `docs/2-Technical-Reference/40-integration/kristal-v5/index.md`
- `docs/2-Technical-Reference/40-integration/kristal-v5/pinned-dependency.md`
- `docs/status/current.md`
- `docs/status/index.md`
- `docs/generated/repository-corpus-2026-09-28.json`

The prior Klassification consolidation remains preserved: active classification material is derived/non-normative and the original v0.2 corpus remains archived for provenance.
