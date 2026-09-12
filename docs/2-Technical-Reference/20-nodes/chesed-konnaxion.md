# Chesed: Konnaxion

**Role:** Civic/public decision platform + connectivity/distribution boundary.
**Primary responsibility:** own Konnaxion/eThikos deliberation and finalized decision state, hand finalized decisions directly to Orgo when governed work is required, and provide the Konnaxion distribution facet for verified/pinned knowledge packs without mutating canonical truth.

## Responsibilities

* Own eThikos deliberation/decision state and finalized DecisionRecords.
* Push finalized Konnaxion/eThikos decisions directly to Orgo through an authenticated, idempotent machine boundary when operational work is required.
* Allow UCKK to consume/publish decisions optionally without making UCKK a required authority or relay.
* Fetch, cache, and serve **Runtime Packs** and related indexes/channels.
* Verify pack integrity **fail-closed** before activation (signatures, hashes, compatibility).
* Activate packs atomically and support deterministic rollback to a last-known-good or pinned version.
* Provide local query and retrieval interfaces over active packs (offline-first).
* Enforce distribution policy (channels, cohorting, pinning, revocation, downgrade prevention).
* Emit telemetry and operational signals (activation outcomes, verification failures, cache health).

## Inputs

* Release intent / rollout directives (channel, cohort, pin rules).
* Candidate pack artifacts and metadata (manifest + payloads + signatures).
* Verification keys and trust policy (key sets, allowed signers, required checks).
* Compatibility policy (supported schema versions, feature flags, migration rules).

## Outputs

* Active pack selection (the currently activated pack ID / version).
* Activation / rollback records (local operational evidence).
* Verification reports (why a candidate was rejected).
* Telemetry signals for Orgo (distribution health, failures, drift).

## Invariants

* **Fail-closed verification:** no activation unless all required checks pass.
* **Atomic activation:** a pack becomes active in one switch; partial activation is impossible.
* **Deterministic rollback:** given the same triggers and state history, rollback target selection is deterministic.
* **Downgrade prevention:** policy can forbid activating older/unsafe versions even if signatures are valid.
* **No truth mutation:** Konnaxion never edits canonical truth; it only distributes and serves verified artifacts.
* **Pinned determinism:** the same active pack + same query yields the same results (within the defined query interface).

## Failure modes

* Network/source unavailable (cannot fetch updates)
* Verification failure (signature mismatch, hash mismatch, untrusted signer)
* Compatibility failure (unsupported schema/features)
* Cache corruption / partial download
* Rollback loops (repeated activation failures)
* Key rotation mishandling (valid pack rejected due to stale trust set)

## Observability

* Pack fetch latency and failure rate
* Verification pass/fail counts by reason
* Activation success rate and time-to-activate
* Rollback frequency and triggers
* Cache utilization, corruption detection, disk pressure
* “Active pack drift” (unexpected active pack changes)

## Interfaces

### Upstream

* Distribution channels / artifact stores
* Orgo release controller (rollout directives)
* Key management service (trusted signers, revocations)

### Downstream

* Product runtimes (offline query, lookup, retrieval)
* UI services (navigation/search backed by pack indexes)
* Audit/telemetry pipeline (activation + verification evidence)

## Minimal contract (conceptual)

Konnaxion must expose:

* `get_active_pack()` → active pack identifier + metadata
* `activate(pack_ref, policy)` → success/failure + reasons
* `rollback(target_policy)` → selected target + evidence
* `query(interface, params)` → deterministic results over active pack
* `health()` → cache + verification + storage status

## Related docs

* `docs/2-Technical-Reference/40-integration/kristal-v4/koa-profile.md`
* `docs/2-Technical-Reference/50-operations/releases.md`
* `docs/2-Technical-Reference/50-operations/rollback.md`
* `docs/2-Technical-Reference/30-artifacts/konnaxion-state.md`

## Direct decision handoff to Orgo

For Konnaxion-owned civic/public decisions, the source event is a **finalized eThikos DecisionRecord**. The direct handoff pattern is:

```text
Konnaxion/eThikos DecisionRecord
→ authenticated/versioned handoff
→ Orgo Signal
→ WorkflowVersion
→ Case / Tasks
```

Smart Vote/EkoH may provide readings used inside the decision process. They are not the cross-system execution trigger by themselves. UCKK is an optional publication/distribution consumer and is not required between Konnaxion and Orgo.

Konnaxion never writes Orgo tables directly.

## Inbound Orgo publication bridge (current implementation profile)

In the current implementation, Konnaxion also exposes a provider-owned bridge for Orgo operational publication. This capability is distinct from Runtime Pack activation: it accepts an explicit Orgo integration envelope and applies the requested mutation through Konnaxion-owned domain/application services.

Current profile requirements:

- Provider operation: `publish` (with `distribute` reserved/allowlisted on the Orgo side where configured).
- World-scoped routing: publication is directed to the selected Konnaxion World and current/promoted Release context.
- Authentication: bearer token at the bridge boundary.
- Idempotency: the Orgo idempotency key is authoritative for duplicate suppression.
- Correlation: `X-Correlation-ID` follows the request across Orgo and Konnaxion.
- Ownership: Konnaxion performs its own mutation; Orgo never writes Konnaxion tables directly.
- Receipt semantics: return `succeeded` for terminal synchronous success, or `accepted` only when a final receipt/callback will later close the Orgo operation.

A repeated request with the same idempotency key MUST NOT create a second business effect.

See `docs/2-Technical-Reference/40-integration/orgo-konnaxion/index.md`.
