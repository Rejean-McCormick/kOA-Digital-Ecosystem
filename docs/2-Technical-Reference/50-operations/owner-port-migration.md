# Owner-repository rollout — local development port assignments

**Status: proposed migration plan, not completed changes.** The C0 registry is [`config/local-dev-ports.v1.json`](../../../config/local-dev-ports.v1.json). This document describes the needed code/docs/test adjustments in **other repositories**, which have not been modified by this coordination patch.

## Order and owners

| Sequence | Owner repository (from `docs/inventory/repositories.json`) | Proposed target | Remaining work |
| --- | --- | --- | --- |
| 1 | `HomePage/HomePage` (initkoa) | `21120` | Set Next.js dev and start to fixed port without fallback; align `.env.example`, launchers and audit target; validate kOA app identity |
| 2 | `Orgo/Orgo` | web `21110`, API `21111` | Inspect existing listeners first, then align frontend/API, CORS, proxy, docs, smoke tests; don't assume previous 3000/4000 claims are still true |
| 3 | `Konnaxion/Konnaxion` | web `21130` | Determine internal API/bridge owners; align launchers and browser origin with Orgo without changing production Docker profiles |
| 4 | `Skope/Skope` | `21140` | Update CLI/config default, documented launch, tests and optional environment overrides; fail on collisions |
| 5 | `Ekole/ekole`, `Ekole/ekole-quebec`, `Ekole/ecole-pastorale` | `21150`–`21154` | Split teacher and OpsConsole (currently both `8766`), update both packs, startup and local docs; verify simultaneous launch |
| 6 | `HomePage/docs-initkoa-org`, Koali and other clients | **No allocation yet** | Inventory actual listeners. Replace links to old ports and audit assumptions; allocate a new service only after owner review |

The bridge mentioned on `8011` is **observed historically**; its target remains unresolved. Do not unilaterally assign a new integration port without confirming its owner and contract.

## Owner checklist

For each owner repo, maintain one application-level port variable or import from the C0 registry as a read-only source during development. Check all of the following against the exact owner snapshot:

1. `package.json`, Makefile, Python CLI, compose development overrides and `.bat`/`.ps1` start scripts.
2. `.env.example`, API base URLs, callback/redirect URIs, CORS allowlists, webhooks and links in documentation.
3. Playwright/browser audit, local smoke tests, health/identity checks, VS Code debug launch configurations, CI environment.
4. Prevent Next/Vite/other frameworks from automatically selecting `port+1` when occupied (`--strictPort` for Vite; set an explicit port in Next and verify the bound service).
5. Verify an intentionally occupied port produces a **clear failure**, then an unoccupied port launches the correct app. Verify the expected identity endpoint and no cross-service false positive.
6. Record tests, exact owner revision, and date in a C0 migration evidence entry; then mark that service `adopted` in the registry.

No general-purpose script should kill another app, mutate machine reservations, change production port mappings or overwrite dirty repositories to force a rollout.

## Explicit non-goals

- This plan does not allocate all 55 repositories a port; many are libraries, tools, or static sites that do not need a local listener.
- It does not change public DNS, production VPS ingress/Compose, API contracts or runtime ownership.
- It does not assert `.localhost` routing or TLS is already configured.
