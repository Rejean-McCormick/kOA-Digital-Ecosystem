# kOA ecosystem — découplage de Skope et Kristal Iroquoiens

**Périmètre : documentation/contrats de frontières uniquement.**

1. `Skope` devient un dépôt d'outil générique, sans racine Wikidata ni sources métier.
2. `Kristal-Iroquoiens-Working` détient seed `Q110654499`, recette, source et working model.
3. Interface explicitée : `Skope --db <working> --recipe <projet>/configs/*.json`, API `GET /api/config`, puis preview/export non canoniques.
4. Les ports ne changent pas : Ékole Core 8765, Enseignant/OpsConsole 8766, Skope 8767.
5. Aucune chaîne v9/v10 qualifiée ni transfert vers Ékole n'est attesté.

**Dépôts logiciels séparés :** l'archive kOA n'embarque ni Skope, ni le projet Iroquoiens, ni les datasets Wikidata.
