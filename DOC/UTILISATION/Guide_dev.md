# DigiCheese – Guide de travail (Git, Docker, API)

## 1. Workflow Git (travail en équipe)

### a. Travailler sur une feature

1. Se placer sur sa branche :

```bash
git checkout ma-branche
```

2. Développer la feature

**Quand la feature est fonctionnelle et propre :**

```bash
git add .
git commit -m "ex: ajout CRUD poids"
git push origin ma-branche
```

✅ Quand faire un commit ?

- feature terminée ou étape logique finie
- code qui fonctionne
- pas de print, pas de code commenté inutile
- indentation propre, fichiers sauvegardés

### b. Pull Request (PR)

Créer une Pull Request vers **dev** sur GitHub

*Quelqu'un s'occupe de faire les corrections*

Corriger les retours éventuels

Pour chaque correction :

```bash
git add .
git commit -m "fix: corrections review poids"
git push origin ma-branche
```

### c. Après merge de la PR

Une fois la branche mergée dans dev :

```bash
git checkout dev
git pull origin dev
git checkout ma-branche
git rebase dev
```

➡️ Objectif : garder ta branche à jour avec dev.

## 2. Docker (base de données locale)

### a. Lancer l’environnement

```bash
docker compose up -d
```

### b. Arrêter l’environnement

```bash
docker compose down
```

### c. Reset complet de la base (⚠️ supprime les données)

**A ne faire que si on modifie les modèles**

```bash
docker compose down -v
docker compose up -d
```

### d. Entrer dans le conteneur MySQL

**Si vous voulez faire des commandes SQL sur vos tables (ex : SELECT * FROM t_utilisateurs)

```bash
docker exec -it digicheese-mysql bash
```

Puis se connecter à MySQL :

```bash
mysql -u group2 -p
```

- Mot de passe :
**digicheese**


Quitter MySQL :

```bash
exit;
```

Quitter le conteneur :

```bash
exit
```

### e. phpMyAdmin

URL : http://localhost:8080

Serveur : mysql

Utilisateur : group2

Mot de passe : digicheese

⚠️ **Important**

Docker est utilisé uniquement en local pour le développement.
Chacun a sa base locale, il n’y a aucun environnement distant.

## 3. Lancement de l’API (FastAPI)

### a. Créer / recréer la base depuis les modèles

(à faire après un reset Docker ou modification des modèles)

```bash
python -m src.utils.create_db
```

### b. Lancer le backend FastAPI

Depuis la racine du projet :

```bash
uvicorn src.main:app --reload
```

### c. Accéder à la documentation Swagger

Swagger UI : http://127.0.0.1:8000/docs

OpenAPI JSON : http://127.0.0.1:8000/openapi.json


## ✅ Rappel final

- Git → gestion du code et du travail en équipe

- Docker → base de données locale

- FastAPI / Uvicorn → serveur backend + Swagger
