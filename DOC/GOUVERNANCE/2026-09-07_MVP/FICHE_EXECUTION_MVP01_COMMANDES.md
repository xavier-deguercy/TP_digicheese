---
title: DigiCheese - Fiche d'execution MVP-01 Commandes
version: 1.1.0
date: 2026-09-07
status: accepte-avec-reserves
---

# MVP-01 - Commandes

## Mandat et point de depart

Xavier a autorise le 2026-09-07 le developpement de bout en bout de MVP-01 « Commandes ». Le travail a ete realise sur la branche `xavier`, depuis le commit `278003a3d70633e3ed8127984a464e8e07f0c59f`.

Le working tree etait deja modifie avant MVP-01. Les travaux anterieurs, dont le repositionnement de `digicheese-ui`, les corrections API et les documents de gouvernance, ont ete preserves. Aucun commit, push, deploiement ni AUTO_NEXT n'a ete execute.

## Fonctionnalites livrees

- Modele MySQL/SQLAlchemy `t_commande` relie au client et, facultativement, au conditionnement.
- API CRUD `/commandes` pour les roles Admin et OP-COLIS.
- Validation des references client et conditionnement.
- `nb_colis` facultatif et strictement positif lorsqu'il est renseigne.
- Remise a vide de `nb_colis` lors d'un changement de conditionnement.
- Archivage d'une commande complete ou incomplete.
- Consultation d'une commande archivee, modification et suppression bloquees jusqu'au desarchivage.
- Suppression d'une commande active ; la contrainte « sans ligne » sera completee avec MVP-02.
- Blocage de la suppression d'un client ou conditionnement reference par une commande.
- Page `digicheese-ui/commandes.html` : liste, recherche, filtre actif/archive, creation, modification, archivage, desarchivage et suppression.
- Schemas et exemples OpenAPI pour la creation et la modification.

## Fichiers du lot

### Ajoutes

- `src/models/commande.py`
- `src/schemas/commande_schema.py`
- `src/repositories/commande_repository.py`
- `src/services/commande_service.py`
- `src/routers/commande_router.py`
- `tests/test_commande.py`
- `digicheese-ui/commandes.html`
- `digicheese-ui/js/commandes.js`
- `reports/raw/mvp01_browser_check.mjs`
- `reports/raw/mvp01_mysql_check.py`
- preuves brutes `reports/raw/*_mvp01.*` et capture `reports/raw/mvp01_commandes_browser.png`

### Modifies pour MVP-01

- `src/main.py`
- `src/models/__init__.py`
- `src/services/client_service.py`
- `src/services/conditionnement_services.py`
- `digicheese-ui/js/config.js`
- `digicheese-ui/partials/header.html`
- `digicheese-ui/README.md`
- `tests/README_tests.md`
- `DOC/FONC/wave2/Regles_Metier_wave2.md`
- `DOC/FONC/wave2/Backlog_wave2.md`
- `DOC/GOUVERNANCE/2026-09-07_MVP/PERIMETRE_MVP.md`

## Controles executes

| Controle | Resultat | Preuve |
|---|---|---|
| Suite pytest complete, SQLite en memoire | 74 tests reussis ; 1 avertissement deprecation Starlette/AnyIO externe au lot | `reports/raw/pytest_mvp01.txt`, `reports/raw/junit_mvp01.xml` |
| Ruff sur `src` et `tests` | tous les controles reussis | `reports/raw/ruff_mvp01.txt` |
| Syntaxe JavaScript | `node --check` reussi sur `commandes.js`, `config.js`, `api.js`, `includes.js` et `ui.js` | sortie de session |
| OpenAPI | `/commandes/` expose GET/POST ; la route element expose GET/PATCH/DELETE ; exemples POST/PATCH presents | `reports/raw/openapi_mvp01.txt` |
| MySQL Docker avec authentification Admin `X-API-Key` | creation 201 ; conflits de references 409 ; archive 200 ; modification archivee 409 ; desarchivage 200 ; remise a vide de `nb_colis` ; liste et suppression 200 ; nettoyage complet | `reports/raw/mysql_mvp01.txt` |
| Parcours Chrome reel pilote par CDP | creation, modification, archivage, verrouillage visuel, desarchivage et suppression reussis ; suppression verifiee par GET 404 | `reports/raw/mvp01_commandes_browser.png`, sortie du controle navigateur |
| Encodage et references UI | 19/19 fichiers lus en UTF-8, aucun U+FFFD, 8/8 ressources referencees presentes | `reports/raw/encoding_refs_mvp01.txt` |

## Limites et reserves

- La regle interdisant la suppression d'une commande possedant des lignes de detail ne peut pas encore etre executee : le modele de lignes appartient a MVP-02. La suppression est actuellement limitee aux commandes actives ; la verification des lignes devra etre ajoutee dans MVP-02.
- Le controle navigateur integre Codex n'a pas pu initialiser sa session sur ce PC (`failed to write kernel assets`, chemin introuvable), y compris apres reinitialisation. Le parcours a donc ete rejoue avec Chrome 152 local via son protocole CDP.
- Chrome demande automatiquement `/favicon.ico`, absent du front statique, et recoit 404. Cette ressource n'intervient dans aucun flux MVP-01.
- Le parcours UI a utilise l'API locale avec `DISABLE_AUTH=true`. L'authentification et les habilitations ont ete controlees separement par la suite pytest et par le scenario MySQL reel avec une cle Admin, sans exposer cette cle.
- Les controles techniques et fonctionnels ont ete executes dans la meme session Codex. Aucune independance entre deux agents de test distincts n'est revendiquee : `INDEPENDANCE_NON_DEMONTREE`.

## Point exact de reprise

Le 2026-09-07, Xavier accepte explicitement MVP-01 avec les reserves ci-dessus. MVP-01 est clos fonctionnellement au statut `ACCEPTE_AVEC_RESERVES`. Les reserves restent tracees et devront etre traitees dans le lot auquel elles s'appliquent.

MVP-02 reste `A_PREPARER` et aucun AUTO_NEXT n'est autorise. La prochaine decision porte uniquement sur l'autorisation de preparer MVP-02.
