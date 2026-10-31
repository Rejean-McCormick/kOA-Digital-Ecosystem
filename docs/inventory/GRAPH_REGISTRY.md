# Registre source du graphe kOA (v1)

Ce registre est **la source architecturale** consommée lors des publications datées de `kOA-Digital-Ecosystem-GitHub-Audit`. Il ne déploie ni ne qualifie une application.

- [`repositories.json`](repositories.json) : inventaire de référence (49 dépôts), **inchangé**.
- [`graph-registry.v1.json`](graph-registry.v1.json) : propriétaires et relations documentés; deux dépôts supplémentaires (`Kolor`, `Karacter`) restent **repérés, non admis** à l'inventaire de référence.
- Les descriptions de rôles sont issues de [`Components.md`](../1-Overview/Components.md). Les passages figurent dans [`Integration.md`](../1-Overview/Integration.md). Les relations indiquent `documented_passage` ou `proposed`, jamais `qualified` par défaut.

## Gouvernance

1. Modifier les données ici, dans le dépôt propriétaire du référentiel, en accompagnant toute nouvelle relation d'une source explicite.
2. Revoir les modifications en pull request. Une description et une proposition ne valent pas certification.
3. Publier ensuite dans GitHub Audit via le workflow manuel. La version publique conserve le commit source et ne change pas au gré des branches de développement.
4. Ne jamais inférer des permissions, contrats ou connexions depuis la seule ressemblance des noms de dépôts.

Cette première version est une **extraction prudente** des 12 propriétaires et 7 passages déjà représentés dans l'ancien graphe public. Elle ne prétend pas couvrir toutes les composantes des 51 dépôts.
