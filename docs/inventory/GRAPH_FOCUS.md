# kOA Graph — Parcours focalisés / Focused paths

Ce registre appartient au **référentiel architectural** `kOA-Digital-Ecosystem`.
L'application `kOA-Digital-Ecosystem-GitHub-Audit` le lit uniquement pendant une
**publication manuelle**, à un commit Git de ce dépôt source. GitHub Pages lit
la copie **datée**, et ne reconstitue jamais le graphe depuis GitHub en direct.

## Pourquoi des parcours ?

Le graphe n'est **pas une chaîne globale**. Un parcours est un angle de lecture
choisi autour d'un échange ou d'une capacité. Il montre un **chemin central**,
plusieurs **circuits secondaires** (facultatifs, alternatifs, retournant vers
une autorité) et les **frontières propriétaires**. Un même composant peut apparaître
plusieurs fois dans un chemin sans devenir plusieurs applications.

## Données

[`graph-focus.v1.json`](graph-focus.v1.json) contient :

- `paths[]` : trois parcours sélectionnables, `spine[]`, liens consécutifs `spine_links[]`,
  `branches[]` ancrées sur une étape du chemin central et placées au-dessus ou au-dessous ;
- `repo` : référence explicite à un dépôt de l'inventaire public des 51 ; pour un artefact ou
  une interface, `repo` peut être nul ;
- `contract` : identifiant exact de l'interface lorsque documenté (ne vaut pas adoption universelle) ;
- `evidence` : `repo` et `path` d'un document source, sans URL fabriquée depuis un dossier Windows ;
- `label` et `description` en **français et en anglais**.

### Statuts des relations

| Valeur | Signification |
|---|---|
| `qualified_local` | Qualification *sur le périmètre local documenté*, pas production globale |
| `implemented_owner` | Mise en œuvre **dans le dépôt du propriétaire**, sans généraliser l'E2E |
| `documented` | Interface, responsabilité ou intégration **documentée** |
| `candidate` | Contrat ou circuit à réaliser, accepter ou qualifier |
| `optional` | Composant ou alimentation **facultative**, jamais obligatoire pour tous |

Le niveau de maturité appartient au **lien / contrat**, pas au dépôt entier.
Les sources de dates différentes peuvent présenter des statuts différents :
la vue choisie explicite le niveau et conserve le lien vers le document.

## Ajouter un parcours

1. Choisir un scénario vérifiable (décision, acquisition, publication, déploiement, etc.).
2. Définir des **étapes distinctes et des liens consécutifs** : il ne doit pas exister de raccourci implicitement inventé.
3. Ajouter les branches avec `anchor` correspondant à l'index du nœud de la ligne, `side` (`above` / `below`).
4. Renseigner la source documentaire exacte pour chaque lien et branche ; ne pas extrapoler un contrat à partir d'une proximité de dépôts.
5. Mettre à jour la documentation d'autorité et exécuter `python -m unittest tests.test_focus_graph` côté Audit après installation.
6. Publier via le workflow manuel en mode `all` (le mode `republish` **ne recollecte pas** ce fichier).

**Limites :** les branches sont une composition de lecture. Les coordonnées ne
sont pas une preuve d'exécution. Interaction Kernel est un transport sous profil
adopté, pas un bus imposé à toutes les applications. Koali Spaces et kOA-Linux
sont optionnels selon le contexte.

---

**English:** This owner-maintained file describes selectable architectural paths,
not one mandatory ecosystem pipeline. Each link preserves its owner, exact
interface where known, evidence document and scope-limited maturity status.
The publication collector pins a single source Git commit, validates each
endpoint against the public inventory and freezes paths with the dated release.
