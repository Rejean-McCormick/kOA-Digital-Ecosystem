# GitSink — état post-alignement et décisions du 17 octobre 2026

**Données de base :** le snapshot reçu le 17 octobre à 22 h 39 et le journal utilisateur GitSink Runner V8 à 22:31. Ces informations ne prouvent pas l'état du disque Windows après l'envoi du ZIP.

## État réconcilié

| Élément | État documenté |
|---|---|
| Entrées `repositories.json` | 133, sans entrée MA-Gustave active |
| Dépôts listés sur le compte GitHub | 76 (CSV daté, non réduit lors du retrait de GitSink) |
| Remotes publiques anciennement erronées | 15 alignées et vérifiées par simulation GitSink V8 à 22:31 |
| Entrées Wiki historiques `remote_alignment_required` | 6 ; hors automatisation |
| `PRET` dans le dernier journal avant retrait | 55 |
| `PRET` **attendu** après retrait de Kristal-Kollection | 54, à confirmer en simulation |
| `BATCH_NON_SECURISÉ` dans le dernier journal | 2, non réparés par ce ZIP |
| `NON_LOCALISE` dans le dernier journal | 9, non réparés par ce ZIP |

### Kristal-Kollection — retrait sans destruction

`Rejean-McCormick/Kristal-Kollection` reste dans l'inventaire (traçabilité) et dans `reports/GITHUB_PUBLIC_REPOS_76.csv` (relevé GitHub daté). Son entrée a désormais `scope: EXCLUDED` et `status: retired`, ce qui l'exclut **strictement** de l'exécution par GitSink Runner V8, dont le filtre exige `scope=PUBLIC` et `status=local_git_marker_seen`. **Ne pas supprimer le dossier local ni le dépôt GitHub automatiquement.**

### SenTient — remplacement manuel de main autorisé

Le journal du 17 octobre 22:26 relève un rejet `main -> main (fetch first)` : le distant contient des commits absents de l'historique local. L'utilisateur a explicitement autorisé un remplacement de `main` par la branche locale. C'est une **opération ponctuelle et potentiellement destructive** : les commits uniquement distants ne figureront plus sur `main`, même si une sauvegarde permet de les retrouver.

**Règles :** pas de `--force` général, pas de `--force` dans `GitSink.bat`, pas de modification du Runner V8. N'exécuter la procédure que depuis le vrai poste Windows où réside le dépôt, après contrôle du dépôt et du SHA. La branche de sauvegarde distante est créée **avant** tout remplacement ; l'option `--force-with-lease=refs/heads/main:<SHA>` refuse le push si `main` a changé pendant l'opération. Une protection de branche GitHub peut refuser le push ; ne pas la contourner.

Exécuter volontairement `scripts/SenTient_ForceWithLease.ps1` en PowerShell depuis un terminal de confiance. Le script affiche les refs, les commits divergents, effectue une sauvegarde locale **et distante**, puis exige la saisie `FORCER SENTIENT` avant le push. Il refuse un arbre de travail sale, une autre branche que `main`, une remote différente de l'URL canonique ou une URL de push différente. Le script ne modifie aucun autre dépôt.

```powershell
# Depuis la racine extraite du paquet (ou le dépôt kOA qui contient scripts/)
powershell.exe -NoProfile -File .\scripts\SenTient_ForceWithLease.ps1
```

Si PowerShell bloque l'exécution des scripts selon la politique de la machine, ne changez pas la politique globale : inspectez le script et utilisez une invocation de session autorisée par votre politique locale ou procédez manuellement avec les mêmes contrôles.

Après succès, vérifier sur Windows :

```powershell
cd C:\mycode\SenTient\SenTient
git status -sb
git fetch origin
git rev-parse main
git rev-parse origin/main
```

Les deux SHA doivent coïncider pour `main` et `origin/main`. Ensuite relancer **GitSink Runner V8 en SIMULATION** et vérifier **`PRET=54`**, **`REMOTE_A_ALIGNER=0`** (pour les dépôts publics), et aucun `Kristal-Kollection` dans les lignes `PRET` ; les 6 Wiki restent des observations non autorisées. Si le script n'a pas été exécuté ou si une protection de branche l'a bloqué, **SenTient continuera à échouer en `git push` normal**.

## Provenance

- Journal utilisateur : `15 termine(s), 0 refuse(s)` et `PRET=55`, `REMOTE_A_ALIGNER=0` en simulation à 22:31.
- Le retrait de Kristal-Kollection et le recours exceptionnel au force-with-lease sur SenTient sont des **décisions utilisateur** ; ce ne sont pas des preuves d'une suppression GitHub ou d'un push réussi.
- Les rapports de scan local et GitHub (`reports/`) sont conservés sans réécrire l'historique.
