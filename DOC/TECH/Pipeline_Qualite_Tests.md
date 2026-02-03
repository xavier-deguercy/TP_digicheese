# Pipeline tests + qualité — DIGICHEESE

> Rôle : dev senior / SDET — Conception d’un pipeline complet “tests + qualité”.
> Langue : français. Orientation : action.
> Contrainte : ne jamais inventer des résultats (logs absents => “NON VÉRIFIABLE”).

---

## 1) Détection (preuves + confiance)

### Langages détectés
- **Python** — Confiance 95/100.
  - Preuves : `requirements.txt` (dépendances Python), structure `src/` avec `main.py` et modules Python, tests `tests/*.py`. 

### Gestionnaires de dépendances
- **pip + requirements.txt** — Confiance 90/100.
  - Preuve : `requirements.txt`.

### Framework applicatif
- **FastAPI (API web)** — Confiance 95/100.
  - Preuves : `fastapi` et `uvicorn` dans `requirements.txt`; README mentionne explicitement “serveur FastAPI” + commande `uvicorn src.main:app --reload`.

### Frameworks de test probables
- **pytest** — Confiance 95/100.
  - Preuves : `pytest` dans `requirements.txt`, dossier `tests/` avec tests nommés `test_*.py`, README contient commandes pytest.
- **httpx** (tests API) — Confiance 70/100.
  - Preuve : `httpx` dans `requirements.txt`.

### Outils qualité existants
- **ruff** — Confiance 80/100.
  - Preuve : `ruff` présent dans `requirements.txt`.
- Aucun outil de couverture explicitement déclaré.

### CI existante
- **Aucune CI détectée** — Confiance 80/100.
  - Preuve : absence de `.github/workflows`, `.gitlab-ci.yml`, `Jenkinsfile` à la racine.

### Particularités
- **Base MySQL via Docker Compose** — Confiance 90/100.
  - Preuves : `docker-compose.yml` avec service `mysql` + `phpmyadmin`.
- **Architecture projet “API + routes/services/repositories”** — Confiance 85/100.
  - Preuve : structure `src/routers`, `src/services`, `src/repositories` décrite dans README.

---

## 2) Hypothèses & alternatives

> Contexte paramétré non fourni (`{PROJECT_NAME}`, `{OS_TARGET}`, `{MAX_TIME}`, etc.). Je propose :

1) **Option conservatrice** (moins d’outils, setup simple)
   - OS cible : **multi** (Windows/Linux) car README parle de PowerShell + Docker.
   - Temps CI max : **5 min** (tests API + MySQL Docker).
   - Outils : `ruff`, `pytest`, `pytest-cov`, `bandit`.
   - Impact : mise en place rapide, couverture/qualité initiales mesurables, peu de barrières à l’adoption.

2) **Option ambitieuse** (industrialisation)
   - OS cible : **Linux CI + local Windows**.
   - Temps CI max : **8–10 min** (intégration DB + e2e API).
   - Outils : + `mypy`, `safety`/`pip-audit`, `radon`, `pytest-xdist`, `openapi` checks.
   - Impact : meilleure robustesse et observabilité, coût de maintenance CI plus élevé.

---

## 3) Résumé

- Stack confirmée : **Python + FastAPI + MySQL (Docker)**, tests **pytest** et quality **ruff**.
- Aucune CI détectée : pipeline à créer (MVP + avancé).
- Livrable principal : documentation + scripts/CI recommandés, rapports KPI horodatés.

---

## 4) Pipeline (tableau ordre strict)

| Étape | Objectif | Outils | Commandes (exemples) | Temps cible | Échec si… | Sorties |
|---|---|---|---|---|---|---|
| 1. Setup | Installer deps | pip | `python -m venv .venv && pip install -r requirements.txt` | 1–2 min | pip fail | env prêt |
| 2. Qualité rapide | Lint/format | ruff | `ruff check src tests` | <1 min | erreurs lint | rapport console |
| 3. Tests unitaires | Valider logique | pytest | `pytest tests -m "not integration"` | 1–2 min | tests KO | junit/xml, logs |
| 4. Tests intégration | Valider DB/API | pytest + mysql | `docker compose up -d && pytest tests -m integration` | 3–5 min | tests KO | logs + DB |
| 5. Couverture | Mesurer couverture | pytest-cov | `pytest --cov=src --cov-report=xml --cov-report=term` | +30s | < seuil | `coverage.xml` |
| 6. Sécurité deps | Détecter failles | pip-audit/safety | `pip-audit -r requirements.txt` | <1 min | vulnérabilités | rapport json |
| 7. Reporting KPI | Générer rapport | scripts | `python scripts/report_kpi.py` | <30s | script fail | `reports/*.md|json` |

> ⚠️ Résultats **NON VÉRIFIABLES** sans exécution locale/CI.

---

## 5) MVP (DoD mesurable)

**Objectif** : pipeline “rapide, robuste, reproductible” en 1–2 jours.

**Definition of Done (DoD)**
- `ruff check` passe sur `src/` et `tests/`.
- `pytest` passe sur un jeu de tests minimal (unitaires + health).
- Couverture **≥ 60%** sur `src/` via `pytest-cov`.
- Rapport KPI horodaté généré dans `reports/`.
- CI minimale (GitHub Actions ou GitLab CI) avec cache pip.

---

## 6) Avancé (industrialisation)

**Objectif** : CI/CD robuste, métriques avancées, gates qualité.

- Matrice Python (ex: 3.11, 3.12, 3.13) + OS Linux (CI) + Windows (optionnel).
- Tests intégration MySQL via Docker service.
- Qualité avancée : `mypy` (typecheck), `radon` (complexité), `bandit` (sécurité code).
- Sécurité dépendances : `pip-audit` en gate.
- Publication rapports (artifacts CI) : couverture, JUnit, KPI.
- Politique de merge : “pas de merge si tests/coverage/seuils KO”.

---

## 7) Qualité interne

**Objectifs concrets**
- Stabiliser le style et réduire la dette technique.
- Contrôler la complexité et la taille des fonctions.

**Métriques & seuils (recommandations)**
- Complexité cyclomatique : seuil **10** par fonction.
- Longueur fonction : max **50–80 lignes**.
- Duplication : alerte si > **5–10%**.

**Outils**
- `ruff` (lint + format)
- `radon` (complexité)
- `pylint` (optionnel pour smells)

**Sorties**
- Rapport console + JSON (radon) + formatters.

---

## 8) Qualité externe

### Performance
- Tests de base : temps de réponse API (smoke).
- Outils : `pytest` + `httpx` (mesures simples), option `locust` pour charge.

### Fiabilité
- Tests d’intégration : DB + API endpoints critiques.
- Contrats : OpenAPI (validation schema).

### Sécurité
- Dépendances : `pip-audit` / `safety`.
- Code : `bandit` sur `src/`.

---

## 9) Qualité perçue

**API (DX/UX)**
- Swagger/OpenAPI : vérifier cohérence des endpoints et des modèles.
- Messages d’erreur : standardiser (HTTP status + message).

**Automatisable**
- Tests e2e API via `pytest + httpx`.

**Manuel**
- Revue de la doc Swagger (UX dev).

---

## 10) Tests automatisés (unit/int/e2e/charge)

**Pyramide recommandée**
- 60–70% **unitaires** (services, utils)
- 20–30% **intégration** (DB, repositories)
- 5–10% **e2e** (API complète)
- Charge : ciblée sur endpoints critiques

**Outils**
- Unit/Integration/E2E : `pytest`, `httpx`
- Couverture : `pytest-cov`
- Charge : `locust` (optionnel)

---

## 11) Dette technique

**Stratégie d’introduction**
- MVP : `ruff` + `pytest-cov`.
- Avancé : `radon`, `mypy`, `bandit`.

**Objectif**
- Traquer complexité, smells, duplication.

---

## 12) CI/CD

### CI (pipeline recommandé)
- `setup` → `lint` → `tests unit` → `tests integration` → `coverage` → `security` → `report`.
- Cache pip (`~/.cache/pip`).
- Artifacts : `coverage.xml`, `junit.xml`, `reports/*.md`.

### CD
- Hors périmètre : pas de release automatique demandée.

---

## 13) TDD (si activé)

> Non activé par défaut (stade projet non précisé).

**Si `{PROJECT_STAGE}=early` et `{TDD_MODE}=oui`** :
- Cycle Red/Green/Refactor.
- Convention tests : `tests/test_<feature>.py`.
- Priorité : règles métier critiques + endpoints principaux.
- CI : gate sur tests unitaires + couverture minimale.

---

## 14) Reporting KPI (template MD + schéma JSON + commandes)

### Règles
- Dossier : `reports/`
- Nom : `{REPORT_PREFIX}_YYYYMMDD_HHMMSS_Europe-Paris.md`

### Template Markdown (exemple)
```md
# Report KPI — {REPORT_PREFIX}_YYYYMMDD_HHMMSS_Europe-Paris

## Résumé
- Couverture : NON VÉRIFIABLE
- Tests : NON VÉRIFIABLE
- Temps tests : NON VÉRIFIABLE
- Cas critiques : NON VÉRIFIABLE

## Détails
| KPI | Valeur | Source |
|---|---|---|
| Couverture (%) | NON VÉRIFIABLE | coverage.xml |
| Taux de réussite (%) | NON VÉRIFIABLE | junit.xml |
| Temps exécution (sec) | NON VÉRIFIABLE | logs tests |
| Cas critiques testés | NON VÉRIFIABLE | tag `critical` |

## Qualité interne
| KPI | Valeur | Source |
|---|---|---|
| Complexité cyclomatique (global) | NON VÉRIFIABLE | radon |
| Top N complexité | NON VÉRIFIABLE | radon |
| Code smells | NON VÉRIFIABLE | pylint |
| Duplication | NON VÉRIFIABLE | (outil) |
| Longueur fonctions (Top N) | NON VÉRIFIABLE | radon |
```

### Schéma JSON (exemple)
```json
{
  "report_id": "{REPORT_PREFIX}_YYYYMMDD_HHMMSS_Europe-Paris",
  "coverage_pct": "NON VÉRIFIABLE",
  "tests_pass_rate_pct": "NON VÉRIFIABLE",
  "tests_duration_sec": "NON VÉRIFIABLE",
  "critical_tests_count": "NON VÉRIFIABLE",
  "internal_quality": {
    "cyclomatic_complexity": "NON VÉRIFIABLE",
    "top_n_complexity": "NON VÉRIFIABLE",
    "code_smells": "NON VÉRIFIABLE",
    "duplication": "NON VÉRIFIABLE",
    "top_n_function_length": "NON VÉRIFIABLE"
  }
}
```

### Commandes (à implémenter)
```bash
mkdir -p reports
pytest --junitxml=reports/junit.xml --cov=src --cov-report=xml --cov-report=term
python scripts/report_kpi.py --prefix DIGICHEESE
```

---

## 15) Pièges & anti-patterns

- **Exécuter les tests sans DB** : faux positifs/negatifs.
- **CI sans cache pip** : lenteur inutile.
- **Gate coverage trop élevé trop tôt** : décourage l’équipe.
- **Aucun rapport publié** : pas de visibilité sur la dette.

---

## Fichiers à créer / modifier

- **Créer** : `DOC/TECH/Pipeline_Qualite_Tests.md`
- **Optionnel (MVP)** : `scripts/report_kpi.py`, `reports/`
- **Optionnel (CI)** : `.github/workflows/ci.yml` ou `.gitlab-ci.yml`

---

## Extraits de config essentiels (copiables)

### `pyproject.toml` (exemple minimal)
```toml
[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
markers = [
  "integration: tests qui nécessitent une DB",
  "critical: tests critiques",
]
```

### GitHub Actions (CI minimal)
```yaml
name: ci
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: digicheese
          MYSQL_USER: group2
          MYSQL_PASSWORD: digicheese
        ports:
          - 3308:3306
        options: >-
          --health-cmd="mysqladmin ping -h localhost -u root -proot"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
      - run: python -m pip install -r requirements.txt
      - run: ruff check src tests
      - run: pytest --junitxml=reports/junit.xml --cov=src --cov-report=xml
      - uses: actions/upload-artifact@v4
        with:
          name: reports
          path: reports/
```

---

## Commandes one-liner local (install / quality / test / report)

```bash
python -m venv .venv && pip install -r requirements.txt
ruff check src tests
pytest --junitxml=reports/junit.xml --cov=src --cov-report=xml --cov-report=term
python scripts/report_kpi.py --prefix DIGICHEESE
```
