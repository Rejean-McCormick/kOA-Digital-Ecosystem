# Local-dev ports: C0 wave 2 (proposed)

Source of truth: `config/local-dev-ports.v1.json`. This proposal is for **Windows-host development** only.

- Konnaxion standalone: web `21130`, Django API `21131`.
- Konnaxion local Agent `21132`, local Capsule Manager `21133`.
- Konnaxion Koali-managed isolated instance: web `21134`, API `21135`.
- Orgo standalone: web `21110`, API `21111` (wave 1).
- Orgo Worlds: web `21112`, API `21113`.
- Orgo Koali-managed isolated instance: web `21114`, API `21115`, PGlite `21116`.
- Koali Spaces: `21170`; Koali Control Panel is a desktop manager, not a web listener.

## Interaction Kernel boundaries

- Orgo -> Konnaxion uses the Konnaxion API endpoint `/api/integrations/ik/konnaxion/interactions/` on host `21131`.
- Konnaxion -> Orgo uses `/api/v3/ik/interactions` on host `21111`.
- IK is an integration protocol, **not** a separate web process to assign a third port.
- For an Orgo process inside Docker, `localhost` means **the container**. Host-side Konnaxion may be reachable via `host.docker.internal:21131` only if Konnaxion listens on an accessible interface and firewall rules permit access. This must be checked, not assumed.
- Never relax token, org-scope or HTTPS rules just to make a port reachable.

Preserve internal Docker container ports such as `3000`, `4000`, `8000`, `5000` and remote droplet Agent `8765`; the registry addresses host-local developer listeners, not deployments. Keep production and secrets out of the patch.

**Conflict rule**: fail with diagnostic; do not silently fall back to another port or terminate unrelated applications.
