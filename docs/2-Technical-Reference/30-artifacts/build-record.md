# Build Record v2 (kOA-owned coordination artifact)

A Build Record records **what happened during a reproducible build/compile workflow** without collapsing independent lifecycle axes.

It is kOA-owned operational evidence. Kristal artifact references remain opaque owner-defined references.

## v2 principle

The record must distinguish:

```text
compile_status
validation_status
recognition_status
publication_status
activation_status
```

A successful compile does not imply validation or recognition. A failed/rejected validation does not imply that no Working Exchange exists. Publication and activation are later transitions.

## Required evidence

A Build Record should answer:

- what inputs/source snapshots were used;
- which toolchain and exact Kristal pin were used;
- which Interaction Kernel Profile/correlation identity applied, if any;
- which stages executed and their operational outcomes;
- which Working artifacts were produced;
- which validation and authority-recognition records apply;
- which reference outputs were recognized, if any;
- which Runtime Packs were produced and their source status;
- whether publication/activation was requested or completed;
- stable reason codes for blocked/failed transitions.

## Kristal v5 mapping

Recommended opaque references include:

- Structured Epistemic State refs;
- Working Exchange refs;
- Validation Report refs;
- Authority Recognition refs;
- Reference Exchange refs;
- Runtime Pack Manifest refs;
- Reader Policy refs.

The Build Record does not re-declare the internal fields of those artifacts.

## Compatibility

Build Record v1 encoded a `PASS|FAIL` validation gate and a single `exchange_ref`. That model is deprecated. Readers may support v1 during migration, but new writers should emit v2.

Schema: `schemas/build-record.schema.json`.
