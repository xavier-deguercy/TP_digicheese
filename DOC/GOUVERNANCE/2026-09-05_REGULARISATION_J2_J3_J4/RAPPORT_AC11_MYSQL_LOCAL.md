---
title: DigiCheese - Preuve AC-11 MySQL local isolé
version: 0.1.0
date: 2026-09-05
status: ac11-local-verified-github-en-attente
---

# AC-11 — Exécution MySQL locale isolée

## Périmètre exécuté

- Projet Compose : `wp01ac11`.
- Image : `mysql:8.0`, empreinte `sha256:7dcddc01f13bab2f15cde676d44d01f61fc9f99fe7785e86196dfc07d358ae2b`.
- Conteneur : `digicheese-mysql`.
- Volume isolé : `wp01ac11_mysql_data`.
- Réseau isolé : `wp01ac11_default`.
- Application : Uvicorn local sur `127.0.0.1:8000`.
- Données : schéma vide et données de test uniquement.

## Résultats

| Contrôle | Résultat |
|---|---|
| Démarrage MySQL 8 | `PASS` — `mysqld is alive` |
| Connexion applicative | `PASS` — application démarrée avec la cible MySQL locale |
| Création du schéma | `PASS` — 10 tables observées dans `digicheese` |
| Healthcheck | `PASS` — HTTP 200, `{"status":"ok"}` |
| Smoke k6 | `PASS` — 100/100 contrôles réussis, 0/100 requête en échec |
| Latence k6 | moyenne 7,07 ms ; p95 9,75 ms ; maximum 11,87 ms |
| Nettoyage | `PASS` — application arrêtée ; conteneur, réseau et volume isolés supprimés |

## Conclusion

La partie locale MySQL/healthcheck/smoke d'AC-11 est `VERIFIED`. L'exécution GitHub Actions reste `EN_ATTENTE` et non autorisée. Ce résultat ne vaut ni preuve du runner GitHub, ni validation cyber formelle, ni autorisation de commit, push ou déploiement.

## Reconfiguration du poste de développement

Après changement de PC, l'environnement a été remis en état le 2026-09-05 : Docker Desktop 4.84.0 avec moteur 29.6.2 et WSL2, Compose 5.3.1, Python 3.13.7 via `uv`, environnement `.venv` cohérent et k6 2.2.0 installé dans le `PATH` utilisateur. Le `.env` local ignoré par Git contient désormais les clés `DATABASE_URL` et `DISABLE_AUTH`, avec authentification active.

La validation sur l'environnement persistant de développement confirme MySQL et phpMyAdmin disponibles sur les ports 3308 et 8080, `/health` en HTTP 200, 51 tests réussis avec 16 avertissements préexistants et un smoke k6 natif à 100/100 contrôles, 0 requête en échec et p95 à 8,57 ms. L'application Uvicorn de contrôle a été arrêtée ; les services Docker de développement restent démarrés.
