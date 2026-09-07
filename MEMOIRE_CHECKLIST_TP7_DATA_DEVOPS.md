# Memoire Checklist TP7 DigiCheese (Data + DevOps)

Contexte retenu:
- Groupe Data.
- CRUD Administrateur obligatoire.
- Version fusionnee maximale Data + DevOps (mettre "N/A" si element explicitement hors scope enseignant).
- Etat mis a jour apres audit local du repo le 2026-03-12.

## 1) Repo Git et organisation
- [x] Repo unique de groupe cree et accessible.
- [x] Une branche par developpeur.
- [x] Branches `test`, `dev`, `prod`, `master` presentes.
- [x] Strategie de merge definie (qui merge vers quoi, quand).
- [x] Historique de commits propre (messages explicites).
- [x] Arborescence claire: `src/`, `tests/`, `scripts/`, `docs/`.

## 2) Setup projet Python
- [x] Environnement Python reproductible.
- [x] `requirements.txt` complet et a jour.
- [x] Script de lancement local documente.
- [x] Variables d'environnement documentees (`.env.example`).
- [x] Connexion MySQL configurable par variables d'environnement.

## 3) Base de donnees MySQL
- [x] Schema DB coherent avec le mini cahier des charges.
- [ ] Script SQL d'initialisation fourni.
- [ ] Script SQL de seed (donnees de test) fourni.
- [x] Contraintes (PK/FK/NOT NULL/UNIQUE) en place.
- [ ] Tracabilite des changements DB (scripts versionnes).

## 4) API Backend (socle)
- [ ] API Python fonctionnelle (framework web stable).
- [ ] Convention d'URL coherente (`/api/v1/...` ou equivalent).
- [x] Reponses HTTP propres (codes 2xx/4xx/5xx corrects).
- [x] Validation des entrees (payload, query params).
- [ ] Gestion d'erreurs centralisee.

## 5) Fonctionnel Admin (CRUD obligatoire)
- [x] CRUD complet de l'acteur Administrateur.
- [x] CRUD des utilisateurs.
- [x] CRUD des parametres metiers (`t_poids`, `t_poidsV`, `t_objet`, `t_conditionnement`, `t_commune`) ou equivalent.
- [ ] Recherche/filtrage/listing cote admin.
- [ ] Suppression securisee (hard/soft delete documente).

## 6) Fonctionnel OP-colis (fusion Data + DevOps)
- [x] CRUD OP-colis implemente (au minimum clients ou commandes).
- [ ] Gestion des commandes (creation, modif, suppression, consultation).
- [ ] Calculs metier colis/conditionnement implementes.
- [ ] Historisation des mouvements colis.
- [ ] Statistiques par intervalle de date (mois/annee).
- [ ] Export/mailing client (fichier texte ou endpoint dedie).
- [ ] Impression/edition (meme en version simplifiee) documentee.

## 7) Securite, roles, conformite
- [x] Authentification en place.
- [x] Autorisation par roles (Admin / OP-colis / OP-stocks si present).
- [x] Controle d'acces sur chaque endpoint sensible.
- [ ] Bonnes pratiques OWASP appliquees (validation, erreurs, secrets, etc.).
- [ ] Mecanismes RGPD documentes (donnees perso, acces, suppression).
- [ ] Chiffrement ou protection des secrets documente.

## 8) Swagger / OpenAPI
- [x] Documentation OpenAPI generee.
- [x] Swagger UI accessible.
- [x] Tous les endpoints principaux documentes.
- [ ] Exemples de requetes/reponses fournis.
- [ ] Schemas d'erreurs documentes.

## 9) Tests (unittest/pytest)
- [x] Framework de test choisi (`pytest` ou `unittest`) et configure.
- [x] Tests unitaires sur logique metier critique.
- [ ] Tests d'integration API (CRUD + auth + erreurs).
- [x] Scenarios de tests complets et scripts (dossier dedie).
- [x] Resultats de tests conserves (rapport/log).
- [x] Corrections suite aux tests tracees.

## 10) Qualite code et efficacite dev
- [x] Code commente de facon utile.
- [ ] Standards de style respectes (lint/format).
- [x] Outils dev documentes (lint, format, scripts, commandes).
- [x] Guide d'efficacite dev redige (setup rapide, workflow, debug).
- [x] Suivi des corrections qualite (journal ou changelog).

## 11) DevOps / exploitation
- [x] Process de deploiement decrit (meme manuel).
- [x] Environnements `dev/test/prod` differencies.
- [x] Description des serveurs/VM Python fournie.
- [ ] Procedure de rollback ou reprise decrite.
- [x] Logs applicatifs exploitables.

## 12) Monitoring KPI + alertes
- [x] KPIs definis (ex: disponibilite, latence, taux d'erreurs, erreurs DB).
- [x] Collecte minimale des metriques en place.
- [ ] Seuils d'alerte definis.
- [x] Preuve de fonctionnement monitoring (captures/logs/rapport).
- [x] Analyse des KPIs incluse dans la doc finale.

## 13) Documentation et livrables finaux
- [x] `README.md` complet (projet, equipe, roles, setup, run, tests).
- [x] Dossier documentation technique.
- [ ] Dossier documentation d'utilisation.
- [x] Dossier scenarios de tests + scripts.
- [ ] Rapport securite.
- [x] Rapport qualite/corrections.
- [x] Rapport monitoring/KPI/alertes.
- [ ] Rapport final global (assiste IA si demande), lisible pour parties prenantes.

## 14) Definition of Done (validation finale)
- [ ] Un clone neuf du repo permet d'installer et lancer l'API.
- [ ] Swagger fonctionne sans manipulation speciale.
- [ ] CRUD Admin demonstrable de bout en bout.
- [ ] Au moins un flux OP-colis demonstrable de bout en bout.
- [ ] Les tests passent sur l'environnement cible.
- [ ] Toute exigence non faite est notee en "N/A justifie".

## Ecarts detectes (audit automatique)
- `pytest` echoue actuellement sur `ImportError: email-validator is not installed`.
- Aucun fichier SQL versionne detecte (`NO_SQL_FILES`) ; la creation/seed passe par `src/utils/create_db.py`.
- `DATABASE_URL` est en dur dans `src/database.py` (pas de configuration DB via variables d'environnement).
- Incoherence de role potentielle: seed `OP-COLIS` mais routes protegees avec `OP-colis`.
- `DOC/UTILISATION/Guide_Utilisateur.md` et `DOC/UTILISATION/FAQ.md` sont vides.
- La branche `master` n'est pas visible localement (usage constate de `main`).
