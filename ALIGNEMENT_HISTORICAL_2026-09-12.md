> **HISTORICAL — superseded by `ALIGNEMENT_UPDATED_2026-09-16.md`.** This file is retained only for change history.

# Alignement global de l'écosystème kOA / Kristal

## Statut

Ce document définit l'architecture cible commune de l'écosystème.

Il décrit uniquement ce qui doit être vrai dans l'état aligné : responsabilités, ownership, frontières, contrats, identités, flux et invariants. Il ne décrit pas un processus de migration et ne crée pas d'autorité supplémentaire au-dessus des systèmes existants.

**Mise à jour 2026-09-12.** Les invariants observés et validés sur la vertical slice UCKK-A014 sont intégrés ci-dessous comme contraintes d'architecture : `IntegrationOperation`/Outbox côté Orgo, bridge provider-owned côté Konnaxion, sémantique `accepted ≠ succeeded`, redrive canonique, idempotency/correlation, absence de write SQL cross-system et conservation explicite de l'autorité décisionnelle Konnaxion/eThikos et du rôle optionnel de diffusion d'UCKK.

Les systèmes principaux sont :

- **Konnaxion** — domaine civique/public, délibération, consultation, lecture collective, expertise contextuelle et surfaces applicatives ;
- **Orgo** — workflow, orchestration, Cases, Tasks, routing, lifecycle et état opérationnel gouverné ;
- **SemantiK Architect** — génération sémantique et linguistique multilingue planner-first ;
- **Kristal** — système épistémique déterministe : spécification normative, artifacts, compilation, validation, identité, query, federation, Runtime Packs et implémentation conforme ;
- **kOA-Linux** — système d'exploitation/environnement local-first qui possède la frontière de plateforme : composants, profiles, ressources, trust, privilèges, lifecycle, artifacts locaux, activation, recovery et offline continuity.

Les systèmes secondaires et spécialisés se branchent sur ces frontières sans redéfinir leurs primitives centrales.

---

# 1. Modèle architectural global

## 1.1 Pas de hiérarchie artificielle entre systèmes

Konnaxion, Orgo, SemantiK Architect et Kristal sont des systèmes autonomes. kOA-Linux peut les héberger, les intégrer ou leur fournir une frontière locale de plateforme, mais ne devient pas propriétaire de leurs domaines internes.

```text
                       ┌───────────────────────┐
                       │       KRISTAL         │
                       │ spec + artifacts +    │
                       │ implementation        │
                       └───────┬───────┬───────┘
                               │       │
                      contracts│       │contracts
                               │       │
              ┌────────────────┘       └────────────────┐
              ▼                                         ▼
       ┌─────────────┐                           ┌──────────────────┐
       │    ORGO     │◄──── explicit boundary ─►│ SEMANTIK         │
       │ workflow    │                           │ ARCHITECT        │
       └──────┬──────┘                           │ NLG              │
              │                                  └────────┬─────────┘
              │ explicit boundary                        │
              ▼                                          │
       ┌─────────────┐◄──────────────────────────────────┘
       │  KONNAXION  │
       │ civic/public│
       └─────────────┘

-------------------------------------------------------------------
                      kOA-LINUX PLATFORM BOUNDARY
-------------------------------------------------------------------
 local-first • profiles • components • trust • resources • privilege
 artifacts • lifecycle • offline • activation • recovery • evidence
```

Le dessin ne signifie pas que chaque paire possède nécessairement une intégration active. Il signifie que toute intégration qui existe entre deux systèmes doit respecter les frontières définies ici.

## 1.2 Kristal est un seul système

Kristal n'est pas séparé en deux produits architecturaux.

```text
Kristal
├── Kristal Specification
│   ├── Core Specification
│   ├── JSON Schemas
│   ├── identity / canonicalization / hashing
│   ├── validation / authority / reader policy
│   ├── query contract
│   ├── reproducibility rules
│   ├── profiles
│   ├── integration contracts
│   ├── security rules
│   └── examples / test vectors
│
└── Kristal implementation
    ├── compiler
    ├── validators
    ├── canonicalization / hashing implementation
    ├── artifact builders
    ├── query implementation
    ├── federation tooling
    ├── Runtime Pack tooling
    └── conformance tooling
```

La Specification est normative. L'implémentation exécute cette specification. Les deux appartiennent au même système Kristal.

## 1.3 kOA-Linux possède directement son architecture de plateforme

Il n'existe pas de système séparé au-dessus de kOA-Linux pour porter ses invariants.

kOA-Linux définit directement, dans ses contracts machine et sa documentation normative :

- les constitutional/system invariants ;
- les architectural layers ;
- les operating modes ;
- les deployment profiles et overlays ;
- les component contracts ;
- les data/authority boundaries ;
- les release channels et artifact classes ;
- les trust et privilege boundaries ;
- les resource governance rules ;
- les offline/degradation rules ;
- les activation/recovery rules ;
- les validators et conformance evidence.

---

# 2. Lois d'alignement globales

## 2.1 Owner unique de l'état autoritaire

Tout état autoritaire possède un owner logique identifiable.

Un autre système peut :

- demander une mutation ;
- lire une projection ;
- recevoir un événement ;
- transporter un artifact ;
- calculer une dérivation ;
- conserver un receipt ;
- afficher l'état ;

mais cela ne lui transfère pas l'ownership de la source.

## 2.2 Aucun write direct inter-domaines

Un système ne modifie pas directement les tables, stores ou structures autoritaires d'un autre système comme mécanisme d'intégration.

```text
sender
  ↓
versioned boundary
  ↓
receiver validates / authorizes
  ↓
receiver mutates its own state
```

La co-localisation sur un même host, une même base physique ou un même cluster ne change pas cette règle.

## 2.3 Source ≠ projection

```text
source state
≠ cache
≠ index
≠ analytics projection
≠ search projection
≠ reading
≠ rendered output
≠ UI state
```

Une projection peut être reproductible, materialized et performante sans devenir source authority.

## 2.4 Intégrité ≠ autorité

```text
bytes received
≠ artifact parsed
≠ digest valid
≠ signature valid
≠ signer trusted for this scope
≠ operation authorized
≠ artifact admitted
≠ artifact activated
```

Chaque transition critique garde sa sémantique propre.

## 2.5 Workflow ≠ état métier ≠ état épistémique

```text
Orgo Task / Case lifecycle
≠ Konnaxion civic state
≠ Kristal assertion / validation / recognition state
≠ Architect generation state
≠ kOA-Linux activation state
```

Une décision dans un axe ne devient jamais automatiquement une décision dans un autre axe.

## 2.6 Présentation ≠ autorité

Une route, page, widget, sidebar, label visible, texte généré ou résultat de recherche n'est pas une source autoritaire du domaine présenté.

## 2.7 Dérivation explicite

Toute donnée dérivée importante doit pouvoir déclarer, selon son contrat :

- la source ;
- l'identité de la transformation ;
- le scope ;
- les paramètres ;
- les versions nécessaires ;
- la provenance ;
- le moment/snapshot pertinent ;
- le résultat.

## 2.8 Interopérabilité minimale

Une frontière ne recopie pas le modèle interne complet de son voisin. Elle expose seulement ce qui est requis pour le use case.

## 2.9 Version et compatibility explicites

Tout contrat critique versionné définit :

- son identité ;
- sa version ;
- ses règles de compatibility ;
- sa réponse aux versions non supportées ;
- son comportement face aux champs inconnus lorsque pertinent.

## 2.10 Fail closed aux frontières d'intégrité ou d'autorité

Lorsqu'une opération déclare une exigence d'intégrité, de trust, de compatibility ou d'autorisation, l'incertitude sur cette exigence ne devient pas un succès implicite.

---

# 3. Modèle commun des frontières

## 3.1 Classes d'interaction

Les classes suivantes restent distinctes.

### Command

Demande de mutation adressée à l'owner.

Une command :

- exprime une intention ;
- ne prouve pas l'autorité ;
- ne prouve pas l'exécution ;
- ne devient effective qu'après validation et commit par le receiver.

### Query

Demande de projection/lecture.

Une query :

- ne transfère pas l'ownership ;
- ne mute pas la source ;
- peut déclarer freshness, snapshot, pagination, redaction et scope.

### Domain event

Annonce d'un fait déjà commis par le publisher.

Un event :

- décrit un fait ;
- n'est pas une command déguisée ;
- peut être replayable ;
- permet au consumer de modifier seulement son propre état ou d'émettre une nouvelle command.

### Asynchronous job

Travail différé avec identité, statut observable et résultat.

Le résultat ne devient autoritaire que via le commit path du système qui possède l'état final.

### Artifact

Contenu immutable ou versionné traversant une frontière.

Son usage dépend du schema, de l'identité, de l'intégrité, du scope, de la compatibility et de l'admission par le receiver.

### Candidate / proposal

Matériau proposé, non autoritaire pour le receiver tant qu'il n'a pas été explicitement accepté/admis.

### Controlled read model

Projection dérivée destinée à des consumers déclarés.

Elle reste dérivée tant qu'un contrat ne lui attribue pas explicitement une autorité propre.

### Policy decision request

Demande d'autorisation, consentement, disclosure ou décision de policy dans le scope déclaré.

### Resource request

Demande de ressources ou de scheduling. Un resource grant n'est pas une autorisation métier ou d'activation.

### Gateway transfer

Passage par une boundary spécialisée : publication, ingestion, disclosure, evidence, privilege ou autre gateway.

### External integration call

Invocation d'une capacité externe remplaçable. Le résultat externe n'est pas automatiquement autoritaire localement.

### Receipt

Preuve structurée d'une transition, d'un refus, d'une acceptation ou d'une exécution.

Un receipt ne remplace pas l'état autoritaire qu'il atteste.

## 3.2 Envelope minimale

Lorsqu'applicable, une frontière doit pouvoir porter :

- interface/artifact type ;
- contract version ;
- request/event/job/artifact ID ;
- sender ;
- intended receiver ;
- tenant / organization / environment / scope ;
- actor/subject context ;
- operation ;
- correlation ID ;
- causal reference ;
- idempotency/replay identity ;
- payload schema/media type ;
- policy/authority references ;
- creation/expiry information ;
- compatibility/release context ;
- trace/evidence context ;
- expected result channel.

Aucun champ n'est requis globalement s'il n'a aucune sémantique pour le contrat concerné.

---

# 4. Konnaxion

## 4.1 Domaine

Konnaxion possède son domaine civique/public et ses surfaces applicatives.

L'alignement conserve les frontières internes déjà définies dans ethiKos Kintsugi parce qu'elles empêchent le mélange entre source facts, délibération, vote, readings et expertise contextuelle.

Le principe structurant est :

> **Single Truth, Multiple Readings.**

Une source civique reste stable. Plusieurs readings déclarées peuvent l'interpréter sans la réécrire.

## 4.2 Korum

Korum est le sous-domaine de délibération structurée.

### Korum possède

- topics ;
- stances ;
- arguments et replies ;
- threaded argument graph ;
- argument moderation ;
- état de participation propre à la délibération ;
- Kialo-style structured deliberation lorsqu'elle est réalisée nativement.

Dans l'implémentation actuelle, les objets existants qui ancrent cette surface incluent :

- `EthikosTopic` ;
- `EthikosStance` ;
- `EthikosArgument` ;
- `EthikosCategory`.

### Korum maintient

- topic-level stance distinct de claim/argument-level evaluation ;
- structure d'argument distincte de l'agrégation Smart Vote ;
- moderation auditable ;
- compatibilité avec la surface `/ethikos/*` existante.

### Korum ne fait pas

- la pondération Smart Vote ;
- la mutation des readings Smart Vote ;
- la mutation des snapshots EkoH ;
- l'absorption silencieuse des ballots Konsultations ;
- l'import d'un modèle externe comme nouvelle source de vérité.

## 4.3 Konsultations

Konsultations possède la consultation, l'intake, le ballot et l'accountability associés.

### Konsultations possède

- issue intake ;
- citizen suggestions ;
- deduplication/scoping de consultation ;
- consultations ;
- consultation prompts ;
- ballot capture ;
- result snapshots ;
- impact tracking ;
- feedback/accountability records associés.

### Invariants

- les ballots restent source facts ;
- les result snapshots restent auditables ;
- Smart Vote lit les sources mais ne les mute pas ;
- EkoH peut fournir du contexte mais ne mute pas les ballots ;
- citizen suggestion, ballot formel et stance de délibération ne sont pas le même objet.

## 4.4 Smart Vote

Smart Vote possède les **derived readings** et leur publication.

### Smart Vote possède

- lens declarations ;
- baseline result publication ;
- derived readings ;
- weighted/cohort-filtered readings ;
- aggregations ;
- result comparison payloads ;
- audit metadata de la reading.

### Règle centrale

```text
Reading = f(BaselineEvents, LensDeclaration, SnapshotContext?)
```

Une reading publiée doit être explicable et reproductible à partir de ses inputs déclarés.

### Une reading garde au minimum, lorsque le contrat applicable le requiert

- `reading_key` ;
- `lens_hash` ;
- `snapshot_ref` lorsque du contexte EkoH est utilisé ;
- `computed_at` ;
- référence au topic/consultation ;
- `results_payload`.

### Smart Vote ne fait pas

- mutation des Korum source records ;
- mutation des ballots Konsultations ;
- remplacement silencieux de la baseline ;
- dissimulation des hypothèses de pondération ;
- appropriation des raw votes/stances/arguments/ballots.

## 4.5 Baseline et readings

La baseline est l'agrégation non pondérée des source events concernés.

Exemples :

- raw topic stances ;
- raw consultation ballots ;
- raw participation counts ;
- raw argument graph state.

Lorsqu'une derived reading est présentée comme résultat, la baseline doit rester identifiable et disponible conformément au contrat de présentation du produit.

Une reading n'est jamais rétroactivement convertie en source fact.

## 4.6 EkoH dans Konnaxion

EkoH possède le contexte d'expertise, d'éthique et de trust utilisé par les surfaces qui en ont besoin.

### EkoH possède

- expertise profiles/context ;
- domain vectors ;
- ethics context ;
- cohort eligibility ;
- credibility/trust signals ;
- snapshots ;
- audit context pertinent aux readings pondérées.

### EkoH peut

- fournir un `snapshot_ref` ;
- fournir une eligibility/cohort decision ;
- fournir un expertise-weighting context ;
- fournir un ethics-adjustment context ;
- contribuer à l'explainability.

### EkoH ne fait pas

- l'enregistrement autoritaire des civic votes ;
- la mutation des stances ;
- la mutation des ballots ;
- la mutation post-publication d'une reading Smart Vote ;
- la décision directe d'un résultat de vote ;
- le remplacement d'un decision protocol transparent.

## 4.7 Séparation des types de participation

Les concepts suivants restent séparés :

| Concept | Owner | Niveau | Sémantique |
|---|---|---|---|
| `EthikosStance` | Korum | topic | position utilisateur sur un topic |
| `ArgumentImpactVote` | Korum | argument/claim | impact/relevance d'un argument dans son graphe |
| ballot event | Konsultations | consultation/decision | input formel d'un protocol de décision |
| `ReadingResult` | Smart Vote | dérivé | agrégation/interprétation déclarée |

```text
ArgumentImpactVote ≠ EthikosStance
ArgumentImpactVote ≠ Smart Vote ballot
EthikosStance ≠ ReadingResult
ReadingResult ≠ source fact
EkoH snapshot ≠ vote
```

## 4.8 Kialo-style deliberation

Kialo est une référence de pattern, pas un nouveau domaine autoritaire.

Le pattern est implémenté comme **native mimic** sous Korum :

```text
Discussion        → EthikosTopic
Claim             → EthikosArgument
Pro/con relation  → parent + side
Impact vote       → ArgumentImpactVote
Source            → source/evidence structure
Perspective       → declared context/reading surface
```

Il ne crée pas une base ou un core parallèle.

## 4.9 External tools

Un outil externe est soit :

- mimicked nativement ;
- intégré par adapter ;
- intégré comme sidecar/annex remplaçable.

Il ne doit pas :

- écrire directement dans les Korum core tables ;
- écrire directement dans les Konsultations core tables ;
- devenir source of truth pour les civic outcomes ;
- contourner les services et ownership rules.

## 4.10 Surface d'implémentation actuelle

Les surfaces actuelles à préserver comme réalités d'implémentation sont notamment :

```text
backend app:  konnaxion.ethikos
API family:   /api/ethikos/*
UI family:    /ethikos/*
```

Les pages `/ethikos/decide`, `/ethikos/deliberate`, `/ethikos/trust`, `/ethikos/pulse`, `/ethikos/impact`, `/ethikos/learn`, `/ethikos/insights` et `/ethikos/admin` appartiennent à la surface Konnaxion et ne doivent pas être remappées vers des abstractions externes sans nécessité réelle.

---

# 5. Orgo

## 5.1 Domaine

Orgo est le moteur de workflow et d'état opérationnel gouverné.

Il coordonne le travail sans absorber l'état métier des systèmes qu'il orchestre.

## 5.2 Backbone multi-tenant

`Organization` constitue le contexte organisationnel/tenant central.

Les opérations métier importantes portent explicitement l'`organization_id` ou l'identité organisationnelle équivalente attendue par leur contrat.

L'isolation cross-organization est une contrainte de base et non une option de présentation.

## 5.3 Task

**Task est l'unité canonique de travail.**

Le modèle commun Task porte notamment :

- organization ;
- optional Case linkage ;
- source ;
- type/domain ;
- category ;
- subtype ;
- canonical label ;
- title/description ;
- status ;
- priority ;
- severity ;
- visibility ;
- ownership/assignment ;
- deadlines/reactivity/escalation ;
- metadata.

Le code actuel expose les statuts canoniques :

```text
PENDING
IN_PROGRESS
ON_HOLD
COMPLETED
FAILED
ESCALATED
CANCELLED
```

Ces valeurs appartiennent au lifecycle Orgo et ne doivent pas être réutilisées pour représenter un lifecycle Kristal ou Konnaxion.

## 5.4 Case

**Case est le conteneur durable de contexte et de travail.**

Il groupe Tasks, contexte, historique et traitement sur une durée plus longue.

Le code actuel expose :

```text
open
in_progress
resolved
archived
```

pour le Case lifecycle.

Un Case peut référencer des artifacts externes sans devenir propriétaire de leur schema ou de leur contenu.

## 5.5 Routing et labels

Le label Orgo canonique conserve la forme documentée :

```text
<BASE>.<CATEGORY><SUBCATEGORY>.<HORIZONTAL_ROLE>
```

Le label sert au routing, à l'organisation et aux flows Orgo. Il n'est pas une taxonomie universelle imposée aux systèmes externes.

Les broadcast bases `10`, `100`, `1000` restent informationnelles par défaut tant qu'une workflow rule ne crée pas explicitement du travail obligatoire.

## 5.6 Domain modules

Les domain modules sont des adapters/refinements autour du core.

Ils :

- utilisent le Task/Case model partagé ;
- réutilisent Task Handler et Workflow Engine ;
- utilisent config/metadata/hooks pour leurs variations ;
- ne créent pas leurs propres Task tables ;
- ne créent pas un lifecycle Task incompatible ;
- ne write pas directement la DB en contournant le Task Handler lorsqu'une mutation appartient au core.

## 5.7 Workflow Engine

Le Workflow Engine possède :

- rule evaluation ;
- routing ;
- state progression du workflow ;
- conditions/gates opérationnels ;
- dispatch vers les services/domain owners ;
- reconciliation des résultats.

Il ne transforme pas un outcome externe en state Orgo sans mapping explicite.

## 5.8 Task Handler

Le Task Handler reste l'entrée commune pour :

- create ;
- update ;
- assign ;
- escalate ;
- status transitions ;
- validations propres à Task.

Les domain modules et interfaces réutilisent cette surface plutôt que d'implémenter leur propre lifecycle.

## 5.9 Audit et Task Events

Les transitions importantes sont représentées par les structures Orgo prévues à cet effet :

- `TaskEvent` ;
- `TaskAssignment` ;
- `ActivityLog` ;
- `SecurityEvent` ;
- workflow transition/event records selon leur scope.

L'audit capture l'action et ses références ; il ne devient pas l'owner de l'objet métier observé.

## 5.10 Insights / cyclic overview

Les patterns détectés peuvent devenir du travail gouverné.

Lorsqu'un pattern exige une action, le flux correct est :

```text
pattern/insight
→ Case/Task creation via Orgo core
→ normal lifecycle
```

Un chart ou une analytics projection n'est pas le workflow.

## 5.11 Orgo et les systèmes externes

Orgo peut :

- référencer leur state/artifacts ;
- leur envoyer commands/jobs/proposals ;
- recevoir events/receipts/results ;
- déclencher du travail ;
- suivre une opération ;
- conserver l'audit et la correlation.

Orgo ne :

- write pas directement leurs stores autoritaires ;
- transforme pas automatiquement leur lifecycle en Task/Case lifecycle ;
- redéfinit pas leurs schemas dans le core Task/Case.

## 5.12 IntegrationOperation et Outbox

Les effets externes durables déclenchés par Orgo utilisent une séparation explicite entre le travail métier et l'état de livraison externe.

```text
Case / Task / workflow state
        ↓
IntegrationOperation
        +
OutboxMessage
        ↓
worker
        ↓
provider adapter
        ↓
external owner
        ↓
receipt / retry / failure
```

### IntegrationOperation possède l'état de publication externe

Une `IntegrationOperation` représente l'opération adressée à un provider. Elle reste distincte du lifecycle du `Case` et des `Task`.

Les champs structurants incluent, selon le contrat :

- organization ;
- provider ;
- operation ;
- subject type / subject ID ;
- external reference ;
- status ;
- idempotency key ;
- correlation ID ;
- request metadata ;
- receipt / error ;
- started/completed timestamps.

Les états opérationnels doivent distinguer au minimum les situations équivalentes à :

```text
PENDING
RUNNING
SUCCEEDED
FAILED
```

Invariant :

```text
IntegrationOperation.status
≠ Case.status
≠ Task.status
```

### Outbox possède la livraison fiable

L'`OutboxMessage` transporte l'effet externe après le commit de l'état métier Orgo.

```text
business mutation
+ IntegrationOperation
+ OutboxMessage
        ↓ same transaction / atomic business boundary
commit
        ↓
worker claims message
        ↓
provider adapter
```

Les états de livraison doivent distinguer au minimum les situations équivalentes à :

```text
PENDING
PROCESSING
SUCCEEDED
DEAD
```

`OutboxMessage.SUCCEEDED` signifie que le message a été livré selon la sémantique du provider. Il ne signifie pas nécessairement que l'opération externe est finalisée si le provider a seulement répondu `accepted`.

### Redrive canonique

Un message terminalement échoué n'est pas réparé par mutation SQL manuelle.

Le redrive passe par la boundary Orgo prévue à cet effet et remet l'opération dans un état retriable tout en conservant :

- l'identity de l'opération ;
- la correlation ;
- l'idempotency identity ;
- l'audit ;
- le lien avec le message d'origine.

Un redrive ne doit pas créer silencieusement une nouvelle business operation lorsqu'une opération existante peut être reprise.

### Configuration de provider

Le provider Konnaxion est configuré explicitement, par exemple via :

```text
KONNAXION_BRIDGE_URL
KONNAXION_BRIDGE_TOKEN
```

Les credentials/tokens de bridge sont secrets d'exécution :

- ils ne sont pas des identifiers métier ;
- ils ne doivent pas être loggés ;
- ils ne doivent pas être intégrés dans les artifacts de documentation ;
- leur persistence éventuelle doit respecter la boundary de secrets du runtime.
---

# 6. SemantiK Architect

## 6.1 Domaine

SemantiK Architect est un système NLG multilingue **planner-centered**, **construction-centered** et **backend-flexible**.

Il reçoit du semantic input et produit du texte/surface output structuré et traçable.

Il n'est pas une base de connaissance et n'est pas un renderer-first system.

## 6.2 Source of runtime truth

Le planner et le shared construction runtime définissent **ce qui est dit**.

Aucun renderer, grammar backend ou router ne devient une source indépendante de sentence-planning truth.

## 6.3 Pipeline nominal

```text
API/request
→ frame normalization
→ frame-to-plan bridge lorsque requis
→ planner
→ PlannedSentence
→ ConstructionPlan
→ lexical resolution
→ renderer backend
→ SurfaceResult
→ public response mapping
```

Les deux objets internes structurants restent :

- `PlannedSentence` ;
- `ConstructionPlan`.

Le renderer reçoit une intention déjà structurée ; il ne reconstruit pas arbitrairement la sémantique.

## 6.4 Input boundary

La surface publique canonique de génération est :

```text
POST /api/v1/generate/{lang_code}
```

Les payloads peuvent prendre plusieurs formes supportées, mais ils convergent vers la normalisation et le domain input partagé.

Une intégration externe doit mapper vers cette abstraction sémantique ou vers un contract runtime explicitement équivalent ; elle ne doit pas piloter directement des détails internes de renderer.

## 6.5 Lexicon

Lexical resolution reste une couche partagée entre planning et realization.

Elle lie :

- planned slots ;
- lexical entries ;
- morphology-relevant metadata ;
- provenance lexicale lorsque disponible.

La même ConstructionPlan peut être réalisée par plusieurs backends sans que chacun redéfinisse l'intention.

## 6.6 Backends

Les backends peuvent inclure :

- GF/PGF ;
- family-oriented renderers ;
- curated/override layers ;
- safe-mode/fallback renderer.

GF est un backend de réalisation et une source de tooling grammatical ; il n'est pas l'architecture entière et ne remplace pas le planner.

## 6.7 Context/discourse

Le contexte/discourse state est cross-cutting.

Il influence planning/reference choice via le planner/runtime lorsqu'il est activé. Il ne doit pas être réalisé comme une série de rewrites ad hoc après la surface realization.

## 6.8 Compatibility path

Le runtime peut conserver un compatibility path qui contourne une partie du pipeline planner-centered pour certains cas actuels.

Ce path doit rester identifiable comme compatibility/fallback behavior. Il ne redéfinit pas la source of truth architecturale.

## 6.9 Public response vs internal objects

Les serializers publics :

- exposent le contrat public ;
- peuvent exposer diagnostics/debug metadata ;
- ne doivent pas inventer des planner-first facts absents ;
- ne doivent pas faire passer `debug_info` pour le seul emplacement d'une information nominale requise.

`SurfaceResult` reste un objet runtime interne distinct du public API response.

## 6.10 Intégration avec une source de connaissance

Lorsqu'Architect génère à partir de Kristal ou d'une autre source knowledge-backed :

- la source fournit le contenu/metadata autorisés ;
- le profile d'intégration définit la projection sémantique ;
- Architect reste owner du planning linguistique ;
- la provenance/trace demandée est conservée ;
- une contrainte no-new-facts peut être imposée par le mode/profile concerné sans transformer Kristal en moteur NLG.

---

# 7. Kristal

## 7.1 Définition

Kristal est un système déterministe et portable d'artifacts épistémiques.

Il compile des **Structured Epistemic States** vers des artifacts immutables, queryables et vérifiables tout en gardant séparés :

```text
compilation
≠ validation

artifact existence
≠ artifact integrity

assertion status
≠ certainty level
≠ validation status
≠ authority recognition
≠ reader visibility
≠ runtime activation
```

## 7.2 Kristal Specification et implementation

La partie normative de Kristal définit le contrat.

La future implementation Kristal doit se conformer à :

- normative prose ;
- JSON Schemas ;
- canonicalization rules ;
- identity/hash rules ;
- examples ;
- golden/test vectors ;
- query contract ;
- integration profiles ;
- security rules.

L'implémentation n'acquiert pas le droit de modifier silencieusement la sémantique simplement parce qu'elle produit un résultat différent.

## 7.3 Normative input

Le **Structured Epistemic State** est l'unité d'entrée normative de Kristal v5.

Il peut porter explicitement :

- assertions/content ;
- provenance ;
- scope ;
- certainty lorsque applicable ;
- validation metadata lorsque applicable ;
- authority references lorsque applicable ;
- references nécessaires à la compilation ;
- profile/extension data déclarée.

`Claim-IR` peut être utilisé par des extractors/resolvers/pipelines mais ne devient pas une entrée universelle obligatoire.

## 7.4 Pipeline

Le pipeline général est :

```text
Signal / Draft / Dataset
        ↓
Structured Epistemic State
        ↓
Compile
        ↓
Working Artifact / Working Exchange
        ↓
Review / Validation / Attestation / Federation
        ↓
Authority Recognition lorsque applicable
        ↓
Reference Artifact / Reference Exchange lorsque applicable
        ↓
Distribution / Runtime Pack / Reader Policy
```

Toutes les étapes ne sont pas obligatoires dans tous les profiles.

## 7.5 Compilation

Compilation produit une représentation portable/reproductible à partir d'un input normatif.

Compilation ne signifie pas validation.

Un Working Exchange peut contenir des assertions :

- unvalidated ;
- disputed ;
- fictional ;
- mythological ;
- speculative ;
- low-certainty ;
- incomplete ;

si ces états sont explicitement représentés.

## 7.6 Assertion status

`assertion_status` représente l'état de l'assertion dans son axe propre.

Il ne doit pas servir à encoder simultanément :

- certainty ;
- validation ;
- authority recognition ;
- reader visibility ;
- activation.

Toute transition appartient à l'enum/lifecycle de cet axe.

## 7.7 Certainty

`certainty_level` représente la certitude déclarée dans le scope applicable.

La certainty :

- n'est pas une signature ;
- n'est pas une validation ;
- n'est pas une recognition institutionnelle ;
- n'est pas un reader filter.

## 7.8 Validation

Validation est scoped et policy-bound.

Une Validation Report peut porter :

- validation status ;
- certainty metadata ;
- `validated_as` classification ;
- policy refs ;
- evidence refs ;
- target refs ;
- scope.

Une assertion peut être validée **comme** hypothèse, fiction, mythe, proposition disputée ou autre classe sans que son contenu devienne une vérité universelle.

## 7.9 Authority Recognition

Authority Recognition indique quelle authority channel reconnaît quoi, dans quel scope et selon quelles règles.

Elle :

- est scoped ;
- peut être conditionnelle ;
- peut être disputée ;
- peut être deprecated/revoked/rejected selon le vocabulaire canonique retenu ;
- ne devient pas universal authority par défaut.

Validation et recognition restent deux opérations distinctes.

## 7.10 Reader Policy

Reader Policy choisit ce qui est visible et comment une surface de lecture filtre/présente les artifacts.

Elle peut :

- sélectionner ;
- filtrer ;
- ordonner ;
- annoter ;
- masquer ;
- imposer des critères de scope/certainty/validation/recognition.

Elle ne mute pas silencieusement l'état épistémique sous-jacent.

## 7.11 Working Exchange et Reference Exchange

### Working Exchange

Artifact compilé, portable, queryable et vérifiable pouvant contenir des états épistémiques non finalisés.

### Reference Exchange

Artifact accepté comme référence sous des constraints déclarées d'authority, validation, certainty et scope.

`reference` ne signifie pas :

- universal truth ;
- universal consensus ;
- certainty absolue ;
- validation par toutes les authorities.

## 7.12 Identity

Kristal doit distinguer clairement les surfaces d'identité qui ont des invariants différents.

Au minimum, le modèle doit permettre de ne pas confondre :

- identité sémantique stable d'un contenu/assertion ;
- identité d'un état/version précis ;
- identité d'un Structured Epistemic State ;
- identité d'un Exchange ;
- identité d'un Runtime Pack Manifest ;
- identité d'un package/bundle dérivé.

Les champs opérationnels ou temporels ne doivent influencer une identité déterministe que si leur inclusion est explicitement définie dans la projection de hash correspondante.

## 7.13 Canonicalization et hashing

Pour chaque artifact content-addressed, Kristal définit :

- la projection exacte hashée ;
- les champs inclus/exclus ;
- l'algorithme ;
- la canonical form ;
- les normalizations admises ;
- la représentation des absences/defaults lorsque pertinente.

Deux implémentations conformes doivent produire le même résultat pour un même input normatif lorsque le profile promet cette déterminisme.

## 7.14 Runtime Pack

Un Runtime Pack est une représentation runtime/offline dérivée d'un Exchange ou shard set selon un profile applicable.

Il doit préserver les metadata nécessaires pour ne pas perdre la sémantique de la source :

- source artifact status ;
- lineage ;
- reader policy constraints ;
- validation labels ;
- certainty labels ;
- authority labels ;
- scope ;
- integrity/inventory ;
- compatibility declarations.

## 7.15 Runtime Pack Manifest

Le Runtime Pack Manifest est l'artifact machine décrivant le pack.

Dans le schema Kristal, son discriminator reste scoped au manifest :

```text
artifact_type = runtime_pack_manifest
```

Cette valeur ne doit pas être confondue avec une classification locale de plateforme telle que `artifact_class = runtime_pack` dans un contract kOA-Linux. Les deux peuvent coexister si leur scope est explicite.

## 7.16 Federation

La federation préserve :

- source identity ;
- authority channel ;
- scope ;
- assertion status ;
- certainty ;
- validation metadata ;
- provenance ;
- disagreement.

Elle ne résout pas artificiellement des positions incompatibles en une pseudo-vérité commune.

## 7.17 Query

Le query contract doit préserver les metadata épistémiques nécessaires au consumer.

Un consumer peut demander une projection utile sans perdre silencieusement :

- scope ;
- provenance ;
- certainty ;
- validation ;
- recognition ;
- reader policy context.

## 7.18 Profiles d'intégration

Les integration contracts Kristal existent pour décrire **la frontière** avec Orgo, Konnaxion, SemantiK Architect, SenTient ou un runtime.

Ils ne doivent pas réécrire l'architecture interne de ces systèmes.

Les documents d'intégration actuels restent à aligner avec les réalités de chaque système lorsqu'ils sont trop spécifiques ou attribuent un ownership qui appartient au consumer/runtime.

---

# 8. kOA-Linux

## 8.1 Domaine

kOA-Linux est un **sovereign local operating system / operating environment**, local-first, offline-capable et contract-driven.

Son identité machine canonique est :

```text
koa_linux_operating_system
```

Il fournit un environnement gouverné pour knowledge, coordination, language, media, navigation, publication, recovery et sovereign deployment.

## 8.2 Autorité normative interne

Les contracts machine sont la source canonique pour les objets qu'ils possèdent.

La documentation prose les interprète ; elle ne devient pas un second owner de :

- component inventory ;
- profile membership ;
- integration records ;
- release channels ;
- artifact structures ;
- requirements ;
- locks ;
- evidence.

## 8.3 Architectural layers

kOA-Linux conserve ses couches internes :

| Layer | Responsabilité |
|---|---|
| L0 — Constitutional principles | explicit authority, fail-closed, offline continuity, safe degradation, separation, audit, recourse, portability, cultural rights |
| L1 — System baseline | system context, capabilities, boundaries, AI, language runtime, resources, degradation, release/artifact identity |
| L2 — Deployment profiles | compositions, overlays, hardware, security, offline guarantees, conformance |
| L3 — Component contracts | inputs, outputs, interfaces, events, states, failure behavior, data boundaries |
| L4 — Implementation recipes | systemd, Quadlet, containers, desktop, storage, networking, commands lorsque non promus en norme |

Une implementation recipe répétée ne devient pas automatiquement un invariant global.

## 8.4 Operating modes

Les modes actuels incluent :

- `interactive_user` ;
- `development` ;
- `build` ;
- `service_node` ;
- `hub` ;
- `control_plane` ;
- `recovery`.

Un operating mode décrit l'activité. Un deployment profile décrit l'environnement déployable. Les deux concepts restent distincts.

## 8.5 Components et systèmes indépendants

Un component kOA-Linux possède seulement ce que son component contract lui attribue.

Les systèmes documentés indépendamment conservent leur internal authority lorsqu'ils sont montés/intégrés.

En particulier, le hosting ou l'intégration de :

- Konnaxion ;
- Orgo ;
- SemantiK Architect ;
- Kristal ;
- Ariane ;
- autres sous-systèmes déclarés ;

ne transfère pas leur state authority à kOA-Linux.

## 8.6 Cross-component communication

Chaque communication boundary identifie :

- sender ;
- receiving owner ;
- versioned interface/artifact contract ;
- interaction class ;
- authority/policy evaluation point ;
- payload rules ;
- failure/retry behavior ;
- compatibility ;
- observable result ;
- evidence requirement.

Le receiving component reste responsable de décider comment son state est modifié.

## 8.7 Data ownership

Logical ownership reste indépendant de la topologie physique.

Une base physique partagée n'autorise pas les cross-domain writes.

Les caches, projections, search indexes et analytics restent dérivés tant que leur contract ne leur attribue pas un owner de source distinct.

## 8.8 Trust, identity et authorization

```text
reachable
≠ authenticated
≠ signature-valid
≠ trusted in this scope
≠ authorized for this capability
```

Les trust roots, identity scopes, tenant/environment boundaries et privileges restent explicites.

## 8.9 Resource governance

Resource admission est séparé de business/policy authority.

Un resource grant permet l'usage de ressources ; il n'autorise pas :

- une mutation métier ;
- un disclosure ;
- un host privilege supplémentaire ;
- une activation d'artifact.

## 8.10 Privilege boundary

Les opérations host-sensitive passent par la boundary privilégiée prévue par la plateforme.

Un subsystem request n'est pas une permission host.

La plateforme peut refuser une opération pour :

- resources ;
- security ;
- lifecycle ;
- policy ;
- compatibility ;

sans modifier le state métier du demandeur.

## 8.11 Offline continuity

Offline operation :

- ne contourne pas trust/authorization ;
- utilise du contenu déjà admis ou un import localement vérifié ;
- conserve les source authorities ;
- garde des behaviors déterministes pour les capacités déclarées offline-capable ;
- degrade de façon explicite lorsque la capacité externe n'est pas disponible.

## 8.12 Safe degradation

La perte d'une dépendance désactive seulement les capacités dépendantes lorsque le profile prévoit un mode dégradé sûr.

Elle ne déclenche pas :

- un ownership transfer ;
- une substitution silencieuse ;
- un bypass d'autorité ;
- un fallback non déclaré.

## 8.13 Artifact lifecycle

La plateforme distingue selon l'artifact/profile :

```text
receive / acquire
→ quarantine
→ verify
→ admit
→ compatibility decision
→ stage/install
→ activate
→ observe
→ rollback / forward repair
```

Ces phases peuvent partager une transaction technique sans fusionner leurs significations.

## 8.14 Receipts et critical transitions

Les transitions critiques produisent les evidence/receipts exigés par leurs contracts.

Exemples :

- artifact admission/rejection ;
- activation ;
- rollback ;
- restore ;
- publication ;
- privileged mutation ;
- trust/security transition.

Un receipt est une preuve de transition ; il ne remplace pas l'authoritative record du component.

## 8.15 `kristal_runtime`

`kristal_runtime` est un component local de kOA-Linux.

### Il possède

- Kristal content-identity resolution à partir du contenu épistémique canonique ;
- Runtime Pack verification records ;
- compatibility evaluation state ;
- active Runtime Pack record/selection ;
- activation state ;
- rollback state ;
- activation/failure receipts ;
- runtime health pertinent.

### Interfaces locales documentées

- `kristal_identity_resolution` — query ;
- `runtime_pack_validation` — command ;
- `runtime_pack_activation` — command ;
- `runtime_pack_rollback` — command ;
- `runtime_status_query` — query.

### Il ne possède pas

- tenant workflow state ;
- Konnaxion business state ;
- universal operational storage ;
- universal workflow execution ;
- governance policy ;
- resource scheduling ;
- host privilege ;
- external AI processing ;
- release-channel identity.

## 8.16 Runtime Pack validation locale

Avant activation eligibility, le runtime local vérifie selon son contract :

- schema ;
- identity ;
- digest/integrity ;
- provenance ;
- compatibility ;
- release channel ;
- required trust ;
- downgrade/substitution policy.

Un pack incompatible, non vérifié ou non autorisé reste non actif.

## 8.17 Atomic activation

Activation est atomique.

Le last valid Runtime Pack reste l'état autoritaire jusqu'à ce que toutes les preconditions de la nouvelle activation soient satisfaites.

Sont interdits :

- implicit downgrade ;
- artifact substitution non autorisée ;
- partial authoritative activation ;
- unverified execution.

## 8.18 kOA Spaces

kOA Spaces est une couche d'expérience/navigation optionnelle et remplaçable.

Elle peut posséder :

- module selector ;
- active-module sidebar ;
- top bar ;
- shared page surface ;
- validated navigation manifests ;
- presentation configuration/preferences ;
- activation receipts de sa propre composition.

Elle ne possède pas :

- business authorization ;
- workflows ;
- subsystem business state ;
- host privilege ;
- resource admission ;
- release signing ;
- Runtime Pack activation ;
- backup/recovery authority.

Une route ou un widget délègue l'opération au système owner.

Désactiver/remplacer kOA Spaces ne doit pas supprimer l'état métier des systèmes.

---

# 9. Frontière Konnaxion ↔ Orgo

## 9.1 Aucun mapping ontologique implicite

```text
Orgo Case ≠ Konnaxion Topic
Orgo Task ≠ Konnaxion Consultation
Orgo Task status ≠ civic decision status
Orgo label ≠ Konnaxion taxonomy
Organization ≠ Konnaxion domain object
```

Une correspondance peut exister dans un use case donné, mais elle reste une projection de frontière et non une identité de modèles.

## 9.2 Orgo demande une opération Konnaxion

Lorsqu'un use case le nécessite :

```text
Orgo Task / Case
    ↓
command / job / proposal / artifact ref
    ↓
Konnaxion boundary
    ↓
Konnaxion auth + validation + domain rules
    ↓
Konnaxion mutates its own state
    ↓
receipt / event / result
    ↓
Orgo reconciles its own workflow
```

## 9.3 Konnaxion crée du travail gouverné dans Orgo

Lorsqu'un événement ou état Konnaxion nécessite un workflow :

```text
Konnaxion fact/event
    ↓
governed-work request
    ↓
Orgo accepts/rejects
    ↓
Orgo creates/links Case/Task
    ↓
Orgo lifecycle
```

Konnaxion n'écrit pas les Task/Case tables directement.

## 9.4 Contrat minimal

Une future interface Konnaxion↔Orgo n'a pas besoin de transporter les modèles complets.

Elle définit seulement ce que le use case exige, par exemple :

- source identity ;
- target identity ;
- organization/tenant/scope ;
- requested operation ;
- references/payload minimal ;
- correlation ;
- idempotency ;
- actor/authorization context ;
- accepted/rejected/blocked result ;
- error codes ;
- receipt/event refs.

## 9.5 Bridge Orgo → Konnaxion

Le bridge est un adapter Orgo-owned qui appelle une boundary Konnaxion-owned.

```text
Orgo IntegrationOperation
        ↓
Orgo provider adapter
        ↓ authenticated/versioned HTTP boundary
Konnaxion provider endpoint
        ↓
Konnaxion service/domain layer
        ↓
Konnaxion-owned mutation
        ↓
receipt
```

Orgo ne possède pas le modèle d'Impact Konnaxion et ne le crée jamais par SQL direct.

Konnaxion ne modifie pas directement `IntegrationOperation` ou `OutboxMessage`. Il répond par receipt/callback selon le contrat.

Les opérations exposées restent allowlistées. Pour le gold path UCKK-A014, l'opération nécessaire est :

```text
publish
```

Une opération additionnelle telle que `distribute` peut exister dans l'adapter sans devenir nécessaire au use case.

## 9.6 `accepted` n'est pas `succeeded`

La boundary distingue explicitement :

```text
accepted
≠ succeeded
```

Réponse `succeeded` :

```text
provider commit terminé
→ external mutation finalisée
→ IntegrationOperation peut devenir SUCCEEDED
```

Réponse `accepted` :

```text
provider a accepté le travail
→ traitement final encore en cours
→ IntegrationOperation reste RUNNING
→ callback/final receipt requis
```

Un receipt final `succeeded` est requis avant de présenter l'effet externe comme terminé.

Invariant :

```text
Outbox delivery completed
≠ external operation finalized
```

lorsque le provider a répondu `accepted`.

## 9.7 Idempotency et correlation

Toute publication durable entre Orgo et Konnaxion utilise une identity de replay/idempotency stable et une correlation stable.

Le retry/redrive du même handoff :

```text
same logical operation
+ same idempotency identity
→ no duplicate Konnaxion business effect
```

La correlation permet de relier les objets sans fusionner leurs identities :

```text
Orgo Case
↔ IntegrationOperation
↔ OutboxMessage
↔ Konnaxion Impact
```

Les UUID runtime ne sont pas des références de scénario portables et ne doivent pas être hardcodés dans les world/scenario packs.

## 9.8 World/Release Konnaxion

Lorsqu'un provider Konnaxion est world-scoped, la destination est résolue dans un contexte Konnaxion explicite de World/Release.

```text
Orgo
→ provider URL / world target
→ Konnaxion World
→ selected/current Release
→ Konnaxion-owned service
→ domain mutation
```

Le World/Release fournit le contexte de destination ; il ne transfère pas l'ownership de la mutation à Orgo.

Une publication cross-system ne contourne jamais :

- les migrations/schema dependencies du World ;
- la validation de release ;
- les services Konnaxion propriétaires ;
- l'idempotency du provider.
---

# 10. Frontière Orgo ↔ Kristal

## 10.1 Rôles

Orgo orchestre.

Kristal définit et produit l'état épistémique/artifacts.

```text
workflow state ≠ epistemic state
```

## 10.2 Orgo peut

Lorsqu'une interface Kristal l'expose :

- référencer un Structured Epistemic State ;
- demander une compilation ;
- demander/lancer une validation ;
- enregistrer artifact refs ;
- orchestrer review/approval work ;
- suivre des jobs ;
- déclencher publication/release work ;
- conserver receipts/diagnostics/correlation.

## 10.3 Orgo ne peut pas implicitement

- convertir `Task.status` en `assertion_status` ;
- convertir `Case.status` en `validation_status` ;
- convertir un approval opérationnel en Authority Recognition ;
- modifier un Exchange en éditant un Task ;
- redéfinir les schemas Kristal dans son core.

## 10.4 Review, validation et recognition

Orgo peut gérer le **workflow** autour d'une review, validation ou recognition.

Le résultat épistémique doit néanmoins exister comme décision/artifact Kristal lorsqu'il est supposé changer l'état Kristal.

```text
Orgo approval record
        +
explicit Kristal operation
        ↓
Kristal validation / recognition artifact or state
```

---

# 11. Frontière Konnaxion ↔ Kristal

## 11.1 Domaine de la frontière

Cette frontière concerne seulement les artifacts Kristal consommés, exposés ou transportés par les surfaces Konnaxion qui en ont réellement besoin.

Konnaxion ne devient pas le propriétaire des primitives Kristal.

## 11.2 Verbes à ne pas fusionner

```text
publish
transport
acquire/download
cache
serve/query
verify for a local purpose
install
activate
rollback
```

Un produit Konnaxion peut posséder certaines opérations de publication, transport, acquisition, cache ou serving selon son contract.

Cela ne lui attribue pas implicitement l'état `active Runtime Pack` d'un node kOA-Linux.

## 11.3 Metadata épistémiques

Lorsqu'une surface Konnaxion présente un artifact/résultat Kristal, elle ne doit pas transformer silencieusement :

- assertion status ;
- certainty ;
- validation ;
- authority recognition ;
- reader policy ;
- provenance.

La présentation peut simplifier l'UX sans changer la sémantique sous-jacente.

---

# 12. Frontière Kristal ↔ SemantiK Architect

## 12.1 Type de frontière

Il s'agit d'une **projection knowledge → semantic generation request**, pas d'une fusion entre compiler épistémique et NLG.

```text
Kristal query/result
    ↓
integration projection
    ↓
Architect semantic request/frame
    ↓
Architect planner
    ↓
PlannedSentence
    ↓
ConstructionPlan
    ↓
lexical resolution
    ↓
renderer
    ↓
SurfaceResult / public response
```

## 12.2 Kristal possède

- source artifacts ;
- query semantics ;
- provenance ;
- epistemic labels ;
- reader-policy-resolved visibility lorsque applicable.

## 12.3 Architect possède

- request normalization ;
- planner ;
- sentence intent ;
- construction plan ;
- lexical resolution ;
- realization backend ;
- surface result ;
- linguistic fallback behavior.

## 12.4 Integration profile

Le profile peut définir :

- comment un Kristal result devient un semantic frame/request ;
- langue/locale ;
- quelles metadata épistémiques doivent être visibles ;
- trace/provenance requirements ;
- no-new-facts constraint pour un mode knowledge-backed ;
- omission/refusal behavior ;
- mapping source refs → surface trace.

Il ne doit pas :

- contourner le planner comme architecture nominale ;
- écrire directement `PlannedSentence` comme si Kristal en était owner ;
- imposer une structure GF comme modèle épistémique ;
- confondre public API response et internal `SurfaceResult`.

---

# 13. Runtime Pack : chaîne complète d'autorité

Le Runtime Pack traverse plusieurs domaines, chacun avec un owner distinct.

```text
KRISTAL
  définit artifact semantics
  compile/builds conforming Runtime Pack
       ↓
PUBLISHER / DISTRIBUTION SURFACE
  rend le candidate disponible
       ↓
TRANSPORT / ACQUISITION
  déplace les bytes
       ↓
kOA-LINUX ARTIFACT BOUNDARY
  quarantine / verify / admit / compatibility
       ↓
kristal_runtime
  active selection / atomic activation / rollback / health
       ↓
LOCAL CONSUMER
  query/use according to rights/profile
```

## 13.1 Kristal possède

- Runtime Pack semantics ;
- Runtime Pack Manifest schema ;
- source/lineage requirements ;
- artifact identity semantics ;
- inventory/integrity format ;
- declared compatibility metadata ;
- embedded/declared trust material semantics ;
- query semantics du pack.

## 13.2 Publisher/distribution possède

Selon le système utilisé :

- publication location ;
- availability ;
- channel/cohort/pinning metadata si applicable à ce contract ;
- transport orchestration.

Il ne possède pas nécessairement l'activation locale.

## 13.3 kOA-Linux possède localement

- candidate admission boundary ;
- local verification record ;
- compatibility result ;
- active Runtime Pack record ;
- atomic activation ;
- rollback/forward repair state ;
- local receipts ;
- local runtime health.

## 13.4 Séparations obligatoires

```text
Runtime Pack validity ≠ local compatibility
local compatibility ≠ activation authorization
activation authorization ≠ activation completed
receipt ≠ active state record
newer version ≠ compatible version
available artifact ≠ admitted artifact
admitted artifact ≠ active artifact
```

---

# 14. K-Port, XKaliber, EkoH Expertise Claims et autres spécialisations

## 14.1 Principe

Les systèmes spécialisés conservent leur domain authority et utilisent des gateways explicites lorsqu'un résultat doit influencer un autre système.

## 14.2 XKaliber

XKaliber mesure la compétence et produit des assessment results/evidence.

Il ne calcule pas la réputation finale d'une personne dans Konnaxion.

```text
XKaliber
  measures competency
     ↓
Calibre Profile / assessment evidence
     ↓
CertifiKation attestation lorsque applicable
     ↓
K-Port
     ↓
EkoH
```

La compétence reste domain-bounded et contestable.

## 14.3 K-Port

K-Port est l'evidence gateway pour les expertise claims destinées à EkoH.

Il collecte/normalise/qualifie l'evidence et décide de son admissibilité vers le handoff EkoH.

Il ne :

- self-assign pas un EkoH score ;
- remplace pas EkoH reputation ;
- re-score pas un résultat XKaliber ;
- permet pas à un evidence producer d'écrire directement dans EkoH reputation state.

## 14.4 Chaîne d'autorité compétence → réputation

```text
XKaliber measures competency
→ CertifiKation attests result when used
→ K-Port qualifies/routes evidence
→ EkoH calculates domain-bounded reputation impact
```

Chaque étape conserve ses propres décisions et evidence.

## 14.5 MediKristal

MediKristal est un consumer/domain specialization de knowledge semantics médicales.

Il ne doit pas créer un second core Kristal incompatible pour :

- identity ;
- provenance ;
- certainty ;
- validation ;
- authority ;
- artifacts ;
- Runtime Pack semantics.

Ses concepts cliniques restent une specialization/domain model au-dessus des primitives communes pertinentes.

## 14.6 KeyFlow et autres consumers

Les applications secondaires peuvent :

- utiliser des APIs du noyau ;
- consommer des artifacts ;
- publier des domain-specific artifacts ;
- demander des workflows Orgo ;
- utiliser kOA-Linux comme platform boundary ;
- utiliser Architect pour la génération ;
- utiliser Kristal pour la représentation épistémique lorsque pertinent.

Elles ne deviennent pas source d'une primitive globale par simple existence locale.

---

# 15. Identity, provenance et audit cross-system

## 15.1 Identity scoped by owner

Chaque système définit ses identities dans son domaine.

Exemples :

```text
Orgo Task ID        → Orgo workflow identity
Orgo Case ID        → Orgo case identity
Konnaxion topic ID  → Konnaxion civic identity
Kristal artifact ID → Kristal artifact/content identity
Runtime activation record → kOA-Linux local runtime identity
```

Une correlation ref entre deux identities ne les fusionne pas.

## 15.2 Provenance

Une dérivation ou artifact cross-system conserve assez de provenance pour répondre à :

- qui a produit quoi ;
- à partir de quelle source ;
- sous quel scope ;
- avec quelle version/configuration ;
- avec quelles transformations ;
- sous quelle authority/policy lorsque pertinente.

## 15.3 Correlation

Correlation est opérationnelle.

Elle peut relier :

- Orgo Task/Case ;
- command/job ;
- Kristal artifact ;
- Konnaxion object ;
- Architect generation request ;
- kOA-Linux receipt.

La correlation ne change l'ownership d'aucun objet.

## 15.4 Audit

Chaque système audit les mutations qui lui appartiennent.

Un central audit/evidence component peut conserver des preuves sans devenir owner des états qu'il observe.

---

# 16. Multi-tenancy et scopes

## 16.1 Scope explicite

Les boundaries multi-tenant utilisent le scope du système concerné :

- organization ;
- tenant ;
- environment ;
- channel ;
- domain ;
- jurisdiction ;
- authority channel ;
- reader policy ;
- autre scope versionné.

Les scopes ne sont pas interchangeables simplement parce qu'ils sont tous représentés par une string/ID.

## 16.2 Pas de cross-tenant shortcut

Aucune optimisation de cache, DB, queue, trust ou artifact store ne doit créer un cross-tenant read/write non autorisé.

## 16.3 Kristal scope

Un artifact/recognition/validation Kristal peut avoir son propre scope épistémique distinct du tenant opérationnel qui l'héberge.

## 16.4 Orgo organization

`organization_id` reste un invariant Orgo pour les objets qui l'exigent. Il ne devient pas automatiquement le scope universel des artifacts Kristal ou Konnaxion.

---

# 17. Trust et signatures

## 17.1 Signature

Une signature prouve seulement ce que son contract cryptographique et sa trust chain permettent de prouver.

Elle ne signifie pas automatiquement :

- contenu vrai ;
- contenu validé ;
- authority recognition ;
- droit d'activer ;
- droit de muter un système cible.

## 17.2 Kristal

Kristal sépare artifact integrity et authority recognition.

## 17.3 kOA-Linux

kOA-Linux applique localement identity/trust/policy/authorization aux opérations de plateforme.

`kristal_runtime` peut enregistrer le résultat de verification sans devenir identity/trust authority globale.

## 17.4 Konnaxion/EkoH

Un expertise/trust signal EkoH n'est pas une cryptographic signature universelle et ne remplace pas un decision protocol.

---

# 18. Determinism

## 18.1 Règle générale

Lorsqu'un système promet un résultat déterministe :

```text
same declared input
+ same pinned configuration
+ same pinned policy
+ same relevant resources
→ same declared output
```

Le niveau exact de sameness peut être :

- bit-identical ;
- canonical-identical ;
- semantically equivalent selon un contract explicitement défini.

## 18.2 Konnaxion

Une Smart Vote reading reproductible doit pouvoir être recomputée à partir de baseline events, lens declaration et snapshot context déclaré.

## 18.3 Orgo

Les gates/routing rules qui prétendent être déterministes utilisent des enums/configurations/inputs explicites. Les retries sont reconciled via Task/event/attempt semantics.

## 18.4 Architect

La génération nominale doit dépendre d'inputs explicites, du planner/runtime, des ressources linguistiques et du renderer sélectionné selon le contract. Un backend ne doit pas introduire un second planning path silencieux.

## 18.5 Kristal

Canonicalization, IDs, hashes, build outputs et query behavior déterministes utilisent des projections/versionnements testables.

## 18.6 kOA-Linux

Activation, rollback, artifact admission et local deterministic core behavior utilisent des policies et states explicitement identifiés.

---

# 19. Error, retry et idempotency

## 19.1 Error ownership

Le receiver définit les erreurs de son interface.

Le sender doit savoir distinguer au minimum, lorsque pertinent :

- accepted ;
- rejected ;
- blocked ;
- retryable failure ;
- permanent failure ;
- unknown outcome ;
- incompatible version ;
- unauthorized ;
- validation/integrity failure.

## 19.2 Retry

Retry ne doit pas créer deux mutations autoritaires ambiguës.

Pour les commands/jobs critiques, un idempotency/replay identity ou une reconciliation semantics est défini.

## 19.3 Failure preservation

Un échec d'intégration ne permet pas au sender de corriger directement l'état du receiver en contournant son contract.

## 19.4 Acceptation asynchrone et finalité

Pour une opération externe asynchrone, l'acceptation du transport et la finalité métier sont deux transitions distinctes.

```text
request sent
→ accepted
→ processing
→ final receipt
→ succeeded | failed
```

Un système de présentation, de monitoring ou de workflow ne doit pas transformer `accepted` en `succeeded`.

## 19.5 Dead-letter et redrive

Après épuisement de la politique de retry, un message peut devenir terminalement non livrable (`DEAD` ou état équivalent).

À partir de cet état :

- la cause reste auditable ;
- l'opération externe reste non réussie ;
- le travail métier local n'est pas réécrit pour simuler le succès ;
- la reprise passe par un redrive canonique ;
- le redrive conserve l'idempotency identity de l'effet logique.

Le redrive n'est pas un prétexte pour bypasser l'API/domain service du receiver.

## 19.6 Provider indisponible ou non configuré

Un provider absent, indisponible ou non configuré produit un échec observable.

```text
provider unavailable/unconfigured
→ retry policy
→ terminal failure if exhausted
→ operator fixes provider/runtime
→ canonical redrive
```

Le rétablissement du provider ne transforme pas automatiquement un ancien état `FAILED/DEAD` en succès. Une reprise explicite et auditable est requise.
---

# 20. Presentation et UX

## 20.1 UI locale

Chaque système peut avoir sa propre UI native.

La composition globale ne change pas l'owner des actions.

## 20.2 kOA Spaces

kOA Spaces peut composer les contributions de navigation des modules.

```text
user action
→ kOA Spaces route/widget
→ owner system API/command/query
→ owner system state
```

## 20.3 Konnaxion

Konnaxion garde ses page shells et module-specific surfaces à l'intérieur de l'expérience globale lorsque déployé sous kOA Spaces.

## 20.4 Architect

Architect peut produire le texte présenté. Il ne devient pas owner du domain fact ou de l'epistemic state rendu.

---

# 21. Architecture cible par flux

## 21.1 Flux civique

```text
Konsultations intake / Korum deliberation
            ↓
source civic facts
            ↓
Smart Vote reading inputs ← EkoH context snapshot
            ↓
reproducible reading
            ↓
Konnaxion presentation / decision surface
            ↓
accountability / impact state
```

## 21.2 Flux de workflow

```text
signal / request / event
        ↓
Orgo Case / Task
        ↓
workflow / routing / gates
        ↓
command/job to real owner
        ↓
owner mutation
        ↓
receipt/event/result
        ↓
Orgo reconciliation/audit
```

## 21.3 Flux épistémique

```text
Structured Epistemic State
        ↓
Kristal compile
        ↓
Working Exchange
        ↓
validation / recognition / federation as applicable
        ↓
Reference Exchange as applicable
        ↓
Runtime Pack / query surface as applicable
```

## 21.4 Flux linguistique

```text
semantic input
        ↓
Architect normalization
        ↓
planner
        ↓
PlannedSentence
        ↓
ConstructionPlan
        ↓
lexical resolution
        ↓
renderer
        ↓
SurfaceResult
        ↓
public response
```

## 21.5 Flux runtime local

```text
artifact candidate
        ↓
kOA-Linux acquisition/quarantine
        ↓
verification
        ↓
compatibility / authority decision
        ↓
local admission
        ↓
kristal_runtime atomic activation
        ↓
active local runtime state
        ↓
health / rollback / forward repair
```

## 21.6 Profile de référence Konnaxion/eThikos → Orgo

La vertical slice historique A014 est conservée comme source de tests techniques, mais son ancien modèle d'autorité UCKK était incorrect. Le profile cible est le suivant.

### Autorité de décision

La délibération et la décision ont lieu dans **Konnaxion/eThikos**. Smart Vote, EkoH et les autres readings peuvent éclairer le processus mais ne remplacent pas le DecisionRecord finalisé par eThikos.

```text
Konnaxion / eThikos
  → deliberation
  → readings / Smart Vote / EkoH
  → decision stage
  → finalized DecisionRecord
  → direct handoff to Orgo
  → Signal / WorkflowVersion / Case / Tasks
```

Le déclencheur opérationnel est donc le **DecisionRecord finalisé dans eThikos**, pas une décision UCKK et pas un Smart Vote pris isolément.

### UCKK est optionnel

UCKK peut être une plateforme de publication, diffusion, présentation ou apprentissage :

```text
Konnaxion/eThikos finalized decision
→ optional UCKK publication/distribution
```

Cette branche est indépendante du handoff vers Orgo. UCKK ne devient ni l'owner de la décision, ni un relay obligatoire.

### Boucle opérationnelle

```text
Konnaxion/eThikos finalized decision
        ↓
Konnaxion → Orgo decision handoff
        ↓
Orgo Signal
        ↓
WorkflowVersion
        ↓
Case + Tasks
        ↓
operational observations / impact
        ↓
IntegrationOperation + Outbox
        ↓
Orgo worker
        ↓
Konnaxion provider
        ↓
Konnaxion Impact / accountability state
        ↓
follow-up / reconsideration in eThikos when needed
```

### Historical A014 identifiers

Les noms `UCKK-A014`, `UCKK-D009`, `corr.uckk.A014.D009` et autres identifiants similaires restent présents dans certains fixtures/runtime historiques. Ils ne doivent plus être interprétés comme une preuve d'ownership UCKK. Ils doivent être renommés ou remappés lors de la refonte du scenario vers des références Konnaxion/eThikos.

Les UUID runtime restent non portables et ne doivent pas être hardcodés dans les packs de scénario.

### Gate de validation

La conformance end-to-end exige d'abord :

```text
finalized eThikos DecisionRecord
→ direct Orgo handoff
→ expected Orgo governed work
```

puis, pour un effet de retour vers Konnaxion :

```text
Orgo IntegrationOperation = SUCCEEDED
AND
exactly one Konnaxion business effect exists for the idempotency identity
```

Un statut `accepted`, un outbox livré ou une simple réponse HTTP ne suffit pas.

### Follow-up

Les observations opérationnelles peuvent ouvrir une reconsidération dans eThikos, mais Orgo ne modifie pas la décision civique de sa propre initiative. Orgo orchestre le travail ; Konnaxion/eThikos possède le processus de décision.

---

# 22. Frontières qui doivent rester petites

## 22.1 Konnaxion ↔ Orgo

Ne pas exporter tout le civic model vers Orgo et ne pas importer tout le Task/Case model dans Konnaxion.

## 22.2 Orgo ↔ Kristal

Orgo transporte refs, intents, workflow decisions et receipts ; Kristal garde ses artifacts et statuses.

## 22.3 Kristal ↔ Architect

Kristal fournit semantic/epistemic input ; Architect garde son internal NLG runtime.

## 22.4 kOA-Linux ↔ subsystems

kOA-Linux fournit platform capabilities, resources, lifecycle, host mediation et local artifact handling. Il ne copie pas les business schemas internes des subsystems.

## 22.5 K-Port ↔ EkoH

K-Port qualifie evidence et produit un scoring handoff ; EkoH calcule l'impact réputationnel dans son domaine.

---

# 23. Noms et concepts à ne pas fusionner

```text
Kristal Specification ≠ système séparé de Kristal

Konnaxion Topic ≠ Orgo Case
Konnaxion Consultation ≠ Orgo Task
Korum stance ≠ consultation ballot
ArgumentImpactVote ≠ topic stance
ReadingResult ≠ source fact
EkoH snapshot ≠ vote

Orgo approval ≠ Kristal validation
Orgo approval ≠ Kristal authority recognition
Task status ≠ assertion status
Case status ≠ validation status

Kristal artifact integrity ≠ truth
certainty ≠ validation
validation ≠ recognition
recognition ≠ reader visibility
reader visibility ≠ runtime activation

Runtime Pack ≠ Runtime Pack Manifest
Kristal manifest artifact_type ≠ kOA-Linux local artifact_class
artifact verified ≠ artifact activated
resource grant ≠ activation authorization
receipt ≠ active state

Architect SurfaceResult ≠ Kristal artifact
renderer backend ≠ planner
GF ≠ Architect architecture
public API response ≠ internal ConstructionPlan

kOA Spaces route ≠ business capability ownership
UI composition ≠ authorization
```

---

# 24. Contrats machine et prose

## 24.1 Général

Lorsqu'un système possède un machine-readable contract canonique, la prose doit être cohérente avec lui.

La prose explique la sémantique ; elle ne crée pas un second enum ou schema concurrent.

## 24.2 Orgo

Les enums/DTOs/schema Prisma/API validators doivent converger avec les docs v3 sur :

- Task status ;
- Case status ;
- Task fields ;
- Case fields ;
- label format ;
- visibility ;
- priority/severity ;
- domain module rules.

## 24.3 Kristal

Les JSON Schemas, examples, query docs, integration contracts et core prose doivent utiliser les mêmes :

- discriminators ;
- enums ;
- field semantics ;
- identity rules ;
- references ;
- scope semantics.

## 24.4 kOA-Linux

Les contracts machine restent owners de leur structure. Les generated catalogs et prose sont des projections/interprétations conformes, pas des sources concurrentes.

## 24.5 Architect

Public API docs, request mapper, planner/runtime types et response serializer doivent rester cohérents sur l'input boundary et la distinction entre runtime objects et response payload.

---

# 25. Conformance de l'état aligné

L'écosystème est aligné lorsque les points suivants sont vrais simultanément.

## 25.1 Ownership

- chaque authoritative state a un owner unique ;
- aucun direct cross-domain write n'est nécessaire ;
- les projections restent dérivées ;
- UI et audit n'acquièrent pas business authority.

## 25.2 Konnaxion

- Korum/Konsultations/Smart Vote/EkoH restent séparés ;
- baseline et readings restent distinctes ;
- readings sont reproductibles ;
- EkoH n'est pas le voting engine ;
- external tools ne write pas le core ;
- vote/stance/impact-vote/readings ne sont pas fusionnés.

## 25.3 Orgo

- Task reste l'unité de travail commune ;
- Case reste le conteneur durable ;
- domain modules réutilisent le core ;
- canonical enums/labels sont cohérents entre code et docs ;
- external artifacts sont référencés sans absorption de leur schema ;
- workflow state ne devient pas state métier/épistémique externe.

## 25.4 SemantiK Architect

- planner/runtime reste la source de sentence intent ;
- `PlannedSentence` et `ConstructionPlan` restent internes à Architect ;
- GF/family/safe-mode restent backends ;
- public API reste sémantique ;
- compatibility path ne redéfinit pas l'architecture nominale.

## 25.5 Kristal

- Kristal est documenté comme un seul système ;
- Specification et implementation sont distinguées sans créer deux produits ;
- Structured Epistemic State reste l'input normatif ;
- Claim-IR reste optionnel/profiled ;
- compilation, validation, recognition et visibility restent séparées ;
- identity/hash projections sont explicites ;
- schemas/examples/prose sont cohérents ;
- Runtime Pack et local activation state restent séparés.

## 25.6 kOA-Linux

- contracts machine restent canoniques ;
- systems indépendants gardent leur authority ;
- profile/component/data/privilege boundaries sont explicites ;
- commands/queries/events/jobs/artifacts/gateways gardent leurs semantics ;
- offline/degradation ne bypass pas trust ;
- `kristal_runtime` ne possède que sa boundary locale ;
- activation est atomic et fail-closed ;
- kOA Spaces reste optional/replaceable.

## 25.7 Secondary systems

- XKaliber mesure la compétence sans devenir reputation engine ;
- K-Port qualifie evidence sans re-scoring XKaliber ni remplacer EkoH ;
- EkoH reste owner de ses domain-bounded reputation signals ;
- specialized apps consomment les contracts centraux au lieu de dupliquer leurs primitives.

## 25.8 Conformance Orgo ↔ Konnaxion

La boundary Orgo↔Konnaxion est alignée lorsque :

- `IntegrationOperation` est distincte de `Case`/`Task` ;
- l'Outbox porte la livraison fiable après commit ;
- Konnaxion est muté uniquement par une boundary/service Konnaxion-owned ;
- aucun SQL cross-system n'est requis ;
- `accepted` reste distinct de `succeeded` ;
- un callback/final receipt ferme les opérations asynchrones ;
- retries/redrives sont idempotents ;
- une même idempotency identity ne crée pas deux effets métier Konnaxion ;
- correlation et external references sont conservées ;
- les runtime UUIDs ne sont pas hardcodés dans les scenario/world packs ;
- les credentials/tokens de bridge ne sont ni loggés ni intégrés à la documentation ;
- un provider non configuré/indisponible échoue de façon observable et fail-closed ;
- une opération terminalement échouée est reprise par redrive canonique, pas par mutation SQL ;
- le World/Release Konnaxion cible est explicite lorsque le provider est world-scoped.
---

# 26. Références architecturales actuelles à respecter

Cette section liste les surfaces existantes qui expriment déjà correctement l'architecture et doivent rester cohérentes avec ce document.

## Konnaxion

- `docs/Technical-Reference/Kintsugi_Kompendio/ethiKos_Kintsugi_Update/03_BOUNDARIES_AND_OWNERSHIP_CONTRACTS.md`
- `docs/Technical-Reference/Kintsugi_Kompendio/ethiKos_Kintsugi_Update/02_SOURCE_OF_TRUTH_AND_DRIFT_CONTROL.md`
- backend actuel `konnaxion.ethikos`
- frontend actuel `/ethikos/*`
- backend actuel `konnaxion.ekoh`

## Orgo

- IntegrationOperation / Outbox / bridge provider contract et redrive canonique tels qu'implémentés dans les surfaces API/worker v3 ;
- Scenario Injector / world packs pour les profiles de conformance sans UUID runtime hardcodés ;

- `Docs/Technical-Reference/v3/1-orgo-database-schema-reference.md`
- `Docs/Technical-Reference/v3/2-orgo-documentation-index.md`
- `Docs/Technical-Reference/v3/5-orgo-Core-Services-Specification.md`
- `Docs/Technical-Reference/v3/8-orgo-cyclic-overview-labels-and-flow-rules.md`
- `apps/api/prisma/schema.prisma`
- `apps/api/src/orgo/core/tasks/*`
- `apps/api/src/orgo/core/cases/*`

## SemantiK Architect

- `docs/Technical-Reference/01-ENGINE_ARCHITECTURE.md`
- `docs/Technical-Reference/04-API_REFERENCE.md`
- `docs/Technical-Reference/CURRENT_RUNTIME_STATUS.md`
- `docs/Technical-Reference/GF_ARCHITECTURE.md`

## Kristal

- `README.md`
- `00-overview/*`
- `01-core-spec/*`
- `02-schemas/*`
- `03-reproducibility/*`
- `04-query/*`
- `05-profiles/*`
- `06-integration/*`
- `07-security/*`
- `08-ops/*`
- `10-examples/*`

Ces chemins appartiennent à la **Kristal Specification**, une partie normative du système Kristal.

## kOA-Linux

- `contracts/system.contract.json`
- `contracts/integration-types.contract.json`
- `contracts/release-channels.contract.json`
- `contracts/artifact-classes.contract.json`
- `contracts/components/*` et `contracts/subsystems/*` selon leur scope
- `02-system/00-system-overview.md`
- `02-system/05-data-authority-and-ownership.md`
- `02-system/07-cross-component-communication.md`
- `02-system/20-receipts-and-critical-transitions.md`
- `02-system/21-koa-spaces-experience-layer.md`
- `04-components/kristal-runtime.md`
- `06-lifecycle/*`

## K-Port / XKaliber

- K-Port `README.md` et `docs/*`
- XKaliber `README.md`, `contracts/*`, `GOVERNANCE.md`

---

# 27. Résumé normatif

L'architecture cible tient en quelques règles fortes :

1. **Kristal est un seul système** : sa Specification est normative et sa future implementation doit s'y conformer.
2. **kOA-Linux porte directement son architecture de plateforme** dans ses contracts et composants.
3. **Konnaxion, Orgo, SemantiK Architect et Kristal gardent leurs domaines autonomes.**
4. **Aucun système n'écrit directement dans l'état autoritaire d'un autre.**
5. **Konnaxion conserve Single Truth, Multiple Readings** : source facts stables, readings dérivées, EkoH contextuel, Smart Vote non mutateur.
6. **Orgo conserve Task/Case comme backbone commun** et ses domain modules comme adapters du core.
7. **SemantiK Architect conserve son pipeline planner-first** et ses backends comme réalisateurs, non comme planners concurrents.
8. **Kristal conserve les axes épistémiques séparés** : integrity, assertion status, certainty, validation, recognition, reader visibility et activation ne se confondent pas.
9. **kOA-Linux conserve authority, policy, resources, trust, artifacts et lifecycle comme boundaries explicites.**
10. **Runtime Pack format et Runtime Pack activation locale appartiennent à des owners différents.**
11. **Les applications spécialisées produisent/consomment des evidence/artifacts sans créer de modèle autoritaire parallèle.**
12. **Les contracts restent petits, versionnés, testables et orientés use case.**
13. **Les effets externes Orgo passent par IntegrationOperation + Outbox + provider adapter**, pas par des writes directs dans le système cible.
14. **`accepted` n'est jamais assimilé à `succeeded`** : une finalité asynchrone exige un receipt final.
15. **Retry et redrive préservent l'idempotency identity**, afin qu'un même handoff logique ne crée pas deux effets métier.
16. **Dans le profile de décision Konnaxion/eThikos, le DecisionRecord finalisé dans eThikos est l'autorité de déclenchement vers Orgo** ; UCKK reste une surface de diffusion optionnelle et Smart Vote une reading/input du processus.

```text
             DOMAIN OWNERSHIP                   PLATFORM OWNERSHIP

 Konnaxion   Orgo   Architect   Kristal              kOA-Linux
     │        │        │          │                      │
     └────────┴────────┴──────────┘                      │
          explicit contracts                            │
                  │                                     │
                  └──────── deployed/integrated ────────┘

No silent authority transfer.
No duplicate source of truth.
No model fusion by convenience.
```
