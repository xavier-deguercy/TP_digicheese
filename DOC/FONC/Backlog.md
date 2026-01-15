# Backlog — DIGICHEESE (TP7)

## Cadre TP7 (rappels)
- Durée : **5 jours**
- Livrables : API Backend + Swagger + tests + MySQL + documentation + requirements.txt + branches (test/dev/prod/master + 1 branche par dev).

---

## Definition of Done (DoD) — commun à toutes les US
Une US est “Done” si :
- endpoint(s) implémenté(s) + validation entrée + gestion erreurs
- persistance en base OK
- documenté dans Swagger (schémas + exemples)
- testé (au moins 1 test nominal + 1 test erreur)
- code conforme conventions projet (lint ruff si activé)
- doc mise à jour si impact

---

## Priorisation (MoSCoW)
### MUST (obligatoire TP7)
- M1 — Socle projet (FastAPI + MySQL + config .env + lancement)
- M2 — Swagger opérationnel (front simulé)
- M3 — CRUD Admin : communes
- M4 — CRUD Admin : objets
- M5 — CRUD Admin : conditionnements
- M6 — CRUD Admin : poids
- M7 — CRUD Admin : poids-vignettes
- M8 — Tests sur CRUD Admin (minimum)
- M9 — Documentation (DOC/ + TECH/ + UTILISATION/)

### SHOULD (fortement recommandé)
- S1 — Healthcheck + version
- S2 — Lint/qualité (ruff) + conventions
- S3 — Docker/Docker-compose reproductible

### COULD (option)
- C1 — CRUD Clients (OP-colis) - CRUD de l’acteur « Opérateur de Colis » : Gestion des clients
- C2 — Sécurité simple (auth basique / roles) si temps
- C3 — Monitoring “simple” (KPIs & alertes définis + doc)

---

## Épics & User Stories

### EPIC A — Socle & environnement
- US-A1 (MUST) : créer venv + requirements + lancement uvicorn
- US-A2 (SHOULD) : docker-compose (API + MySQL)
- US-A3 (SHOULD) : conventions env (Europe/Paris)

### EPIC B — Modèle & persistance
- US-B1 (MUST) : modèles SQLModel (tables admin)
- US-B2 (MUST) : DB init (script / création tables)

### EPIC C — Endpoints Admin (CRUD)
- US-C1 (MUST) : CRUD communes
- US-C2 (MUST) : CRUD objets
- US-C3 (MUST) : CRUD conditionnements
- US-C4 (MUST) : CRUD poids
- US-C5 (MUST) : CRUD poids-vignettes

### EPIC D — Endpoints OP-colis (option)
- US-D1 (COULD) : CRUD clients

### EPIC E — Tests
- US-E1 (MUST) : tests CRUD admin (nominal + erreurs)
- US-E2 (SHOULD) : tests non régression simples (smoke)

### EPIC F — Documentation
- US-F1 (MUST) : doc fonctionnelle (contexte, périmètre, règles, parcours, backlog)
- US-F2 (MUST) : doc technique (archi, changements CDC, env)
- US-F3 (MUST) : doc utilisation (guide + FAQ)

---

## Plan de réalisation (5 jours — proposition)
- Jour 1 : socle (env + db) + modèles + swagger OK
- Jour 2 : CRUD Admin (communes + objets)
- Jour 3 : CRUD Admin (conditionnements + poids)
- Jour 4 : CRUD Admin (poids-vignettes) + tests
- Jour 5 : doc complète + stabilisation + option clients si avance

---

## Risques & parades
- Risque : surcharge fonctionnelle (CDC complet) → Parade : cadrage TP7 (CRUD admin + clients option)
- Risque : dette qualité → Parade : DoD + ruff + tests minimum
- Risque : instabilité DB → Parade : docker-compose + .env.example
