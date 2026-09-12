# Historical A014 — Orgo↔Konnaxion Runtime Validation Snapshot (2026-09-12)

**Status:** historical validation note — **architecture misalignment identified; not current acceptance evidence**  
**Normative for kOA:** NO  
**Secrets:** intentionally omitted

---

## Architecture correction (2026-09-12)

The original A014 fixture incorrectly modeled the decision authority/path as **UCKK/Assembly → Orgo**. The corrected architecture is:

```text
Konnaxion / eThikos
→ finalized decision
→ direct Konnaxion→Orgo handoff
→ Signal / Workflow / Case / Tasks
```

UCKK is an **optional publication/distribution surface**, not the decision authority and not a mandatory relay. Decisions for this flow are finalized in **Konnaxion/eThikos**.

As a result, the checkpoint results below remain useful as historical runtime/mechanics evidence, but they do **not** prove conformance of the corrected end-to-end decision path.

---

## Purpose

Capture the exact historical runtime stopping point and preserve evidence that may still be useful while the scenario is refactored to the corrected Konnaxion/eThikos → Orgo path.

---

## Historical checkpoint results

```text
T-14     PASS (historical fixture)
T-7      PASS (historical fixture)
T0-pre   PASS (historical fixture)
T0-post  PASS (historical fixture)
J3       PASS (historical fixture)
```

T0-post validated useful Orgo mechanics after aligning scenario work references with canonical work IDs and using legal Task state transitions. However, the inbound decision authority/path for these runs was wrong and must be replaced.

J30 request creation also remains useful as outbound transport evidence, but final Orgo→Konnaxion publication was not completed.

---

## Konnaxion runtime state

Validated local provider runtime:

```text
World                 uckk-a014
Release               r1
World status          READY
Promoted release      CURRENT
Bridge listener       127.0.0.1:8011
Provider runtime      Python 3.12 virtual environment
```

The bridge endpoint is authenticated; an unauthenticated health/request may return an authorization response while still proving the listener is reachable.

The World/Release bridge storage path was validated after fixing schema dependency and migration-ledger idempotency issues.

---

## Orgo runtime state

Validated local Orgo database/runtime facts:

```text
PostgreSQL host       127.0.0.1
PostgreSQL port       5432
Database              orgo_test
Database user         orgo_test
Worker                active with bridge configuration
API                   available on port 4000 when started
```

Passwords and full database URLs are intentionally not recorded here.

The Orgo worker is started with runtime-only Konnaxion bridge URL/token configuration. The generated bridge token must not be logged or persisted.

---

## J30 IntegrationOperation

Existing operation (do not recreate blindly):

```text
operation_id          6b8c5523-096e-4fc0-b6a9-be644240b497
provider              konnaxion
operation             publish
status                FAILED
error                 PROVIDER_UNCONFIGURED
idempotency_key       uckk:A014:impact:J30:v1
correlation_id        corr.uckk.A014.D009
```

Request metadata identifies the synthetic day-30 Impact:

```text
external_reference    impact:UCKK-A014:day30:v1
checkpoint            day_30
synthetic             true
```

The failure occurred before the Konnaxion adapter/provider was active.

---

## J30 outbox state

Existing outbox item:

```text
outbox_id             2def0f3a-f62c-4104-bb14-779d239d2237
type                  integration
status                DEAD
attempts              8
last_error            PROVIDER_UNCONFIGURED
aggregate_id          6b8c5523-096e-4fc0-b6a9-be644240b497
correlation_id        corr.uckk.A014.D009
```

This item is the one to redrive after confirming the provider/worker runtime is healthy.

---

## Correct resume procedure

Do **not** continue the old scenario as if only J30 redrive remained. The architecture must be corrected first.

Resume in this order:

1. Define/confirm the Konnaxion/eThikos finalized decision object/event that is authoritative for the scenario.
2. Implement or configure the direct **Konnaxion/eThikos → Orgo** authenticated handoff.
3. Remove UCKK/Assembly as a required decision authority/relay from the scenario and fixtures. UCKK may remain as an optional publication consumer.
4. Re-run the inbound path and verify Orgo receives/deduplicates the decision Signal and creates the expected governed work.
5. Revalidate the scenario checkpoints against this corrected authority path.
6. Then validate the outbound **Orgo → Konnaxion** Impact path using the existing IntegrationOperation/Outbox mechanics or a clean corrected-scenario operation.
7. Require terminal `SUCCEEDED` and exactly one Konnaxion business effect for the relevant idempotency identity.
8. Only then continue later follow-up checkpoints.

The existing failed/dead J30 operation may be inspected/redriven for transport debugging, but it is not sufficient acceptance evidence for the corrected end-to-end architecture.

No cross-system SQL mutation should be used.

---

## Known authentication distinction

The local PostgreSQL username/password are database credentials. They are **not** the Orgo application login credential for the E2E user. The Orgo API login uses the test organization/user credential configured for the browser/API test profile.

This distinction was confirmed when a database credential was rejected by the Orgo API with `UNAUTHENTICATED / Invalid credentials`.

---

## Acceptance criteria before later follow-up checkpoints

The corrected scenario must first prove:

```text
Konnaxion/eThikos finalized decision
→ direct Orgo handoff
→ expected Signal / Case / Tasks
```

Then the outbound impact path must prove:

```text
Orgo IntegrationOperation.status == SUCCEEDED
AND
Konnaxion business effect count for the idempotency identity == 1
```

Until both inbound and outbound conditions are true, later follow-up checkpoints remain blocked.
