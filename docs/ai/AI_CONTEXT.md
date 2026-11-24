<!-- kOA Doc Server · Docs IA · lot 01 · source datée, non-certifiante -->
# Documentation IA — kOA Digital Ecosystem (coordination C0)

**Périmètre :** Registre de coordination C0 : architecture cible, autorités, contrats, portefeuille, interfaces et état des preuves.

**Origine :** snapshot local documenté (20 novembre 2026, ou archive complémentaire). Les chemins et versions actifs sont à vérifier sur le poste avant toute modification.

**Autorité :** Les contrats et données d’un produit restent chez leur propriétaire. C0 maintient la coordination, pas les vérités sémantiques, décisions métier, publications ni qualifications finales.

## Méthode de travail IA

1. Identifier le produit propriétaire et le contrat adopté avant tout changement de carte C0.
2. Séparer architecture cible, observation locale, test qualifié, intégration et exploitation.
3. Conserver le statut `OBSERVED_SNAPSHOT`, `DOCUMENTED`, `USER_DECIDED`, `PROPOSED`, `BLOCKED` ou `UNKNOWN` selon la preuve réelle.
4. Générer les vues documentaires par les scripts du dépôt, sans les considérer comme sources normatives distinctes.

## Entrées et validations attestées par les sources

- `python scripts/validate_c0_coordination.py`
- `python scripts/render_repository_inventory.py --check`
- `python scripts/render_target_wiki.py --validate`

*Avant exécution, vérifier les préconditions locales et les effets possibles de la commande. Les commandes sont des points d’entrée documentés, pas des validations effectuées par cet overlay.*

## Frontières à ne jamais franchir

- Ne jamais substituer une capture ZIP à un commit HEAD vérifié ni à une preuve de déploiement.
- Ne jamais promouvoir une observation ou altérer les contrats historiques pour obtenir un PASS.
- Le générateur wiki prépare une vue; il ne confirme pas la publication GitHub.

## Incertitudes et limites explicites

- Le snapshot examiné fait référence à `docs/target/` mais n’en contient pas les pages. Vérifier leur existence sur le disque avant toute régénération.
- Les 55 rôles C0 sont un périmètre de coordination; des projets complémentaires peuvent vivre hors de cet inventaire.

## Sources à relire

- [`AGENTS.md`](../../AGENTS.md) — Consignes gouvernantes du dépôt — ne pas remplacer.
- [`README.md`](../../README.md) — Mission et avertissements de preuve.
- [`docs/2-Technical-Reference/10-system/authority-map.md`](../../docs/2-Technical-Reference/10-system/authority-map.md) — Autorités propriétaires.
- [`docs/2-Technical-Reference/40-integration/contract-map.md`](../../docs/2-Technical-Reference/40-integration/contract-map.md) — Frontières contractuelles.
- [`docs/inventory/README.md`](../../docs/inventory/README.md) — Inventaire des dépôts.
- [`docs/status/current.md`](../../docs/status/current.md) — Maturité et portée temporelle.
- [`scripts/render_target_wiki.py`](../../scripts/render_target_wiki.py) — Projection wiki C0 si sources présentes.
- [`scripts/validate_c0_coordination.py`](../../scripts/validate_c0_coordination.py) — Validateur C0.
