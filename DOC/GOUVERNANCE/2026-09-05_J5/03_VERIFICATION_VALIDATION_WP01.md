---
title: DigiCheese - Vérification et validation WP-01
version: 0.1.0
date: 2026-09-05
status: verification-locale-avec-reserves-externes
---

# DigiCheese — Vérification et validation WP-01

Ce dossier consolide les preuves locales produites après le GO explicite du chef de projet humain : « lance le développement du lot ». Il prépare J5 sans attribuer de validation business, SSI, RGPD ou de déploiement. Le PPM officiel et l'autorité institutionnelle restent **à-confirmer**.

## Références

- Lot autorisé : [02_CONCEPTION_PLANIFICATION.md](../2026-09-05_J2/02_CONCEPTION_PLANIFICATION.md)
- Branche : `xavier`
- HEAD de baseline : `6790d40902c32f207923c8d174169e280cddadc9`
- Profil : SOCLE + DEV + INT + IAM proposé ; WP-01 limité à la configuration et aux tests reproductibles
- Mode de delivery : lot local fermé ; mode DSI formel à-confirmer

## Résultat de l'itération

| Élément | Développement | Technique | Fonctionnel | Cyber | Porte qualité |
|---|---|---|---|---|---|
| WP-01 | `DEV_COMPLETE` par HEPHAESTOS | `TECH_VERIFIED` localement | Non applicable au changement de configuration ; non-régression CRUD vérifiée | IAM hors lot ; SSI historique à-confirmer | `PASS_WITH_RESERVATIONS` externes par CERBERUS |

## Preuves techniques

| Contrôle | Résultat | Limite |
|---|---|---|
| Python | 3.13.7 dans `.venv`, runtime utilisateur géré par `uv` | Le lanceur `py` ne découvre pas ce runtime ; repli `uv` documenté |
| Installation | `requirements.txt` installé ; `pip check` réussi | Réseau et certificat système nécessaires lors de la création initiale |
| Email | `email-validator==2.3.0` ; import `EmailStr` réussi | Aucune validation métier supplémentaire revendiquée |
| Configuration | Trois tests : priorité processus, chargement `.env`, absence explicite | Aucun secret affiché dans les preuves |
| Baseline Admin + Clients | 10/10 tests utilisateurs et clients | Authentification neutralisée dans ce profil de test |
| Suite complète | 51/51 tests réussis | 16 avertissements préexistants |
| Ruff | Réussi sur `src/database.py`, `tests/conftest.py`, `tests/test_database_config.py` | Dette de lint globale hors lot |
| Git | `.env` local présent, empreinte conservée, ignoré et non suivi | Identifiants déjà présents dans l'historique Git |
| CI | YAML valide ; `unit-tests` vers SQLite ; `perf-k6` vers MySQL `127.0.0.1:3308` | GitHub Actions, MySQL réel et healthcheck non exécutés |

## Couverture des critères

| Critère | Verdict CERBERUS | Réserve |
|---|---|---|
| AC-01 à AC-10 | `PASS` | Aucune réserve applicative détectée |
| AC-11 | `PASS_WITH_RESERVATION` | Configuration statique conforme ; résultat GitHub CI/MySQL à-confirmer |

## Préservation et périmètre

HEPHAESTOS a modifié uniquement `requirements.txt`, `.env.example`, l'index Git de `.env`, `src/database.py`, `tests/conftest.py`, `tests/test_database_config.py`, `.github/workflows/quality.yml`, `README.md`, `DOC/TECH/Serveurs_Virtuels_Python.md` et `tests/README_tests.md`. Les fichiers Wave 1, Wave 2 et Obsidian de la baseline locale sont préservés. Aucun commit, push, déploiement ou service distant n'a été exécuté.

## Anomalies, réserves et risques

| ID | Impact | Décision actuelle | Statut |
|---|---|---|---|
| RES-WP01-01 | AC-11 ne possède pas de preuve d'exécution GitHub/MySQL | Conserver la preuve statique ; exécution externe à autoriser séparément | OUVERT — à-confirmer |
| RES-WP01-02 | L'IAM, `/dev/api-key`, `DISABLE_AUTH` et les rôles ne sont pas corrigés | Traiter dans un lot IAM séparé | HORS WP-01 |
| RES-WP01-03 | Les identifiants MySQL figurent dans l'historique Git | Validité, rotation et traitement historique à décider | OUVERT — à-confirmer |
| RES-WP01-04 | 16 avertissements pytest préexistants | Dette technique à prioriser séparément | OUVERT — hors WP-01 |

## Rollback

Les fichiers suivis de WP-01 peuvent être restaurés depuis le HEAD de baseline. La suppression d'index de `.env` peut être annulée avec `git restore --staged .env`, sans écraser sa copie locale. `.env.example` et `tests/test_database_config.py` sont deux créations séparables. `.venv` et le runtime `uv` sont des artefacts locaux réversibles. Aucune donnée n'a été modifiée.

## État J5 et suite

- Recommandation CERBERUS : `PASS_WITH_RESERVATIONS`.
- Décision humaine J5 : `EN_ATTENTE`.
- Validation business : `EN_ATTENTE`, validateur à-confirmer.
- RGPD : `EN_COURS`, aucune donnée réelle consultée ou migrée.
- SSI : `EN_COURS`, IAM et historique des identifiants à-confirmer.
- J6 et déploiement : `EN_ATTENTE`, aucun GO implicite.

Prochaine décision : accepter WP-01 avec la réserve AC-11, ou autoriser une exécution distincte de GitHub CI/MySQL. Le lot IAM reste séparé.
