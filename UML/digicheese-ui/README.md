# DIGICHEESE — Admin UI (V1) — Front statique connecté à l'API

## Contenu
- `admin-dashboard.html` : statut API + raccourcis
- `admin-objets.html` : CRUD Objets (`/objets`)
- `admin-conditionnements.html` : CRUD Conditionnements (`/conditionnements`)
- `login.html` : login optionnel (token Bearer) configurable

## Pré-requis côté backend (FastAPI)
### 1) API accessible
Par défaut l'UI appelle : `http://127.0.0.1:8000` (configurable dans `js/config.js`).

### 2) CORS (si front et API sont sur des ports différents)
Dans ton `main.py` FastAPI, ajoute le middleware CORS (exemple) :

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Lancer le front (Windows / PowerShell)
Dans le dossier qui contient ces fichiers :

```powershell
python -m http.server 5500
```

Puis ouvrir :
- `http://127.0.0.1:5500/login.html`
- ou directement `http://127.0.0.1:5500/admin-objets.html`

## Auth (optionnel)
Dans `js/config.js` :
- `AUTH.enabled = true`
- ajuste `loginPath`, `mode` et `tokenResponseField`

Modes :
- `oauth2` : attend un endpoint type FastAPI OAuth2 `/token` (form urlencoded)
- `json` : attend un endpoint JSON

## Mapping de champs
Si tes modèles API n'ont pas exactement les mêmes noms de champs :
- modifie `DC_CONFIG.FIELDS.objet` et `DC_CONFIG.FIELDS.conditionnement`.


## Auth Digicheese (réel) : X-API-Key (pas de JWT)
Dans `src/utils/dependencies.py`, l'API attend un header `X-API-Key`.  
L'IHM stocke cette clé dans le navigateur (LocalStorage) via `login.html` puis l'envoie sur chaque requête.

### Générer / récupérer la clé Admin
Depuis la racine du projet backend :

```powershell
python -m src.utils.create_db
```

Le script seed les rôles + crée un admin et affiche la clé dans la console.

### Désactiver l'auth en dev
Tu peux démarrer l'API avec :

```powershell
$env:DISABLE_AUTH="true"
uvicorn src.main:app --reload
```
