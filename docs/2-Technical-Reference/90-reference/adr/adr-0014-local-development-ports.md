# ADR-0014 — Coordinated local development port allocation

- **Status:** Proposed (C0, 2026-11-19)
- **Scope:** developer-host TCP loopback; not production/VPS/cluster ports
- **Authority:** C0 maintains coordination metadata; each product owns its runtime and adoption proof

## Context

HomePage/Orgo browser audits can accidentally target an unrelated dev service when multiple web applications rely on `localhost:3000`. The existing Skope/Ékole local port matrix also records a real candidate collision between Québec teacher and OpsConsole, both on `8766`. Dynamic port search suppresses the signal of a collision and can lead to misleading audit results.

## Proposed decision

Create a versioned, machine-readable target allocation in [`config/local-dev-ports.v1.json`](../../../../config/local-dev-ports.v1.json), using per-owner blocks in `21100–21199`. All proposed local HTTP listeners bind IPv4 loopback; development audit clients use a registered target, not a guessed port. Fail closed on collision. A per-service identity check is required to qualify consumer/test use. Track observed legacy ports separately; adopt only via exact owner revision evidence.

## Consequences and trade-offs

- C0 becomes the **coordination source of truth for target port numbers**, not an operating-system reservation service or deployable process manager.
- Target owners must migrate local configuration, scripts, documentation, integration tests and local origins. CI must identify collisions and mismatched targets.
- The IANA user/registered range supports local choices but does **not** reserve the block for kOA; actual service assignments and host conflicts require due diligence.
- Production exposed ports, Docker internal addressing, IPv6-specific listeners, `.localhost` proxying and cross-machine service discovery are separate decisions.
- Existing 8766 overlap remains until an Ékole owner migration lands; the C0 document alone does not fix it.

## Acceptance gates

1. Registry integrity checks and mutation tests pass.
2. Owner repositories adopt their exact target ports with explicit failure on collisions, documented setup, and service-identity checks.
3. A local test verifies simultaneous startup of intended coexisting apps and rejects a wrong-app audit target.
4. A new ADR revision records cross-owner evidence before promoting this proposal to adopted.

See [operations policy](../../50-operations/local-development-ports.md) and [migration plan](../../50-operations/owner-port-migration.md).
