# Rapport Qualité Logicielle — Référentiel ISO/IEC 25010

Projet : DIGICHEESE — TP Diginamic (UML + socle dev)  
Client / Organisation : Diginamic (TP pédagogique)  
Auditeur : QualityPilot V3 (Codex)  
Version : N/D (non fournie)  
Date : 2026-02-07  

---

# 1. Contexte et périmètre

## 1.1 Objectif de l’audit

> Évaluer la qualité logicielle au regard d’ISO/IEC 25010 à partir des éléments disponibles (tests, analyses statiques, performance).  
> Identifier les écarts et proposer un plan d’action pragmatique.

## 1.2 Périmètre technique

- Application : API FastAPI DIGICHEESE
- Stack : Python 3.13, FastAPI, SQLModel, MySQL (via Docker)
- API / Front / DB : API + DB (MySQL) ; Front non identifié
- Version auditée : état local au 2026-02-07

## 1.3 Méthodologie

Outils utilisés :

- Tests unitaires : pytest (exécution incomplète)
- Couverture : pytest-cov (NON VÉRIFIABLE)
- Analyse statique : flake8, pylint, radon
- Performance : k6 (Docker) — smoke sur `/health`
- CI/CD : workflow GitHub Actions `quality.yml` (créé)

---

# 2. Référentiel ISO 25010 — Évaluation par caractéristique

Notation recommandée :  
1 = critique / non conforme  
2 = insuffisant  
3 = acceptable  
4 = bon  
5 = excellent

---

## 2.1 Fonctionnalité

### Description
Capacité du système à fournir les fonctions attendues correctement.

### Évaluation

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Exactitude des résultats | NON VÉRIFIABLE (tests non exécutables) | N/V | `reports/raw/pytest_cov_20260207_222231.log` |
| Complétude des fonctionnalités | Endpoints cibles `/login`, `/users`, `/orders` non trouvés | 2 | `reports/consolidated/phase0_existing_20260207_182614.md` |
| Validation métier | NON VÉRIFIABLE | N/V | — |

Score global Fonctionnalité : N/V (données incomplètes)

---

## 2.2 Fiabilité

### Description
Capacité à fonctionner sans erreur dans le temps.

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Stabilité | NON VÉRIFIABLE (tests incomplets) | N/V | `reports/raw/pytest_cov_20260207_222231.log` |
| Gestion des erreurs | NON VÉRIFIABLE | N/V | — |
| Robustesse sous charge | Partielle (k6 smoke uniquement) | 3 | `reports/raw/k6_20260207_231044.json` |

Score global Fiabilité : N/V (données incomplètes)

---

## 2.3 Performance

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Temps de réponse | `/health` avg ~7.82 ms, p95 ~27.83 ms (smoke) | 3 | `reports/raw/k6_20260207_231044.json` |
| Consommation ressources | NON VÉRIFIABLE | N/V | — |
| Scalabilité | NON VÉRIFIABLE (pas de test full) | N/V | — |

Score global Performance : 3 / 5 (scope limité à `/health`)

---

## 2.4 Compatibilité

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Interopérabilité | NON VÉRIFIABLE | N/V | — |
| Coexistence avec autres systèmes | NON VÉRIFIABLE | N/V | — |

Score global Compatibilité : N/V

---

## 2.5 Utilisabilité

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Clarté interface | NON VÉRIFIABLE (pas d’IHM auditée) | N/V | — |
| Courbe d’apprentissage | NON VÉRIFIABLE | N/V | — |
| Feedback utilisateur | NON VÉRIFIABLE | N/V | — |

Score global Utilisabilité : N/V

---

## 2.6 Sécurité

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Authentification | Présente (API key), mais tests désactivent l’auth | N/V | `tests/conftest.py`, `src/utils/dependencies.py` |
| Autorisation | Dépend de rôles, NON VÉRIFIABLE en exécution | N/V | `src/routers/*_router.py` |
| Protection données | NON VÉRIFIABLE | N/V | — |
| Gestion vulnérabilités | NON VÉRIFIABLE | N/V | — |

Score global Sécurité : N/V

---

## 2.7 Maintenabilité

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Lisibilité code | Nombreux défauts de style/docstrings | 2 | `reports/raw/flake8_20260207_222905.log`, `reports/raw/pylint_20260207_222905.json` |
| Complexité | Majorité A, max B=6 (`patch_objet`) | 3 | `reports/raw/radon_20260207_222905.json` |
| Dette technique | Élevée (E501/W293/E302 fréquents) | 2 | `reports/raw/flake8_20260207_222905.log` |
| Testabilité | Partielle (tests présents, exécution bloquée) | 2 | `reports/raw/pytest_cov_20260207_222231.log` |

Score global Maintenabilité : 2 / 5

---

## 2.8 Portabilité

| Critère | Observation | Score | Preuve |
|--------|------------|------|--------|
| Déploiement | Docker Compose fourni (MySQL/phpMyAdmin) | 3 | `docker-compose.yml` |
| Environnements supportés | NON VÉRIFIABLE | N/V | — |

Score global Portabilité : 3 / 5 (partiel)

---

# 3. KPI techniques consolidés

| KPI | Valeur | Objectif | Statut |
|----|-------|---------|-------|
| Couverture tests | NON VÉRIFIABLE | = 70% | NON VÉRIFIABLE |
| Taux succès tests | NON VÉRIFIABLE | 100% | NON VÉRIFIABLE |
| Complexité moyenne | N/V (max=6, rank B) | < seuil | PARTIEL |
| Latence moyenne | 7.82 ms (smoke `/health`) | < seuil | OK (scope limité) |
| Taux erreur | 0% (k6 smoke) | < 1% | OK (scope limité) |

Sources : `reports/raw/k6_20260207_231044.json`, `reports/raw/radon_20260207_222905.json`, `reports/raw/pytest_cov_20260207_222231.log`.

---

# 4. Synthèse globale ISO 25010

| Dimension | Score |
|----------|------|
| Fonctionnalité | N/V |
| Fiabilité | N/V |
| Performance | 3 |
| Compatibilité | N/V |
| Utilisabilité | N/V |
| Sécurité | N/V |
| Maintenabilité | 2 |
| Portabilité | 3 |

Score global : N/V (scores incomplets)

---

# 5. Analyse des risques

| Risque | Impact | Probabilité | Priorité |
|-------|-------|------------|---------|
| Endpoints attendus (/login, /users, /orders) non présents | Écart fonctionnel | Élevée | Haute |
| Tests non exécutables (dépendance manquante) | Blocage QA / CI | Élevée | Haute |
| Dette de style élevée (lint) | Maintenabilité faible | Élevée | Moyenne |
| Perf mesurée uniquement sur `/health` | Vision partielle | Moyenne | Moyenne |
| Auth désactivée en tests | Risque sécurité non évalué | Moyenne | Moyenne |

---

# 6. Plan d’action recommandé

## Court terme (quick wins)
- Installer `email-validator` (ou `pydantic[email]`) et relancer pytest + coverage.
- Nettoyer les défauts de style les plus fréquents (E501/W293/E302) via formatage auto.
- Ajouter des marqueurs `critical` sur les tests essentiels.

## Moyen terme
- Étendre les tests unitaires/services et stabiliser la couverture.
- Ajouter des scénarios k6 sur endpoints métier (ex: création client).
- Documenter clairement les endpoints attendus ou adapter le périmètre.

## Long terme
- Définir des gates CI (coverage min, taux d’erreur max, lint strict).
- Renforcer la sécurité (tests auth/roles, revue secrets/DB).
- Mettre en place des benchmarks perf récurrents en CI.

---

# 7. Conclusion exécutive

> L’audit met en évidence un socle technique fonctionnel, mais plusieurs points bloquants pour la validation qualité (tests incomplets, endpoints cibles manquants, dette de style importante).  
> Les performances observées sur `/health` sont bonnes en smoke, mais non représentatives du métier.  
> Priorité à la remise en état du pipeline de tests et à l’alignement du périmètre fonctionnel.

---

Fin du rapport
