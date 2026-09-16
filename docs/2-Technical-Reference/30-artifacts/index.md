# kOA-owned and referenced cross-system artifacts

The ecosystem should prefer owner-system artifacts over duplicate integration-layer authorities.

## Active

- **Build Record** — optional ecosystem correlation/reproducibility evidence; never replaces owner artifacts.
- **kOA-Linux Release Set** — authoritative platform compatibility artifact across `system`, `services`, `governance`, and `knowledge` channels.
- **Kristal Runtime owner records** — `runtime_pack_verification_record`, `active_runtime_pack_record`, activation/rollback receipts and runtime health, owned by `kristal_runtime`.
- **kOA Node Agent receipts** — privileged node-local operation/activation/recovery evidence when applicable.
- **Koali Space artifacts/state** — presentation composition and Space lifecycle owned by Koali Spaces.

## Compatibility-only

- `Release Record v2` — deprecated as an authority; may be retained only as a projection that references Release Set/owner receipts.
- `Runtime Activation State` — deprecated for kOA-Linux; do not create a parallel active-state authority beside `kristal_runtime`.
- `Konnaxion State` — historical compatibility artifact from the older universal-Konnaxion activation model.

Kristal artifacts are referenced according to the pinned Kristal v5 contracts and are not redefined here. Source product databases are not ecosystem artifacts and remain authoritative at their product owner. Immutable source exports/snapshots may be referenced by ArtifactRef/ExportManifest for compilation and provenance.

Runtime Pack tables/indexes/columnar data/read-only database representations, when present under an adopted profile, are **derived query materializations** rather than new authoritative artifacts. They must remain tied to the source Kristal artifact and be rebuildable without changing authoritative knowledge state.
