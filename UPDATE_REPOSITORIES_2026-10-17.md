# Mise à jour des listes — 17 octobre 2026

Cette archive est une **copie modifiée du snapshot fourni**, pas un commit publié ni une écriture dans `C:\mycode`.

## Résultat

| Source | Avant | Après |
|---|---:|---:|
| GitHub public Rejean-McCormick | 66 | 76 |
| Entrées locales/externes/wiki | 49 | 56 |
| Dépôt utilisateur BoKristal (non public confirmé) | 1 | 1 |
| Entrées opérationnelles MA-Gustave | 6 | 0 |
| **Total** | **116** | **133** |

Les **23 nouveaux chemins Git** identifiés hors Gustave se répartissent ainsi : 10 nouveaux dépôts publics, 12 Wiki, 1 clone externe. Le diagnostic entier conserve 131 observations non Gustave (dont 7 sans chemin trouvé). **15 remotes publiques et 6 remotes Wiki** sont marquées à aligner et **2 remotes manquent** (`Kompose`, `Kontexte`).

## Fichiers modifiés / créés

- `docs/inventory/repositories.json` — 133 entrées, canonisation des noms Wiki repos parents, 21 drapeaux d'alignement (15 publics + 6 Wiki).
- `docs/inventory/repositories.md` — projection complète et cohérente du JSON.
- `docs/inventory/README.md` — nouvelle méthodologie et avertissements.
- `reports/GITHUB_PUBLIC_REPOS_76.csv` — liste GitHub actuelle (76).
- `reports/LOCAL_GIT_SCAN_2026-10-17.csv` — relevé local du diagnostic, filtré sans Gustave (131).
- Les anciennes listes de 66 dépôts et 100 marqueurs ont été archivées dans `reports/history/` pour conserver leur provenance et éviter d'être prises pour la liste active.
- `README_FIRST.md` — avertissement que la liste d'octobre 9 n'est plus la liste courante.

Les documents `docs/generated/repository-corpus-2026-09-28.json`, `docs/2-Technical-Reference/10-system/repository-corpus.md` et `reports/RECONCILIATION_NOTES.md` sont **des archives** : pas de réécriture du passé.

## Prudence pour GitSink

La présence dans l'inventaire ne permet **jamais** un push. Ne pas confondre identité GitHub canonique et remote réelle. Les remotes n'ont pas été réécrites ici ; les fichiers source locaux sur Windows n'étaient pas accessibles. Les GitHub Wiki `*.wiki` ne sont pas des repos additionnels dans les 76 renvoyés par GitHub.

## Application

Pour conserver tes autres fichiers, décompresse le ZIP complet dans un **nouveau dossier**, compare les changements, puis copie les listes que tu approuves dans ton projet. Il est préférable de préserver la sauvegarde du `repositories.json` original avant tout remplacement. Les chemins suivis restent ceux de `C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem`.

## Actualisation après GitSink Runner V8 — 17 octobre, 22 h 39

Cette nouvelle édition conserve les **133 entrées** et le fichier de **76 dépôts GitHub** ; elle ne retire rien de l'historique GitHub.

1. `Kristal-Kollection` : décision de retrait opérationnel. `scope=EXCLUDED` et `status=retired` dans `docs/inventory/repositories.json`. Le dossier et le dépôt distant ne sont **pas** supprimés par ce paquet.
2. `SenTient` : autorisation utilisateur de remplacer manuellement `origin/main` via `--force-with-lease` explicite, avec branche de sauvegarde ; **aucun push n'est exécuté ni automatisé**.
3. **15 remotes publiques alignées** sur Windows, selon le journal GitSink Runner V8 fourni (22:29–22:31), avec `PRET=55` avant l'exclusion de Kristal-Kollection ; cible **54** dans un prochain scan, si les autres contrôles restent inchangés. Les six entrées Wiki en attente de contrôle ne sont pas modifiées.
4. Les fichiers `reports/GITHUB_PUBLIC_REPOS_76.csv` et `reports/LOCAL_GIT_SCAN_2026-10-17.csv` conservent leur valeur de relevés datés, indépendamment des décisions de synchronisation.

Voir `docs/inventory/GITSINK_OPERATION_2026-10-17.md` et `scripts/SenTient_ForceWithLease.ps1`.
