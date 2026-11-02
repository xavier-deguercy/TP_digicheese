---
title: DigiCheese - Prochain lot revue refactor et repositionnement UI
version: 0.5.0
date: 2026-09-06
status: clos-avec-reserves
---

# DigiCheese — Prochain lot après WP-01

## Décisions acquises

- WP-01 : J5 `GO_AVEC_RÉSERVES`, décision de Xavier du 2026-09-06.
- GitHub Actions : retiré de la cible d'exploitation du projet ; le workflow d'apprentissage de la première version a été supprimé localement dans WP-05.
- Aucun commit, push ou déploiement autorisé par cette décision.
- `AUTO_NEXT` reste non autorisé.

Le fichier `.github/workflows/quality.yml` a été supprimé localement dans le lot autorisé. Aucun changement distant n'a été effectué.

## Inventaire du front à repositionner

- Source historique : `UML/digicheese-ui`.
- Cible appliquée : `digicheese-ui` à la racine du dépôt.
- Contenu : 24 fichiers HTML, CSS, JavaScript, fragments et pages historiques.
- Dépôt Git imbriqué : aucun.
- Références actuelles identifiées dans le dossier J1, ses preuves JSON et le backlog Wave 2.
- API configurée par défaut : `http://127.0.0.1:8000`.
- Lancement documenté : `python -m http.server 5500`.

## Lots proposés

| ID | Lot | Résultat attendu | Statut |
|---|---|---|---|
| WP-02 | IAM déjà identifié | Préparer matrice, critères, tests et rollback | `PROPOSÉ`, non `READY` |
| WP-03 | Revue de code et refactorisation conditionnelle | Rapport de revue priorisé ; refactor seulement pour les défauts confirmés et autorisés | `ACCEPTÉ_AVEC_RÉSERVES` — décision métier de Xavier du 2026-09-06 |
| WP-04 | Repositionnement du front | Déplacer `UML/digicheese-ui` vers `digicheese-ui`, mettre à jour toutes les références et vérifier UI/API | `ACCEPTÉ_AVEC_RÉSERVES` — décision métier de Xavier du 2026-09-06 |
| WP-05 | Retrait de GitHub Actions | Désactiver ou supprimer le workflow actif et distinguer les rapports historiques | `ACCEPTÉ` — décision métier de Xavier du 2026-09-06 |

## Séquence recommandée

1. Geler l'inventaire des 24 fichiers et leurs empreintes.
2. Effectuer une revue de code en lecture seule sur l'API et le front.
3. Classer les constats : défaut, dette, amélioration ou absence d'action.
4. Déplacer le front avec un déplacement Git traçable, sans suppression intermédiaire.
5. Mettre à jour les chemins actifs ; conserver les références historiques avec une note de relocalisation lorsqu'elles constituent une preuve datée.
6. Vérifier HTML, CSS, JavaScript, fragments, URLs, CORS, authentification et appels API.
7. Exécuter les tests Python, le front local, les parcours Objets/Conditionnements et le smoke k6.
8. Refactoriser uniquement les constats acceptés dans l'enveloppe corrective.
9. Rejouer les contrôles technique, fonctionnel et cyber minimal impactés.
10. Traiter séparément le retrait de `.github/workflows/quality.yml` avant tout futur push.

## Enveloppe J4 décidée

L'autorisation du 2026-09-06 couvre la revue, le déplacement WP-04, les corrections confirmées issues de la revue et le retrait WP-05. Commit, push et déploiement restent exclus.

## Décision J4 du 2026-09-06

Xavier autorise le lot fermé WP-03 à WP-05 en `GO_AVEC_RÉSERVES` : revue API et front, refactorisation limitée aux défauts confirmés, déplacement des 24 fichiers vers `digicheese-ui` à la racine, mise à jour des références actives, contrôles UI/API/Python/k6 et retrait du workflow GitHub Actions. Les preuves historiques doivent rester traçables.

Commit, push, déploiement, nouvelle fonctionnalité et `AUTO_NEXT` restent non autorisés. L'exécution s'arrête après consolidation de ce lot.

## Clôture d'exécution du 2026-09-06

Le lot fermé WP-03 à WP-05 est exécuté et contrôlé. Les résultats, empreintes, réserves et limites figurent dans le [rapport de lot](RAPPORT_LOT_REVUE_REFACTOR_UI.md).

L'enveloppe J4 de ce lot est consommée. WP-02 IAM reste `PROPOSÉ`, non `READY` et non autorisé. `AUTO_NEXT` reste `NON_AUTORISÉ` : aucun élément suivant n'est simultanément prêt et couvert par une enveloppe active.

## Décision de clôture métier du 2026-09-06

Xavier prononce `CLOS_AVEC_RÉSERVES` pour le lot WP-03 à WP-05. WP-03 et WP-04 restent `ACCEPTÉ_AVEC_RÉSERVES` ; WP-05 reste `ACCEPTÉ`. L'enveloppe J4 du lot est définitivement consommée et les réserves de sécurité sont reportées après le MVP.

Cette clôture n'ouvre aucun nouvel élément. Le prochain lot MVP doit être sélectionné, préparé et autorisé séparément. WP-02 IAM reste non `READY`, non autorisé et reporté avec les travaux de sécurité.

## Protections du déplacement

- Ne jamais effacer récursivement la source avant vérification de la cible.
- Comparer la liste, la taille et les empreintes des fichiers avant et après.
- Utiliser un seul déplacement au sein du dépôt.
- Rechercher et mettre à jour toutes les références actives à `UML/digicheese-ui`.
- Vérifier qu'aucun chemin relatif CSS, JavaScript ou fragment n'est cassé.
- Ne pas mélanger le déplacement avec une refonte fonctionnelle non décidée.
- Prévoir un rollback par déplacement inverse avant toute autre modification.
