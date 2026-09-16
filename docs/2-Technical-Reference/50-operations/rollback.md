# Operations — Runtime Pack rollback

For kOA-Linux, `kristal_runtime` owns the last-valid/current Runtime Pack state and rollback result.

Rollback verifies that the target is valid/compatible/allowed and atomically restores the declared last valid runtime state. If a privileged host mutation is necessary, kOA Node Agent executes that narrow authorized transition.

Record the rollback through the owner component's receipt/evidence paths. Do not create a parallel Digital Ecosystem Runtime Activation State.
