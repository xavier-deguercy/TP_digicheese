---
title: DigiCheese - Demande de décision consolidée J2 à J5
version: 0.1.0
date: 2026-09-05
status: j5-go-avec-reserves-auto-next-non-autorise
---

# DigiCheese — Demande de décision consolidée

Cette fiche permet d'enregistrer quatre décisions ou constats séparés. Chaque choix prendra effet à sa date réelle. Une validation de ligne ne valide pas les autres lignes et ne crée aucune autorisation implicite.

## 1. Séquence de décision

| Ordre | Objet | Statut actuel | Décision ou constat attendu |
|---|---|---|---|
| 1 | J2 — GO Conception | `GO_AVEC_RÉSERVES` | Décision humaine du 2026-09-05 |
| 2 | J3 — Kick-off | `ATTEINT_AVEC_RÉSERVES` | Constat humain du 2026-09-05 |
| 3 | J4 — GO Développement / Production | `REPORTÉ` ; mandat WP-01 consommé | Mode `SPRINTS` retenu, aucune nouvelle enveloppe ouverte |
| 4 | J5 — GO Tests / Validation business de WP-01 | `GO_AVEC_RÉSERVES` | Décision humaine du 2026-09-06 |

Le [dossier de régularisation](REGULARISATION_J2_J3_J4.md) expose les critères, preuves, inconnues et conséquences de J2, J3 et J4.

## 2. Demande d'autorisation ciblée AC-11

**Statut : MySQL local isolé autorisé le 2026-09-05 ; GitHub Actions non autorisé.** Cette décision ne couvre ni commit, ni push, ni modification de workflow, ni service distant.

### 2.1 Exécution distante GitHub Actions envisagée

| Champ | Proposition à autoriser ultérieurement |
|---|---|
| Cible | Dépôt `github.com/xavier-deguercy/TP_digicheese`, sur une branche et un commit contenant uniquement la candidate WP-01 autorisée |
| Déclenchement observé | Le workflow `.github/workflows/quality.yml` réagit actuellement à `push` et ne propose pas `workflow_dispatch` |
| Actions nécessaires | Isoler et relire le diff WP-01 ; exclure `.env` et tout travail local étranger ; créer un commit ciblé ; pousser la branche autorisée pour déclencher le workflow. Toute modification préalable du workflow, par exemple l'ajout de `workflow_dispatch`, demanderait une autorisation séparée |
| Effets attendus | Modification de l'historique Git distant ; exécution des jobs `unit-tests`, `debt-tech`, `perf-k6` et `consolidate-kpi` sur des runners GitHub ; installation des dépendances ; création d'un service MySQL 8 éphémère ; démarrage d'Uvicorn ; appel `/health` ; exécution k6 ; dépôt d'artefacts |
| Risques | Publication accidentelle de fichiers locaux hors WP-01 ou de secrets ; exposition de valeurs dans les logs ; mutation de branche ; consommation de minutes CI ; échec de workflow ou artefacts incomplets ; résultat trompeur si le SHA ou les jobs ne sont pas tous vérifiés |
| Protections attendues | Liste fermée des fichiers WP-01 ; diff relu ; `.env` absent ; identifiants fictifs et service éphémère uniquement ; branche et SHA nommés ; aucune donnée réelle ; permissions GitHub minimales |
| Preuves attendues | URL du run, branche, SHA, déclencheur, conclusion de chaque job, nombre de tests, logs d'installation, réponse `/health`, synthèse k6, artefacts bruts et consolidés, durée et réserves |

### 2.2 Validation locale MySQL complémentaire envisagée

| Champ | Proposition à autoriser ultérieurement |
|---|---|
| Cible | Docker local uniquement, avec MySQL 8 issu de `docker-compose.yml`, dans un projet Compose et un volume explicitement isolés ; aucune base distante ou donnée réelle |
| Actions nécessaires | Vérifier la configuration Compose ; contrôler la disponibilité du port 3308 ; créer le service et le volume isolés ; attendre l'état sain ; démarrer l'application avec la configuration de test ; appeler `/health` ; exécuter le smoke test applicable ; collecter les preuves ; arrêter et nettoyer les ressources autorisées |
| Effets attendus | Téléchargement éventuel de l'image ; création locale de conteneur, réseau et volume ; ouverture temporaire du port 3308 ; création possible du schéma et écriture de données de test éphémères ; consommation CPU, mémoire et disque |
| Risques | Collision de port ; modification d'un volume existant ; persistance involontaire de données ; exposition locale d'identifiants ; consommation de ressources ; nettoyage incomplet |
| Protections attendues | Nom de projet et volume dédiés ; aucune réutilisation de `mysql_data` existant sans décision ; données fictives ; secrets de test ; inventaire avant et après ; arrêt en cas de collision ou de cible ambiguë |
| Preuves attendues | Sortie `docker compose config`, version et empreinte de l'image, noms du projet/conteneur/volume, état de santé, journaux de création du schéma, HTTP 200 de `/health`, résultat k6, codes retour et preuve de nettoyage |

### 2.3 Choix AC-11 à enregistrer

- [ ] `AC11-AUTORISÉ-GITHUB` — autoriser plus tard le commit et le push ciblés décrits en 2.1, avec branche : `À_CONFIRMER`.
- [x] `AC11-AUTORISÉ-MYSQL-LOCAL` — exécution locale isolée décrite en 2.2, autorisée le 2026-09-05.
- [ ] `AC11-AUTORISÉ-DEUX-CIBLES` — autoriser les deux campagnes dans cet ordre : local isolé, puis GitHub sur la candidate validée.
- [ ] `AC11-RESTE-EN-RÉSERVE` — ne rien exécuter et conserver l'absence de preuve dynamique.
- [ ] `AC11-REPORTÉ` — demander une révision du protocole avant décision.

Autorité : Xavier, décideur et pilote formel du projet individuel. Date effective : 2026-09-05. GitHub Actions, commit et push restent non autorisés.

## 3. Disposition cyber à décider

L'analyse de WP-01 conclut à une applicabilité préliminaire pour la configuration, les secrets et la CI. Elle ne conclut ni à la conformité ni à la non-applicabilité.

Décision du 2026-09-05 : exécuter un contrôle cyber minimal local avec le skill Codex `codex-security:security-diff-scan`, limité aux changements WP-01, aux secrets, à `.env`, à `DATABASE_URL`, aux dépendances, au workflow GitHub Actions, à `DISABLE_AUTH`, à MySQL et aux journaux. Aucun test intrusif, offensif, destructif ou appel externe n'est autorisé.

| Option | Réserves | Conséquence |
|---|---|---|
| Fournir et adopter des sources cyber | Référentiels, versions, périmètres et autorité d'adoption requis | Permet de préparer puis d'autoriser une revue source-grounded |
| Autoriser seulement des contrôles locaux non intrusifs après adoption du périmètre | Cibles, outils et critères à nommer ; aucune action externe incluse | Produit des preuves limitées sans Label SSI ni verdict global automatique |
| Maintenir `CYBER_BLOCKED` | Sources `À_FOURNIR` et autorité SSI `À_CONFIRMER` | Empêche la porte V2 formelle si un verdict cyber est obligatoire |
| Décider ultérieurement `CYBER_NOT_APPLICABLE` | Exige une justification écrite par le propriétaire du risque après examen des surfaces identifiées | Ferme la porte cyber uniquement pour le périmètre explicitement justifié ; aucune telle décision n'est prise ici |

## 4. Options de décision J5 pour WP-01

| Option J5 | Réserves à enregistrer | Conséquences |
|---|---|---|
| `REPORTÉ` / maintien `EN_ATTENTE` | J2-J4 à régulariser ; AC-11 et cyber non tranchés | Conserve les preuves WP-01 ; aucun `QUALITY_GATE_PASSED`, `AUTO_NEXT`, commit, push ou déploiement |
| `GO_AVEC_RÉSERVES` pour ouvrir la recette ou validation business | AC-11 sans preuve dynamique, disposition cyber ouverte, 16 avertissements, identifiants historiques et acceptation métier distincte | Autorise uniquement la phase et les cibles écrites dans la décision ; ne vaut pas acceptation business, J6, déploiement ou `AUTO_NEXT` |
| `GO` | Nécessite d'abord les preuves AC-11 exigées, une disposition cyber justifiée et les critères métier ou réserves levées selon l'autorité | Ouvre la recette ou validation business sur la version identifiée ; ne vaut pas GO déploiement |
| `NO_GO` | Motifs de rejet et critères affectés à identifier | Renvoie WP-01 en correction ou en conception selon le défaut constaté ; aucune correction n'est lancée sans mandat |

La recommandation ZEUS reste `REPORTÉ` / `EN_ATTENTE` tant que J2, J3 et J4 ne sont pas régularisés. Les résultats `TECH_VERIFIED` et `FUNCTIONAL_VERIFIED` restent des preuves préparatoires sur `wp01-7d113810cc2d0216`.

## 5. Bloc de décision à compléter sans antidatation

| Objet | Choix | Autorité | Date effective | Réserves / limites |
|---|---|---|---|---|
| J2 | `GO_AVEC_RÉSERVES` | Xavier | 2026-09-05 | H0 minimal D-06 ; API/Swagger ; profil SOCLE + DEV + INT + IAM ; autres inconnues conservées |
| J3 | `ATTEINT_AVEC_RÉSERVES` | Xavier | 2026-09-05 | Xavier est formellement décideur et pilote du projet individuel ; autorités spécialisées à confirmer si requises |
| J4 | `REPORTÉ` | Xavier | 2026-09-05 | Mode `SPRINTS` retenu ; mandat WP-01 consommé ; WP-02 à préparer `READY` avant nouvelle enveloppe |
| AC-11 | `MYSQL_LOCAL_AUTORISÉ` | Xavier | 2026-09-05 | Projet et volume isolés ; GitHub, commit et push non autorisés |
| Cyber WP-01 | `CYBER_MINIMAL_AUTORISÉ` | Xavier | 2026-09-05 | Skill Codex Security, contrôle local non intrusif ; aucun verdict anticipé |
| J5 WP-01 | `GO_AVEC_RÉSERVES` | Xavier | 2026-09-06 | GitHub Actions retiré de la cible future ; contrôle cyber minimal accepté pour le MVP ; identifiants historiques à vérifier ; `AUTO_NEXT` non autorisé |

## 6. Arrêt du dispositif

Les contrôles autorisés sont terminés : [AC-11 MySQL local](RAPPORT_AC11_MYSQL_LOCAL.md) est vérifié et le [contrôle cyber minimal](RAPPORT_CYBER_MINIMAL_WP01.md) ne confirme aucune vulnérabilité nouvelle reportable, avec réserves. Xavier a décidé J5 `GO_AVEC_RÉSERVES` le 2026-09-06. GitHub Actions n'est plus une cible du projet après son usage d'apprentissage initial ; le workflow encore présent doit être retiré ou désactivé avant tout futur push. Aucune action GitHub, cyber externe, commit, push ou déploiement n'est autorisée. `AUTO_NEXT` reste non autorisé.

Le prochain lot proposé est décrit dans [PROCHAIN_LOT_REVUE_REFACTOR_UI.md](../2026-09-06_POST_WP01/PROCHAIN_LOT_REVUE_REFACTOR_UI.md).
