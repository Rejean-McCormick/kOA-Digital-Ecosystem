# Malkuth — runtime query and serving role

Malkuth is a conceptual runtime-consumption role, not an ownership grant.

## Responsibilities

- query/serve the active Runtime Pack through its Query Contract;
- apply Reader Policy;
- preserve source/validation/recognition/certainty labels;
- expose deterministic query errors and bounded behavior.

## kOA-Linux mapping

On kOA-Linux, `kristal_runtime` owns the active Runtime Pack record and runtime health. If a privileged host transition is needed, kOA Node Agent performs that narrow operation. Malkuth-like consumers observe/use the active selection; they do not create another activation authority.
