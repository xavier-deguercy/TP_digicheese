# Phase 2 - Campagne de test (plan + artefacts)
Timestamp: 20260207_221839_EuropeParis

## Faits (preuves/logs)
- Creation des artefacts de campagne: `tests/README_tests.md`, `tests/markers.md`, templates KPI, `perf/k6_template.js`.

## Plan de campagne
### Qualite interne / externe / percue
- Interne: qualite du code, dette technique, complexite, lint.
- Externe: conformite API aux attentes (codes HTTP, schemas, erreurs), securite basique.
- Percue: latence et disponibilite percue (k6 smoke).

### Perimetre endpoints cibles
- /login: NON TROUVE (a confirmer ou a ajouter).
- /users: NON TROUVE (existant: /utilisateurs).
- /orders: NON TROUVE.
- Endpoints existants pour tests: /health, /utilisateurs, /roles, /clients, /commune, /adresse, /objet, /poids, /poidsv, /conditionnement.

### Pyramide de tests
- Unitaires: services/utils (logique sans I/O)
- Integration: services + DB (SQLite memoire en tests)
- E2E API: routes FastAPI via TestClient
- Charge: k6 smoke (10 VUs / 10s), full (10/50/100 VUs / 30s)

### Tags / priorites
- `critical`: parcours essentiels (auth, creation user/client)
- `integration`: interaction DB
- `smoke`: tests rapides (health, list)

### KPI a suivre
- Tests: coverage, pass_rate, duration, critical_count
- Dette: cyclomatic (radon), smells (pylint), lint errors (flake8)
- Perf: latency_avg, latency_max, error_rate, throughput

## Interpretation
- La campagne est structuree par niveau (unit/integration/e2e/perf) et alignee sur les endpoints existants.

## Recommandations
- Normaliser les endpoints /login /users /orders si attendus par le cahier des charges.
- Ajouter les markers `critical` sur les tests essentiels.

