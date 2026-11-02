# Environnement Python / serveurs virtuels — DIGICHEESE (TP7)

## Objectif

Décrire un environnement reproductible pour exécuter l'API localement et ses tests.

## 1) Pré-requis

- Python 3.13, installé directement ou géré avec `uv`
- Git
- Docker et Docker Compose pour l'exécution avec MySQL

Vérifier l'interpréteur disponible :

```powershell
py -3.13 --version
```

Si cette commande ne trouve pas l'interpréteur, installer un runtime utilisateur
avec `uv` :

```powershell
uv python install 3.13
```

## 2) Créer l'environnement virtuel sous Windows/PowerShell

Depuis la racine du dépôt :

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip check
```

Avec le runtime géré par `uv`, remplacer la première commande par :

```powershell
uv venv --python 3.13 --seed .venv
```

Si la stratégie PowerShell interdit le script d'activation, utiliser directement
`.\.venv\Scripts\python.exe` pour les commandes suivantes.

## 3) Configurer la base

Créer la configuration locale à partir de l'exemple :

```powershell
Copy-Item .env.example .env
```

Remplacer le mot de passe `change-me` dans `.env` par celui de l'environnement local.
`DATABASE_URL` est obligatoire. Une variable définie dans le processus est prioritaire
sur `.env`. `DISABLE_AUTH` doit rester à `false` dans l'environnement développeur.

Le fichier `.env` est ignoré et reste local. Ne pas y stocker ni publier des
identifiants de production.

## 4) Exécuter les contrôles locaux

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_database_config.py tests/test_dependencies.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_utilisateur.py tests/test_client.py -q
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m ruff check src/database.py tests/conftest.py tests/test_database_config.py
```

Les tests utilisent une base SQLite en mémoire et neutralisent l'authentification.
Ils ne prouvent ni l'intégration MySQL, ni l'IAM, ni un déploiement.

## 5) Exécuter l'API locale avec MySQL

Après configuration de `.env` et démarrage du service Docker :

```powershell
docker compose up -d
.\.venv\Scripts\python.exe -m uvicorn src.main:app --reload
```

L'environnement de production, ses secrets, son exploitation et son déploiement
restent à-confirmer.
