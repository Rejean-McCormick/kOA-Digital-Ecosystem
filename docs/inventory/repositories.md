# Repository inventory — reconciled local observations

> **Inventory update — 2026-10-09:** Added BoKristal from the user's explicit Windows `.git` path and GitHub URL; this entry is **user-reported, not independently verified**. The existing reconciliation remains the historical baseline.

**Scope:** 66 repositories in the previous public list, 49 additional local/third-party/wiki checkout entries, and 1 newly reported BoKristal repository (**116 entries**). The earlier tree contains **100 independently observed `.git` markers**; the additional BoKristal marker was reported later by the user and was not counted in that scan. Six nested wiki caches were previously observed but are not freshly checked by that tree.

**Excluded from anomaly follow-up:** `Omni-Wiki` and `OurAI`.

## Status meanings

- `local_git_marker_seen`: the submitted Windows tree explicitly marks the path with `[GIT]`. Repo name association comes from the earlier GitSink scan.
- `previous_gitsink_observation_only`: previous runner identified a nested checkout, but the new tree stops at the outer `.git`.
- `local_root_unknown`: no checkout confirmed at the expected location.
- `legacy_path_not_found`: old candidate local folder not found; GitHub remote status was not checked.
- `ambiguous_repository_identity`: a checkout was assigned to two different repos in older inventory; no authoritative assignment.
- `excluded_from_followup`: explicitly excluded by user.
- `user_reported_git_path`: repository and `.git` path explicitly supplied by user; neither checked locally nor independently associated through `git remote`.

## Public repository list (66)

| GitHub repository | Local root | Status |
|---|---|---|
| [Rejean-McCormick/Ame-Artificielle](https://github.com/Rejean-McCormick/Ame-Artificielle) | `C:\mycode\02-Experimental\AmeArtificielle\Ame-Artificielle` | `local_git_marker_seen` |
| [Rejean-McCormick/Book-Civilizational-Coherence](https://github.com/Rejean-McCormick/Book-Civilizational-Coherence) | `C:\mycode\01-Text_Based_Git\Civilisational_Coherence` | `local_git_marker_seen` |
| [Rejean-McCormick/Book-Colin-Row](https://github.com/Rejean-McCormick/Book-Colin-Row) | `C:\mycode\01-Text_Based_Git\Colin_Row` | `local_git_marker_seen` |
| [Rejean-McCormick/EncyKlopedia](https://github.com/Rejean-McCormick/EncyKlopedia) | `C:\mycode\EncyKlopedia\EncyKlopedia` | `local_git_marker_seen` |
| [Rejean-McCormick/Freeze-Vote-Rebuild-Operational-Peace-Framework](https://github.com/Rejean-McCormick/Freeze-Vote-Rebuild-Operational-Peace-Framework) | `C:\mycode\01-Text_Based_Git\FreezeVoteRebuild\Freeze-Vote-Rebuild_Operational-Peace-Framework` | `local_git_marker_seen` |
| [Rejean-McCormick/Grammatical-Framework-Albanian](https://github.com/Rejean-McCormick/Grammatical-Framework-Albanian) | `C:\mycode\Grammatical_Framework\Grammatical_Framework-Albanian` | `local_git_marker_seen` |
| [Rejean-McCormick/Grammatical-Framework-audit](https://github.com/Rejean-McCormick/Grammatical-Framework-audit) | `` | `local_root_unknown` |
| [Rejean-McCormick/HELLO-WORLD-Autopsie-d-un-Clown-Royal](https://github.com/Rejean-McCormick/HELLO-WORLD-Autopsie-d-un-Clown-Royal) | `C:\mycode\01-Text_Based_Git\HelloWorld(Suno)` | `local_git_marker_seen` |
| [Rejean-McCormick/HomePage-initkoa.org](https://github.com/Rejean-McCormick/HomePage-initkoa.org) | `C:\mycode\HomePage\HomePage` | `local_git_marker_seen` |
| [Rejean-McCormick/initkoa-docs](https://github.com/Rejean-McCormick/initkoa-docs) | `C:\mycode\HomePage\docs-initkoa-org` | `local_git_marker_seen` |
| [Rejean-McCormick/Interaction-Kernel](https://github.com/Rejean-McCormick/Interaction-Kernel) | `C:\mycode\Interaction-Kernel\interaction_kernel` | `local_git_marker_seen` |
| [Rejean-McCormick/King-Klown-Canon](https://github.com/Rejean-McCormick/King-Klown-Canon) | `C:\mycode\01-Text_Based_Git\King_Klown\king-clown-canon` | `local_git_marker_seen` |
| [Rejean-McCormick/kOA-Digital-Ecosystem](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem) | `C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem` | `local_git_marker_seen` |
| [Rejean-McCormick/kOA-Linux-Koali](https://github.com/Rejean-McCormick/kOA-Linux-Koali) | `C:\mycode\kOA-Linux\koa-linux` | `local_git_marker_seen` |
| [Rejean-McCormick/kOA-Obama-Foundation-Briefing](https://github.com/Rejean-McCormick/kOA-Obama-Foundation-Briefing) | `C:\mycode\01-Text_Based_Git\kOA-Obama` | `local_git_marker_seen` |
| [Rejean-McCormick/Koali-Control-Panel](https://github.com/Rejean-McCormick/Koali-Control-Panel) | `C:\mycode\kOA-Linux\Koali-Control-Panel` | `local_git_marker_seen` |
| [Rejean-McCormick/Koali-Scenario-Mosaic](https://github.com/Rejean-McCormick/Koali-Scenario-Mosaic) | `C:\mycode\kOA-Linux\Koali_Scenario_Mosaic` | `local_git_marker_seen` |
| [Rejean-McCormick/Koali-Spaces](https://github.com/Rejean-McCormick/Koali-Spaces) | `C:\mycode\kOA-Linux\koali-spaces` | `local_git_marker_seen` |
| [Rejean-McCormick/Kompiler](https://github.com/Rejean-McCormick/Kompiler) | `C:\mycode\Kristal\Kompiler` | `local_git_marker_seen` |
| [Rejean-McCormick/Konductor](https://github.com/Rejean-McCormick/Konductor) | `C:\mycode\Konductor\Konductor` | `local_git_marker_seen` |
| [Rejean-McCormick/Konfid](https://github.com/Rejean-McCormick/Konfid) | `C:\mycode\Konfid\konfid` | `local_git_marker_seen` |
| [Rejean-McCormick/Konnaxion](https://github.com/Rejean-McCormick/Konnaxion) | `C:\mycode\Konnaxion\Konnaxion` | `local_git_marker_seen` |
| [Rejean-McCormick/Konnaxion-Ashoka-Systems-Change-Dossier](https://github.com/Rejean-McCormick/Konnaxion-Ashoka-Systems-Change-Dossier) | `C:\mycode\01-Text_Based_Git\Ashoka` | `local_git_marker_seen` |
| [Rejean-McCormick/Konnaxion-Capsule-Manager](https://github.com/Rejean-McCormick/Konnaxion-Capsule-Manager) | `C:\mycode\Konnaxion\Konnaxion_Capsule_Manager` | `local_git_marker_seen` |
| [Rejean-McCormick/Konnaxion-LevelUpDiag](https://github.com/Rejean-McCormick/Konnaxion-LevelUpDiag) | `` | `local_root_unknown` |
| [Rejean-McCormick/Konnaxion-SecurityDiag](https://github.com/Rejean-McCormick/Konnaxion-SecurityDiag) | `` | `local_root_unknown` |
| [Rejean-McCormick/Konnaxion-Worlds](https://github.com/Rejean-McCormick/Konnaxion-Worlds) | `C:\mycode\Konnaxion\Konnaxion_Worlds` | `local_git_marker_seen` |
| [Rejean-McCormick/KonnaxionDiag](https://github.com/Rejean-McCormick/KonnaxionDiag) | `C:\mycode\Konnaxion\KonnaxionDiag` | `local_git_marker_seen` |
| [Rejean-McCormick/Konstellation](https://github.com/Rejean-McCormick/Konstellation) | `C:\mycode\Konstellation\Konstellation` | `local_git_marker_seen` |
| [Rejean-McCormick/Konstellation-Light](https://github.com/Rejean-McCormick/Konstellation-Light) | `C:\mycode\Konstellation\Konstellation-Light` | `local_git_marker_seen` |
| [Rejean-McCormick/Kristal-Authoring-Kit](https://github.com/Rejean-McCormick/Kristal-Authoring-Kit) | `C:\mycode\Kristal\Kristal-Authoring-Kit` | `local_git_marker_seen` |
| [Rejean-McCormick/Kristal-Farms](https://github.com/Rejean-McCormick/Kristal-Farms) | `C:\mycode\01-Text_Based_Git\Kristal_Farms\kristal-farms` | `local_git_marker_seen` |
| [Rejean-McCormick/Kristal-Framework](https://github.com/Rejean-McCormick/Kristal-Framework) | `C:\mycode\Kristal\Kristal-Framework` | `local_git_marker_seen` |
| [Rejean-McCormick/Kristal-Integration-Pack](https://github.com/Rejean-McCormick/Kristal-Integration-Pack) | `C:\mycode\Kristal\Kristal-Integration-Pack` | `local_git_marker_seen` |
| [Rejean-McCormick/Kristal-Kollection](https://github.com/Rejean-McCormick/Kristal-Kollection) | `C:\mycode\Kristal\Kristal-Kollection` | `local_git_marker_seen` |
| [Rejean-McCormick/Kristal-Manager](https://github.com/Rejean-McCormick/Kristal-Manager) | `C:\mycode\Kristal\Kristal-Manager` | `local_git_marker_seen` |
| [Rejean-McCormick/kristal-public](https://github.com/Rejean-McCormick/kristal-public) | `C:\mycode\Kristal\kristal-public` | `local_git_marker_seen` |
| [Rejean-McCormick/Kristal-Reference](https://github.com/Rejean-McCormick/Kristal-Reference) | `` | `legacy_path_not_found` |
| [Rejean-McCormick/KristalDiag](https://github.com/Rejean-McCormick/KristalDiag) | `C:\mycode\Kristal\KristalDiag` | `local_git_marker_seen` |
| [Rejean-McCormick/KristalV10](https://github.com/Rejean-McCormick/KristalV10) | `` | `legacy_path_not_found` |
| [Rejean-McCormick/LevelUpDiag-kOA-Linux](https://github.com/Rejean-McCormick/LevelUpDiag-kOA-Linux) | `C:\mycode\kOA-Linux\LevelUpDiag-Koali` | `local_git_marker_seen` |
| [Rejean-McCormick/LevelUpDiag-Kristal](https://github.com/Rejean-McCormick/LevelUpDiag-Kristal) | `` | `legacy_path_not_found` |
| [Rejean-McCormick/LevelUpDiag-Orgo](https://github.com/Rejean-McCormick/LevelUpDiag-Orgo) | `C:\mycode\Orgo\LevelUpDiag-Orgo` | `local_git_marker_seen` |
| [Rejean-McCormick/LevelUpDiag_SemantiK-Architect](https://github.com/Rejean-McCormick/LevelUpDiag_SemantiK-Architect) | `C:\mycode\SemantiK_Architect\LevelUpDiag_SemantiK_Architect` | `local_git_marker_seen` |
| [Rejean-McCormick/Mediatheque](https://github.com/Rejean-McCormick/Mediatheque) | `C:\mycode\kOA_Mediatheque\mediatheque` | `local_git_marker_seen` |
| [Rejean-McCormick/Mediatheque-blank](https://github.com/Rejean-McCormick/Mediatheque-blank) | `C:\mycode\kOA_Mediatheque\mediatheque-blank` | `local_git_marker_seen` |
| [Rejean-McCormick/MediKristal](https://github.com/Rejean-McCormick/MediKristal) | `C:\mycode\Kristal\MediKristal\MediKristal` | `local_git_marker_seen` |
| [Rejean-McCormick/MediKristal-LevelUpDiag-](https://github.com/Rejean-McCormick/MediKristal-LevelUpDiag-) | `C:\mycode\Kristal\MediKristal\LevelUpDiag-MediKristal` | `local_git_marker_seen` |
| [Rejean-McCormick/Omni-Wiki](https://github.com/Rejean-McCormick/Omni-Wiki) | `` | `excluded_from_followup` |
| [Rejean-McCormick/Omni-Wiki-Rejean-King-Klown](https://github.com/Rejean-McCormick/Omni-Wiki-Rejean-King-Klown) | `C:\mycode\OmniWiki\Omni-Wiki-Rejean-King-Klown` | `local_git_marker_seen` |
| [Rejean-McCormick/Orgo](https://github.com/Rejean-McCormick/Orgo) | `C:\mycode\Orgo\Orgo` | `local_git_marker_seen` |
| [Rejean-McCormick/Orgo-Worlds](https://github.com/Rejean-McCormick/Orgo-Worlds) | `C:\mycode\Orgo\Orgo_Worlds` | `local_git_marker_seen` |
| [Rejean-McCormick/OurAI](https://github.com/Rejean-McCormick/OurAI) | `` | `excluded_from_followup` |
| [Rejean-McCormick/Partners-for-Public-Good-Pressure-Test-Koali](https://github.com/Rejean-McCormick/Partners-for-Public-Good-Pressure-Test-Koali) | `C:\mycode\01-Text_Based_Git\PPG` | `local_git_marker_seen` |
| [Rejean-McCormick/Pi-Theory](https://github.com/Rejean-McCormick/Pi-Theory) | `C:\mycode\01-Text_Based_Git\Pi-theory\Pi_Theory` | `local_git_marker_seen` |
| [Rejean-McCormick/Power-Dynamics](https://github.com/Rejean-McCormick/Power-Dynamics) | `C:\mycode\01-Text_Based_Git\Power_Dynamics\power_dynamics` | `local_git_marker_seen` |
| [Rejean-McCormick/Projet-ORPHEE-Walk-Straight](https://github.com/Rejean-McCormick/Projet-ORPHEE-Walk-Straight) | `C:\mycode\01-Text_Based_Git\Orphee(Prison)\orphee-walk-straight` | `local_git_marker_seen` |
| [Rejean-McCormick/Rejean-McCormick](https://github.com/Rejean-McCormick/Rejean-McCormick) | `C:\mycode\Rejean_McCormick-OrganisationGit\Rejean-McCormick` | `local_git_marker_seen` |
| [Rejean-McCormick/Science-Silk-Road-Koali](https://github.com/Rejean-McCormick/Science-Silk-Road-Koali) | `C:\mycode\01-Text_Based_Git\Science_Silk_Road\science_silk_road` | `local_git_marker_seen` |
| [Rejean-McCormick/SemantiK-Architect](https://github.com/Rejean-McCormick/SemantiK-Architect) | `C:\mycode\SemantiK_Architect\SemantiK_Architect` | `local_git_marker_seen` |
| [Rejean-McCormick/SemantiK_Runtime_Orchestrator](https://github.com/Rejean-McCormick/SemantiK_Runtime_Orchestrator) | `C:\mycode\SemantiK_Architect\SemantiK_Runtime_Orchestrator` | `local_git_marker_seen` |
| [Rejean-McCormick/SenTient](https://github.com/Rejean-McCormick/SenTient) | `C:\mycode\SenTient\SenTient` | `local_git_marker_seen` |
| [Rejean-McCormick/UCKK](https://github.com/Rejean-McCormick/UCKK) | `` | `ambiguous_repository_identity` |
| [Rejean-McCormick/UCKK-Assets](https://github.com/Rejean-McCormick/UCKK-Assets) | `C:\mycode\UCKK\UCKK_Assets` | `local_git_marker_seen` |
| [Rejean-McCormick/UCKK-Ops-Console](https://github.com/Rejean-McCormick/UCKK-Ops-Console) | `C:\mycode\UCKK\UCKK_ops_console` | `local_git_marker_seen` |
| [Rejean-McCormick/VotingMachine](https://github.com/Rejean-McCormick/VotingMachine) | `C:\mycode\02-Experimental\VotingMachine\VotingMachine` | `local_git_marker_seen` |

## Newly user-reported repository (1; pending verification)

| GitHub repository | Local root | Status |
|---|---|---|
| [Rejean-McCormick/BoKristal](https://github.com/Rejean-McCormick/BoKristal) | `C:\mycode\BoKristal\BoKristal` | `user_reported_git_path` |

Reported `.git` marker: `C:\mycode\BoKristal\BoKristal\.git`.

**Verification:** GitHub access through the current connector returned HTTP 404 for this repository; this does not prove nonexistence, since it could be private or inaccessible. The Windows checkout and Git remote mapping were not inspected directly. The record's `scope` is `USER_REPORTED`, not `PUBLIC`.

## Other local, external and wiki checkouts (49)

| Repository | Local root | Status |
|---|---|---|
| `Rejean-McCormick/Business-Plan` | `C:\mycode\01-Text_Based_Git\Business-plan` | `local_git_marker_seen` |
| `Rejean-McCormick/kOA-International-Strategy` | `C:\mycode\01-Text_Based_Git\International-Strategy` | `local_git_marker_seen` |
| `Rejean-McCormick/king-klown-canon.wiki` | `C:\mycode\01-Text_Based_Git\King_Klown\king-klown-canon.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/Kristal_Farms.wiki` | `C:\mycode\01-Text_Based_Git\Kristal_Farms\Kristal_Farms.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/Pi-Theory.wiki` | `C:\mycode\01-Text_Based_Git\Pi-theory\Pi-Theory.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/Power-Dynamics.wiki` | `C:\mycode\01-Text_Based_Git\Power_Dynamics\Power-Dynamics.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/science-silk-road-koali.wiki` | `C:\mycode\01-Text_Based_Git\Science_Silk_Road\science-silk-road-koali.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/Ame-Artificielle.wiki` | `C:\mycode\02-Experimental\AmeArtificielle\Ame-Artificielle.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/Astro-App` | `C:\mycode\02-Experimental\Astro-App\astro_app` | `local_git_marker_seen` |
| `Rejean-McCormick/Math-Challenges` | `C:\mycode\02-Experimental\MathChallenges` | `local_git_marker_seen` |
| `Rejean-McCormick/Voxtral-Audiobook-Studio` | `C:\mycode\02-Experimental\Voxtral_Audiobook_Studio\Voxtral_Audiobook_Studio` | `local_git_marker_seen` |
| `MA-Gustave/MA-Gustave` | `C:\mycode\03-Brands\Gustave\GitHub_Profile` | `local_git_marker_seen` |
| `Rejean-McCormick/theophile-mini-site` | `C:\mycode\03-Brands\Theophile\theophile-mini-site` | `local_git_marker_seen` |
| `Alfresco/alfresco-community-repo` | `C:\mycode\Alfresco\alfresco-community-repo` | `local_git_marker_seen` |
| `Rejean-McCormick/Ariane` | `C:\mycode\Ariane\Ariane` | `local_git_marker_seen` |
| `MA-Gustave/ars-magna-lulli` | `C:\mycode\Grammatical_Framework\ars-magna-lulli\ars-magna-lulli` | `local_git_marker_seen` |
| `GrammaticalFramework/gf-core` | `C:\mycode\Grammatical_Framework\gf-core` | `local_git_marker_seen` |
| `GrammaticalFramework/gf-rgl` | `C:\mycode\Grammatical_Framework\gf-rgl` | `local_git_marker_seen` |
| `krangelov/gf-wikidata` | `C:\mycode\Grammatical_Framework\gf-wikidata_repos_source\gf-wikidata` | `local_git_marker_seen` |
| `GrammaticalFramework/gf-wikidata-tools` | `C:\mycode\Grammatical_Framework\gf-wikidata_repos_source\gf-wikidata-tools` | `local_git_marker_seen` |
| `foerstner-lab/GFF_to_Wikidata_importer` | `C:\mycode\Grammatical_Framework\gf-wikidata_repos_source\GFF_to_Wikidata_importer` | `local_git_marker_seen` |
| `MA-Gustave/GF_Observatory` | `C:\mycode\Grammatical_Framework\GF_Observatory` | `local_git_marker_seen` |
| `MA-Gustave/GF_RGL_AI_Compendium` | `C:\mycode\Grammatical_Framework\GF_RGL_AI_Compendium` | `local_git_marker_seen` |
| `MA-Gustave/GF_Wordbench` | `C:\mycode\Grammatical_Framework\GF_Wordbench\GF_Wordbench` | `local_git_marker_seen` |
| `Rejean-McCormick/kOA_Digital_Ecosystem.wiki` | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\kOA Digital Ecosystem` | `previous_gitsink_observation_only` |
| `Rejean-McCormick/Konnaxion.wiki` | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\Konnaxion` | `previous_gitsink_observation_only` |
| `Rejean-McCormick/kristal-framework.wiki` | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\Kristal Framework` | `previous_gitsink_observation_only` |
| `Rejean-McCormick/Orgo.wiki` | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\Orgo` | `previous_gitsink_observation_only` |
| `Rejean-McCormick/SemantiK_Architect.wiki` | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\SemantiK Architect` | `previous_gitsink_observation_only` |
| `Rejean-McCormick/SenTient.wiki` | `C:\mycode\HomePage\docs-initkoa-org\.wiki-cache\SenTient` | `previous_gitsink_observation_only` |
| `Rejean-McCormick/Kamel` | `C:\mycode\Kamel\Kamel` | `local_git_marker_seen` |
| `Rejean-McCormick/kOA-Linux_Koali.wiki` | `C:\mycode\kOA-Linux\koa-linux-wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/kOA_Digital_Ecosystem.wiki` | `C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/Konfid.wiki` | `C:\mycode\Konfid\Konfid.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/Konnaxion.wiki` | `C:\mycode\Konnaxion\Konnaxion.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/kristal-framework.wiki` | `C:\mycode\Kristal\kristal-framework.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/MediKristal.wiki` | `C:\mycode\Kristal\MediKristal\MediKristal.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/LevelUpDiag` | `C:\mycode\LevelUpDiag\LevelUpDiag` | `local_git_marker_seen` |
| `Rejean-McCormick/Orgo.wiki` | `C:\mycode\Orgo\Orgo.wiki` | `local_git_marker_seen` |
| `GrammaticalFramework/gf-rgl` | `C:\mycode\SemantiK_Architect\gf-rgl` | `local_git_marker_seen` |
| `Rejean-McCormick/SemantiK_Architect.wiki` | `C:\mycode\SemantiK_Architect\SemantiK_Architect.wiki` | `local_git_marker_seen` |
| `Rejean-McCormick/SenTient.wiki` | `C:\mycode\SenTient\SenTient.wiki` | `local_git_marker_seen` |
| `MA-Gustave/simdjson-rvv-vla` | `C:\mycode\Simdjson\simdjson-rvv-vla` | `local_git_marker_seen` |
| `simdjson/simdjson` | `C:\mycode\Simdjson\simdjson-upstream` | `local_git_marker_seen` |
| `Rejean-McCormick/SwarmCraft` | `C:\mycode\SwarmCraft\SwarmCraft` | `local_git_marker_seen` |
| `Rejean-McCormick/tools` | `C:\mycode\Tools\toolz` | `local_git_marker_seen` |
| `Rejean-McCormick/KeyFlow` | `C:\mycode\UCKK\KeyFlow(formulaires)` | `local_git_marker_seen` |
| `moodle/moodle` | `C:\mycode\UCKK\moodle\moodle` | `local_git_marker_seen` |
| `Rejean-McCormick/UCKK-Moodle` | `C:\mycode\UCKK\uckk-moodle` | `local_git_marker_seen` |

## Source and interpretation

Machine-readable inventory: [`repositories.json`](repositories.json).
Preserved legacy entries that could not be safely reconciled are listed in the accompanying report, not silently reassigned.
A `.git` marker is not proof of remote identity, clean state, push authorization, publication, activation or release qualification.
