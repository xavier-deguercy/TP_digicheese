---
title: DigiCheese - Rapport du lot revue refactor et repositionnement UI
version: 1.3.0
date: 2026-09-06
status: clos-avec-reserves
---

# DigiCheese — Rapport du lot WP-03 à WP-05

## 1. Baseline et mandat

- Branche : `xavier`.
- HEAD inchangé : `6790d40902c32f207923c8d174169e280cddadc9`.
- Périmètre autorisé : revue API et UI, correction des défauts confirmés, repositionnement de l'UI, contrôles locaux, configuration Docker/MySQL et retrait du workflow GitHub Actions.
- Exclusions respectées : aucun commit, push, déploiement, test cyber externe ou action GitHub.
- Le working tree antérieur, les documents métier, le backlog Wave 2, les décisions et les preuves historiques ont été préservés.

## 2. Réalisation

### WP-03 — Revue et refactorisation

Les corrections confirmées ont été appliquées dans l'enveloppe autorisée : suppression de la route de développement qui exposait une clé par identifiant utilisateur, centralisation des rôles, correction du libellé `OP-COLIS`, validation renforcée des adresses, rôles et mots de passe, modernisation SQLAlchemy/Pydantic, enregistrement complet des modèles et nettoyage Ruff.

Les tests activent les clés étrangères SQLite et couvrent désormais l'authentification active, l'accès OP-COLIS, l'absence de clé, une clé invalide et l'absence de la route supprimée.

### WP-04 — Repositionnement UI

Les 24 fichiers de `UML/digicheese-ui` ont été repositionnés sous `digicheese-ui` à la racine. L'intégrité de l'inventaire a été contrôlée avant adaptation ; 17 fichiers ont ensuite été adaptés. Les chemins actifs de documentation ont été corrigés et la preuve historique J1 a été conservée telle quelle.

Les corrections UI couvrent la déconnexion injectée, le panneau équipe, la navigation active, les accès Admin/Objets/Conditionnements, le formulaire Objet sans doublon `lib`, les footers et les liens de recherche historiques.

### WP-05 — Retrait de GitHub Actions

Le fichier `.github/workflows/quality.yml` a été supprimé localement. GitHub Actions sort de la cible du projet après son usage d'apprentissage sur la première version. Aucun changement distant n'a été effectué.

### Docker et MySQL local

Le Compose n'impose plus de nom de conteneur, ajoute un healthcheck MySQL et attend l'état sain avant de lancer phpMyAdmin. MySQL a été recréé avec le volume nommé `tp_digicheese_mysql_data`, puis contrôlé sain avec neuf tables. Le parcours API MySQL réel a couvert santé, authentification et CRUD Objet. k6 a été exécuté dans son image Docker officielle.

## 3. Contrôles et preuves

| Contrôle | Résultat | Périmètre prouvé |
|---|---|---|
| CERBERUS-TECH indépendant | `TECH_VERIFIED` | Candidate complète, empreinte `692290a6416b8a6efb2abf2d816cf4fec664b643a0ba4151874bb3e13048e315` ; matière WP `26555ba4020f82ad284f7a3967cc444cf3962a22c177ff25af7a49cde38ca4f3` |
| Pytest | `63 passed` | API, schémas, configuration et authentification locale ; un avertissement Starlette/AnyIO externe |
| Ruff | `All checks passed` | Sources et tests Python |
| JavaScript | `6/6` | Contrôles statiques ciblés |
| API MySQL réelle | `PASS` | santé 200, sans clé 401, clé valide 200, route dev 404, CRUD Objet 201/200/200 |
| k6 Docker | `PASS` | 100 requêtes, 0 échec, p95 8,2 ms ; preuve `reports/raw/k6_post_wp01.json` |
| CERBERUS-FONCTIONNEL indépendant | `FUNCTIONAL_VERIFIED` | 8 pages, includes, navigation, authentification, logout, formulaires, aucune erreur console ; UI `3aad15d082f8e07615d44c478929d74a811182d8181b5a75d784310ca8ed196b` |
| Codex Security diff scan | Couverture complète, 0 finding reportable | Scan `592df2d4-dc1b-42fc-b240-ce101ca49236`, 81/81 éléments, six surfaces sans problème introduit détecté |
| Validateur équipe DSI V2 | `37/37` | Version chargée `2.0.0`, aucun contrôle structurel en échec |
| UTF-8, références et diff | `PASS` | Encodage strict, références HTML et Markdown, `git diff --check` |

Les contrôles technique, fonctionnel et cyber ont été réalisés par des sous-agents distincts du développement. Leur indépendance d'exécution est démontrée pour ce lot.

## 4. Réserves

- La confirmation native finale de suppression dans Chrome n'a pas été rejouée, car le dialogue bloquait l'outil navigateur. Le bouton a ouvert la confirmation ; la suppression authentifiée a été prouvée séparément par HTTP 200 et absence de résidu.
- Le scan cyber est une analyse locale du diff. Les sources cyber formelles restent `À_FOURNIR` ; aucun verdict de conformité ni `CYBER_NOT_APPLICABLE` n'est prononcé.
- `LocalStorage`, le CORS permissif de développement, `DISABLE_AUTH`, le bootstrap Admin, la rotation des clés, TLS, CSP, exposition des ports et gestion des secrets restent des sujets du futur lot IAM/cyber.
- La production, l'exposition réseau et l'utilisation de données réelles restent `À_CONFIRMER`.
- Git reconnaîtra formellement les déplacements lors d'une future indexation ou d'un futur commit autorisé ; aucune de ces actions n'a été exécutée.

## 5. Backlog, enveloppe et reprise

| Élément | Statut après contrôle |
|---|---|
| WP-03 | `ACCEPTÉ_AVEC_RÉSERVES` — décision de Xavier du 2026-09-06 |
| WP-04 | `ACCEPTÉ_AVEC_RÉSERVES` — décision de Xavier du 2026-09-06 |
| WP-05 | `ACCEPTÉ` — décision de Xavier du 2026-09-06 |
| WP-02 IAM | `PROPOSÉ`, non `READY`, non autorisé |
| Lot WP-03 à WP-05 | `CLOS_AVEC_RÉSERVES` — décision de Xavier du 2026-09-06 |
| Enveloppe J4 WP-03 à WP-05 | définitivement consommée |
| `AUTO_NEXT` | `NON_AUTORISÉ` |

## 6. Décisions métier

Le 2026-09-06, Xavier accepte tous les éléments présentés avec le statut `ACCEPTÉ_AVEC_RÉSERVES`. Cette décision clôt l'acceptation métier de WP-03 et WP-04 avec leurs réserves documentées. Xavier accepte également WP-05 et confirme la sortie de GitHub Actions du périmètre du projet.

Xavier prononce ensuite la clôture consolidée `CLOS_AVEC_RÉSERVES` du lot WP-03 à WP-05. L'enveloppe J4 correspondante est définitivement consommée. Les réserves de sécurité sont reportées après le MVP. Cette clôture n'autorise aucun commit, push, déploiement, action GitHub, nouvel élément ou passage `AUTO_NEXT`.

Le lot WP-03 à WP-05 ne nécessite plus de décision métier. Le point exact de reprise est la sélection et la préparation du prochain lot MVP par une décision séparée. WP-02 IAM reste non `READY`, non autorisé et reporté avec les travaux de sécurité ; aucun développement ne commence automatiquement.
