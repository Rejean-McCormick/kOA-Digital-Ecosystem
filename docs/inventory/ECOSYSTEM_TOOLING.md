# Documentation, diagnostics and audit — key kOA ecosystem repositories

This page groups the **documentation and observability hinge repositories** used to understand kOA. It is a separate companion-tool registry, not a new C0 product authority map. Machine-readable local paths and reported verification states are in [`companion-tools.v1.json`](companion-tools.v1.json).

## Companion repositories (outside the canonical 55-role C0 inventory)

| Tool | Observed local root | What it helps explain | Current evidence |
|---|---|---|---|
| **[kOA Doc Server](https://github.com/Rejean-McCormick/kOA-Doc-Server)** | `C:\mycode\DocServer\kOA-Doc-Server` (Git checkout); `C:\mycode\DocServer\kOA-Doc-Server-1.3.0` (installed app) | Cross-repository document navigation, AI documentation, RepoSurveyor profiles, wiki reading and provenance-aware ZIP export | GitHub repository identity verified; local checkout marker reported; **local `origin` and current HEAD not independently checked** |
| **[kOADiag](https://github.com/Rejean-McCormick/kOADiag)** | `C:\mycode\kOA_Digital_Ecosystem\kOADiag` (Git checkout) | Passive cross-repository boundary checks, C0 service ports, IK contracts, traces and scoped E2E evidence | GitHub repository identity verified; v5.7.0 source snapshot; **local `origin` and current HEAD not independently checked** |
| **[GitHub Audit](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit)** · [public dashboard](https://rejean-mccormick.github.io/kOA-Digital-Ecosystem-GitHub-Audit/) | `C:\mycode\kOA-Digital-Ecosystem-GitHub-Audit\kOA-D-E-GitHub-Audit` (operator-reported working root) | Local static observations, remote read-only GitHub observation and explicitly authorized aggregate publication | [2026-11-28 operating evidence](GITHUB_AUDIT.md); local `origin` and exact HEAD not independently checked |

The GitHub hyperlinks above resolve to verified repository identities. The Windows paths and `.git` markers were reported by the user, not independently inspected; neither local `origin` nor exact HEAD is verified. A repository link is **not** GitSink authorization or evidence of live integration. None of these tools is a source of canonical product state.

## How the hinge tools relate

```text
kOA Digital Ecosystem (C0: architecture, owners, declared portfolio)
   |                            |
   | read-only architecture     | declared contracts/boundaries
   v                            v
kOA Doc Server                kOADiag
   |                            |
   | local docs/wikis           | static observations, ports, evidence
   +-- RepoSurveyor             +-- optional owner-supplied evidence exports
   |   engineering profile      |
   +-- provenance ZIP           +-- scoped reports / private Audit handoff
   |
   +-- initkoa-docs — independent public documentation portal

Kompiler — separate semantic Context Pack builder (not Doc Server ZIP export)
GitHub Audit — reads the C0 inventory / pinned graph registry
   +-- LOCAL_OBSERVE: local static scan -> local reports
   +-- OBSERVE: scheduled GitHub metadata observation -> separate reports
   +-- explicit aggregate synchronization -> Pages deployment
   +-- dated graph publication -> frozen source revisions
```

## Authority and safety boundaries

1. **C0 is the architectural coordinator:** The [55-role owner inventory](repositories.md), [authority map](../2-Technical-Reference/10-system/authority-map.md), [status](../status/current.md) and [target portfolio](../target/PORTFOLIO.md) remain unchanged.
2. **Doc Server is a documentation reader and exporter:** It must not infer approval or release readiness from file existence, AI context text, profile generation, or a successful ZIP export. Wiki checkouts are separate from their owner repositories.
3. **RepoSurveyor is independent:** It generates a local engineering profile and an AI navigation brief from the code. These are observations, not a release qualification or maturity score.
4. **kOADiag is an observation engine:** A static finding, a responding health endpoint, or a scoped `EVIDENCE_COMPLETE` result does not certify all ecosystem edges. Network probes are opt-in; isolated transactional test-stack execution is separately authorized and can write to test data.
5. **Kompiler is not Doc Server:** Semantic Context Packs follow Kompiler's contracts; generic documentary ZIP exports do not become Kristal authority.
6. **GitHub Audit observes without certifying:** local scans do not mutate target repositories; remote observation is read-only and runs weekly. Explicit confirmation is required for local aggregate publication to the audit repository; Pages deployment is separate. Dated graph publication pins source revisions. Doc Server and kOADiag do not silently write, promote, or rewrite historic proof. See [audit operations and evidence](GITHUB_AUDIT.md).

## Recommended reading path

Start with [C0 README](../../README.md), [repository inventory](repositories.md), [authority map](../2-Technical-Reference/10-system/authority-map.md), and [current evidence status](../status/current.md). Next, use Doc Server to browse owner documents and RepoSurveyor profiles; use kOADiag to inspect diagnostic observations and their limitations. Use [GitHub Audit operations](GITHUB_AUDIT.md) and the [public dashboard](https://rejean-mccormick.github.io/kOA-Digital-Ecosystem-GitHub-Audit/) for repository observations. When a discrepancy arises, consult the owner repositories and the exact dated evidence instead of treating any UI as authoritative.

## Evidence status (2026-11-28)

The Doc Server and kOADiag GitHub identities were checked on 2026-11-22. GitHub Audit identity and [successful remote observation #5](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/actions/runs/46146239397) were checked on 2026-11-28. Metadata was observed for 55/55 repositories; security alert coverage remained unknown. The companion registry does not equate this observed count with exact canonical inventory membership. This is not a fresh scan of local checkouts, Git remotes, deployed integrations, or product maturity. The 55-entry C0 identity inventory, 53-role target portfolio, 53 archived code snapshots, historic proof, and graph contracts remain unchanged. The separate [wiki tooling overview](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Ecosystem-Tooling) is a derived navigation page, not an authority source.
