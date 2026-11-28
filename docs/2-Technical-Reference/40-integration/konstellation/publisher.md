# Konstellation Publisher — documentation integration

**Historical recorded state: 2026-10-27.** Descriptive documentation; not an operational admission or a deployment authorization.

- **Owning repository:** [`Rejean-McCormick/Konstellation-Publisher`](https://github.com/Rejean-McCormick/Konstellation-Publisher). Its public GitHub repository was reported/verified in the snapshot review; **the presence of the candidate code on that remote is not established**.
- **Declared local root:** `C:\mycode\Konstellation\Konstellation-Publisher`, derived from the path supplied by the operator. Local checkout existence and `origin` were not independently verified in this snapshot.
- **Code reviewed:** `0.2.0-alpha.1` local candidate supplied separately; do not infer publication from repository existence.
- **Responsibility:** Windows preflight interface for Konstellation 1.x sources, package preparation from an authorized allowlist, Docker/Compose template generation and local reports.
- **Deployment status:** remote publication is intentionally disabled. Windows UI qualification, VPS staging, TLS/Traefik routing, promotion and tested rollback remain open.

## Later offline observation — 2026-11-27

The supplied Publisher snapshot identifies `0.2.0-alpha.2`. Its local transaction simulator rehearses rollback; the remote entrypoint remains disabled. Its source allowlist includes Konstellation application code, including Koreograph, but not local `artifacts/` or reports. The current Konstellation snapshot is `1.0.0-rc.2`; the owner preflight still requires its matching `package-lock.json` (not present in the supplied ZIP). The SemantiK example remains disabled; profile/runtime pins must be verified independently before changing them. See [current integration observation](koreograph-2026-11-27.md). No live release or remote HEAD was established.

## Authority boundaries and gates

Publisher does **not** own Kristal data, semantic/epistemic authority or the approval to publish. A manifest, checksum, public repository, Compose profile or operator checkbox is not a substitute for independent authorization and qualification.

C1/C2/C3 gates, immutable receipts, independently qualified exact input and transactional deployment/rollback verification remain prerequisites before any remote activation or publication may be proposed. This page changes no frozen Kristal/IK contract, makes no production release claim, and authorizes neither GitSink nor any VPS operation.

See [repository inventory](../../../inventory/repositories.md) and [Konstellation integration](index.md).
