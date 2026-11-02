# kOA Graph — parcours Koali → Écosystème → UCKK

Ce parcours représente **Koali comme la vision de composition d’un écosystème de systèmes autonomes** : ni Koali Spaces, ni kOA-Linux, ni UCKK ne sont propriétaires de tous les sous-systèmes kOA. Chaque application conserve ses règles, son état et ses preuves.

## Ligne centrale

1. **Koali** — vision globale et parcours d’usage. Cette entrée est un **nœud conceptuel**, pas une application monolithique ni une nouvelle API.
2. **Ressource approuvée** — contenu ou projection choisi par son propriétaire, avec droits, audience, consentement et version explicites.
3. **Médiathèque kOA** — source locale privée par défaut, avec références, versions, intégrité et provenance.
4. **Passerelle kOA-Linux** — passage de publication entre domaines et autorisations indépendantes; `publish_to_uckk` est un contrat d’opération, **pas une preuve de déploiement qualifié**.
5. **UCKK** — Moodle et Médiathèque externes; objets de destination distincts, pas de base commune.
6. **Reçu / suivi** — suivi de l’envoi accepté et, séparément, retrait, correction ou nouvelle publication lorsque les droits le permettent.

## Branches et limites

- **Konnaxion** : apprentissage, participation, délibération et décisions; son état appartient à Konnaxion.
- **Orgo** : tâches, workflows et coordination; ses actes opérationnels restent sous son autorité.
- **Kristal / Authoring Kit** : identités, connaissance, auteur et provenance selon les versions compatibles; aucune publication UCKK implicite.
- **SemantiK Architect / Spek** : formulation et composition éditoriale facultatives; Spek peut fonctionner sans SemantiK.
- **Koali Spaces** : composition d’interfaces facultative, pas un runtime obligatoire ni le propriétaire de l’ensemble.
- **Politique / consentement** : admission et publication sont indépendantes de la simple lecture ou du stockage.
- **`import_from_uckk`** : opération distincte d’import d’une ressource choisie; pas de synchronisation bilatérale automatique.
- **Révision / republication** : scénario d’usage composé, **non vérifié comme intégration opérationnelle de bout en bout**.

## Provenance documentaire

Le parcours s’appuie sur les documents publics normatifs :

- [`Components.md`](../1-Overview/Components.md) et [`Integration.md`](../1-Overview/Integration.md) : propriétés, autonomie et échange UCKK.
- [`contract-map.md`](../2-Technical-Reference/40-integration/contract-map.md) : échanges kOA/UCKK et périmètre des contrats.
- `kOA-Linux-Koali/docs/07-security/17-cross-domain-publication.md` : publication inter-domaines gouvernée.
- `Mediatheque/README.md` et `Koali-Spaces/README.md` : limites du stockage et de la composition des surfaces.
- `Spek/docs/STANDALONE_AND_CONNECTORS.md` : édition autonome et entrées facultatives.

Les trois archives fournies pour ce travail éclairent le **modèle éditorial** : `koa-linux-wiki (2).zip`, `36 usage scenarios en(4).zip`, `120KoaliScenarioMosaicen(4).zip`. La wiki rappelle qu’UCKK est externe et que `publish_to_uckk` et `import_from_uckk` sont deux opérations distinctes. Les scénarios `SCN-113` (rapport annuel vivant) et `SCN-120` (média devenu désuet après modification de source) décrivent des possibilités **COMPOSED · runtime UNVERIFIED**. Ces scénarios n’établissent pas qu’un mécanisme automatique de suivi/republication est déployé.

Le graphe affiche donc des statuts `documented`, `optional` ou `candidate`, et **ne transforme aucune capacité projetée en qualification de production**.

## Mise en ligne

Le fichier `docs/inventory/graph-focus.v1.json` appartient au dépôt d’architecture. GitHub Audit le collecte sur un commit figé et le convertit en `docs/data/focus-paths.json` pendant une publication `selected` qui inclut `kOA-Digital-Ecosystem` (ou `all`). Le site affichera automatiquement ce quatrième parcours sans changement de son JavaScript.
