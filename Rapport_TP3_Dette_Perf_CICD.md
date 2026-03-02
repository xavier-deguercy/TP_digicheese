# Rapport TP 3.1 / TP 3.2 / TP 3.3 — DigiCheese

Date : 2026-02-07

---

## TP 3.1 — Analyse detaillee de la dette technique

### Perimetre et preuves
- Analyse statique (flake8) : `reports/raw/flake8_20260207_222905.log`
- Analyse statique (pylint) : `reports/raw/pylint_20260207_222905.json`
- Complexite (radon) : `reports/raw/radon_20260207_222905.json`
- Mapping endpoints cible : `reports/consolidated/phase0_existing_20260207_182614.md`

### Resultats (faits)
- Flake8 : 360 issues detectees.
  - Top codes : E501(90), W293(61), E302(57), E252(40), E231(35), E303(16), E251(14), F401(13).
- Pylint : score 6.5979, 392 messages.
  - Top symbols : missing-function-docstring(141), trailing-whitespace(64), missing-module-docstring(51), line-too-long(33), missing-class-docstring(22).
- Radon : complexite maximale B=6.
  - Top 5 :
    - B=6 `src/repositories/objet_repository.py:26` `patch_objet`
    - A=5 `src/services/client_service.py:22` `__validate_adresses`
    - A=5 `src/services/client_service.py:29` `__validate_email_unique`
    - A=4 `src/utils/create_db.py:27` `seed_roles_and_admin`
    - A=4 `src/utils/dependencies.py:14` `get_current_user_api_key`
- Endpoints attendus `/login`, `/users`, `/orders` non trouves dans le code actuel.

### Interpretation
- Dette principalement liee au style (longues lignes, espaces, lignes blanches) et a l'absence de docstrings.
- Complexite globalement faible (majorite A), mais un point d'attention sur `patch_objet` (B=6).

### Actions recommandees (priorisees)
1. Haute : normaliser le style (formatage auto + correction E501/W293/E302) et nettoyer imports inutiles (F401).
2. Moyenne : ajouter docstrings minimales sur modules/classes/fonctions exposees.
3. Faible : harmoniser ordre des imports et nommage (pylint C0411/C0103).

---

## TP 3.2 — Tests de performance

### Perimetre et preuves
- k6 execute via Docker : `reports/raw/k6_run_20260207_231044.log`
- Summary k6 : `reports/raw/k6_20260207_231044.json`
- Scripts : `perf/k6_smoke_20260207_231044.js`
- API : endpoint `/health`

### Resultats (faits)
- Scenario : smoke (10 VUs / 10s) sur `/health`.
- Latence moyenne : 7.819 ms.
- Latence max : 35.979 ms.
- P95 : 27.834 ms.
- Taux d'erreur : `http_req_failed.value = 0` (champ `rate` absent dans le summary).
- Throughput : 9.845 req/s.

### Interpretation
- La performance du endpoint `/health` est stable en smoke dans l'environnement local.
- Les metriques ne representent pas la charge metier (pas de scenario CRUD).

### Actions recommandees
1. Ajouter un scenario k6 sur un endpoint metier (ex: creation client) avec donnees de test.
2. Executer un profil full (10/50/100 VUs) pour observer degradations.
3. Conserver un baseline en CI avec le profile smoke.

---

## TP 3.3 — Pipeline CI/CD avec integration des tests

### Perimetre et preuves
- Workflow : `.github/workflows/quality.yml`
- Consolidation KPI : `tools/collect_kpi.py`
- KPI consolides : `reports/consolidated/kpi_20260207_231553.json`, `reports/consolidated/kpi_20260207_231553.md`

### Resultats (faits)
- Pipeline `quality` declenche a chaque push.
- Jobs definis :
  - `unit-tests` (pytest + junit + coverage)
  - `debt-tech` (flake8/pylint/radon)
  - `perf-k6` (uvicorn + k6 smoke)
  - `consolidate-kpi` (aggregation KPI)
- Artifacts produits : `raw-unit`, `raw-debt`, `raw-perf`, `consolidated-kpi`.

### Interpretation
- La pipeline couvre tests, dette technique, performance et consolidation KPI.
- Les gates (seuils coverage, error_rate, lint) ne sont pas encore actives.

### Actions recommandees
1. Stabiliser l'execution des tests (dependances manquantes) avant d'ajouter des gates.
2. Ajouter des seuils progressifs (coverage min, error_rate max) une fois les baselines stables.
3. Etendre la collecte KPI aux tests critiques (markers).

---

## Annexes — Fichiers cles
- Flake8 : `reports/raw/flake8_20260207_222905.log`
- Pylint : `reports/raw/pylint_20260207_222905.json`
- Radon : `reports/raw/radon_20260207_222905.json`
- K6 summary : `reports/raw/k6_20260207_231044.json`
- Workflow CI : `.github/workflows/quality.yml`
- KPI consolidation : `tools/collect_kpi.py`

Fin du rapport
