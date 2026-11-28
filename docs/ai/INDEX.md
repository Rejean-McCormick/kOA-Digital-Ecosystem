<!-- kOA Doc Server · Docs IA · lot 01 · source datée, non-certifiante -->
# Documentation IA — kOA Digital Ecosystem (coordination C0)

**Périmètre :** Registre de coordination C0 : architecture cible, autorités, contrats, portefeuille, interfaces et état des preuves.

**Origine :** snapshot local documenté (20 novembre 2026, ou archive complémentaire). Les chemins et versions actifs sont à vérifier sur le poste avant toute modification.

**Autorité :** Les contrats et données d’un produit restent chez leur propriétaire. C0 maintient la coordination, pas les vérités sémantiques, décisions métier, publications ni qualifications finales.

## Ordre de lecture conseillé à un agent

1. [`AGENTS.md`](../../AGENTS.md) — Consignes gouvernantes du dépôt — ne pas remplacer.
2. [`README.md`](../../README.md) — Mission et avertissements de preuve.
3. [`docs/2-Technical-Reference/10-system/authority-map.md`](../../docs/2-Technical-Reference/10-system/authority-map.md) — Autorités propriétaires.
4. [`docs/2-Technical-Reference/40-integration/contract-map.md`](../../docs/2-Technical-Reference/40-integration/contract-map.md) — Frontières contractuelles.
5. [`docs/inventory/README.md`](../../docs/inventory/README.md) — Inventaire des dépôts.
6. [`docs/status/current.md`](../../docs/status/current.md) — Maturité et portée temporelle.
7. [`scripts/render_target_wiki.py`](../../scripts/render_target_wiki.py) — Projection wiki C0 si sources présentes.
8. [`scripts/validate_c0_coordination.py`](../../scripts/validate_c0_coordination.py) — Validateur C0.

## Documents produits par cet overlay

- [`AI_CONTEXT.md`](AI_CONTEXT.md) — limites, parcours et points de contrôle.
- `PROFIL_INGENIERIE.md` — produit **sur demande** à partir d'un scan RepoSurveyor du code local; ce fichier n'est pas fourni par le lot rédactionnel.
- `AGENTS.md` à la racine — consignes de dépôt existantes conservées ou nouvelles si elles n'existaient pas.

## Règles transversales

- Une capture documentaire n'établit ni conformité, ni maturité, ni disponibilité en production.
- Ne pas remplacer contrats, ADR, README ou preuves propriétaires par cette aide de navigation.
- Nouveau Framework v11 : lire le profil effectivement adopté; ne jamais imposer une migration par défaut.

## Procédure opérationnelle proposée (lot 04)

- [`OPERATIONS.md`](OPERATIONS.md) — parcours concret et points de contrôle à vérifier avant tout effet.

## Multilingual work context (2026-11-26)

- [C0 multilingual coordination](../../docs/2-Technical-Reference/40-integration/multilingual/README.md) — dated owner reconciliation, language scope matrix and open gates.

## Konstellation coordination (2026-11-27)

- [Current offline integration observation](../2-Technical-Reference/40-integration/konstellation/koreograph-2026-11-27.md) — owner contracts, Koreograph and Publisher boundaries.
