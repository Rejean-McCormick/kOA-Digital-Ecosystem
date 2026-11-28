# kOA GitHub Audit — companion observation and public dashboard

**[Open the public kOA audit dashboard](https://rejean-mccormick.github.io/kOA-Digital-Ecosystem-GitHub-Audit/)** · [Owner repository](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit) · [Weekly observation workflow](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/actions/workflows/observe.yml)

## Role and ownership

GitHub Audit is an independent cross-cutting engineering companion alongside kOA Doc Server (documentation) and kOADiag (diagnostics). C0 owns the architectural inventory and graph registries; the Audit owner maintains its scanner, report formats, synchronization and Pages workflows. The public dashboard is a derived reading surface, not a product owner, release grant, certification engine or source of canonical maturity. The 55-entry C0 inventory, historical ledgers, target design, graph contracts and GitSink authority remain unchanged.

## Operating modes and publication boundaries

| Mode | Input | Output and boundary |
|---|---|---|
| `LOCAL_OBSERVE` | Local Windows repositories, operator-selected scan root | Read-only static observations and local reports. No execution or mutation of audited repositories. |
| `OBSERVE` | C0 inventory and public-owner discovery through authenticated GitHub API | Read-only remote observations; sanitized workflow artifacts with 14-day retention. Distinct from local observations. |
| Aggregate refresh | Explicitly confirmed local scan and report regeneration | Only allowlisted aggregate dashboard data synchronized to the audit repository; Pages deployment requested separately. No raw local reports, paths, secrets or source code published. |
| Dated graph publication | Source graph registries pinned to exact revisions | Frozen public graph views; no live inference of contracts or maturity. See [graph registry](GRAPH_REGISTRY.md) and [focused paths](GRAPH_FOCUS.md). |

The Windows launcher offers **Scanner, actualiser et publier** (scan, refresh and publish). The equivalent explicit CLI operation, from the audit working directory, is `python -m koa_audit dashboard-refresh --root "C:\mycode" --confirm-publish`. It is a publication command, not an unattended local scan. GitHub CLI authentication and publication permissions are required; any deployment approval remains separate.

Remote observation is scheduled every Monday at 08:27 UTC (`27 8 * * 1`), with manual dispatch also available. Scheduling is best effort. The workflow uses a dedicated read credential stored in GitHub Actions Secrets, or an appropriately scoped GitHub App installation token; credentials must never enter source files, logs or reports. A successful run does not automatically publish a new dashboard or change C0's inventory. Artifact visibility follows repository access; do not treat artifacts from a public repository as a private storage boundary.

## Dated operating evidence — 2026-11-28

| Observation | Evidence and limits |
|---|---|
| Local scan and aggregate synchronization | Operator-reported Windows execution; local origin and exact checked-out revision not independently inspected. |
| Public Pages deployment | [Successful run 46097058483](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/actions/runs/46097058483); deployment confirmed separately from local scanning. |
| Permanent CLI and UI regression correction | [Merged PR #6](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/pull/6); audit owner commit [`ab2e61d`](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/commit/ab2e61d11c037cd9080d84590cf0a5dac8e5a344). Public Windows suite: 155 tests passed, 47 private-evidence tests skipped. No claim of a complete private-evidence suite. |
| Remote observation | [Successful run #5 / 46146239397](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/actions/runs/46146239397), at audit owner commit `ab2e61d11c037cd9080d84590cf0a5dac8e5a344`; duration 1 min 04 s; artifact produced. |
| Metadata coverage | 55 in observed scope, 55 observed, 0 without metadata. The scope includes public-owner discovery and is not proof of exact identity equivalence with the 55-entry C0 inventory. |
| Security coverage | CodeQL, Dependabot alerts, code scanning alerts and secret scanning alerts: unknown for all 55 repositories. Observed lower bound zero is not a verified zero-alert count. |
| Maintenance | Nonblocking Node.js 20 action deprecation warning in run #5; modernization remains owner maintenance. Windows scheduled local scans were not configured by this evidence. |

Evidence status: `DOCUMENTED` for the operating boundaries; dated workflow observations are scoped operational evidence for the audit tool only. Future scheduled runs, additional permissions, owner integrations and private qualifications remain unverified until independently observed. Successful observation does not imply absence of vulnerabilities, product readiness or deployment of the final-system architecture.

## Related central references

- [Companion tooling map](ECOSYSTEM_TOOLING.md) and [machine-readable companion registry](companion-tools.v1.json)
- [Canonical repository inventory](repositories.json) — unchanged
- [Current evidence and maturity map](../status/current.md)
- [C0 authority map](../2-Technical-Reference/10-system/authority-map.md)
