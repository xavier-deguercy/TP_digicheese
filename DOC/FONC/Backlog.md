# Backlog — DIGICHEESE (TP7) (version exécution)

## Cadre TP7 (rappels)
- Durée : **5 jours**
- Livrables : API Backend + Swagger + tests + MySQL + documentation + requirements.txt + branches (test/dev/prod/master + 1 branche par dev)

---

## Definition of Done (DoD) — commun à toutes les US
Une US est “Done” si :
- endpoint(s) implémenté(s) + validation entrée + gestion erreurs (HTTP codes)
- persistance en base OK
- documenté dans Swagger (schémas + exemples)
- testé (au moins 1 test nominal + 1 test erreur)
- code conforme conventions projet (lint ruff si activé)
- doc mise à jour si impact

---

## Priorisation (MoSCoW)

### MUST (obligatoire TP7)
- **M1** — Socle projet (FastAPI + MySQL + config .env + lancement)
- **M2** — Swagger opérationnel (front simulé)
- **M3** — CRUD Admin : utilisateurs
- **M4** — CRUD Admin : communes
- **M5** — CRUD Admin : objets
- **M6** — CRUD Admin : conditionnements
- **M7** — CRUD Admin : poids
- **M8** — CRUD Admin : poids-vignettes
- **M9** — Tests sur CRUD Admin (minimum)
- **M10** — Documentation (DOC/ + TECH/ + UTILISATION/)

### SHOULD (fortement recommandé)
- **S1** — Healthcheck + version
- **S2** — Lint/qualité (ruff) + conventions
- **S3** — Docker/Docker-compose reproductible

### COULD (option)
- **C1** — CRUD Clients (OP-colis)
- **C2** — Sécurité simple (auth basique / roles)
- **C3** — Monitoring “simple” (KPIs & alertes définis + doc)

---

## Dépendances (pour travailler en parallèle)
- **Socle (M1 + M2)** est la base : une fois `main.py` + DB + session OK, on peut attaquer les CRUD en parallèle.
- Les CRUD (M3..M8) sont **indépendants entre eux** si on respecte une convention commune :
  - routes → services → repositories → models
  - réponses/erreurs standardisées
  - schémas de payload cohérents
- Les tests (M9) peuvent démarrer **dès qu’un premier CRUD est stable** (ex : communes).
- La doc (M10) peut avancer en parallèle **dès le jour 1**.

---

## Conventions communes (à verrouiller dès J1)
> Objectif : éviter les conflits Git + faciliter le travail en parallèle.

- Base path : `/api/v1`
- Structure endpoint CRUD :
  - GET collection, POST collection
  - GET item, PUT/PATCH item, DELETE item
- Conventions réponse :
  - 200/201/204 nominal, 400 validation, 404 absent
- Pattern technique :
  - `routes/<ressource>.py`
  - `services/<ressource>_service.py`
  - `repositories/<ressource>_repo.py`
  - `models/<ressource>.py`
- Gestion DB : un module `conf/db.py` (Session/engine) unique pour tous

---

## Épics & User Stories (découpées en tâches “exécutables”)

### EPIC A — Socle & environnement (MUST)
**US-A1 (M1/M2/S1)** : Socle API + Swagger + Health
- T1 : config `.env` + `.env.example` (DB_*, TZ)
- T2 : `conf/db.py` (engine + Session)
- T3 : `main.py` (FastAPI + include_router)
- T4 : endpoints `GET /health` et `GET /version` (S1)
- T5 : lancer `uvicorn` + vérif Swagger `/docs`

**US-A2 (S3)** : Docker-compose reproductible
- T1 : container MySQL + variables
- T2 : container API (Dockerfile) + réseau
- T3 : doc “comment lancer”

**US-A3 (S2)** : Qualité / ruff
- T1 : ruff config minimale
- T2 : commande standard (lint) + doc

---

### EPIC B — Modèle & persistance (MUST)
**US-B1 (M1)** : modèles SQLModel (tables admin)
- T1 : créer modèles : users, communes, objets, conditionnements, poids, poids_vignettes
- T2 : aligner clés/relations si nécessaires (minimum)

**US-B2 (M1)** : init DB
- T1 : create_all au démarrage (si retenu) OU script init (selon votre choix)
- T2 : vérifier création des tables en MySQL

---

### EPIC C — CRUD Admin (MUST)
> Chaque US CRUD suit le même squelette : routes + service + repo + validations + swagger examples.

**US-C0 (M3)** : CRUD Admin — Utilisateurs
- T1 : endpoints CRUD users
- T2 : validations (unicité login/email si retenu)
- T3 : exemples Swagger

**US-C1 (M4)** : CRUD Admin — Communes
- T1 : endpoints CRUD communes
- T2 : validations
- T3 : exemples Swagger

**US-C2 (M5)** : CRUD Admin — Objets
- T1 : endpoints CRUD objets
- T2 : validations
- T3 : exemples Swagger

**US-C3 (M6)** : CRUD Admin — Conditionnements
- T1 : endpoints CRUD conditionnements
- T2 : validations
- T3 : exemples Swagger

**US-C4 (M7)** : CRUD Admin — Poids
- T1 : endpoints CRUD poids
- T2 : validations
- T3 : exemples Swagger

**US-C5 (M8)** : CRUD Admin — Poids-vignettes
- T1 : endpoints CRUD poids-vignettes
- T2 : validations
- T3 : exemples Swagger

---

### EPIC D — OP-colis (COULD)
**US-D1 (C1)** : CRUD Clients (option)
- T1 : endpoints CRUD clients
- T2 : validations
- T3 : exemples Swagger

---

### EPIC E — Tests (MUST/SHOULD)
**US-E1 (M9)** : tests CRUD admin (minimum)
- T1 : test “smoke” /health
- T2 : pour 2 ressources minimum : nominal (create→get→update→delete) + erreur (404)
- T3 : adapter ensuite aux autres CRUD (si temps)

**US-E2 (SHOULD)** : tests non-régression simples
- T1 : tests “contrat” : codes HTTP + champs essentiels
- T2 : tests de list/pagination si implémentée

---

### EPIC F — Documentation (MUST)
**US-F1 (M10)** : doc fonctionnelle (FONC)
- Contexte_Objectifs, Perimetre, Regles_Metier, Parcours, Backlog

**US-F2 (M10)** : doc technique (TECH)
- Architecture, Changements_CDC, Serveurs_Virtuels_Python

**US-F3 (M10)** : doc utilisation (UTILISATION)
- Guide_Utilisateur (Swagger), Guide_dev, FAQ

---

## Plan d’exécution 5 jours (parallélisable)

### Jour 1 — Mise en place + démarrage parallèle
Objectif : “API up + DB OK + Swagger OK + conventions lockées”
- A : Socle (US-A1) + DB (US-B2)
- B : Modèles SQLModel (US-B1)
- C : Doc en parallèle (US-F1/F2 structure + index)
- D : Docker OU ruff (S3 ou S2) (si vous avez une 4e personne)

### Jour 2 — CRUD en parallèle (2 à 3 ressources)
Objectif : 2 CRUD complets + swagger examples
- Dev1 : Communes
- Dev2 : Objets
- Dev3 : Utilisateurs
- Dev4 : commence tests (health + 1 CRUD) OU Docker/ruff

### Jour 3 — CRUD en parallèle (2 à 3 ressources)
- Dev1 : Conditionnements
- Dev2 : Poids
- Dev3 : Poids-vignettes
- Dev4 : tests (étendre) + doc parcours Swagger

### Jour 4 — Stabilisation + tests + doc
- Finaliser CRUD restants
- Tests sur plusieurs ressources (E1)
- Harmonisation erreurs / exemples Swagger
- Doc “Guide utilisateur” + “Guide dev”

### Jour 5 — Finition + options (si avance)
- Option Clients (C1)
- Sécurité simple (C2) ou monitoring doc (C3)
- Relecture globale, packaging livrables, démo Swagger

---

## Répartition type “4 personnes” (recommandation)
> Chaque personne prend une “feature branch” + 1 ressource CRUD (routes/services/repo/models).
> Un “intégrateur” gère les merges sur `dev`.

- **P1 (Intégration / socle)** : A1 + B2 + S1 + harmonisation
- **P2 (CRUD Admin #1)** : communes + tests associés
- **P3 (CRUD Admin #2)** : objets + conditionnements
- **P4 (CRUD Admin #3 / Qualité)** : users + poids + ruff + démarrage tests/doc

---

## Répartition “2 personnes” (si vous n’êtes pas 4 en continu)
- **P1** : socle + DB + users + communes
- **P2** : objets + conditionnements + poids + poids-vignettes
- Tests et doc : 30-45 min par jour chacun (obligatoire), puis J4/J5 consolidation.

---

## Risques & parades
- Conflits Git sur `main.py` / `conf/db.py` → verrouiller dès J1, un seul owner
- Endpoints incohérents → conventions + squelette commun
- Tests “trop tard” → commencer dès J2 sur 1 CRUD
- Dérapage fonctionnel (CDC complet) → rester TP7 (CRUD admin + option clients)
