# Inventaire courant des dépôts kOA

For **all repository roles in the final-system design**, see the [target portfolio](../target/PORTFOLIO.md) and [target architecture](../target/architecture.md). This inventory remains an identity and declared-path registry, not evidence of integration.

Ce dossier décrit **ce qui figure actuellement dans le périmètre kOA**, sans mélanger l'inventaire avec des archives de relevés, des clones tiers ou des projets personnels.

- [`GRAPH_FOCUS.md`](GRAPH_FOCUS.md) — mode d’emploi des parcours focalisés.
- [`graph-focus.v1.json`](graph-focus.v1.json) — parcours focalisés typés, branches, contrats, preuves documentaires et niveaux de maturité (indépendants de la qualification des applications).
- [`repositories.json`](repositories.json) — **source de référence machine**, 53 dépôts retenus.
- [`code-snapshots-53.v1.json`](code-snapshots-53.v1.json) — manifestes SHA-256 des 53 archives de code hors Git et état d’audit `NOT_EVALUATED`.
- [`repositories.md`](repositories.md) — vue humaine générée du même périmètre.
- [diK/Kristalizer integration coordination](../2-Technical-Reference/40-integration/dik-kristalizer/README.md) — source-root evidence and the separate owner-boundary workstream.
- [`GITHUB_DESCRIPTIONS.md`](GITHUB_DESCRIPTIONS.md) — descriptions proposées pour les applications concernées.
- [`apps-skope-ekole.json`](apps-skope-ekole.json) — métadonnées applicatives Skope / Ékole.

## Règle de périmètre

Une entrée est conservée si elle appartient au portefeuille kOA déclaré, dispose d'une identité GitHub et d'un chemin local déclaré, et n'est pas explicitement exclue ou retirée. Les projets hors périmètre, les espaces de textes et d'expérimentation, les clones Wiki/tiers, les chemins introuvables et les relevés historiques ne font pas partie du registre.

Le statut de vérification repris dans chaque ligne décrit **la qualité de la dernière observation disponible** ; il ne certifie pas que le disque ou `origin` sont inchangés aujourd'hui. Une remote locale non vérifiée est signalée telle quelle, pas présentée comme vérifiée.

## Sécurité de synchronisation

L'inventaire est **descriptif, non prescriptif**. Une entrée `scope=PUBLIC` ne vaut ni autorisation GitSink ni preuve que le dépôt est prêt au push. La sélection explicite, le contrôle de la racine Git, la comparaison directe de `origin`, et les contrôles de publication s'appliquent au moment de toute opération.

Pour l'état des intégrations, voir [`../status/current.md`](../status/current.md) et la [carte d'autorité](../2-Technical-Reference/10-system/authority-map.md).
