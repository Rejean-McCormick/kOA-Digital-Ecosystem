# Wiki synchronization — 2026-10-27 source snapshot

**Scope:** the local `kOA-Digital-Ecosystem` repository snapshot and locally collected sibling `kOA_Digital_Ecosystem.wiki` pages. The repo snapshot contains 213 listed files (plus its embedded snapshot index). This report is **documentation reconciliation, not a source-code audit of other kOA systems**, a remote GitHub HEAD verification, or a release approval.

## What changed in the wiki

- Retired `Status.md`'s claim that **2026-09-28** is the current alignment baseline; preserved `Status-2026-09-28.md` as history.
- Distinguished Kristal v5 RC history, the frozen Kristal Standard **6.0.0** + IK **2.0.0** knowledge lane, and the later v9 semantic / v10 GitHub hosting coordination proposal.
- Corrected the Konnaxion↔Orgo IK boundary to the **locally qualified** integrated evidence reported on **2026-09-21**, without implying real production deployment.
- Added navigation to the **2026-10-08 C0** workstreams, **2026-10-12 v10** harmonization, **2026-10-18 Tandem VPS/Capsule Agent** target, Skope/Ékole owner-repository boundaries, and **2026-10-27 Konstellation Publisher** candidate.
- Kept source acquisition, epistemic validation, platform release, runtime activation, and consumer projection as separate authorities.

## Authority and evidence table

| Topic | Repository evidence | Interpretation and gate |
|---|---|---|
| Cross-system maturity | [`current.md`](current.md) | Specified, implemented, tested, integrated, and production-proven must remain distinct |
| Konnaxion ↔ Orgo | [`2026-09-21-konnaxion-orgo-ik-e2e-qualification.md`](2026-09-21-konnaxion-orgo-ik-e2e-qualification.md) | Qualifies the scoped local IK flow; not a production deployment |
| Frozen knowledge lane | [`../2-Technical-Reference/40-integration/knowledge-projection.md`](../2-Technical-Reference/40-integration/knowledge-projection.md) | Historical/pinned v6+IK v2+UCKK baseline, not a claim of current v10 runtime |
| C0 and v10 | [`../2-Technical-Reference/40-integration/orchestration-c0/README.md`](../2-Technical-Reference/40-integration/orchestration-c0/README.md), [`../2-Technical-Reference/40-integration/kristal-v10-alignment/README.md`](../2-Technical-Reference/40-integration/kristal-v10-alignment/README.md) | Separate coordination records; remote pins, independent E2E and publication gates open |
| Tandem VPS | [`../2-Technical-Reference/40-integration/tandem-vps-capsule-agent/README.md`](../2-Technical-Reference/40-integration/tandem-vps-capsule-agent/README.md) | Target selected by operator; local tests reported; Lot1C/real VPS not qualified |
| Skope / Ékole | [`../2-Technical-Reference/40-integration/skope-ekole/index.md`](../2-Technical-Reference/40-integration/skope-ekole/index.md) | Standalone features described; cross-system adapter/handoff remains proposed |
| Konstellation Publisher | [`../2-Technical-Reference/40-integration/konstellation/publisher.md`](../2-Technical-Reference/40-integration/konstellation/publisher.md) | Local package/preflight candidate only; no remote publication grant |

## Maintenance rule

1. Treat owner contract/test/release evidence as authoritative; the wiki is a **secondary explanation**.
2. Update dated status pages only to correct factual errors within their **own date**; otherwise add a newer page and link to the archived snapshot.
3. Cite a concrete repository path for every changed version/qualification claim. A documented schema or tested-local tool does **not** establish E2E deployment or publication.
4. Do not alter frozen historical contract JSON to match newer proposals; keep C0/v10 coordination separately versioned.
5. Root `README.md` and wiki pages use English, UTF-8, LF newlines and **no NUL bytes**. Do not add an extra trailing blank line to root README.

**Limits:** Snapshots do not establish current remote HEAD, GitHub Wiki contents, owner signatures, public publication permission, runtime deployment or the complete source of other owner repositories.
