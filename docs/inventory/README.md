# Repository inventory — état des listes au 17 octobre 2026

Ce dossier présente des **observations** (dépôts, chemins, remotes) et non une autorisation de commit/push, de déploiement ou une validation de la maturité logicielle.

## Sources de vérité et dénombrement

- `repositories.json` : registre principal — **133 entrées** : **76** dépôts publics accessibles chez `Rejean-McCormick`, **56** checkouts locaux/tiers/wiki et **1** dossier `BoKristal` signalé par l'utilisateur (dépôt distant non confirmé).
- `repositories.md` : projection lisible **synchronisée** de ces 133 lignes.
- `../../reports/GITHUB_PUBLIC_REPOS_76.csv` : liste officielle des 76 noms publics accessibles sur GitHub, vérifiée le 2026-10-17.
- `../../reports/LOCAL_GIT_SCAN_2026-10-17.csv` : les **131 résultats non Gustave** du dernier diagnostic RepoRadar transmis, dont 7 sans chemin détecté. Ce CSV n'est pas un scan Windows effectué par ce paquet.

Par rapport à la base historique de 116 lignes : **+10** nouveaux repos publics (`Akor`, `Arketype`, `Daat`, `Ekole`, `Ekole-Pastorale`, `Kompose`, `Kontainer`, `Kontexte`, `Skope`, `Spek`) ; **+12** clones Wiki et **+1** clone externe (`openai/math`) ; **-6** anciennes entrées de l'organisation MA-Gustave = **133**.

Les dépôts et lignes associés à Gustave sont exclus de ces listes de travail. Les archives de septembre et les anciennes notes de rapprochement restent datées et ne doivent pas être interprétées comme une liste actuelle.

## Alignement canonique

Les identités publiques utilisent exclusivement les noms **actuels** retournés par GitHub ; **aucune liste d'alias ni redirection n'est permise comme mécanisme de correspondance**. Les URL de navigation des Wiki utilisent `/wiki` pour l'identité du parent et leur checkout Git utilise `<repo>.wiki.git`.

Le diagnostic initial du 2026-10-17 relevait **15 remotes publiques et 6 remotes Wiki historiques non alignées**. Le journal GitSink Runner V8 suivant confirme que **les 15 remotes publiques ont été alignées à 22:30**, puis validées en simulation à **22:31** (`REMOTE_A_ALIGNER=0`, `PRET=55` avant retrait de Kristal-Kollection). Les **6 remotes Wiki** sont conservées avec le statut historique `remote_alignment_required` et n’ont pas été modifiées ici. Ce ZIP n’a pas accès au disque Windows.

`Kompose` et `Kontexte` sont publics sur GitHub et ont un dossier local détecté, mais **aucune remote lisible** : association non prouvée, push interdit jusqu'à vérification. Tous les autres chemins locaux doivent également être revalidés sur le poste Windows pour confirmer leur état présent.

## Champs et sécurité

Le format historique (`local_root`, `github_repo`, `github_url`, `status`, `description`, `source_docs_paths`, `note`, `scope`, `evidence`) est conservé ; les informations facultatives `observed_remote` et `github_clone_url` sont incluses lorsque disponibles. `local_root` peut être nul. `scope: PUBLIC` est utilisé par le Runner comme un prérequis de synchronisation, non une garantie d’admission : seul le statut `local_git_marker_seen` et les contrôles Git réels peuvent donner `PRET`. `scope: EXCLUDED` / `status: retired` bloque Kristal-Kollection malgré sa présence dans la liste publique GitHub de 76. `scope: LOCAL_OR_OTHER` désigne un clone ou checkout local dont la cible n'est pas un des 76 dépôts normaux ; `scope: USER_REPORTED` ne garantit pas l'existence publique d'un dépôt.

La politique d'autorisation GitSink est séparée de cet inventaire. **Aucun nouveau dépôt n'est autorisé à être poussé automatiquement.** La présence de `.git`, d'une URL, d'une entrée Wiki ou d'un dossier observé n'est pas une autorisation de push.

Les instantanés `docs/generated/repository-corpus-2026-09-28.json` et `docs/2-Technical-Reference/10-system/repository-corpus.md` sont des documents d'archives et ne sont pas actualisés rétroactivement.

## Décision GitSink du 17 octobre 2026

- `Kristal-Kollection` : projet retiré du périmètre automatisé (`EXCLUDED` / `retired`), sans suppression des observations ou de la fiche GitHub.
- `SenTient` : l’utilisateur autorise un **push forcé manuel** remplaçant `main` par la version locale. Ce ZIP **n’effectue pas cette opération**. Une sauvegarde de l’ancien `origin/main` et un `--force-with-lease` explicite sont requis.
- Dernier relevé V8 : `PRET=55`. Après le retrait de Kristal-Kollection, cible **54 `PRET`** si les autres dépôts restent identiques ; les 2 batchs non sécurisés et les 9 chemins non localisés restent distincts.

Voir [`GITSINK_OPERATION_2026-10-17.md`](GITSINK_OPERATION_2026-10-17.md).
