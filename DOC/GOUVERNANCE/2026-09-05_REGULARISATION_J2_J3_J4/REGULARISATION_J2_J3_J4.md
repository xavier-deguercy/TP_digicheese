---
title: DigiCheese - Régularisation documentaire J2 J3 J4
version: 0.1.0
date: 2026-09-05
status: j2-j3-decides-j4-reporte
---

# DigiCheese — Régularisation documentaire J2, J3 et J4

Ce dossier corrige le point de reprise de la gouvernance. Il rassemble les preuves déjà produites et prépare des décisions datées au jour où elles seront effectivement prises. Il ne refait aucun travail, n'antidate aucune décision et ne transforme ni le mandat local de WP-01 ni un verdict d'agent en franchissement de jalon.

## 1. Point de reprise corrigé

| Élément | Statut au 2026-09-05 | Effet |
|---|---|---|
| J1 — GO Étude | Étude autorisée et dossier documentaire vérifié | J1 n'est pas rejoué |
| J2 — GO Conception | `GO_AVEC_RÉSERVES` | Décision humaine effective le 2026-09-05 |
| J3 — Kick-off | `ATTEINT_AVEC_RÉSERVES` | Xavier est le décideur et pilote formel de ce projet individuel |
| J4 — GO Développement / Production | `REPORTÉ` | Mode `SPRINTS` retenu ; mandat WP-01 consommé ; aucune nouvelle enveloppe ouverte |
| WP-01 | Développement local terminé ; preuves techniques et fonctionnelles disponibles | Ces preuves préparent J5 mais ne font pas franchir J2, J3, J4 ou J5 |
| J5 — GO Tests / Validation business | `EN_ATTENTE` | Décision à préparer après régularisation de J2, J3 et J4 |
| `AUTO_NEXT` | `NON_AUTORISÉ` | Aucun élément suivant n'est à la fois `READY` et autorisé |

J2, J3 et J4 ont été régularisés le 2026-09-05 sans réécrire l'ordre historique des travaux. Après exécution des contrôles AC-11 local et cyber minimal autorisés, le point exact de reprise est une nouvelle décision J5 sur WP-01.

## 2. Éléments historiques conservés

- Décision D-06 : périmètre H0 minimal Data + DevOps, baseline Admin + Clients, stabilisation avant commandes, front hors H0, Wave 2 conservée comme futur backlog non validé et IAM séparé.
- Profil `SOCLE + DEV + INT + IAM` : `PROPOSÉ`, à décider à J2.
- Branche et baseline de travail : `xavier`, HEAD `6790d40902c32f207923c8d174169e280cddadc9`, avec travail local préexistant préservé.
- Mandat utilisateur du 2026-09-05 : réalisation et contrôles locaux de WP-01, sans commit, push, déploiement ou service distant. Ce mandat est consommé.
- Candidate WP-01 : `wp01-7d113810cc2d0216`.
- Preuves WP-01 : 51 tests réussis, 16 avertissements préexistants, contrôles ciblés et statiques réussis, réserve AC-11 sur l'exécution GitHub Actions/MySQL/healthcheck.
- Sources cyber : `À_FOURNIR`. Autorité SSI, PPM, budget, charge, dates cibles, tolérances et responsables institutionnels : `À_CONFIRMER`.

## 3. Décision distincte attendue à J2

**Nature :** décision `GO`, `GO_AVEC_RÉSERVES`, `NO_GO`, `REPORTÉ` ou maintien `EN_ATTENTE` pour la conception et la planification.

La décision J2 doit indiquer séparément :

1. le besoin et le périmètre retenus, avec D-06 comme décision H0 déjà acquise ;
2. le livrable cible, notamment API seule ou interface comprise ;
3. le profil de modules retenu, actuellement `SOCLE + DEV + INT + IAM` proposé ;
4. les critères et preuves attendus, les KPI, la faisabilité et les risques acceptés ;
5. la nature des environnements et des données, ainsi que les résultats initiaux RGPD et SSI ;
6. l'autorité de décision, la date effective, la capacité, la charge ou le budget et les réserves.

| Option J2 | Conséquence |
|---|---|
| `GO` | Autorise la conception sur le périmètre et les conditions explicitement adoptés |
| `GO_AVEC_RÉSERVES` | Autorise la conception tout en rendant les réserves, propriétaires et échéances opposables |
| `NO_GO` | Interrompt la conception et demande un nouveau cadrage ou l'arrêt |
| `REPORTÉ` / `EN_ATTENTE` | Conserve les documents préparatoires sans créer d'autorisation supplémentaire |

Les inconnues non décidées restent `À_CONFIRMER`. La future décision portera sa date réelle et ne sera pas présentée comme antérieure à WP-01.

## 4. Constat distinct attendu à J3

J3 est un résultat vérifiable. Le statut attendu est `ATTEINT`, `ATTEINT_AVEC_RÉSERVES`, `NON_ATTEINT` ou `EN_ATTENTE`.

Le constat J3 doit vérifier et enregistrer :

1. l'équipe et les rôles humains, dont PMO, métier ou évaluateur, technique, SSI, RGPD et exploitation selon applicabilité ;
2. la gouvernance, la source de vérité et la cadence COPROJ ;
3. les objectifs, le profil de modules et le plan de conception partagés ;
4. les responsabilités pour les décisions, les preuves et le traitement des réserves ;
5. l'autorité du constat et sa date effective.

Xavier a confirmé être formellement décideur et pilote de ce projet individuel. J3 est `ATTEINT_AVEC_RÉSERVES` ; le PPM, la cadence et les autorités spécialisées restent `À_CONFIRMER` lorsqu'ils deviennent nécessaires.

## 5. Décision distincte attendue à J4

**Nature :** décision `GO`, `GO_AVEC_RÉSERVES`, `NO_GO`, `REPORTÉ` ou maintien `EN_ATTENTE` pour le développement ou la production.

La décision J4 doit indiquer séparément :

1. la solution, l'architecture et la baseline retenues ;
2. le mode `CYCLE_V` ou `SPRINTS` ;
3. le backlog autorisé, sa priorité, ses critères `READY` et `DONE`, et le nombre maximal d'éléments ;
4. l'enveloppe d'autonomie : écritures locales, actions externes, corrections, portes qualité, tolérances et conditions d'arrêt ;
5. le budget ou la charge, les risques acceptés, la stratégie de tests et le rollback ;
6. l'autorité de décision, la date effective et les réserves.

| Option J4 | Conséquence |
|---|---|
| `GO` | Ouvre uniquement l'exécution comprise dans l'enveloppe documentée |
| `GO_AVEC_RÉSERVES` | Ouvre l'exécution bornée et impose le suivi des réserves définies |
| `NO_GO` | Interdit tout nouveau développement et renvoie à la conception |
| `REPORTÉ` / `EN_ATTENTE` | N'ouvre aucun nouveau lot ni aucune boucle autonome |

Le mandat WP-01 est une autorisation locale historique, ciblée et consommée. Il ne doit pas être prolongé vers WP-02, Wave 2, une action externe ou `AUTO_NEXT`.

## 6. Indépendance des contrôles WP-01

**Statut : `INDÉPENDANCE_DÉMONTRÉE`.**

| Contrôle | Sous-agent / mission | Candidate | Livrable et verdict |
|---|---|---|---|
| Technique | `/root/cerberus_tech_v2` — `MIGRATION-V2-WP01-TECH-20260905` | `wp01-7d113810cc2d0216` | [Rapport technique](../2026-09-05_MIGRATION_V2/RAPPORT_TECHNIQUE_WP01.md) — `TECH_VERIFIED` |
| Fonctionnel | `/root/cerberus_fonc_v2` — `MIGRATION-V2-WP01-FONCTIONNEL-20260905` | `wp01-7d113810cc2d0216` | [Rapport fonctionnel](../2026-09-05_MIGRATION_V2/RAPPORT_FONCTIONNEL_WP01.md) — `FUNCTIONAL_VERIFIED` |

La preuve d'indépendance repose sur deux chemins de sous-agents, deux missions et deux mandats de contrôle distincts, exécutés sur la même candidate, puis consolidés par une troisième mission `/root/cerberus_gate_v2` (`MIGRATION-V2-WP01-GATE-20260905`). Les rapports spécialisés séparent aussi leurs critères, commandes et limites. Cette indépendance organisationnelle ne transforme pas `FUNCTIONAL_VERIFIED` en acceptation business et ne couvre pas le cyber.

Le développement de WP-01 reste historiquement attribué à HEPHAESTOS avant la migration. Il n'est pas renommé rétroactivement en production HEPHAESTOS-DEV V2.

## 7. Applicabilité cyber de WP-01

WP-01 touche des surfaces qui peuvent avoir un effet de sécurité : source et priorité de `DATABASE_URL`, retrait de `.env` du suivi Git, exemple de configuration, identifiants historiques, variable `DISABLE_AUTH`, workflow GitHub Actions, journaux, artefacts CI et accès MySQL. Une analyse cyber limitée à la configuration, aux secrets et à la CI est donc **applicable en première analyse**.

### Éléments déjà observés

- `DATABASE_URL` est externalisée et son absence provoque une erreur explicite.
- `.env` est conservé localement, ignoré et retiré de l'index ; son contenu n'est pas reproduit dans les preuves.
- `.env.example` contient un exemple et active l'authentification par défaut.
- Le code source contrôlé ne contient plus l'URL MySQL historique en littéral.
- Le workflow de test utilise `DISABLE_AUTH=true` et des identifiants MySQL de service éphémère visibles dans le YAML.
- Des identifiants MySQL figurent déjà dans l'historique Git ; leur validité, leur rotation et leur traitement restent `À_CONFIRMER`.

### Sources et décisions manquantes

- référentiel SSI adopté et versionné : `À_FOURNIR` ;
- standard de gestion des secrets et de durcissement GitHub Actions : `À_FOURNIR` ;
- classification de l'environnement et des données : `À_CONFIRMER` ;
- propriétaire du risque, autorité SSI, cibles et outils autorisés : `À_CONFIRMER` ;
- traitement attendu des identifiants historiques et de `DISABLE_AUTH` : `À_CONFIRMER`.

**Disposition actuelle :** aucun verdict `CYBER_VERIFIED` ou `CYBER_NOT_APPLICABLE` n'est prononcé. Si un verdict formel est requis avant adoption des sources, l'état attendu est `CYBER_BLOCKED`. Aucun contrôle intrusif, offensif, externe ou destructif n'est inclus dans cette régularisation.

## 8. Réserves maintenues

| Réserve | Statut |
|---|---|
| AC-11 — preuve GitHub Actions/MySQL/healthcheck | `OUVERTE`, autorisation ciblée demandée séparément |
| Applicabilité et verdict cyber | Applicabilité préliminaire établie ; conclusion formelle `EN_ATTENTE` |
| IAM, `/dev/api-key`, rôles et `DISABLE_AUTH` produit | Hors WP-01 ; lot séparé non autorisé |
| Identifiants dans l'historique Git | Traitement et rotation `À_CONFIRMER` |
| 16 avertissements pytest préexistants | Dette technique hors WP-01 |
| Acceptation métier | `EN_ATTENTE` |

## 9. Limite de la régularisation

Ce document prépare des décisions. Il n'enregistre aucun nouveau `GO`, ne valide pas WP-01 à J5, n'autorise pas `AUTO_NEXT` et n'exécute aucune action GitHub, MySQL, cyber externe, commit, push ou déploiement.

## 10. Décisions humaines du 2026-09-05

- J2 : `GO_AVEC_RÉSERVES`, périmètre H0 minimal D-06, livrable API/Swagger et profil `SOCLE + DEV + INT + IAM`. Les autres inconnues restent `À_CONFIRMER`.
- J3 : `ATTEINT_AVEC_RÉSERVES`. Xavier est formellement le décideur et pilote de ce projet individuel ; les autorités spécialisées restent distinctes lorsqu'elles sont requises.
- J4 : `REPORTÉ`, avec mode `SPRINTS` retenu. Aucun nouveau lot ni `AUTO_NEXT` n'est autorisé ; WP-02 doit être préparé `READY` avant une nouvelle enveloppe.
- AC-11 : test MySQL local isolé autorisé ; GitHub Actions, commit et push non autorisés.
- Cyber : contrôle minimal local avec le skill Codex Security autorisé ; aucun test intrusif, externe ou destructif.
- J5 : `EN_ATTENTE` jusqu'à consolidation d'AC-11 et du contrôle cyber minimal.

Ces décisions prennent effet le 2026-09-05 et ne sont pas antidatées.
