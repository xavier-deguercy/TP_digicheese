---
title: DigiCheese - Fiche d'execution MVP-02 Details de commande
version: 1.0.0
date: 2026-09-07
status: pret-pour-acceptation-metier
---

# MVP-02 - Details de commande

## Mandat et decisions appliquees

Le 2026-09-07, Xavier a valide le lot complet et autorise son developpement de bout en bout. Le travail a ete realise sur la branche `xavier`, depuis le commit de reference `278003a3d70633e3ed8127984a464e8e07f0c59f`, en preservant le working tree existant.

Les decisions appliquees sont : une seule ligne par objet et commande, report du champ historique `Colis`, commentaire facultatif, ajout d'un objet indisponible interdit et anciennes lignes indisponibles conservables.

Aucun commit, push, deploiement ou AUTO_NEXT n'a ete execute.

## Fonctionnalites livrees

- Modele `t_detail_commande` avec FK commande/objet et contrainte unique `(id_commande, id_objet)`.
- API CRUD `/details-commandes` pour Admin et OP-COLIS.
- Consultation filtree par `commande_id`.
- Quantite strictement positive et commentaire facultatif.
- Rejets `404` pour les references inconnues et `409` pour doublon, objet indisponible ou commande archivee.
- Remise a `null` de `nb_colis` dans la meme transaction que chaque creation, modification ou suppression de ligne.
- Suppression d'une commande ou d'un objet reference bloquee avec `409`.
- Lecture des objets autorisee a OP-COLIS ; leurs mutations restent reservees a Admin.
- Page `commande-details.html` accessible depuis la liste des commandes.
- Ajout, modification et suppression de ligne ; objets indisponibles et deja utilises exclus de la creation.
- Commande archivee affichee en lecture seule.

## Fichiers du lot

### Ajoutes

- `src/models/detail_commande.py`
- `src/schemas/detail_commande_schema.py`
- `src/repositories/detail_commande_repository.py`
- `src/services/detail_commande_service.py`
- `src/routers/detail_commande_router.py`
- `tests/test_detail_commande.py`
- `digicheese-ui/commande-details.html`
- `digicheese-ui/js/commande-details.js`
- scripts et preuves MVP-02 sous `reports/raw/`

### Modifies

- `src/main.py`
- `src/models/__init__.py`
- `src/services/commande_service.py`
- `src/services/objet_services.py`
- `src/routers/objet_router.py`
- `digicheese-ui/js/config.js`
- `digicheese-ui/js/commandes.js`
- documentation fonctionnelle, tests et gouvernance du lot

## Controles executes

| Controle | Resultat | Preuve |
|---|---|---|
| Suite pytest complete | 84 tests reussis ; 1 avertissement deprecation Starlette/AnyIO externe au lot | `reports/raw/pytest_mvp02.txt`, `reports/raw/junit_mvp02.xml` |
| Ruff sur `src` et `tests` | tous les controles reussis | `reports/raw/ruff_mvp02.txt` |
| Syntaxe JavaScript | controles Node reussis | `reports/raw/node_mvp02.txt` |
| OpenAPI | GET/POST collection, GET/PATCH/DELETE element et exemples POST/PATCH presents | `reports/raw/openapi_mvp02.txt` |
| MySQL Docker avec authentification Admin | creation 201 ; doublon, indisponibilite, suppressions liees et ecriture archivee rejetes 409 ; remise a vide de `nb_colis` ; nettoyage complet | `reports/raw/mysql_mvp02.txt` |
| Parcours Chrome reel pilote par CDP | navigation depuis Commandes, ajout, modification, filtrage des objets, lecture seule archivee et suppression finale 404 | `reports/raw/browser_mvp02.txt`, `reports/raw/mvp02_details_browser.png` |

## Limites et reserves

- Le champ historique `Colis` est volontairement hors du lot. Son eventuelle implementation dependra du cadrage futur de l'affectation des lignes aux colis physiques.
- Le controle navigateur integre Codex etait indisponible sur ce PC lors de MVP-01. Le meme navigateur Chrome local et le protocole CDP ont ete reutilises pour la preuve MVP-02.
- Chrome demande automatiquement `/favicon.ico`, absent du front statique, et recoit 404 sans effet sur les flux.
- Le parcours UI a utilise `DISABLE_AUTH=true`. L'authentification Admin a ete testee separement sur MySQL reel et les droits OP-COLIS sont couverts par pytest.
- Les controles techniques et fonctionnels ont ete executes dans la meme session Codex : `INDEPENDANCE_NON_DEMONTREE`.

## Point exact de reprise

MVP-02 est `DEVELOPPE_ET_VERIFIE` et attend une acceptation metier explicite avec les reserves ci-dessus. MVP-03 reste hors execution et aucun AUTO_NEXT n'est autorise.
