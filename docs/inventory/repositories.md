# Inventaire des dépôts — kOA Digital Ecosystem

**Référence initiale : 17 octobre 2026 ; ajout ciblé : 27 octobre 2026.** Le socle est dérivé du snapshot du 17 octobre à 20 h 32 et du diagnostic RepoRadar partagé : **76 dépôts publics** vérifiés alors. Le 27 octobre, **Konstellation-Publisher** a été confirmé séparément sur GitHub ; la validité des chemins `C:\mycode` et de leurs remotes n'est **pas vérifiée ici**.

- **134 entrées :** 77 dépôts publics `Rejean-McCormick` répertoriés (76 au relevé du 17 octobre + Publisher confirmé le 27), 56 entrées locales / tierces / Wiki, 1 dépôt signalé par l'utilisateur (`BoKristal`, non confirmé sur GitHub).
- **10 dépôts publics ajoutés au relevé du 17 octobre**, tous présents dans son diagnostic local ; **+1 Publisher le 27 octobre** (chemin Git déclaré, non scanné).
- **13 entrées locales ajoutées**, soit 12 checkouts Wiki et un dépôt externe (`openai/math`).
- **6 anciennes entrées MA-Gustave exclues**, et 16 lignes Gustave omises du rapport de scan local.
- **15 remotes de dépôts publics et 6 remotes Wiki historiques à aligner** avec leurs adresses GitHub actuelles. Aucun alias ou mécanisme de redirection n'est présent dans l'inventaire.
- **2 associations non confirmées** : `Kontexte` et `Kompose` disposent d'un dossier Git observé mais sans remote lisible.

> **Important :** `local_git_marker_seen` signifie que le scan a identifié un dossier Git à cette date ; cela ne garantit ni sa présence aujourd'hui ni une autorisation GitSink. Les entrées `*.wiki` sont des checkouts Git Wiki, **pas** des repos supplémentaires dans la liste des dépôts GitHub. Une URL GitHub Wiki est déduite du nom canonique du dépôt parent et doit être validée localement avant synchronisation.

## Statuts et règles de preuve

- `local_git_marker_seen` : dossier marqué Git dans l'observation disponible, remote pas nécessairement actuelle.
- `github_and_local_remote_verified` : URL du repo public et remote du diagnostic correspondent ; contrôle Windows à refaire.
- `github_verified_local_remote_unverified` : dépôt GitHub connu, mais remote locale non lisible ; **pas de push**.
- `remote_alignment_required` : GitHub actuel correspond à l'inventaire, mais `origin` du diagnostic utilise l'ancien nom ; **pas de push sans correction**.
- `previous_gitsink_observation_only` : checkout rapporté par un log historique, pas par le dernier scan.
- `retired` avec `scope=EXCLUDED` : projet connu mais **exclu du Runner GitSink** par décision explicite ; sa présence dans le CSV GitHub n’accorde aucun droit de push.
- `local_root_unknown`, `legacy_path_not_found`, `ambiguous_repository_identity`, `excluded_from_followup`, `user_reported_git_path` : statuts préexistants conservés ; pas de supposition de validité ou de suppression.

## Dépôts du compte GitHub (77 répertoriés : 76 dans le périmètre PUBLIC, 1 retiré de GitSink)

| Dépôt GitHub | Racine locale observée / historique | Statut |
|---|---|---|
| [`Rejean-McCormick/Akor`](https://github.com/Rejean-McCormick/Akor) | `C:\mycode\Ekole\Akor\Akor` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/Ame-Artificielle`](https://github.com/Rejean-McCormick/Ame-Artificielle) | `C:\mycode\02-Experimental\AmeArtificielle\Ame-Artificielle` | `local_git_marker_seen` |
| [`Rejean-McCormick/Arketype`](https://github.com/Rejean-McCormick/Arketype) | `C:\mycode\Kristal\Arketype\arketype` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/Book-Civilizational-Coherence`](https://github.com/Rejean-McCormick/Book-Civilizational-Coherence) | `C:\mycode\01-Text_Based_Git\Civilisational_Coherence` | `remote_alignment_required` |
| [`Rejean-McCormick/Book-Colin-Row`](https://github.com/Rejean-McCormick/Book-Colin-Row) | `C:\mycode\01-Text_Based_Git\Colin_Row` | `remote_alignment_required` |
| [`Rejean-McCormick/Daat`](https://github.com/Rejean-McCormick/Daat) | `C:\mycode\Interaction-Kernel\Daat` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/Ekole`](https://github.com/Rejean-McCormick/Ekole) | `C:\mycode\Ekole\ekole` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/Ekole-Pastorale`](https://github.com/Rejean-McCormick/Ekole-Pastorale) | `C:\mycode\Ekole\ecole-pastorale` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/EncyKlopedia`](https://github.com/Rejean-McCormick/EncyKlopedia) | `C:\mycode\EncyKlopedia\EncyKlopedia` | `local_git_marker_seen` |
| [`Rejean-McCormick/Freeze-Vote-Rebuild-Operational-Peace-Framework`](https://github.com/Rejean-McCormick/Freeze-Vote-Rebuild-Operational-Peace-Framework) | `C:\mycode\01-Text_Based_Git\FreezeVoteRebuild\Freeze-Vote-Rebuild_Operational-Peace-Framework` | `remote_alignment_required` |
| [`Rejean-McCormick/Grammatical-Framework-Albanian`](https://github.com/Rejean-McCormick/Grammatical-Framework-Albanian) | `C:\mycode\Grammatical_Framework\Grammatical_Framework-Albanian` | `local_git_marker_seen` |
| [`Rejean-McCormick/Grammatical-Framework-audit`](https://github.com/Rejean-McCormick/Grammatical-Framework-audit) | — | `local_root_unknown` |
| [`Rejean-McCormick/HELLO-WORLD-Autopsie-d-un-Clown-Royal`](https://github.com/Rejean-McCormick/HELLO-WORLD-Autopsie-d-un-Clown-Royal) | `C:\mycode\01-Text_Based_Git\HelloWorld(Suno)` | `remote_alignment_required` |
| [`Rejean-McCormick/HomePage-initkoa.org`](https://github.com/Rejean-McCormick/HomePage-initkoa.org) | `C:\mycode\HomePage\HomePage` | `remote_alignment_required` |
| [`Rejean-McCormick/initkoa-docs`](https://github.com/Rejean-McCormick/initkoa-docs) | `C:\mycode\HomePage\docs-initkoa-org` | `local_git_marker_seen` |
| [`Rejean-McCormick/Interaction-Kernel`](https://github.com/Rejean-McCormick/Interaction-Kernel) | `C:\mycode\Interaction-Kernel\interaction_kernel` | `local_git_marker_seen` |
| [`Rejean-McCormick/King-Klown-Canon`](https://github.com/Rejean-McCormick/King-Klown-Canon) | `C:\mycode\01-Text_Based_Git\King_Klown\king-clown-canon` | `local_git_marker_seen` |
| [`Rejean-McCormick/kOA-Digital-Ecosystem`](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem) | `C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem` | `remote_alignment_required` |
| [`Rejean-McCormick/kOA-Linux-Koali`](https://github.com/Rejean-McCormick/kOA-Linux-Koali) | `C:\mycode\kOA-Linux\koa-linux` | `remote_alignment_required` |
| [`Rejean-McCormick/kOA-Obama-Foundation-Briefing`](https://github.com/Rejean-McCormick/kOA-Obama-Foundation-Briefing) | `C:\mycode\01-Text_Based_Git\kOA-Obama` | `local_git_marker_seen` |
| [`Rejean-McCormick/Koali-Control-Panel`](https://github.com/Rejean-McCormick/Koali-Control-Panel) | `C:\mycode\kOA-Linux\Koali-Control-Panel` | `local_git_marker_seen` |
| [`Rejean-McCormick/Koali-Scenario-Mosaic`](https://github.com/Rejean-McCormick/Koali-Scenario-Mosaic) | `C:\mycode\kOA-Linux\Koali_Scenario_Mosaic` | `remote_alignment_required` |
| [`Rejean-McCormick/Koali-Spaces`](https://github.com/Rejean-McCormick/Koali-Spaces) | `C:\mycode\kOA-Linux\koali-spaces` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kompiler`](https://github.com/Rejean-McCormick/Kompiler) | `C:\mycode\Kristal\Kompiler` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kompose`](https://github.com/Rejean-McCormick/Kompose) | `C:\mycode\Ekole\Kompose\kompose` | `github_verified_local_remote_unverified` |
| [`Rejean-McCormick/Konductor`](https://github.com/Rejean-McCormick/Konductor) | `C:\mycode\Konductor\Konductor` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konfid`](https://github.com/Rejean-McCormick/Konfid) | `C:\mycode\Konfid\konfid` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konnaxion`](https://github.com/Rejean-McCormick/Konnaxion) | `C:\mycode\Konnaxion\Konnaxion` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konnaxion-Ashoka-Systems-Change-Dossier`](https://github.com/Rejean-McCormick/Konnaxion-Ashoka-Systems-Change-Dossier) | `C:\mycode\01-Text_Based_Git\Ashoka` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konnaxion-Capsule-Manager`](https://github.com/Rejean-McCormick/Konnaxion-Capsule-Manager) | `C:\mycode\Konnaxion\Konnaxion_Capsule_Manager` | `remote_alignment_required` |
| [`Rejean-McCormick/Konnaxion-LevelUpDiag`](https://github.com/Rejean-McCormick/Konnaxion-LevelUpDiag) | — | `local_root_unknown` |
| [`Rejean-McCormick/Konnaxion-SecurityDiag`](https://github.com/Rejean-McCormick/Konnaxion-SecurityDiag) | — | `local_root_unknown` |
| [`Rejean-McCormick/Konnaxion-Worlds`](https://github.com/Rejean-McCormick/Konnaxion-Worlds) | `C:\mycode\Konnaxion\Konnaxion_Worlds` | `remote_alignment_required` |
| [`Rejean-McCormick/KonnaxionDiag`](https://github.com/Rejean-McCormick/KonnaxionDiag) | `C:\mycode\Konnaxion\KonnaxionDiag` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konstellation`](https://github.com/Rejean-McCormick/Konstellation) | `C:\mycode\Konstellation\Konstellation` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konstellation-Light`](https://github.com/Rejean-McCormick/Konstellation-Light) | `C:\mycode\Konstellation\Konstellation-Light` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konstellation-Publisher`](https://github.com/Rejean-McCormick/Konstellation-Publisher) | `C:\mycode\Konstellation\Konstellation-Publisher` *(déclaré, non scanné)* | `github_verified_local_remote_unverified` |
| [`Rejean-McCormick/Kontainer`](https://github.com/Rejean-McCormick/Kontainer) | `C:\mycode\Kristal\Kontainer` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/Kontexte`](https://github.com/Rejean-McCormick/Kontexte) | `C:\mycode\Ekole\Kontexte\Kontexte` | `github_verified_local_remote_unverified` |
| [`Rejean-McCormick/Kristal-Authoring-Kit`](https://github.com/Rejean-McCormick/Kristal-Authoring-Kit) | `C:\mycode\Kristal\Kristal-Authoring-Kit` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kristal-Farms`](https://github.com/Rejean-McCormick/Kristal-Farms) | `C:\mycode\01-Text_Based_Git\Kristal_Farms\kristal-farms` | `remote_alignment_required` |
| [`Rejean-McCormick/Kristal-Framework`](https://github.com/Rejean-McCormick/Kristal-Framework) | `C:\mycode\Kristal\Kristal-Framework` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kristal-Integration-Pack`](https://github.com/Rejean-McCormick/Kristal-Integration-Pack) | `C:\mycode\Kristal\Kristal-Integration-Pack` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kristal-Kollection`](https://github.com/Rejean-McCormick/Kristal-Kollection) | `C:\mycode\Kristal\Kristal-Kollection` | `retired` — GitSink exclu |
| [`Rejean-McCormick/Kristal-Manager`](https://github.com/Rejean-McCormick/Kristal-Manager) | `C:\mycode\Kristal\Kristal-Manager` | `local_git_marker_seen` |
| [`Rejean-McCormick/kristal-public`](https://github.com/Rejean-McCormick/kristal-public) | `C:\mycode\Kristal\kristal-public` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kristal-Reference`](https://github.com/Rejean-McCormick/Kristal-Reference) | — | `legacy_path_not_found` |
| [`Rejean-McCormick/KristalDiag`](https://github.com/Rejean-McCormick/KristalDiag) | `C:\mycode\Kristal\KristalDiag` | `local_git_marker_seen` |
| [`Rejean-McCormick/KristalV10`](https://github.com/Rejean-McCormick/KristalV10) | — | `legacy_path_not_found` |
| [`Rejean-McCormick/LevelUpDiag-kOA-Linux`](https://github.com/Rejean-McCormick/LevelUpDiag-kOA-Linux) | `C:\mycode\kOA-Linux\LevelUpDiag-Koali` | `local_git_marker_seen` |
| [`Rejean-McCormick/LevelUpDiag-Kristal`](https://github.com/Rejean-McCormick/LevelUpDiag-Kristal) | — | `legacy_path_not_found` |
| [`Rejean-McCormick/LevelUpDiag-Orgo`](https://github.com/Rejean-McCormick/LevelUpDiag-Orgo) | `C:\mycode\Orgo\LevelUpDiag-Orgo` | `local_git_marker_seen` |
| [`Rejean-McCormick/LevelUpDiag_SemantiK-Architect`](https://github.com/Rejean-McCormick/LevelUpDiag_SemantiK-Architect) | `C:\mycode\SemantiK_Architect\LevelUpDiag_SemantiK_Architect` | `local_git_marker_seen` |
| [`Rejean-McCormick/Mediatheque`](https://github.com/Rejean-McCormick/Mediatheque) | `C:\mycode\kOA_Mediatheque\mediatheque` | `local_git_marker_seen` |
| [`Rejean-McCormick/Mediatheque-blank`](https://github.com/Rejean-McCormick/Mediatheque-blank) | `C:\mycode\kOA_Mediatheque\mediatheque-blank` | `local_git_marker_seen` |
| [`Rejean-McCormick/MediKristal`](https://github.com/Rejean-McCormick/MediKristal) | `C:\mycode\Kristal\MediKristal\MediKristal` | `local_git_marker_seen` |
| [`Rejean-McCormick/MediKristal-LevelUpDiag-`](https://github.com/Rejean-McCormick/MediKristal-LevelUpDiag-) | `C:\mycode\Kristal\MediKristal\LevelUpDiag-MediKristal` | `local_git_marker_seen` |
| [`Rejean-McCormick/Omni-Wiki`](https://github.com/Rejean-McCormick/Omni-Wiki) | — | `excluded_from_followup` |
| [`Rejean-McCormick/Omni-Wiki-Rejean-King-Klown`](https://github.com/Rejean-McCormick/Omni-Wiki-Rejean-King-Klown) | `C:\mycode\OmniWiki\Omni-Wiki-Rejean-King-Klown` | `local_git_marker_seen` |
| [`Rejean-McCormick/Orgo`](https://github.com/Rejean-McCormick/Orgo) | `C:\mycode\Orgo\Orgo` | `local_git_marker_seen` |
| [`Rejean-McCormick/Orgo-Worlds`](https://github.com/Rejean-McCormick/Orgo-Worlds) | `C:\mycode\Orgo\Orgo_Worlds` | `remote_alignment_required` |
| [`Rejean-McCormick/OurAI`](https://github.com/Rejean-McCormick/OurAI) | — | `excluded_from_followup` |
| [`Rejean-McCormick/Partners-for-Public-Good-Pressure-Test-Koali`](https://github.com/Rejean-McCormick/Partners-for-Public-Good-Pressure-Test-Koali) | `C:\mycode\01-Text_Based_Git\PPG` | `remote_alignment_required` |
| [`Rejean-McCormick/Pi-Theory`](https://github.com/Rejean-McCormick/Pi-Theory) | `C:\mycode\01-Text_Based_Git\Pi-theory\Pi_Theory` | `local_git_marker_seen` |
| [`Rejean-McCormick/Power-Dynamics`](https://github.com/Rejean-McCormick/Power-Dynamics) | `C:\mycode\01-Text_Based_Git\Power_Dynamics\power_dynamics` | `local_git_marker_seen` |
| [`Rejean-McCormick/Projet-ORPHEE-Walk-Straight`](https://github.com/Rejean-McCormick/Projet-ORPHEE-Walk-Straight) | `C:\mycode\01-Text_Based_Git\Orphee(Prison)\orphee-walk-straight` | `remote_alignment_required` |
| [`Rejean-McCormick/Rejean-McCormick`](https://github.com/Rejean-McCormick/Rejean-McCormick) | `C:\mycode\Rejean_McCormick-OrganisationGit\Rejean-McCormick` | `local_git_marker_seen` |
| [`Rejean-McCormick/Science-Silk-Road-Koali`](https://github.com/Rejean-McCormick/Science-Silk-Road-Koali) | `C:\mycode\01-Text_Based_Git\Science_Silk_Road\science_silk_road` | `local_git_marker_seen` |
| [`Rejean-McCormick/SemantiK-Architect`](https://github.com/Rejean-McCormick/SemantiK-Architect) | `C:\mycode\SemantiK_Architect\SemantiK_Architect` | `local_git_marker_seen` |
| [`Rejean-McCormick/SemantiK_Runtime_Orchestrator`](https://github.com/Rejean-McCormick/SemantiK_Runtime_Orchestrator) | `C:\mycode\SemantiK_Architect\SemantiK_Runtime_Orchestrator` | `local_git_marker_seen` |
| [`Rejean-McCormick/SenTient`](https://github.com/Rejean-McCormick/SenTient) | `C:\mycode\SenTient\SenTient` | `local_git_marker_seen` |
| [`Rejean-McCormick/Skope`](https://github.com/Rejean-McCormick/Skope) | `C:\mycode\Skope\Skope` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/Spek`](https://github.com/Rejean-McCormick/Spek) | `C:\mycode\Spek_Semantic-publishing\Spek` | `github_and_local_remote_verified` |
| [`Rejean-McCormick/UCKK`](https://github.com/Rejean-McCormick/UCKK) | — | `ambiguous_repository_identity` |
| [`Rejean-McCormick/UCKK-Assets`](https://github.com/Rejean-McCormick/UCKK-Assets) | `C:\mycode\UCKK\UCKK_Assets` | `remote_alignment_required` |
| [`Rejean-McCormick/UCKK-Ops-Console`](https://github.com/Rejean-McCormick/UCKK-Ops-Console) | `C:\mycode\UCKK\UCKK_ops_console` | `local_git_marker_seen` |
| [`Rejean-McCormick/VotingMachine`](https://github.com/Rejean-McCormick/VotingMachine) | `C:\mycode\02-Experimental\VotingMachine\VotingMachine` | `local_git_marker_seen` |

## Dépôt signalé séparément (1)

| Dépôt | Racine rapportée | Statut |
|---|---|---|
| [`Rejean-McCormick/BoKristal`](https://github.com/Rejean-McCormick/BoKristal) | `C:\mycode\BoKristal\BoKristal` | `user_reported_git_path` |

`BoKristal` n'apparaissait pas dans le relevé des 76 dépôts publics du 17 octobre ; il peut s'agir d'un dépôt privé, supprimé ou inaccessible. Cette ligne **ne constitue pas** une confirmation de visibilité GitHub.

## Checkouts locaux, tiers et GitHub Wiki (56)

| Identité connue ou observée | Racine locale | Statut |
|---|---|---|
| [`Rejean-McCormick/Business-Plan`](https://github.com/Rejean-McCormick/Business-Plan) | `C:\mycode\01-Text_Based_Git\Business-plan` | `local_git_marker_seen` |
| [`Rejean-McCormick/kOA-International-Strategy`](https://github.com/Rejean-McCormick/kOA-International-Strategy) | `C:\mycode\01-Text_Based_Git\International-Strategy` | `local_git_marker_seen` |
| [`Rejean-McCormick/King-Klown-Canon.wiki`](https://github.com/Rejean-McCormick/King-Klown-Canon/wiki) | `C:\mycode\01-Text_Based_Git\King_Klown\king-klown-canon.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kristal-Farms.wiki`](https://github.com/Rejean-McCormick/Kristal-Farms/wiki) | `C:\mycode\01-Text_Based_Git\Kristal_Farms\Kristal_Farms.wiki` | `remote_alignment_required` |
| [`Rejean-McCormick/Pi-Theory.wiki`](https://github.com/Rejean-McCormick/Pi-Theory/wiki) | `C:\mycode\01-Text_Based_Git\Pi-theory\Pi-Theory.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Power-Dynamics.wiki`](https://github.com/Rejean-McCormick/Power-Dynamics/wiki) | `C:\mycode\01-Text_Based_Git\Power_Dynamics\Power-Dynamics.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Science-Silk-Road-Koali.wiki`](https://github.com/Rejean-McCormick/Science-Silk-Road-Koali/wiki) | `C:\mycode\01-Text_Based_Git\Science_Silk_Road\science-silk-road-koali.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Ame-Artificielle.wiki`](https://github.com/Rejean-McCormick/Ame-Artificielle/wiki) | `C:\mycode\02-Experimental\AmeArtificielle\Ame-Artificielle.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Astro-App`](https://github.com/Rejean-McCormick/Astro-App) | `C:\mycode\02-Experimental\Astro-App\astro_app` | `local_git_marker_seen` |
| [`Rejean-McCormick/Math-Challenges`](https://github.com/Rejean-McCormick/Math-Challenges) | `C:\mycode\02-Experimental\MathChallenges` | `local_git_marker_seen` |
| [`openai/math`](https://github.com/openai/math) | `C:\mycode\02-Experimental\MathChallenges\math` | `local_git_marker_seen` |
| [`Rejean-McCormick/Voxtral-Audiobook-Studio`](https://github.com/Rejean-McCormick/Voxtral-Audiobook-Studio) | `C:\mycode\02-Experimental\Voxtral_Audiobook_Studio\Voxtral_Audiobook_Studio` | `local_git_marker_seen` |
| [`Rejean-McCormick/theophile-mini-site`](https://github.com/Rejean-McCormick/theophile-mini-site) | `C:\mycode\03-Brands\Theophile\theophile-mini-site` | `local_git_marker_seen` |
| [`Alfresco/alfresco-community-repo`](https://github.com/Alfresco/alfresco-community-repo) | `C:\mycode\Alfresco\alfresco-community-repo` | `local_git_marker_seen` |
| [`Rejean-McCormick/Ariane`](https://github.com/Rejean-McCormick/Ariane) | `C:\mycode\Ariane\Ariane` | `local_git_marker_seen` |
| [`Rejean-McCormick/Akor.wiki`](https://github.com/Rejean-McCormick/Akor/wiki) | `C:\mycode\Ekole\Akor\Akor.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Ekole-Pastorale.wiki`](https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki) | `C:\mycode\Ekole\Ekole-Pastorale.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Ekole.wiki`](https://github.com/Rejean-McCormick/Ekole/wiki) | `C:\mycode\Ekole\Ekole.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kompose.wiki`](https://github.com/Rejean-McCormick/Kompose/wiki) | `C:\mycode\Ekole\Kompose\Kompose.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kontexte.wiki`](https://github.com/Rejean-McCormick/Kontexte/wiki) | `C:\mycode\Ekole\Kontexte\Kontexte.wiki` | `local_git_marker_seen` |
| [`GrammaticalFramework/gf-core`](https://github.com/GrammaticalFramework/gf-core) | `C:\mycode\Grammatical_Framework\gf-core` | `local_git_marker_seen` |
| [`GrammaticalFramework/gf-rgl`](https://github.com/GrammaticalFramework/gf-rgl) | `C:\mycode\Grammatical_Framework\gf-rgl` | `local_git_marker_seen` |
| [`krangelov/gf-wikidata`](https://github.com/krangelov/gf-wikidata) | `C:\mycode\Grammatical_Framework\gf-wikidata_repos_source\gf-wikidata` | `local_git_marker_seen` |
| [`GrammaticalFramework/gf-wikidata-tools`](https://github.com/GrammaticalFramework/gf-wikidata-tools) | `C:\mycode\Grammatical_Framework\gf-wikidata_repos_source\gf-wikidata-tools` | `local_git_marker_seen` |
| [`foerstner-lab/GFF_to_Wikidata_importer`](https://github.com/foerstner-lab/GFF_to_Wikidata_importer) | `C:\mycode\Grammatical_Framework\gf-wikidata_repos_source\GFF_to_Wikidata_importer` | `local_git_marker_seen` |
| [`Rejean-McCormick/kOA-Digital-Ecosystem.wiki`](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki) | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\kOA Digital Ecosystem` | `remote_alignment_required` |
| [`Rejean-McCormick/Konnaxion.wiki`](https://github.com/Rejean-McCormick/Konnaxion/wiki) | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\Konnaxion` | `previous_gitsink_observation_only` |
| [`Rejean-McCormick/Kristal-Framework.wiki`](https://github.com/Rejean-McCormick/Kristal-Framework/wiki) | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\Kristal Framework` | `previous_gitsink_observation_only` |
| [`Rejean-McCormick/Orgo.wiki`](https://github.com/Rejean-McCormick/Orgo/wiki) | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\Orgo` | `previous_gitsink_observation_only` |
| [`Rejean-McCormick/SemantiK-Architect.wiki`](https://github.com/Rejean-McCormick/SemantiK-Architect/wiki) | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\SemantiK Architect` | `remote_alignment_required` |
| [`Rejean-McCormick/SenTient.wiki`](https://github.com/Rejean-McCormick/SenTient/wiki) | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\SenTient` | `previous_gitsink_observation_only` |
| [`Rejean-McCormick/Daat.wiki`](https://github.com/Rejean-McCormick/Daat/wiki) | `C:\mycode\Interaction-Kernel\Daat.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kamel`](https://github.com/Rejean-McCormick/Kamel) | `C:\mycode\Kamel\Kamel` | `local_git_marker_seen` |
| [`Rejean-McCormick/kOA-Linux-Koali.wiki`](https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki) | `C:\mycode\kOA-Linux\koa-linux-wiki` | `remote_alignment_required` |
| [`Rejean-McCormick/kOA-Digital-Ecosystem.wiki`](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki) | `C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem.wiki` | `remote_alignment_required` |
| [`Rejean-McCormick/Konfid.wiki`](https://github.com/Rejean-McCormick/Konfid/wiki) | `C:\mycode\Konfid\Konfid.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konnaxion.wiki`](https://github.com/Rejean-McCormick/Konnaxion/wiki) | `C:\mycode\Konnaxion\Konnaxion.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Konstellation.wiki`](https://github.com/Rejean-McCormick/Konstellation/wiki) | `C:\mycode\Konstellation\Konstellation.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Arketype.wiki`](https://github.com/Rejean-McCormick/Arketype/wiki) | `C:\mycode\Kristal\Arketype\Arketype.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kontainer.wiki`](https://github.com/Rejean-McCormick/Kontainer/wiki) | `C:\mycode\Kristal\Kontainer.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kristal-Framework.wiki`](https://github.com/Rejean-McCormick/Kristal-Framework/wiki) | `C:\mycode\Kristal\kristal-framework.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Kristal-Integration-Pack.wiki`](https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki) | `C:\mycode\Kristal\Kristal-Integration-Pack.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/MediKristal.wiki`](https://github.com/Rejean-McCormick/MediKristal/wiki) | `C:\mycode\Kristal\MediKristal\MediKristal.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/LevelUpDiag`](https://github.com/Rejean-McCormick/LevelUpDiag) | `C:\mycode\LevelUpDiag\LevelUpDiag` | `local_git_marker_seen` |
| [`Rejean-McCormick/Orgo.wiki`](https://github.com/Rejean-McCormick/Orgo/wiki) | `C:\mycode\Orgo\Orgo.wiki` | `local_git_marker_seen` |
| [`GrammaticalFramework/gf-rgl`](https://github.com/GrammaticalFramework/gf-rgl) | `C:\mycode\SemantiK_Architect\gf-rgl` | `local_git_marker_seen` |
| [`Rejean-McCormick/SemantiK-Architect.wiki`](https://github.com/Rejean-McCormick/SemantiK-Architect/wiki) | `C:\mycode\SemantiK_Architect\SemantiK_Architect.wiki` | `remote_alignment_required` |
| [`Rejean-McCormick/SenTient.wiki`](https://github.com/Rejean-McCormick/SenTient/wiki) | `C:\mycode\SenTient\SenTient.wiki` | `local_git_marker_seen` |
| [`simdjson/simdjson`](https://github.com/simdjson/simdjson) | `C:\mycode\Simdjson\simdjson-upstream` | `local_git_marker_seen` |
| [`Rejean-McCormick/Skope.wiki`](https://github.com/Rejean-McCormick/Skope/wiki) | `C:\mycode\Skope\Skope.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/Spek.wiki`](https://github.com/Rejean-McCormick/Spek/wiki) | `C:\mycode\Spek_Semantic-publishing\Spek.wiki` | `local_git_marker_seen` |
| [`Rejean-McCormick/SwarmCraft`](https://github.com/Rejean-McCormick/SwarmCraft) | `C:\mycode\SwarmCraft\SwarmCraft` | `local_git_marker_seen` |
| [`Rejean-McCormick/tools`](https://github.com/Rejean-McCormick/tools) | `C:\mycode\Tools\toolz` | `local_git_marker_seen` |
| [`Rejean-McCormick/KeyFlow`](https://github.com/Rejean-McCormick/KeyFlow) | `C:\mycode\UCKK\KeyFlow(formulaires)` | `local_git_marker_seen` |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `C:\mycode\UCKK\moodle\moodle` | `local_git_marker_seen` |
| [`Rejean-McCormick/UCKK-Moodle`](https://github.com/Rejean-McCormick/UCKK-Moodle) | `C:\mycode\UCKK\uckk-moodle` | `local_git_marker_seen` |

## Dépôts publics ajoutés (10 au 17 octobre ; +1 au 27 octobre)

`Akor`, `Arketype`, `Daat`, `Ekole`, `Ekole-Pastorale`, `Kompose`, `Kontainer`, `Kontexte`, `Skope`, `Spek`.

**27 octobre 2026 — `Konstellation-Publisher` :** dépôt public GitHub confirmé ; racine `C:\mycode\Konstellation\Konstellation-Publisher` déclarée via son dossier `.git`, non sondée sur Windows. Publisher 0.2.0-alpha.1 est un outil de préparation locale : publication et déploiement distant **bloqués**. **Aucune permission GitSink ni validation de `origin` n'est implicite.** Voir [intégration Publisher](../2-Technical-Reference/40-integration/konstellation/publisher.md).

## Suites à effectuer sur Windows

Le scan du 17 octobre a relevé **15 `origin` périmées pour les dépôts publics**, et **6 checkouts Wiki** ayant une remote utilisant un ancien slug. Corriger les remotes locales avec le slug actuel **après vérification**, et contrôler l'URL enregistrée sans substitution Git `insteadOf`. Vérifier également les associations `Kontexte` / `Kompose` avant de configurer une remote. Ne pas autoriser GitSink à pousser automatiquement des dépôts ajoutés : l'adhésion à l'inventaire n'est pas une approbation de publication.

## Décisions GitSink — 17 octobre 2026

- **Kristal-Kollection** : retrait du Runner par `scope=EXCLUDED` / `status=retired` ; entrée conservée dans la liste historique et dans la liste GitHub officielle de 76.
- **SenTient** : push normal rejeté (branche distante en avance). Remplacement de `main` par la version locale **autorisé par l’utilisateur**, mais **pas encore exécuté par cette mise à jour**. Utiliser seulement la procédure manuelle sauvegardée dans [`GITSINK_OPERATION_2026-10-17.md`](GITSINK_OPERATION_2026-10-17.md) avec un bail (`--force-with-lease=<ref>:<SHA>`). Aucun `--force` n’est ajouté à GitSink Runner V8 ni à `GitSink.bat`.
- **Sélection attendue** : de 55 `PRET` dans le dernier journal à **54 `PRET`** après retrait, sous réserve de l’état local courant.

## Sources

- `repositories.json` : registre de travail et observations, sans alias.
- [`../../reports/GITHUB_PUBLIC_REPOS_76.csv`](../../reports/GITHUB_PUBLIC_REPOS_76.csv) : relevé historique des 76 repos publics GitHub au 17 octobre ; Publisher, confirmé le 27, n'y est pas ajouté rétroactivement.
- [`../../reports/LOCAL_GIT_SCAN_2026-10-17.csv`](../../reports/LOCAL_GIT_SCAN_2026-10-17.csv) : diagnostic RepoRadar filtré sans Gustave, avec ses 131 résultats (dont 7 sans chemin).
- `docs/generated/repository-corpus-2026-09-28.json` et `docs/2-Technical-Reference/10-system/repository-corpus.md` sont des **archives historiques** (2026-09-28), pas la liste opérationnelle actuelle.
