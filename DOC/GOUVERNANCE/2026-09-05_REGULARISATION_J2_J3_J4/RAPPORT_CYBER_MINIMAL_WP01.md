---
title: DigiCheese - Contrôle cyber minimal WP-01
version: 0.1.0
date: 2026-09-05
status: cyber-minimal-reviewed-with-reservations
---

# Security Review: DigiCheese WP-01

## Scope

Contrôle local non intrusif du diff WP-01 avec la méthode `codex-security:security-diff-scan`. Le précontrôle de capacité a retourné `ready`. Aucun service de renseignement de vulnérabilités, service externe, test offensif ou test destructif n'a été utilisé.

Fichiers examinés : `.env` supprimé de l'index, `.env.example`, `.github/workflows/quality.yml`, `requirements.txt`, `src/database.py`, `tests/conftest.py`, `tests/test_database_config.py`, `README.md`, `DOC/TECH/Serveurs_Virtuels_Python.md` et `tests/README_tests.md`. Les chemins d'authentification et de clé API ont été lus uniquement comme contexte direct de `DISABLE_AUTH`.

## Threat Model

Les actifs concernés sont l'URL de connexion, les identifiants MySQL, les secrets locaux, les journaux et artefacts CI, ainsi que la capacité à désactiver l'authentification. Les frontières de confiance sont le processus local, le fichier `.env`, le dépôt Git privé, le runner GitHub futur et le service MySQL. Un contributeur ou un processus local capable de modifier l'environnement ou le workflow est l'acteur pertinent. L'exploitation publique du service et l'utilisation de données réelles restent `À_CONFIRMER`.

Les invariants minimaux sont : aucun secret réel dans Git ou les artefacts ; l'environnement du processus reste prioritaire sur `.env` ; l'authentification reste active hors tests explicitement bornés ; les identifiants de service CI ne donnent accès à aucune ressource réelle ; le workflow futur s'exécute sur un SHA et une branche identifiables.

## Findings

Aucune vulnérabilité nouvelle reportable n'a été confirmée dans le diff WP-01.

- `.env.example` contient `change-me` et `DISABLE_AUTH=false` ; il ne contient pas le secret local.
- `.env` est ignoré et absent de l'index courant. Sa suppression du suivi réduit l'exposition future, mais n'efface pas l'historique.
- `_load_database_url` conserve la priorité de la variable processus avec `override=False` et échoue explicitement lorsque la configuration manque.
- `DISABLE_AUTH=true` est limité aux tests automatisés et aux jobs CI examinés. Le diff n'active pas ce drapeau dans l'exemple développeur.
- Les identifiants MySQL du workflow désignent un service éphémère local au runner. Ils ne doivent pas être réutilisés pour une cible réelle.

## Reviewed Surfaces

| Surface | Risk Area | Outcome | Notes |
|---|---|---|---|
| `.env` et `.env.example` | Secret versionné | No issue found | Secret local absent de l'index ; historique non purgé |
| `src/database.py` | Priorité ou fuite de configuration | No issue found | Variable processus prioritaire ; message d'erreur sans valeur sensible |
| `tests/conftest.py` | Désactivation d'authentification | No issue found | Portée de test ; risque si le même drapeau est réutilisé hors tests |
| GitHub Actions | Secrets, dépendances d'actions et journaux | Needs follow-up | Exécution distante non autorisée ; actions référencées par tags majeurs et résultats du runner non observés |
| MySQL local | Identifiants par défaut et exposition de port | Reviewed with reservation | Preuve AC-11 locale réussie sur cible isolée ; ne pas réutiliser les identifiants sur une cible réelle |
| Historique Git | Anciens identifiants | Needs follow-up | Validité et rotation `À_CONFIRMER` ; la suppression de `.env` n'efface pas les commits antérieurs |
| Dépendance `email-validator==2.3.0` | Risque de dépendance | Needs follow-up | Version figée et import testé ; aucune base externe d'avis de sécurité consultée dans ce contrôle local |

## Réserves et suites

1. Confirmer que les identifiants historiques ne sont valides sur aucune cible ; les révoquer ou les faire tourner s'ils l'ont été.
2. Conserver `DISABLE_AUTH=false` dans tout environnement hors tests et empêcher sa propagation vers un déploiement.
3. Avant activation GitHub, vérifier les permissions minimales du workflow, le SHA exécuté, les journaux et les artefacts ; envisager le verrouillage des actions par SHA dans un lot de durcissement.
4. Exécuter plus tard une vérification de dépendances avec une source d'avis autorisée.

## Verdict

`CYBER_MINIMAL_REVIEWED_WITH_RESERVATIONS` pour le MVP. Ce verdict décrit le contrôle local autorisé ; il ne vaut pas `CYBER_VERIFIED`, Label SSI ou conformité exhaustive. `CYBER_NOT_APPLICABLE` n'est pas prononcé.
