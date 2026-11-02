---
title: DigiCheese - Cadrage et faisabilité J1
date: 2026-09-05
version: 0.1.0
status: dossier-j1-verifie-profil-propose
---

# DigiCheese — Cadrage et faisabilité

Date d'exécution : **2026-09-05**, Europe/Paris. Dossier préparé par ZEUS à partir de l'étude ATHENA et de l'inspection actuelle du dépôt. ARGOS a été sollicité mais n'a pas produit de verdict en raison d'une limite d'usage des sous-agents ; ZEUS a repris localement la faisabilité initiale. L'état du contrôle indépendant est référencé dans [CONTROLE_J1.md](CONTROLE_J1.md).

**L'étude J1 est lancée sur demande explicite de l'utilisateur.** Le présent dossier prépare la reprise du développement sur `xavier`. Le périmètre produit, le profil définitif et le passage à J2 restent à décider. Aucune acceptation de production ou validation métier n'est déduite de la présence du code.

## 1. Identification, mandat et source de vérité

| Élément | État au 2026-09-05 |
|---|---|
| Projet | TP_digicheese / DigiCheese, TP Diginamic et socle de développement évolutif [S01] |
| Demandeur | Utilisateur de la présente session ; nom et rôle de gouvernance officiels : à-confirmer |
| Chef de projet / PMO, Sponsor, validation métier | à-confirmer ; les contributions historiques de l'équipe dans DOC/README.md ne valent pas délégation actuelle |
| Dépôt étudié | C:/Users/xavie/Dropbox/projet_perso_xavier/TP_digicheese |
| Branche | xavier, choix explicitement confirmé par l'utilisateur |
| HEAD | 6790d40902c32f207923c8d174169e280cddadc9 |
| Travail local | Déplacements Wave 1, ajouts Wave 2/SQL/extraits/checklist et fichiers Obsidian préexistants ; distincts du contenu commité |
| Baseline technique observée | HEAD ci-dessus + photographie des fichiers locaux au début de l'étude ; cette photographie n'est pas une baseline produit approuvée |
| Baseline produit, planning, budget/charges et tolérances | à-confirmer ; aucun engagement ni seuil actuel n'est inventé |
| Outil PPM officiel | à-confirmer ; aucun accès à un PPM externe n'a été effectué |
| Source de travail du cadrage | Le présent dossier regroupe constats, propositions, risques, questions et actions de J1 ; il n'est pas désigné comme PPM officiel |
| Source des décisions utilisateur | Messages de cette session, repris dans [MISSION_J1.md](MISSION_J1.md) et dans le registre §10 |
| Méthode | SOCLE COMMUN + MODULES UTILES, paquet utilisateur 1.2.0 du 2026-09-04, importé le 2026-09-05 |

Les faits portent le statut **VÉRIFIÉ** lorsqu'une source ou un contrôle actuel les soutient, **INFÉRÉ** pour une conclusion dérivée, **HYPOTHÈSE** pour une piste et **à-confirmer** pour une inconnue. Les recommandations restent **PROPOSÉES** jusqu'à une décision humaine tracée.

## 2. J1 — Besoin, valeur et périmètre de l'étude

**Besoin actuel — VÉRIFIÉ :** reprendre le développement du projet existant et disposer d'un cadrage qui sépare les obligations du TP, les extensions envisagées et le fonctionnement réellement prouvé. Le README décrit un TP pédagogique prioritaire et un socle évolutif [S01].

**Scénario métier documentaire — VÉRIFIÉ comme contenu de la source :** la fromagerie du cahier des charges souhaite remplacer une application Access/VBA pour la gestion des cadeaux fidélité, avec administration, colis et stocks [S02]. L'existence d'un commanditaire, d'une base Access à reprendre ou d'une exploitation réelle dans le projet actuel reste **à-confirmer**.

**Valeur initiale — PROPOSÉE :** obtenir une application structurée, testable, documentée et démontrable ; limiter les reprises de travail dues aux règles ouvertes et au périmètre contradictoire. Les gains métier quantifiés, coûts évités et bénéfices mesurés restent **à-confirmer**.

**Bénéficiaires :** le développeur qui reprend le dépôt ; l'équipe et les évaluateurs cités par la documentation, avec implication actuelle à-confirmer ; les administrateurs et opérateurs colis/stocks du scénario. Les clients sont bénéficiaires indirects ; aucun accès direct de clients réels n'est présumé.

| Périmètre | Contenu |
|---|---|
| Inclus dans l'étude J1 | Inventaire de l'existant et des sources ; comparaison Data/DevOps/Wave 2 ; besoin, valeur, minimum démontrable, profil initial, faisabilité, screenings, risques et décisions utiles avant J2 |
| Production documentaire autorisée | Import personnel de l'équipe et nouveaux livrables dans DOC/GOUVERNANCE/2026-09-05_J1 |
| Hors exécution de cette mission | Modification du code ou des tests, migration/seed, installation des dépendances applicatives, lancement de services, changement de branche, commit/push, déploiement et écriture dans un outil externe |
| Périmètre produit futur | à-confirmer à J2 ; les options étudiées ne deviennent pas des fonctions autorisées à développer |
| Contraintes et urgence | Préservation du travail existant et des inconnues ; échéance actuelle, capacité et budget : à-confirmer |
| Effet d'un report — INFÉRÉ | Le risque de poursuivre sur des exigences contradictoires demeure ; son coût et son impact calendaire sont à-confirmer |

Les 5 jours et les soutenances de janvier 2026 indiqués dans les sujets sont historiques [S03]. Ils ne sont pas repris comme planning actuel.

## 3. État réel et limites de preuve

| Statut | Constat | Preuve et portée |
|---|---|---|
| VÉRIFIÉ | API FastAPI structurée en routers/services/repositories/schemas/models, avec SQLAlchemy et configuration MySQL | src/main.py, inventaire src et requirements.txt [S08] ; fonctionnement non exécuté |
| VÉRIFIÉ | 59 fichiers Python dans src, 13 fichiers test_*.py, 48 fonctions de test définies | Inspection AST du 2026-09-05 ; ce sont des définitions, pas des tests réussis |
| VÉRIFIÉ | 47 déclarations statiques de routes HTTP et 9 tables ORM t_* | Inventaire AST ; nombre de déclarations source, sans validation dynamique de l'API |
| VÉRIFIÉ | Référentiels administratifs, utilisateurs/rôles, communes/adresses/clients présents | Modèles et routeurs actuels [S08] |
| VÉRIFIÉ | Aucun routeur ni modèle ORM commandes ou stocks identifié dans src | Inventaire complet src et routeurs importés dans src/main.py:10-19,44-53 |
| VÉRIFIÉ | Interface statique d'administration Objets/Conditionnements et appels API présents | digicheese-ui/README.md et js/api.js [S09] ; parcours navigateur non exécuté |
| VÉRIFIÉ | Workflow qualité présent : tests, couverture, analyse, k6, consolidation | .github/workflows/quality.yml [S10] ; aucun résultat CI courant consulté |
| VÉRIFIÉ | Tests configurés avec SQLite mémoire et désactivation générale de l'authentification ; tests unitaires d'habilitation distincts présents | tests/conftest.py:25-41 et tests/test_dependencies.py [S11] ; la présence de ces tests ne prouve pas une matrice de droits complète |
| VÉRIFIÉ | Le venv référence C:/Python313 ; C:/Python313/python.exe est absent ; Python global 3.14.7 sans pytest, FastAPI, SQLAlchemy ni email-validator | .venv/pyvenv.cfg et contrôle de présence du 2026-09-05 ; tests applicatifs non exécutés |
| VÉRIFIÉ | .env suivi par Git et .env.example absent | git ls-files et inventaire actuel ; aucune valeur de secret reproduite dans ce dossier |
| VÉRIFIÉ | Guide utilisateur et FAQ vides ; liens fonctionnels de l'index pointant encore vers l'ancien emplacement | DOC/UTILISATION et DOC/README.md:19-25 [S12] |
| à-confirmer | Application effectivement déployée, recette passée, service exploité et données réelles présentes | Les assertions « production » de Wave 2 ne suffisent pas à établir ces faits [S06] |

La lecture syntaxique Python n'a détecté aucune erreur dans les sources et tests examinés. Elle ne vérifie ni les imports, ni le démarrage, ni les règles métier, ni les performances. Les rapports historiques et la checklist sont utilisés comme sources de questions, jamais comme résultats d'exécution actuels.

## 4. Besoin et options de périmètre — PROPOSÉES

| Option étudiée | Contenu et valeur | Conditions et limites |
|---|---|---|
| A — Consolider le TP Data | Stabiliser et démontrer les CRUD Admin ; clients OP-colis en option selon le sujet | Option recommandée pour le premier incrément d'étude ; choix du périmètre pédagogique et liste complète des obligations à-confirmer [S03,S05] |
| B — Ajouter les commandes du sujet DevOps | Compléter le parcours colis par commandes et droits associés | Dépend de la cible pédagogique et des règles commande/conditionnement/archivage ; effort à-confirmer [S04] |
| C — Étendre vers Wave 2 | Commandes/détails, prix, relations de conditionnement, rôles, stocks et boutique | Périmètre plus large ; schéma, règles, UI, données et capacité à arbitrer ; n'est pas validé par la seule présence d'un backlog [S06,S07] |

**Premier parcours démontrable candidat :** un utilisateur autorisé crée, consulte, modifie et supprime un objet de référence selon les règles retenues, avec contrôle d'une entrée invalide et d'une action interdite, persistance et procédure reproductible. Le parcours est déjà décrit dans Wave 1 [S05]. Cette unité de démonstration ne remplace pas l'ensemble du CRUD Admin demandé par le TP.

**Éléments reportables proposés :** commandes jusqu'au choix du périmètre et des règles ; stocks/boutique jusqu'à clarification des mouvements ; front complet jusqu'au choix du livrable ; mailing, statistiques et impression jusqu'à justification de priorité.

### Critères et KPI candidats

Les critères ci-dessous sont des **propositions à valider à J2**, distinctes des critères documentaires de fin de mission.

- Le parcours retenu s'exécute sur un jeu de démonstration identifié, dans un environnement désigné, avec résultat daté.
- Les données relues reflètent les modifications acceptées ; les opérations invalides ou interdites sont rejetées sans effet indésirable.
- La suppression suit la règle métier retenue et explicite les dépendances.
- Une autre personne peut rejouer la procédure ; chaque exigence retenue dispose d'un scénario et d'une preuve ou d'un écart explicite.

| KPI candidat | Mesure | Situation initiale | Cible, échéance et propriétaire |
|---|---|---|---|
| Réussite des parcours | Parcours réussis / parcours exécutés, version et environnement identifiés | à-confirmer | à-confirmer |
| Exigences reliées à une preuve | Exigences avec scénario et résultat / exigences retenues | à-confirmer | à-confirmer |
| Reproductibilité | Résultat d'une nouvelle exécution depuis la procédure | à-confirmer | à-confirmer |
| Droits métier | Cas autorisés/interdits vérifiés / cas attendus dans la matrice | à-confirmer | à-confirmer |
| Cohérence des données | Cas de règles métier réussis / cas exécutés | à-confirmer | à-confirmer |
| Qualité complémentaire | Tests, couverture, latence et taux d'erreurs, déjà envisagés dans Wave 2 | à-confirmer | à-confirmer |

## 5. Profil SOCLE COMMUN + MODULES UTILES

**Profil initial recommandé : SOCLE COMMUN + DEV + INT + IAM. Statut : PROPOSÉ. Validation humaine de J2 : EN_ATTENTE.**

Le SOCLE comprend cadrage, pilotage, parties prenantes, périmètre, planning, charges/budget, risques, KPI, RGPD, SSI, conception, validation, déploiement, Run et clôture. Dans cette étude, le contexte, les sources et les questions sont renseignés ; les engagements, activités ultérieures et autorités sont à préparer avec les jalons concernés. Aucun élément du socle n'est supprimé parce que le projet est pédagogique.

| Module examiné | Proposition initiale | Déclencheur et justification | Impact initial |
|---|---|---|---|
| DEV | PROPOSÉ | Reprise de développement, API et tests existants | Construction, versions, tests et qualité à planifier ; charges à-confirmer |
| INT | PROPOSÉ | API attendue et interface statique consommatrice ; aucun système tiers présumé | Contrats d'API, flux et tests d'intégration à étudier |
| IAM | PROPOSÉ | Comptes, rôles, clés d'API et autorisations | Matrice de droits et scénarios autorisés/interdits à définir |
| ON-PREM | CONDITIONNEL | Exécution locale décrite ; infrastructure sur site et responsabilité d'exploitation à-confirmer | À activer si les environnements ou un déploiement sur site entrent effectivement dans le mandat |
| CLOUD | NON RETENU au profil initial proposé | Aucun service Cloud du produit identifié ; GitHub et Dropbox sont des outils utilisés, pas une architecture produit décidée | Réexaminer si la cible d'hébergement l'exige |
| SAAS | NON RETENU au profil initial proposé | Aucun produit éditeur à sélectionner ou intégrer identifié | Réexaminer si une solution SaaS entre dans le périmètre |
| DATA | CONDITIONNEL | Une reprise Access, migration ou transformation serait un déclencheur ; ni le nom du cursus Data ni MySQL seuls ne le sont | Mapping, qualité, réconciliation et retour arrière si reprise retenue ; données sources à-confirmer |
| CHANGE | CONDITIONNEL | Utilisateurs réels et changement d'usage ou de pratique à-confirmer | Formation, adoption et support à définir si déclenché |
| DECOM | CONDITIONNEL | Remplacement Access décrit dans le scénario, mais aucun arrêt réel autorisé | Dépendances, archivage et retrait des accès uniquement si décommissionnement retenu |

Tout ajout/retrait ultérieur d'un module validé suivra une décision tracée. La formalisation de ce profil ne vaut pas commande de réalisation.

## 6. Screenings obligatoires — niveau J1

### RGPD

**Statut : EN_COURS, screening documentaire initial réalisé ; résultat humain à-confirmer.** Les modèles prévoient noms/prénoms, email, téléphone, adresses et comptes utilisateurs [S13]. La conception porte donc sur des catégories susceptibles d'identifier des personnes. La présence effective de données réelles, leur provenance et leur utilisation restent **à-confirmer** ; aucun contenu de base n'a été consulté.

| Élément | Résultat ou action d'étude |
|---|---|
| Finalités candidates | Gestion des utilisateurs, clients et référentiels ; traitement réellement exploité : à-confirmer |
| Catégories | Identité, coordonnées, comptes et habilitations ; étendue réelle : à-confirmer |
| Responsable humain / autorité RGPD | à-confirmer |
| Questions avant J2 | Données fictives ou réelles, sources, destinataires, accès, conservation, suppression et contexte de démonstration |
| Analyse complémentaire | À qualifier avec l'autorité compétente selon le traitement retenu ; nécessité d'un registre ou d'une AIPD : à-confirmer |
| Échéance | Résultat initial et actions à intégrer avant J2 ; date calendaire à-confirmer |

Il s'agit d'un inventaire de questions et de preuves de conception, sans conclusion de conformité ni avis juridique.

### SSI

**Statut : EN_COURS, screening documentaire initial réalisé ; exigences et autorité à-confirmer.** L'API, les habilitations et la persistance justifient le screening. Les constats initiaux portent sur la configuration, les accès et la capacité à prouver les contrôles ; ils ne constituent pas un audit de sécurité exhaustif.

| Sujet | Observation initiale ou action |
|---|---|
| Identités et accès | Clés d'API/rôles présents ; matrice des droits actuelle et cible à-confirmer |
| Configuration | .env suivi et configuration applicative à examiner ; .env.example absent ; aucune valeur de secret reproduite |
| Surface et données | Exposition réelle de l'API, catégories de données et environnements à-confirmer |
| Preuves | Tests de droits présents, mais campagne applicative et CI actuelle non exécutées/consultées |
| Autorité, exigences et réserves acceptables | à-confirmer ; aucune réserve acceptée au nom de l'utilisateur |
| Label SSI | Dispositif applicable et signataire à-confirmer ; aucune attestation émise. Préparation selon la méthode avant J6, pas exigence de déploiement satisfaite à J1 |
| Échéance | Exigences initiales et plan d'actions avant J2 ; date calendaire à-confirmer |

**Métier et Run :** validation métier, environnement de service, exploitant, disponibilité attendue, sauvegarde, support et modalités de reprise sont **à-confirmer**. Les contrôles des jalons ultérieurs sont à préparer au moment utile.

## 7. Faisabilité initiale et trajectoire d'étude

**Faisabilité métier : PARTIELLE.** Un scénario, des sujets pédagogiques et des parcours existent ; périmètre de référence, règles et critères actuels restent à arbitrer.

**Faisabilité organisationnelle : à-confirmer.** Les noms/contributions historiques existent, mais les disponibilités, autorités, responsabilités et cadence actuelles ne sont pas établies. « Bimensuelle » n'est pas converti silencieusement en un calendrier.

**Faisabilité technique : PARTIELLE.** Le socle est lisible et structuré ; ses sources et tests peuvent être examinés. Sa reproductibilité n'est pas prouvée dans l'environnement actuel. Le SQL Wave 2 est un document local distinct du modèle ORM ; son application n'est pas autorisée par cette étude.

Compléments techniques vérifiés par ZEUS en lecture seule, après lecture de la configuration et des tests :

| Observation | Preuve actuelle | Conséquence pour l'étude |
|---|---|---|
| Le routeur de développement retourne une clé d'API depuis un identifiant utilisateur, sans dépendance d'authentification locale ou globale déclarée dans l'application inspectée | src/routers/dev_router.py:7-17 et src/main.py:30,44 | Qualifier l'exposition et préparer le traitement de cette route avant de démontrer des accès protégés ; pas de test d'exploitation exécuté |
| DISABLE_AUTH peut court-circuiter l'authentification et les rôles | src/utils/dependencies.py:19-20,39-40 | Identifier la configuration cible et tester avec authentification active ; ne pas confondre les tests CRUD avec une preuve de sécurité |
| Le seed utilise OP-COLIS alors que le routeur clients exige OP-colis et compare les chaînes sans normalisation | src/utils/create_db.py:20, src/routers/client_router.py:9, src/utils/dependencies.py:42-43 | Risque d'un refus de droit pour le rôle seedé ; convention et test de bout en bout à préparer |
| L'utilisateur ORM possède une seule clé de rôle, alors que Wave 2 propose une table d'association | src/models/utilisateur.py:16,19 et SQL Wave 2:15-20 | Cumul des rôles et éventuelle migration à décider ; aucune transformation du modèle réalisée |
| Le SQL Wave 2 utilise des noms sans préfixe t_* et contient des VARCHAR sans longueur explicite | database/modelisation_base_digicheese_wave2.sql:1-45 ; inventaire ORM | Compatibilité et validité SQL à établir dans une étude dédiée avant application ; aucun SQL exécuté |
| L'URL de connexion est une valeur littérale du code ; EmailStr est utilisé sans dépendance email-validator explicite dans requirements.txt | src/database.py:4-6, src/schemas/client_schema.py:2,7,22,58 et requirements.txt | Préparer configuration et dépendances reproductibles ; aucune valeur de connexion divulguée, aucun diagnostic d'installation réussie |

Ces observations initiales justifient DEV/INT/IAM et les questions de migration conditionnelles. Elles ne constituent ni un audit exhaustif, ni un verdict attribué à ARGOS.

Trajectoire proposée : préciser le périmètre utile → définir un parcours et ses preuves → préparer la remise en état de l'environnement et les contrôles → choisir un incrément limité → soumettre besoin, faisabilité et profil à J2. Le plan de développement, les fichiers à modifier et les éventuelles migrations seront préparés après les décisions appropriées.

Budget initial, charges, capacité disponible, séquencement calendaire, dates de jalons et prévision à terminaison : **à-confirmer**, à estimer une fois le périmètre et les ressources précisés. Aucun engagement de 5 jours, 2 sprints ou 11 sprints n'est repris automatiquement.

## 8. Gouvernance et état des jalons

| Partie prenante | Ce qui est connu | Autorité/implication actuelle |
|---|---|---|
| Utilisateur de la session | A choisi xavier et demandé l'étude J1 | Décideur du mandat de cette session ; rôle PMO/Sponsor officiel à-confirmer |
| Équipe du TP | Contributions historiques dans DOC/README.md | Participation et responsabilité actuelles à-confirmer |
| Enseignant / évaluateur | Sujets et critères pédagogiques disponibles | Référentiel retenu, calendrier et validateur actuel à-confirmer |
| Utilisateurs métier | Administrateurs et opérateurs du scénario | Représentants et participation réels à-confirmer |
| DPO / SSI / architecture / exploitation | Aucun responsable actuel nommé par le mandat | à-confirmer ; aucun agent ne se substitue à ces autorités |
| ZEUS / spécialistes | Préparation, analyse et contrôle du dossier | Assistance et recommandations, sans décision de jalon à la place des autorités |

| Jalon | Situation dans ce cadrage | Preuve ou prochaine condition |
|---|---|---|
| J1 — GO Étude | Étude lancée sur mandat utilisateur ; formalisation institutionnelle éventuelle : à-confirmer | Demande du 2026-09-05 tracée D-02 ; aucune permission identique redemandée |
| J2 — GO Conception | EN_ATTENTE | Besoin/périmètre, profil, faisabilité, critères, charges et screenings initiaux à décider |
| J3 — Kick-off | EN_ATTENTE | Équipe, responsabilités, cadence et objectifs à partager |
| J4 — GO Développement / Production | EN_ATTENTE dans cette nouvelle démarche | Solution, plan, contrôles et baseline approuvés à préparer ; le code antérieur ne vaut pas preuve de GO |
| J5 — GO Tests | EN_ATTENTE | Version, environnement, données et critères à préparer |
| J6 — GO / NO-GO Déploiement | EN_ATTENTE | Tests, acceptations, cutover/rollback et contrôles applicables à prouver |
| J7 — Mise en service | EN_ATTENTE | Déploiement et disponibilité opérationnelle à constater |
| J8 — Clôture | EN_ATTENTE | Bilan, transfert et décision humaine à préparer |

Cadence COPROJ et interprétation de « bimensuelle », réunions, participants, tolérances et circuit d'escalade : **à-confirmer**. Aucun COPROJ n'a été tenu. Une éventuelle synthèse future devra référencer ce dossier et la source PPM désignée, sans ressaisie concurrente.

## 9. Risques, problèmes et inconnues

Les identifiants ci-dessous sont locaux au dossier. Les probabilités et impacts chiffrés, propriétaires responsables et échéances calendaires sont **à-confirmer**. Les mesures sont proposées et ne sont pas exécutées par cette étude.

| ID | Risque ou problème observé | Preuve / module | Conséquence possible et mesure proposée |
|---|---|---|---|
| R-01 | Périmètres Data, DevOps et Wave 2 confondus | S03-S07 / DEV | Développement excessif ou incomplet ; choisir le référentiel avant J2 |
| R-02 | Production affirmée sans preuve actuelle | S06 / SOCLE, Run | Mauvaises hypothèses de compatibilité/exploitation ; identifier environnements et preuve d'acceptation |
| R-03 | Front et planning contradictoires | S07 / INT, DEV | Charge et livrable mal évalués ; choisir API/Swagger ou UI et estimer avec capacité réelle |
| R-04 | Règles commande, stock et suppression ouvertes | S05-S07 / DEV, IAM | Résultats métier incohérents ; décider seulement les règles nécessaires au premier incrément |
| R-05 | Schéma Wave 2 distinct du socle ORM | database/ et S08 / DATA conditionnel | Migration ou compatibilité non maîtrisée ; comparer les modèles avant toute application SQL |
| R-06 | Reproductibilité non démontrée dans l'environnement actuel | S11 et inventaire / DEV | Démonstration/tests impossibles ; préparer un environnement isolé et une campagne adaptée dans un lot autorisé |
| R-07 | Contrôles d'accès/configuration sans preuve de validation actuelle | S10-S11 / IAM, SSI | Comportement sensible mal maîtrisé ; cartographier les accès et définir les contrôles |
| R-08 | Nature et gouvernance des données inconnues | S13 / RGPD | Démonstration ou exploitation avec données inadaptées ; identifier provenance, finalité et responsables |
| R-09 | Documentation partielle et liens obsolètes | S12 / SOCLE | Reprise et démonstration difficiles ; prévoir mise en cohérence après choix du périmètre |
| R-10 | Travail local et baseline produit non consolidés | Git, S06-S07 / DEV | Confusion entre version livrée et préparation locale ; conserver les traces et préparer des commits cohérents dans un mandat ultérieur |

| Question | Information à obtenir | Jalon / effet si absente | Répondant et statut |
|---|---|---|---|
| Q-01 | Cible actuelle : TP Data, extension DevOps ou produit Wave 2 ? | J2 ; périmètre non validable | Utilisateur / évaluateur à désigner ; à-confirmer |
| Q-02 | Livrable API/Swagger seul ou interface incluse ? | J2 ; critères et charge incomplets | Utilisateur / métier à désigner ; à-confirmer |
| Q-03 | Qui porte PMO, décision de périmètre, validation métier, SSI, RGPD et Run ? Quel PPM ? | J2/J3 ; gouvernance non formalisée | Utilisateur ; à-confirmer |
| Q-04 | Capacité disponible, date cible et budget/charge autorisés ? | J2/J4 ; estimation et baseline à préparer | Utilisateur ; à-confirmer |
| Q-05 | Démonstration locale ou service réellement exploité ? Environnements et données fictives/réelles ? | J2 ; faisabilité et contrôles incomplets | Utilisateur / exploitant à désigner ; à-confirmer |
| Q-06 | Droits, cumul des rôles, suppression et ressources référencées ? | J2/J4 ; règles à préciser selon incrément | Métier à désigner ; à-confirmer |
| Q-07 | Conditionnement, calcul nbColis, archivage et mouvements de stock ? | J2/J4 si extension retenue | Métier à désigner ; à-confirmer |
| Q-08 | Reprise Access, migration et arrêt d'un ancien système réellement prévus ? | J2 ; DATA/DECOM conditionnels | Utilisateur / propriétaire des données à désigner ; à-confirmer |
| Q-09 | Quels critères et preuves seront acceptés pour le premier parcours et le TP complet ? | J2/J5 ; réussite non définie | Utilisateur / évaluateur ; à-confirmer |
| Q-10 | Cadence COPROJ, tolérances et responsabilités de suivi ? | J3/J4 ; pilotage à formaliser | PMO à désigner ; à-confirmer |

Ces questions ne bloquent pas la production du présent dossier J1. Elles deviennent des conditions de décision pour le jalon ou l'extension indiqué.

## 10. Décisions et actions de travail

| ID | Date | Décision / proposition | Statut | Autorité et source |
|---|---|---|---|---|
| D-01 | 2026-09-05 | Poursuivre le développement sur xavier | VALIDÉE | Utilisateur, message précédent dans cette session |
| D-02 | 2026-09-05 | Importer l'équipe et lancer le cadrage J1 avec SOCLE + MODULES et inconnues « à-confirmer » | VALIDÉE pour ce mandat | Demande utilisateur actuelle, MISSION_J1.md |
| D-03 | 2026-09-05 | Profil initial SOCLE + DEV + INT + IAM, autres modules selon §5 | PROPOSÉE | Recommandation ATHENA/ZEUS ; décision J2 en attente |
| D-04 | 2026-09-05 | Étudier d'abord la consolidation d'un parcours Admin démontrable | PROPOSÉE | ATHENA ; ne remplace pas le périmètre complet des sujets |
| D-05 | à-confirmer | Choix du périmètre, UI, critères, charges et responsabilités | À_ARBITRER | Autorité humaine à désigner ; questions Q-01 à Q-10 |

| Action | Résultat attendu | Dépendance / point de passage | Responsable, charge et date |
|---|---|---|---|
| A-01 | Confirmer le référentiel pédagogique/produit et API/UI | Q-01/Q-02 ; avant J2 | à-confirmer |
| A-02 | Nommer les décideurs et préciser source PPM/cadence | Q-03/Q-10 ; J2/J3 | à-confirmer |
| A-03 | Identifier environnement cible et nature des données | Q-05 ; résultats initiaux RGPD/SSI à J2 | à-confirmer |
| A-04 | Fixer le premier parcours, les règles et les preuves attendues | A-01 puis Q-06/Q-09 ; avant J2 | à-confirmer |
| A-05 | Préparer un lot de restauration de reproductibilité et de validation du socle | A-03/A-04 ; autorisation d'exécution distincte, aucune installation applicative dans J1 | à-confirmer |
| A-06 | Comparer schémas et clarifier les règles des extensions retenues | A-01 et Q-07/Q-08 ; conditionnel avant conception concernée | à-confirmer |
| A-07 | Estimer charge, capacité et planning puis préparer le paquet J2 | A-01 à A-04 ; Q-04 | à-confirmer |
| A-08 | Préparer la correction des liens et des guides utiles | Périmètre retenu ; futur lot documentaire | à-confirmer |

Aucune baseline approuvée n'a été modifiée. Les propositions ci-dessus ne masquent pas les divergences des plans existants. Si un PPM officiel est désigné, transférer/référencer ces éléments avec leur historique plutôt que tenir deux registres concurrents.

## 11. Préparation de J2 et verdict du dossier

**Livrable J1 : produit et vérifié indépendamment par CERBERUS le 2026-09-05, verdict documentaire VERIFIED.** La demande, la valeur initiale, le périmètre d'étude, le profil initial et les screenings sont explicités ; les autorités et engagements inconnus sont conservés. **Étude : autorisée par le mandat utilisateur. Décision humaine J2 : EN_ATTENTE.**

Pour soumettre J2 : trancher Q-01/Q-02, nommer les responsabilités, préciser le parcours et ses critères, compléter la faisabilité et les résultats initiaux RGPD/SSI, estimer la capacité/charge et valider le profil. Le développement du premier lot sera cadré au jalon approprié, avec périmètre de fichiers et contrôles explicites.

Le verdict de contrôle documentaire, ses limites et le journal des contributions sont dans [CONTROLE_J1.md](CONTROLE_J1.md). Il ne constitue ni une validation de l'application, ni une acceptation métier, ni un GO de déploiement.

## 12. Sources et méthode

| Référence | Source | Passage / usage |
|---|---|---|
| S01 | [README](../../../README.md) | Lignes 19-41 et 81-103 : TP, objectifs et MVP documentaire |
| S02 | [Extrait du mini cahier des charges](../../../reports/raw/sujet_tp_extracts/MiniCahierDesChargesFromagerieDigiCheese.txt) | Lignes 6-8,96-143,233-262 : scénario Access, acteurs et rôles |
| S03 | [Sujet Data, extrait](../../../reports/raw/sujet_tp_extracts/PROJETTP7_API_WEB_2026_Data.txt) | Lignes 16-29,40-50 : périmètre et contraintes historiques |
| S04 | [Sujet DevOps, extrait](../../../reports/raw/sujet_tp_extracts/PROJETTP7_API_WEB_2026_Devops_V2.txt) | Lignes 40-48 : commandes et contrôles d'accès |
| S05 | [Périmètre Wave 1](../../FONC/wave1/Perimetre_In_Out.md), [parcours](../../FONC/wave1/Parcours_Utilisateur.md), [règles](../../FONC/wave1/Regles_Metier.md) | Périmètre lignes 17-37 ; parcours 14-35,58-68 ; rôles et données |
| S06 | [Contexte Wave 2](../../FONC/wave2/Contexte_Objectifs_wave2.md), [périmètre](../../FONC/wave2/Perimetre_In_Out_wave2.md) | Contexte lignes 3-15,35-38 ; périmètre lignes 9-44 |
| S07 | [Backlog Wave 2](../../FONC/wave2/Backlog_wave2.md), [plan de sprints](../../FONC/wave2/sprint_wave2.md), [règles](../../FONC/wave2/Regles_Metier_wave2.md) | Backlog 7-10,114-141,257-294,317-321 ; sprints 3-40,254-273 ; règles 15-48 |
| S08 | [Application](../../../src/main.py), [modèles](../../../src/models), [dépendances](../../../requirements.txt) | src/main.py:10-19,44-53 ; inventaire AST source/test au 2026-09-05 |
| S09 | [Interface statique](../../../digicheese-ui/README.md), [client API](../../../digicheese-ui/js/api.js) | Au J1 : intention UI et appels HTTP présents, comportement non testé. Le 2026-09-06 : 24 fichiers déplacés depuis `UML/digicheese-ui`, puis 17 fichiers adaptés dans le lot WP-03/WP-04 |
| S10 | Workflow qualité historique | Au J1 : définition locale des jobs, sans consultation de résultats distants. Le fichier `.github/workflows/quality.yml` a été supprimé localement dans WP-05 le 2026-09-06 |
| S11 | [Configuration de tests](../../../tests/conftest.py), [tests des dépendances d'accès](../../../tests/test_dependencies.py) | SQLite mémoire, désactivation d'authentification et tests de droits distincts |
| S12 | [Index documentaire](../../README.md), [checklist historique](../../../MEMOIRE_CHECKLIST_TP7_DATA_DEVOPS.md) | Index 19-25,39-52 ; checklist 3-7,108-122 ; vérification de taille des guides |
| S13 | [Client](../../../src/models/client.py), [utilisateur](../../../src/models/utilisateur.py), [adresse](../../../src/models/adresse.py) | Client 10-17 ; utilisateur 11-16 ; catégories de données prévues |
| S14 | [Modélisation Wave 2](../../../database/modelisation_base_digicheese_wave2.md), [SQL](../../../database/modelisation_base_digicheese_wave2.sql) | Proposition locale non appliquée, distincte des tables ORM |

Méthode : lectures actuelles et inspection statique, sans appel à l'application, à une base ou à un PPM externe. Les extraits TXT des sujets sont des sources secondaires locales : leur fidélité complète aux PDF n'a pas été revalidée dans cette mission. Les figures des pages 10 à 16 du mini cahier des charges, peu représentées dans l'extraction textuelle, n'ont pas été évaluées. La faisabilité détaillée les concernant reste à-confirmer.
