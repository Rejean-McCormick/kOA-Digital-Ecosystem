# C0 local development ports — target allocation and migration

**Status: PROPOSED — 2026-11-19.** The machine-readable source of truth for the **target local-development allocation** is [`config/local-dev-ports.v1.json`](../../../config/local-dev-ports.v1.json). This is a C0 coordination decision proposal, **not** evidence that any owner code or machine has adopted the ports. Individual product repositories remain authoritative for runtime implementation. See [ADR-0014](../90-reference/adr/adr-0014-local-development-ports.md).

## Why this lives here

C0 coordinates **cross-owner port allocation** and records the proposed mapping, but it does not launch services, seize sockets, control a user's processes, or change product deployments. A port in this file is a **logical allocation**, not an operating-system reservation. The architecture owner maintains the registry; runtime owners validate and implement the assignments in their repositories.

## Allocation (target, not deployed)

All target TCP listener addresses use `127.0.0.1`, and the proposed registry pool is `21100–21199`. It sits inside the RFC 6335 **user/registered** range `1024–49151`, away from the common JavaScript defaults; **it is not reserved for kOA by IANA or by Windows**. Check each developer machine's occupied and excluded ports before adoption.

| Block | Target owner | Proposed endpoint(s) |
| --- | --- | --- |
| 21100–21109 | Local edge (optional) | Local reverse proxy in a later decision; not deployed |
| 21110–21119 | Orgo | Frontend `21110`, API `21111` |
| 21120–21129 | initkoa / HomePage | Site `21120`; audit **consumes** this port |
| 21130–21139 | Konnaxion | Frontend `21130` |
| 21140–21149 | Skope | Explorer `21140` |
| 21150–21159 | Ékole | Québec learner `21150`; teacher `21151`; OpsConsole `21152`; Pastorale learner `21153`, teacher `21154` |
| 21160–21169 | Integrations | Unallocated pending owner agreement |
| 21170–21179 | Koali | Unallocated pending owner agreement |
| 21180–21189 | Shared tools | Unallocated pending owner agreement |
| 21190–21199 | Spare | Unallocated |

The `services` records in the JSON file, not this table, are canonical. Do not assign an unallocated port by inferring from a block. An audit/test client doesn't need a listener and must use its target service port explicitly.

## Existing observed configuration (do not rewrite historical evidence)

The snapshot already documents Ékole Québec `8765/8766`, OpsConsole `8766`, Skope `8767`, Ékole Pastorale `8775/8776` ([source](../40-integration/skope-ekole/local-ports.md)). Ékole teacher and OpsConsole therefore **collide** when launched simultaneously on the same loopback host. A dated Orgo–Konnaxion validation report also mentions a `127.0.0.1:8011` bridge, without establishing a new owner-approved target port. These remain **legacy observations**; the new values are proposals until the respective repositories accept them.

## Invariants

1. **No automatic next-free-port fallback.** On an occupied target, fail with the expected service ID, configured port and information about the actual listener when available. Do not terminate a different app.
2. **One owner block and one target port per listener.** Do not allocate within another owner's block. Avoid sharing a port even if services are normally launched in different sessions.
3. **Loopback only by default.** Do not expose the dev listener on `0.0.0.0`, Docker host networks, LAN or public interfaces. Container-internal ports and production ingress are **outside this registry**.
4. **Identity before audit.** A port answering HTTP 200 is not proof of service identity. Consumers should request a stable, app-specific identity/health endpoint in their owner implementation; stop on mismatch.
5. **Single source for tooling.** Local dev scripts, tests, docs, Playwright, `.env.example`, launchers and development CORS/origin lists should derive from the same target assignment. Do not duplicate magic port constants across a repository.
6. **No OS-level reservations as a substitute for ownership.** The registry does not attempt Windows `excludedportrange`, a privileged bind, a firewall rule or host changes.
7. **Migration is owner-gated.** C0 can define the target; it cannot assert migration complete without owner commits, tests, and a verified runtime handshake.

## Commands (Python 3.11+, standard library)

From the Digital Ecosystem repository root:

```powershell
py -3 scripts/dev_ports.py validate
py -3 scripts/dev_ports.py list
py -3 scripts/dev_ports.py get initkoa-web --format url
py -3 scripts/dev_ports.py check --service initkoa-web
```

`check` tests whether IPv4 loopback can **temporarily bind** the configured port; it does not reserve it. A running correct service also appears occupied. It cannot identify every excluded range or guarantee the next `bind()` will succeed. For Windows diagnostics:

```powershell
Get-NetTCPConnection -State Listen | Where-Object { $_.LocalPort -ge 21100 -and $_.LocalPort -le 21199 } | Select-Object LocalAddress,LocalPort,OwningProcess
netsh interface ipv4 show excludedportrange protocol=tcp
netsh interface ipv4 show dynamicport tcp
```

Use `Get-Process -Id <PID>` to identify a process. Do **not** delete exclusions, stop services, or edit firewall rules automatically. For a local DNS/reverse proxy (`*.localhost`) start a separate owner-approved implementation proposal; the registry itself adds no listener or hostname.

## Adoption gate and updating the registry

Follow [owner-repository migration instructions](owner-port-migration.md). An allocation changes from `proposed` to `adopted` only when the corresponding owner supplies: the exact code revision, documented local startup, CI checks for fixed-port collision, an app identity check, and a coordinated audit or consumer that targets the assigned port. The **registry-wide** status becomes `adopted` only when every assigned service has met its gate. Never promote the legacy observations based merely on this design document.

The proposed values must be reviewed against actual IANA entries and machine-local conflicts before rollout. Relevant standards: [RFC 6335](https://www.rfc-editor.org/rfc/rfc6335), [IANA port registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml).
