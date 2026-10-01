# Integration

kOA integrations preserve owner boundaries and use explicit versioned contracts.

## Current integration layers

- **Owner contracts** remain authoritative inside each product/platform.
- **Interaction Kernel** carries selected cross-system envelopes/Profiles only where explicitly adopted.
- **EncyKlopedia** hands off immutable acquisition evidence and referent candidates through `encyklopedia.corpus-harvest-handoff/1.0.0`.
- **Da’at** maps acquisition/operational inputs into Kristal-native contracts without taking source or Kristal authority.
- **Kristal** owns referent identity semantics and Kristal v6 knowledge/state artifacts; the active baseline is Standard `6.0.0` + Referent Registry `1.0.0`.
- **UCKK / Univers-Cité** consumes pinned Kristal artifacts through `uckk.univers-cite-projection/1.0.0`; Moodle/glossary/media views are rebuildable projections.
- **kOA-Linux Release Sets** coordinate compatible platform artifact versions across release channels.
- **Koali Spaces** composes presentation surfaces without taking product authority.
- **UCKK interchange with kOA-Linux** remains directional (`publish_to_uckk`, `import_from_uckk`) and does not create a shared database.
- **SemantiK / GF release integration** uses owner-preserving external contracts; sequencing does not transfer grammar, semantics or diagnostic authority.

## Key non-confusions

```text
source acquisition            ≠ knowledge validation
referent candidate            ≠ authority-recognized referent
Kristal artifact              ≠ UCKK projection state
IK Profile                    ≠ kOA-Linux internal contract unless adopted
Release Set                   ≠ Kristal validation/recognition
Space activation              ≠ Runtime Pack activation
kOA Node Agent operation      ≠ active Runtime Pack ownership
UCKK import/publication       ≠ shared database or background sync
SemantiK release sequencing   ≠ ownership of GF/SA semantics
```

See the [contract map](../2-Technical-Reference/40-integration/contract-map.md) and [knowledge projection boundary](../2-Technical-Reference/40-integration/knowledge-projection.md).

## v6 actionability rule

Kristal may describe actionability, but an `automatic` classification is not cross-system execution authority. Automation still crosses the explicit owner contract and admission boundary.
