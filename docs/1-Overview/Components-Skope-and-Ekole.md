# Skope & Ékole — nouvelles applications cartographiées

**Status: owner-snapshot reconciliation / proposal; no claim of production integration.**

## Skope

- **Owner:** Skope repository (generic repository `Skope`).
- **Role:** visually scopes a Wikidata-derived working skeleton for a future Kristal, preserving QIDs/PIDs and source assertions.
- **Capabilities evidenced:** local Python/SQLite index from supported Wikibase JSON formats, per-branch depth controls, directional/property filters, external convergence candidates with explicit acceptance, offline preview, reproducible *prototype* ZIP export.
- **Does not own:** EncyKlopedia's acquisition authority, Da’at mapping/ACL, Kristal canonical identity/validation, UCKK pedagogical decisions, publishing.
- **State:** operational local prototype with synthetic fixture; the user clone `D:` format and end-to-end v9/v10 qualification are **not established**.

## Kristal Iroquoiens — working model indépendant

- **Owner :** `Kristal-Iroquoiens-Working`, dépôt distinct de Skope.
- **Possède :** `Q110654499` en seed éditorial, ses recettes, archives documentaires, axes, mappings candidats, règles de revue culturelle et ses propres zones working/canon.
- **Relation :** appelle Skope par `--db` + `--recipe` externe. Aucun code Skope copié et aucun couplage entre l’UI générique et la racine iroquoienne.
- **Statut :** projet non canonique; démonstration synthétique; vraie extraction depuis le clone utilisateur `D:` non établie.

## Ekole

| Repository | Ownership in the November 12 snapshots |
| --- | --- |
| [Ekole](https://github.com/Rejean-McCormick/Ekole) | Curriculum-neutral engine, pack loader, learner portal and teacher editor. |
| [Ekole-Quebec](https://github.com/Rejean-McCormick/Ekole-Quebec) | Québec primary-school corpus with 202 candidate courses, six pathways and its own Kristal authoring sources. |
| [Ekole-Pastorale](https://github.com/Rejean-McCormick/Ekole-Pastorale) | Independent Catholic pastoral corpus with 32 prototype courses and seven pathways. |

Both content repositories provide their own `pack.json` using `ekole.content-pack/0.1`. Install them beside the `ekole` checkout and use the launcher of the desired pack. The [FC-11 design](../target/functional-chains/chains/FC-11-learning-delivery.md) describes the owner boundary. Editorial review and institutional or Moodle qualification remain open.

## Atelier Images

[Ekole-Atelier-Images](https://github.com/Rejean-McCormick/Ekole-Atelier-Images) is the illustration studio associated with Ekole. Its documented workflow covers scene prompts, palettes, batch generation using ComfyUI or Cloudflare, and review before export. The content repository owns the decision to adopt an illustration. See [FC-21](../target/functional-chains/chains/FC-21-creative-assets.md).

## Local coexistence

| Service | Default | Notes |
| --- | --- | --- |
| Ekole Québec learner portal | `127.0.0.1:8765` | Portal `/`, learner `/eleve/` |
| Ekole Québec teacher editor | `127.0.0.1:8766` | Started by the Québec pack launcher |
| Ékole OpsConsole | `127.0.0.1:8766` | Alternative/admin launch; **collides with Enseignant** when both use defaults |
| Ekole Pastorale learner portal and teacher editor | `127.0.0.1:8775` / `127.0.0.1:8776` | Started by the pastoral pack launcher |
| Skope | `127.0.0.1:8767` | Default in accompanying updated Skope repo; overridable |

The port convention is local documentation, **not** an OIDC/Koali/IK service registration or an assertion that every Ékole interface can run concurrently. The historical OpsConsole default overlaps the Québec teacher editor port.

See [contracts & evidence](../2-Technical-Reference/40-integration/skope-ekole/index.md) and [app inventory](../inventory/apps-skope-ekole.json).
