# Ecosystem artifacts

Artifacts remain authoritative at their owning system/component.

| Family | Owner | Examples |
|---|---|---|
| Civic/governance | Konnaxion | DecisionRecord, consultations, readings |
| Operational/work | Orgo | Signal, WorkflowVersion, Case, Task, IntegrationOperation |
| Epistemic/reference | Kristal | Structured Epistemic State, Working Exchange, Validation Report, Authority Recognition, Reference Exchange, Reader Policy, Runtime Pack manifest |
| Platform release | kOA-Linux | Release Set; registered channel/artifact contracts; lifecycle receipts |
| Runtime Pack local state | `kristal_runtime` | verification record, active Runtime Pack record, activation/rollback receipts, runtime health |
| Privileged node lifecycle | kOA Node Agent | privileged-operation/activation/recovery receipts under its contract |
| Presentation | Koali Spaces | Space definition, presentation/runtime registration, surface descriptors and Space lifecycle state |
| Cross-system reference | source + adopted integration contract | ArtifactRef, ExportManifest or equivalent source-owned references |
| Ecosystem build evidence | kOA integration layer | Build Record, when used as non-authoritative correlation/reproducibility evidence |

## Three storage/artifact layers

kOA distinguishes three layers that must not be collapsed:

```text
1. Operational state
   mutable, transactional, product-owned
   Orgo / Konnaxion / other owner database
        │
        │ immutable source-owned export/snapshot
        ▼
2. Kristal knowledge artifact
   content-addressed epistemic representation
   Working / Reference Exchange and related artifacts
        │
        │ deterministic derivation
        ▼
3. Query/runtime materialization
   Runtime Pack tables/indexes/columnar data/read-only database profile
   non-authoritative and rebuildable
```

A record does not become Kristal-owned merely because knowledge is derived from it. For example, a Konnaxion DecisionRecord remains Konnaxion-owned; a Kristal assertion derived from a pinned DecisionRecord export is a separate Kristal-owned knowledge artifact with provenance back to the source.

A Runtime Pack materialization must not become a second writable source of truth. If a query database or index is included, deleting and deterministically rebuilding it from the referenced Kristal source artifact must preserve the authoritative knowledge state.

## Release Set

Digital Ecosystem uses the **kOA-Linux Release Set** as the platform release compatibility artifact rather than inventing a competing Release Record authority. Release Sets bind tested-compatible versions across independent `system`, `services`, `governance` and `knowledge` channels.

## Runtime Pack activation state

Digital Ecosystem does **not** define a new authoritative Runtime Activation State for kOA-Linux. The active Runtime Pack state is owned by `kristal_runtime`; privileged node operations can be executed by kOA Node Agent where the active profile requires them.
