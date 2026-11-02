---
title: DigiCheese - Conception et planification du prochain lot
date: 2026-09-05
version: 0.2.0
status: lot-realise-localement-controle-avec-reserves-externes
---

# DigiCheese — Prochain lot de développement

Date d'exécution : **2026-09-05**, Europe/Paris.

Ce dossier a préparé le lot H0 à partir du [cadrage J1](../2026-09-05_J1/01_CADRAGE_FAISABILITE.md) et de la [reprise ZEUS](../2026-09-05_J1/REPRISE_ZEUS.md). Le 2026-09-05, le chef de projet humain a donné le mandat explicite « lance le développement du lot ». Ce mandat autorise la réalisation locale de WP-01 ; l'autorité institutionnelle et la validation formelle des jalons DSI restent à-confirmer.

## 1. Références et état de gouvernance

| Élément | État |
|---|---|
| Projet | TP_digicheese / DigiCheese |
| Branche de travail | `xavier` |
| HEAD de préparation | `6790d40902c32f207923c8d174169e280cddadc9` |
| Décision H0 | VALIDÉE : fusion minimale Data + DevOps ; baseline Admin + Clients ; stabilisation avant commandes ; front hors H0 ; Wave 2 futur backlog non validé |
| Profil | SOCLE + DEV + INT + IAM, PROPOSÉ ; validation formelle J2 à-confirmer |
| PPM officiel | à-confirmer ; ce dossier est le support local de préparation |
| Responsable PMO / Sponsor | à-confirmer |
| J2 | EN_ATTENTE |
| J3 | EN_ATTENTE |
| J4 | GO de réalisation locale WP-01 donné par le chef de projet humain le 2026-09-05 ; validation institutionnelle à-confirmer |
| Autorisation actuelle | Réalisation et contrôles locaux de WP-01 ; aucun commit, push, déploiement ou service distant autorisé |

Le dépôt contient déjà de nombreux déplacements et ajouts locaux Wave 1/Wave 2, ainsi que des fichiers Obsidian. Ils appartiennent au travail existant et doivent rester intacts. Le lot ci-dessous ne les utilise pas comme surface de modification.

## 2. Choix du prochain lot

### WP-01 — Configuration et environnement de test reproductibles

**Recommandation ARGOS/ZEUS : PROPOSÉE.**

Objectif observable : depuis un clone ou checkout propre disposant de Python 3.13, une personne peut créer un environnement, installer les dépendances, configurer la base sans secret dans le code, puis exécuter les contrôles ciblés avec des commandes documentées. La preuve attendue porte sur l'installation et les tests ; elle ne prouve ni un déploiement ni l'ensemble du H0.

Ce lot précède les corrections IAM. Il retire les blocages qui empêchent aujourd'hui de tester proprement la protection des routes et les rôles.

### Pourquoi ce lot vient en premier

- `EmailStr` est utilisé dans `src/schemas/client_schema.py`, tandis que `email-validator` est absent de `requirements.txt`.
- `src/database.py` contient une URL MySQL littérale.
- `.env` est suivi par Git alors qu'il est aussi ignoré ; aucun `.env.example` n'est présent.
- Le `.venv` courant référence `C:/Python313`, qui n'existe pas sur la machine observée. Le Python global 3.14 ne possède pas les dépendances applicatives.
- Les tests importent l'application avant de remplacer sa session SQLAlchemy ; la variable de test doit donc être définie avant cet import si la configuration runtime devient obligatoire.
- Le workflow qualité installe les dépendances sur Python 3.13 mais ne fournit pas explicitement de configuration de base au job de tests.

Ces faits sont établis par lecture actuelle. Aucun résultat de test vert n'est revendiqué.

## 3. Périmètre fermé

### Inclus

1. Compléter la dépendance nécessaire à la validation des adresses électroniques.
2. Externaliser `DATABASE_URL` et définir un comportement explicite lorsque la variable manque.
3. Fournir un exemple de configuration sans secret réel, avec l'authentification active par défaut.
4. Cesser de versionner `.env` tout en conservant le fichier local de chaque développeur.
5. Adapter l'initialisation des tests et la CI : SQLite explicite pour les tests unitaires, MySQL du service pour le job de performance.
6. Ajouter des tests ciblés de chargement de configuration, sans connexion à MySQL.
7. Aligner la documentation d'installation et de validation sur les commandes réellement prévues.

### Exclus

- Correction de `/dev/api-key/{user_id}` et de `DISABLE_AUTH`.
- Normalisation `OP-COLIS` / `OP-colis`, matrice des droits et migration vers les rôles cumulables.
- Modification des CRUD Admin ou Clients et de leurs règles métier.
- Commandes, détails de commandes, stocks, boutique, front et Wave 2.
- Application de `database/modelisation_base_digicheese_wave2.sql`.
- Migration ou lecture de données réelles.
- Démarrage ou modification d'un environnement distant, déploiement, publication et push Git.
- Refonte globale de la CI, ajout d'outils ou traitement de toute dette de lint existante.

Les exclusions IAM constituent un lot suivant candidat. Elles ne sont pas considérées comme résolues après WP-01.

## 4. Liste fermée des cibles modifiables

| Cible | Mutation autorisable dans WP-01 | Preuve attendue |
|---|---|---|
| `requirements.txt` | Ajouter la dépendance runtime compatible avec `EmailStr` | Installation propre réussie et import du schéma client |
| `.env.example` | Créer un exemple avec `DATABASE_URL`, `DISABLE_AUTH=false` et valeurs factices documentées | Aucun secret réel ; authentification active par défaut ; variables requises compréhensibles |
| Index Git pour `.env` | Retirer uniquement `.env` du suivi avec conservation du fichier local | `git ls-files .env` vide ; fichier local toujours présent |
| `src/database.py` | Charger le fichier `.env` avant de lire `DATABASE_URL`, laisser la variable système prioritaire, puis produire une erreur explicite si aucune valeur n'existe, sans la divulguer | Tests de priorité, chargement `.env` et absence ; aucune connexion déclenchée par ces tests |
| `tests/conftest.py` | Définir l'URL de test avant l'import de l'application et préserver l'isolation SQLite | Suite CRUD existante continue d'utiliser SQLite mémoire |
| `tests/test_database_config.py` | Créer les tests ciblés de configuration | Cas variable présente et manquante prouvés |
| `.github/workflows/quality.yml` | Définir une URL SQLite pour `unit-tests` et l'URL du service MySQL pour `perf-k6`, en conservant Python 3.13 | Tests unitaires configurés ; démarrage `uvicorn` et healthcheck du job de performance compatibles avec le service |
| `README.md` | Corriger le parcours de création d'environnement, configuration et tests | Procédure cohérente avec les fichiers du lot |
| `DOC/TECH/Serveurs_Virtuels_Python.md` | Terminer la procédure Windows/PowerShell et la configuration de la base | Rejeu documenté depuis un environnement propre |
| `tests/README_tests.md` | Distinguer tests CRUD avec auth neutralisée et limites de preuve | Commandes et limites explicites |

Tout autre fichier est hors périmètre. Une découverte nécessitant un fichier supplémentaire arrête l'exécution avec `NEEDS_DECISION` et une proposition d'extension ; elle ne conduit pas à élargir silencieusement la liste.

## 5. Conception proposée

### Option retenue pour décision

**Configuration par variable d'environnement obligatoire**, chargée dans `src/database.py` avant la lecture de `DATABASE_URL` et avant la création de l'engine SQLAlchemy. `load_dotenv()` ne remplace pas une variable système déjà définie : l'environnement du processus reste prioritaire. Ce choix couvre aussi les imports directs de `src.database` et ne nécessite pas de modifier `src/main.py`.

`.env.example` documente une URL locale compatible avec le Docker Compose existant et fixe `DISABLE_AUTH=false`. La valeur `true` reste limitée aux environnements de tests explicitement identifiés. `unit-tests` reçoit une URL SQLite dédiée avant tout import applicatif ; `perf-k6` reçoit l'URL du service MySQL déclaré dans le workflow.

Cette option évite un secret ou identifiant de base dans le code. Elle rend aussi l'absence de configuration visible, au lieu de basculer silencieusement vers une base implicite.

### Options écartées pour WP-01

| Option | Motif |
|---|---|
| Conserver l'URL littérale | Ne satisfait pas l'objectif de configuration reproductible et maintient un identifiant dans le code |
| Valeur MySQL par défaut dans le code | Masque les erreurs de configuration et continue de coupler l'application à un poste local |
| Introduire une bibliothèque de settings ou un nouveau module de configuration | Complexité inutile pour ce premier lot ; à réexaminer si le nombre de variables devient significatif |
| Refondre Docker Compose avec gestion complète des secrets | Hors unité de travail ; environnement cible et politique de secrets à-confirmer |

## 6. Séquence d'exécution candidate

| Ordre | Travail | Dépendance | Contrôle |
|---|---|---|---|
| 1 | Capturer Git, versions et état de `.env` sans afficher son contenu | Autorisation WP-01 | Working tree utilisateur préservé |
| 2 | Ajouter `.env.example` et compléter `requirements.txt` | Aucune | Analyse du diff et absence de secret réel |
| 3 | Adapter les tests pour définir `DATABASE_URL` avant l'import applicatif | Étape 2 | Collecte des tests possible sans MySQL |
| 4 | Externaliser l'URL dans `src/database.py` | Étape 3 | Tests ciblés de configuration |
| 5 | Retirer `.env` du suivi tout en conservant sa copie locale | Étape 2 | Fichier présent localement, absent de `git ls-files` |
| 6 | Aligner `unit-tests` sur SQLite et `perf-k6` sur son service MySQL | Étapes 2 à 4 | Lecture du workflow ; import unitaire ; démarrage applicatif et healthcheck de performance lors d'une exécution CI autorisée |
| 7 | Mettre à jour les trois documents fermés | Comportement final connu | Rejeu de la procédure sur environnement propre |
| 8 | Exécuter les contrôles puis faire vérifier par CERBERUS | Toutes | Matrice critères/preuves et contrôle des changements inattendus |

## 7. Critères d'acceptation du lot

| ID | Critère obligatoire | Preuve attendue |
|---|---|---|
| AC-01 | Un environnement Python 3.13 neuf installe toutes les dépendances depuis `requirements.txt` | Commande, code retour et journal daté |
| AC-02 | Le schéma client utilisant `EmailStr` s'importe sans dépendance manquante | Test ou import ciblé réussi |
| AC-03 | La variable système `DATABASE_URL` est prioritaire ; à défaut, une valeur peut être chargée depuis `.env` ; sans aucune des deux, l'application échoue avec un message explicite | Trois tests automatisés distincts, sans valeur sensible dans les sorties |
| AC-04 | Les tests utilisent explicitement SQLite mémoire sans dépendre d'une instance MySQL | Configuration lue et tests ciblés réussis |
| AC-05 | `.env.example` contient seulement des exemples ; `.env` reste local et n'est plus suivi | Inspection Git et contrôle de contenu sensible adapté |
| AC-06 | Les tests ciblés, `tests/test_utilisateur.py`, `tests/test_client.py` et `tests/test_dependencies.py` passent, puis la suite complète passe sans nouvelle exclusion | Résultats datés, nombre de tests et échecs visibles |
| AC-07 | `ruff check` sur les fichiers Python modifiés ne signale aucune erreur | Sortie et code retour conservés |
| AC-08 | La procédure Windows/PowerShell est rejouée depuis un environnement propre | Journal des commandes et écarts éventuels |
| AC-09 | Le diff ne contient que les cibles fermées et ne modifie pas les fichiers Wave 1/Wave 2/Obsidian préexistants | `git status`, `git diff --name-status` et comparaison à la photographie initiale |
| AC-10 | Aucun test ou document ne présente l'authentification comme validée par WP-01 | Relecture CERBERUS des affirmations et limites |
| AC-11 | `unit-tests` utilise SQLite et `perf-k6` démarre l'application avec l'URL du service MySQL avant de réussir son healthcheck | Configuration statique vérifiée ; résultats GitHub CI à-confirmer jusqu'à une exécution distante autorisée |

Le seuil de couverture global n'est pas utilisé comme condition du lot : sa baseline actuelle n'est pas prouvée. Il pourra être fixé après une mesure reproductible.

## 8. Stratégie de test et preuves

Commandes candidates, à confirmer selon l'environnement réellement créé :

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest tests/test_database_config.py tests/test_dependencies.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_utilisateur.py tests/test_client.py -q
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m ruff check src/database.py tests/conftest.py tests/test_database_config.py
```

Si `py -3.13` n'est pas disponible, le chemin ou l'installation autorisée de Python 3.13 reste **à-confirmer** ; HEPHAESTOS ne télécharge pas un runtime sans l'autorisation correspondante. Les logs doivent indiquer l'interpréteur, les versions, le nombre de tests, le code retour et la date. Un code retour sans sortie exploitable ne suffit pas.

La CI distante n'est pas une condition vérifiable localement sans publication. WP-01 prépare le workflow ; son exécution GitHub reste **à-confirmer** et nécessite une action externe distincte si demandée.

## 9. Charge, dépendances et responsabilités

| Élément | Estimation candidate |
|---|---|
| Analyse et tests de configuration | 2 à 3 h |
| Dépendances, exemple d'environnement et externalisation DB | 2 à 3 h |
| Adaptation tests et CI | 2 à 3 h |
| Documentation, rejeu et contrôle | 2 à 3 h |
| Total | **9 à 12,5 h**, à confirmer après disponibilité de Python 3.13 |

Responsable institutionnel, disponibilité, tolérances et échéance formelle : **à-confirmer**. HEPHAESTOS est intervenu sous le mandat utilisateur explicite du 2026-09-05 ; CERBERUS a effectué la vérification indépendante de la réalisation.

## 10. Risques, rollback et changements

| Risque | Réponse prévue |
|---|---|
| Imports cassés par une variable devenue obligatoire | Définir la variable avant import dans tests/CI ; tests ciblés avant suite complète |
| `.env` supprimé localement par erreur | Employer une opération d'index qui conserve le fichier ; vérifier sa présence avant/après |
| Secret recopié dans `.env.example`, logs ou documentation | N'utiliser que des valeurs factices et contrôler le diff avant validation |
| Identifiants MySQL déjà présents dans l'historique Git | Vérifier s'ils sont encore valides ; rotation et traitement éventuel de l'historique restent à-confirmer et hors WP-01 sans décision d'extension |
| Tests verts uniquement parce que l'auth est neutralisée | Conserver cette limite visible ; préparer les tests IAM dans le lot suivant |
| Élargissement vers Docker, IAM ou Wave 2 | Arrêt et `NEEDS_DECISION` si une cible hors liste devient nécessaire |
| Échec causé par Python 3.13 indisponible | Marquer BLOCKED avec preuve ; décider séparément de l'installation ou du changement de version cible |

Rollback candidat : restaurer les versions initiales des seuls fichiers WP-01 à partir du patch/commit du lot ; réinscrire `.env` dans l'index uniquement si une décision humaine l'exige, sans écraser sa copie locale. Les commandes de restauration exactes seront préparées par HEPHAESTOS à partir de l'état Git constaté juste avant exécution. Aucune base ni donnée n'est modifiée, donc aucun rollback de données n'est attendu.

## 11. RGPD, SSI et Run

- **RGPD : EN_COURS.** Ce lot ne consulte ni ne migre les données. Les configurations et journaux ne doivent pas exposer de données personnelles ou secrets. Autorité et traitement réel : à-confirmer.
- **SSI : EN_COURS.** WP-01 retire l'identifiant littéral de l'état courant et prépare des contrôles reproductibles. Il n'efface pas l'historique Git et ne prouve pas que les identifiants historiques sont révoqués. Validité, rotation éventuelle et traitement de l'historique : à-confirmer. Il ne corrige pas encore les routes de développement, le contournement d'authentification ou les rôles.
- **Métier :** aucun comportement CRUD ne doit changer ; les tests existants servent de non-régression technique, sans validation métier humaine.
- **Run :** environnement de production, sauvegarde, monitoring et support restent à-confirmer. Aucun déploiement n'est inclus.

## 12. Conditions de passage et verdict ZEUS

### Traçabilité des conditions d'entrée HEPHAESTOS

1. WP-01, sa liste fermée et ses critères ont été validés pour réalisation par le mandat utilisateur du 2026-09-05.
2. Les écritures locales et la modification d'index de `.env` ont été autorisées par ce mandat.
3. Python 3.13.7 a été installé comme runtime utilisateur géré par `uv`, sans modification de configuration système globale.
4. La branche `xavier`, le HEAD et l'état Git ont été capturés avant réalisation ; le travail local préexistant a été préservé.
5. Le responsable institutionnel et les tolérances restent à-confirmer et demeurent visibles dans le dossier.
6. `.env.example` fixe `DISABLE_AUTH=false` ; la neutralisation reste limitée aux tests et jobs nommés.

### État des jalons

- J2 : **EN_ATTENTE** — profil et conditions de conception non formellement approuvés.
- J3 : **EN_ATTENTE** — responsabilités et cadence non confirmées.
- J4 : **GO local WP-01 tracé** — mandat du chef de projet humain reçu le 2026-09-05 ; validation institutionnelle à-confirmer.

**Verdict ZEUS : WP-01 RÉALISÉ LOCALEMENT. HEPHAESTOS : TERMINÉ. CERBERUS : PASS_WITH_RESERVATIONS externes.**

Prochaine décision utile : accepter la réalisation locale avec AC-11 limité à une preuve statique, ou autoriser séparément l'exécution GitHub CI/MySQL. Le lot IAM demeure séparé et non autorisé.

## 13. Contrôles de préparation

| Contrôle | Résultat |
|---|---|
| ARGOS — `DIGICHEESE-ARGOS-LOT1-20260905` | `READY` ; lot de configuration séparé de l'IAM ; charge proposée 9 à 12,5 h |
| CERBERUS — `DIGICHEESE-WP01-CERBERUS-20260905` | `PASS` final ; cinq réserves initiales intégrées et levées ; aucune réserve restante |

Réserves intégrées : configuration distincte de `unit-tests` et `perf-k6`, chargement de `.env` avant lecture par `src.database`, limite explicite concernant l'historique Git, `DISABLE_AUTH=false` dans l'exemple et baseline de tests nommée. CERBERUS a relu le delta et confirmé que les cinq réserves sont levées.

## 14. Réalisation WP-01

| Élément | Résultat observé |
|---|---|
| Mandat | GO explicite du chef de projet humain le 2026-09-05 pour lancer le développement du lot |
| HEPHAESTOS | `READY` ; liste fermée respectée ; aucun commit, push ou déploiement |
| Runtime | Python 3.13.7 géré par `uv` ; `.venv` local recréé |
| Dépendances | Installation réussie ; `pip check` sans paquet cassé |
| Tests ciblés | Configuration et dépendances : 10/10 ; utilisateurs et clients : 10/10 |
| Régression | Suite complète : 51/51 ; 16 avertissements préexistants |
| Qualité | Ruff réussi sur les trois fichiers Python modifiés ; UTF-8 valide |
| Configuration | URL littérale retirée de `src/` ; `.env` local intact, ignoré et non suivi ; `.env.example` disponible |
| CERBERUS réalisation | `PASS_WITH_RESERVATIONS` ; AC-01 à AC-10 PASS, AC-11 statique conforme |

Réserves externes maintenues : GitHub Actions, démarrage MySQL réel et healthcheck `perf-k6` non exécutés ; leur preuve reste **à-confirmer**. IAM, révocation éventuelle des identifiants historiques, validation RGPD/SSI, Run et déploiement restent hors WP-01.

Le dossier de vérification correspondant est [03_VERIFICATION_VALIDATION_WP01.md](../2026-09-05_J5/03_VERIFICATION_VALIDATION_WP01.md).
