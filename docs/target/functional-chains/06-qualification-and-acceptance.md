# 06 — Qualification and acceptance

**Status:** `TARGET_DESIGN`.

Levels: `TARGET_DESIGN`, `SOURCE_OBSERVED`, `OWNER_TESTED`, `CROSS_OWNER_QUALIFIED`, `RELEASE_AUTHORIZED`, `DEPLOYED_OBSERVED`. Never promote a level merely because a code file or CI workflow is present.

Every boundary requires exact revision pins, positive/negative schema fixtures, authorization denial, source integrity checks, changed-intent replay rejection, pending-versus-terminal reconciliation, private/public classification, dependent-service failure and rollback.

A full composed chain is qualified only when all its required producer/consumer pairs pass together on the selected environment/profile. The 53 snapshot hashes only prove offline bytes were captured.

[Functional chain index](README.md) · [Repository coverage](05-repository-coverage.md) · [Acceptance](06-qualification-and-acceptance.md)
