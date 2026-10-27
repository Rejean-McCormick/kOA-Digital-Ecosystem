# Konstellation Publisher — intégration documentaire

**État : 27 octobre 2026.** Référence descriptive, non admission opérationnelle.

- **Dépôt propriétaire :** [`Rejean-McCormick/Konstellation-Publisher`](https://github.com/Rejean-McCormick/Konstellation-Publisher) (public GitHub confirmé).
- **Racine locale déclarée :** `C:\mycode\Konstellation\Konstellation-Publisher`, dérivée du chemin `.git` communiqué par l’utilisateur ; existence et `origin` non vérifiés sur Windows.
- **Version du code fournie pour revue :** `0.2.0-alpha.1`, archive locale fournie séparément ; la présence du code dans le dépôt GitHub n’est pas établie par l’existence du dépôt.
- **Responsabilité :** interface Windows de pré-vérification des sources Konstellation 1.x, préparation de paquets à partir d’une liste autorisée de fichiers, gabarits Docker/Compose et rapports locaux.
- **État de déploiement :** publication distante volontairement désactivée. Les tests d’UI Windows, de staging VPS, de routage TLS/Traefik, de bascule et de restauration restent non qualifiés.

## Frontières et garde-fous

Le Publisher **n’est ni une autorité sur les données Kristal ni une autorité d’approbation de publication**. Un manifeste, un hash, une visibilité GitHub, un profil Compose ou une case cochée par l’opérateur ne remplacent pas les contrôles d’autorisation et de qualification. Les barrières C1/C2/C3, les reçus immuables et un déploiement transactionnel avec rollback vérifié sont des préalables à toute future activation distante.

Cette page ne modifie aucun contrat figé Kristal/IK, ne déclare aucune release de production et n’autorise ni GitSink ni une opération sur le VPS. Voir [l’index du registre de dépôts](../../../inventory/repositories.md) et [la fiche Konstellation](index.md).
