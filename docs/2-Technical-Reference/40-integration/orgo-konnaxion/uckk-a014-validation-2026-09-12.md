# UCKK A014 — Orgo↔Konnaxion Runtime Validation Snapshot (2026-09-12)

**Status:** historical validation note / resume point  
**Normative for kOA:** NO  
**Secrets:** intentionally omitted

---

## Purpose

Capture the exact validated stopping point of the UCKK A014 vertical slice so work can resume without reconstructing state from chat logs.

---

## Validated checkpoints

```text
T-14     PASS
T-7      PASS
T0-pre   PASS
T0-post  PASS
J3       PASS
```

T0-post was validated after aligning scenario work references with canonical work IDs and using legal Task state transitions.

J30 request creation was validated, but final Orgo→Konnaxion publication is not yet complete.

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

## Resume procedure

Do not inject J30 again as the first recovery action.

Resume in this order:

1. Keep/start the Konnaxion provider for World `uckk-a014`.
2. Keep/start the bridge-enabled Orgo worker against the same Orgo test database.
3. Start the Orgo API if required for the control-plane redrive action.
4. Authenticate with the Orgo application credential for the test organization/user (not the PostgreSQL credential).
5. Inspect the existing IntegrationOperation/outbox item.
6. Redrive the existing dead outbox item through the canonical Orgo API/manager action.
7. Wait for terminal `SUCCEEDED` (not merely `accepted`).
8. Verify **exactly one** Konnaxion Impact with the stable J30 identifiers.
9. Only after steps 7–8 pass, run J90.

No cross-system SQL mutation should be used to publish the Impact or repair delivery state.

---

## Known authentication distinction

The local PostgreSQL username/password are database credentials. They are **not** the Orgo application login credential for the E2E user. The Orgo API login uses the test organization/user credential configured for the browser/API test profile.

This distinction was confirmed when a database credential was rejected by the Orgo API with `UNAUTHENTICATED / Invalid credentials`.

---

## Acceptance criteria before J90

```text
Orgo IntegrationOperation.status == SUCCEEDED
AND
Konnaxion Impact count for idempotency/external reference == 1
```

Until both conditions are true, J90 remains blocked.
