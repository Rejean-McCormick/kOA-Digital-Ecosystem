# Validation post-overlay — SmartDump du 23 novembre 2026 à 14:48

**Classification :** `OBSERVED_SNAPSHOT_NON_NORMATIVE`. Cette note s’ajoute à l’[audit initial](2026-11-23-documentation-drift.md) et à son [registre JSON](2026-11-23-documentation-drift.v1.json), **sans en réécrire les constats historiques**.

## Contrôle effectivement réalisé

- Source : `SmartDump_20261123_144857.zip` (13 dépôts ciblés).
- **22/22 fichiers documentaires** du multi-overlay v2 retrouvés à empreinte identique dans les dépôts applicatifs.
- **10/10 fichiers** du premier overlay C0 retrouvés à empreinte identique.
- La comparaison est **statique et binaire**; elle ne représente ni une exécution de tests applicatifs, ni une validation fonctionnelle, ni une autorisation de publication.

## Statuts de suivi (sans modification de la baseline d’audit)

| Identifiants | Observation post-overlay | Restant à faire |
|---|---|---|
| `DOC-003`, `DOC-004`, `DOC-005`, `DOC-006`, `DOC-007`, `DOC-008`, `DOC-010`, `DOC-011`, `DOC-013` | Fichiers de correction retrouvés identiques ; **correction documentaire observée dans la capture** | Faire l’acceptation fonctionnelle propre aux dépôts si nécessaire ; ne pas déduire une qualification interapplications |
| `DOC-012` — Kristal Manager | Cinq guides ajoutés identiques, mais neuf autres liens README toujours cassés à 14:48 | Overlay complémentaire de réconciliation de README préparé ; installation et nouvelle capture à confirmer |
| `DOC-014` — Ékole Pastorale | Navigation corrigée, trois pages Wiki sans équivalent vérifié | Retrouver les sources ou écrire des guides fondés sur les pratiques courantes |
| `DOC-001` — C0 | `docs/target/` absent du SmartDump mais observé sur GitHub `main` | Revoir le filtrage de capture, **ne pas** recréer le référentiel cible |
| `REL-001` — Konstellation | `package-lock.json` non capturé ; rapport d’installation : `UNCHANGED`; GitHub `main` présente le lockfile correspondant | Vérifier présence et intégrité directement dans le checkout, puis qualifier la release |
| `VER-001` | Compatibilité Koali Control Panel ↔ LevelUpDiag-Koali non testée | Qualification côté propriétaires, pas de relèvement automatique |
| `DOC-002`, `DOC-009`, `VER-002` — diK | **Différés** : mise à jour propriétaire en cours | Aucune intervention C0 ou autre overlay sur diK |

## Événement de suivi du 23 novembre

Le complément d’overlay **Kristal Manager + C0** corrige les références mortes et clarifie les limites d’exécution documentées. Ce complément est **préparé, pas encore démontré installé** par une nouvelle capture. Il modifie le README de Kristal Manager et des pages C0; il ne touche ni aux sources métier ni à `docs/target/`.

## Preuves et limitations

- Rapport initial de validation : `verification_overlays_koa_2026-11-23.md` (remis séparément dans la conversation).
- Registre machine-readable : [post-overlay-validation.v1.json](2026-11-23-post-overlay-validation.v1.json).
- La capture n’est pas un clone Git complet ; un fichier absent d’une archive n’est pas nécessairement absent sur disque.
- Aucun push, aucune migration, aucune synchronisation distante, aucune qualification C1/C2/C3 ni release n’est impliqué.
