# Validation locale kOADiag — 27 novembre 2026

**Portée.** Résultats observés sur le poste Windows et ses dépôts locaux.
Les statuts s'appliquent aux contrôles et aux piles indiqués. Les décisions
de déploiement et les qualifications de livraison restent chez les propriétaires.

## Campagne Approfondie

| Champ | Valeur observée |
| --- | --- |
| Campagne | `20261127T204457Z-50433563` |
| Début UTC | 2026-11-27 20:44:57 |
| Durée | 304,95 s |
| Verdict | **PARTIAL** |
| Bilan | 19 PASS, 2 WARN, 2 PARTIAL, 4 BLOCKED sur 27 contrôles |
| GF Wordbench | `native-gf-wordbench-exhaustive` **PASS** · 4 445 réussis, 10 ignorés, code 0, 137,94 s |
| Koali, SemantiK Architect, Kristal | PASS dans la campagne |
| Transversal | 9 services accessibles sur 21, 2 essentiels sur 5, 4 liaisons accessibles sur 6, aucune erreur de santé ou d'identité signalée |

Source locale du bilan.

```text
C:\mycode\kOA_Digital_Ecosystem\kOADiag\reports\Diagnostic-kOA-Digital-Ecosystem\campagnes\20261127T204457Z-50433563\summary.json
```

Dans ce même dossier, `native-gf-wordbench-exhaustive.json` et
`native-gf-wordbench-exhaustive.log` donnent la preuve et le journal du contrôle.
La suite exécutée est la suite Python `tests/contracts tests/components tests/unit`.
Les correctifs de novembre ont couvert les rapports, les contrats d'architecture,
les exécutables GF simulés sous Windows, les journaux et la validation des
résultats. La compilation réelle de grammaires relève de sa suite propriétaire.

## Contrôles ouverts

| Contrôle | Verdict | Suite à documenter chez le propriétaire |
| --- | --- | --- |
| Konstellation Astro | BLOCKED | Entrée ou répertoire introuvable pour la commande de kOADiag. Examiner `native-konstellation-build.json`. Le build propriétaire du 27 novembre est une observation distincte. |
| Konstellation Node | PARTIAL | 275 réussis sur 276, un ignoré, aucun échec. Identifier la condition du test ignoré dans le journal. |
| Daat → Kristal-Framework | BLOCKED | Raccorder un parcours officiel à la frontière `1f2498730e97c890bdcf`. |
| EncyKlopedia → Daat | BLOCKED | Raccorder un parcours officiel à la frontière `4870ff5c8d8f61490fff`. |
| IK E2E dans ce run | BLOCKED | World et autorisation d'écriture de test absents de cette invocation. Voir le PASS séparé ci-dessous. |
| Transversal | PARTIAL | `orgo-web`, `initkoa-web` et `konnaxion-web` manquants dans la topologie C0 observée. |
| Orgo | WARN | N01. Le profil `database` sur copie isolée a validé N08, N09 et N11 lors du run ciblé `20261127T131823Z-1a70a42e`. La copie isolée évite la DLL Prisma ouverte par un autre processus Windows. |
| Konnaxion | WARN | N02, N04 et N11. La relance ciblée S02 après retrait du secret du Compose suivi donne WARN (fichiers locaux et limites de couverture). |

## Preuve fonctionnelle Orgo ↔ Konnaxion

Le run réel kOADiag du 26 novembre au soir (27 novembre, 02:00:51–02:01:15
UTC) donne **PASS** pour le World de test `fp-electromecanique-informatique`.
Le signal a été accepté, l'impact est `succeeded`, le kit officiel s'est terminé
avec le code 0 et son marqueur PASS. Empreinte SHA-256 du kit pour ce run.

```text
ac406471f48b35782adb24fed0f8e0c9f9d859e37409f3d046a4966e1faf08b5
```

Le test terminal du 25 novembre, importé par la suite, avait aussi validé
le rejeu idempotent (un Signal, un impact) et le conflit sur un rejeu divergent.
La [qualification historique du 21 septembre](2026-09-21-konnaxion-orgo-ik-e2e-qualification.md)
reste l'entrée pour sa propre campagne et ses références.

## Autres preuves ciblées

- **Koali** — `koali-system` PASS (N00, N12, run `20261126T235020Z-9a69fd42`)
  et `koali-final` PASS (N00, N12, N14, run `20261126T235224Z-3fded07e`).
  La pile Windows avait été relancée. La validation Koali porte sur son périmètre système.
- **SemantiK** — profil `semantik` 13 PASS
  (`20261127T002614Z-5375b033`), puis S80 10 PASS
  (`20261127T124804Z-674a0d54`). Le venv de diagnostic dans Ubuntu-24.04
  sous WSL utilise Python 3.12, `pgf==1.1` et `pytest`. S80 exécute le
  validateur canonique dans ce venv.
- **CI multi-dépôts** — l'overlay de triage a déclaré les correctifs appliqués
  dans 27 dépôts. `kOA-Digital-Ecosystem-GitHub-Audit` était indiqué ABSENT
  lors de cette installation. L'état des checks CI à distance reste à vérifier.

## Profil matériel de la campagne

Mesure système entier. Hôte Windows AMD64, 16 processeurs logiques, 293
échantillons à intervalle nominal de 1 s. CPU moyen **57,3 %**, pointe **100 %**.
RAM totale **23,41 Gio**, pic utilisé **21,04 Gio**, minimum disponible
**2,37 Gio**. Augmentation maximale sur la ligne de base **2,61 Gio**.
Baisse maximale d'espace libre observée **629 Mio**. Dépôts et rapports
partageaient le même volume. Ces chiffres décrivent la charge observée
pendant ce run. Les mesures sur d'autres charges restent à faire.
