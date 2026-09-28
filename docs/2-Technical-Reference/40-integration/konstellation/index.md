# Konstellation — intégration versionnée

Konstellation v0.4 est une application de lecture/exploration. Kristal reste responsable des données, de leur provenance et des métadonnées épistémiques. SA réalise une demande sémantique explicite; l'orchestrateur gère la qualification et l'activation du runtime.

| Producteur | Contrat consommé | Responsabilité |
|---|---|---|
| Kristal | Runtime Pack v5 + profil `konstellation:reader-json-v1`, ou Parquet à mapping explicite | Identités, sources, politique et intégrité |
| Konstellation | QuerySpec/ExplorationState 0.2, CommunicationRequest 1.0 | Sélection, requête et portée de communication |
| SA | `konstellation-explorer-1`, bridge 1.0, CommunicationResult 1.0 | Présentation structurée fidèle, labels français, couverture |
| Runtime Orchestrator | pipeline.lock 1.0, conformance CLI, activation 1.0 | Vérification, qualification, promotion et activation |
| EncyKlopedia | Handoff explicite vers le producteur Kristal | Préparer les données, sans inventer une validation |

La formulation est désactivée tant que SA ne publie pas le runtime/profil/langue demandés. Le profil livré est candidat jusqu'à compilation GF et conformité sur le vrai PGF. La commande de conformité candidate ne crée aucune publication; elle est réservée au pipeline hors ligne.

Les cas de test provenant de Konstellation couvrent les critères, pages, entités et filtres négatifs. Les métadonnées ne sont pas réduites à une validation binaire. Les déclarations de capacité incompatibles sont refusées plutôt que remplacées par un résultat vide ou un texte de repli.

Aucune modification du bus Interaction Kernel n'est nécessaire pour la lecture locale. Les connexions HTTP sont explicites et configurées par l'opérateur; les URI de service et credentials n'appartiennent pas aux requêtes utilisateur.
