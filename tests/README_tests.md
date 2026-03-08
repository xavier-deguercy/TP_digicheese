# Tests - Guide rapide

## Prerequis
- Environnement virtuel active
- Dependances installees: `pip install -r requirements.txt`

## Lancer tous les tests
```
pytest
```

## Lancer un test specifique
```
pytest tests/test_utilisateur.py -k test_create_user
```

## Lancer par markers
```
pytest -m critical
pytest -m integration
pytest -m smoke
```

## Couverture (exemple)
```
pytest --cov=src --cov-report=term --cov-report=xml:reports/raw/coverage_<TS>.xml
```

## Sorties brutes (exemple)
```
pytest -q --maxfail=1 --disable-warnings --junitxml=reports/raw/junit_<TS>.xml
```

## Notes
- `tests/conftest.py` force `DISABLE_AUTH=true` et utilise SQLite memoire.
- Les endpoints proteges ne necessitent pas de token en tests.
