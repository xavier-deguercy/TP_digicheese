# Tests - Guide rapide

## Prerequis
- Environnement virtuel Python 3.13 active
- Dependances installees: `python -m pip install -r requirements.txt`
- `DATABASE_URL` configuree pour l'application ; la suite pytest impose SQLite memoire

## Lancer tous les tests
```
python -m pytest -q
```

## Lancer un test specifique
```
python -m pytest tests/test_utilisateur.py -k test_create_user
```

## Lancer par markers
```
python -m pytest -m critical
python -m pytest -m integration
python -m pytest -m smoke
```

## Couverture (exemple)
```
python -m pytest --cov=src --cov-report=term --cov-report=xml:reports/raw/coverage_<TS>.xml
```

## Sorties brutes (exemple)
```
python -m pytest -q --maxfail=1 --disable-warnings --junitxml=reports/raw/junit_<TS>.xml
```

## Notes
- `tests/conftest.py` definit `DATABASE_URL` avant l'import de l'application, force
  `DISABLE_AUTH=true` et utilise SQLite memoire.
- Les tests CRUD couverts ici ne necessitent pas de token.
- Leur reussite prouve la non-regression CRUD dans cet environnement de test. Elle
  ne valide pas l'authentification, les habilitations, MySQL ou le deploiement.
- `tests/test_commande.py` couvre le CRUD Commandes, les references client et
  conditionnement, `nb_colis`, l'archivage, la suppression et le role OP-COLIS.
- `tests/test_detail_commande.py` couvre le CRUD des lignes, l'unicite
  commande/objet, les objets indisponibles, les commandes archivees, les conflits
  de suppression et la remise a vide de `nb_colis`.
- L'integration MySQL et le parcours navigateur MVP-01 sont consignes dans la
  fiche d'execution du lot sous `DOC/GOUVERNANCE/2026-09-07_MVP/`.
