# 11 — Boundary traceability

**Status:** `TARGET_DESIGN`; these 26 design edges are not globally qualified.

| C0 boundary | Producer → consumer | Intended chain |
|---|---|---|
| `B-KNOW-01` | Skope → Mediatheque | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-02` | Mediatheque → Daat | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-03` | Daat → Kristal-Authoring-Kit | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-04` | diK → Kristal-Authoring-Kit | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-05` | Kristalizer → Kristal-Authoring-Kit | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-06` | Kristal-Framework → Kristal-Authoring-Kit | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-07` | Kristal-Authoring-Kit → KristalDiag | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-08` | Kristal-Authoring-Kit → Kristal-Manager | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-09` | Kristal-Manager → kristal-public | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-10` | Kristal-Framework → Kristal-Integration-Pack | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-11` | Kristal-Integration-Pack → Kompiler | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-12` | Kristal-Integration-Pack → EncyKlopedia | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-13` | kristal-public → Konstellation | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-KNOW-14` | Skope → Kristalizer | [FC-01](chains/FC-01-research-and-acquisition.md) |
| `B-CIVIC-01` | Konnaxion → Orgo | [FC-07](chains/FC-07-civic-deliberation.md) |
| `B-CIVIC-02` | Orgo → Konnaxion | [FC-07](chains/FC-07-civic-deliberation.md) |
| `B-CIVIC-03` | Konnaxion-Worlds → Konnaxion | [FC-07](chains/FC-07-civic-deliberation.md) |
| `B-EDU-01` | Kontexte → Kompose | [FC-10](chains/FC-10-education-design.md) |
| `B-EDU-02` | Kompose → Orgo | [FC-10](chains/FC-10-education-design.md) |
| `B-EDU-03` | Akor → Orgo | [FC-10](chains/FC-10-education-design.md) |
| `B-EDU-04` | Ekole → UCKK-Ops-Console | [FC-10](chains/FC-10-education-design.md) |
| `B-PLAT-01` | Koali-Control-Panel → kOA-Linux-Koali | [FC-16](chains/FC-16-platform-lifecycle.md) |
| `B-PLAT-02` | kOA-Linux-Koali → Koali-Spaces | [FC-16](chains/FC-16-platform-lifecycle.md) |
| `B-SEC-01` | Konfid → Daat | [FC-14](chains/FC-14-identity-and-policy.md) |
| `B-LANG-01` | SemantiK-Architect → SemantiK_Runtime_Orchestrator | [FC-12](chains/FC-12-language-runtime.md) |
| `B-LANG-02` | SemantiK-Architect → Spek | [FC-12](chains/FC-12-language-runtime.md) |

The proposed connections in the [boundary registry](../boundaries.v1.json) require exact producer and consumer consent and tests before claiming deployment. Unnamed third-party or agentic connections remain `TBD`.
