# Création de l’arborescence projet (bootstrap PowerShell)

## Objectif
Ce script initialise l’arborescence complète du projet DIGICHEESE (code + tests + documentation),
sur le modèle “repo prof”, **sans doublons** et **en conservant** les dossiers `UML/` et `docs_cours/`.

- Une seule commande PowerShell
- Création des dossiers `src/` (couches), `tests/`, `DOC/` (FONC/TECH/UTILISATION), `UML/`, `docs_cours/`
- Création des fichiers racine (README, requirements, docker, env)
- Préparation de la venv `.venv` (à ignorer dans Git)

---

## Pré-requis
- Windows + PowerShell
- Python installé (commande `python` disponible)

> Si l’exécution des scripts est bloquée, lancer PowerShell en admin :
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

---

## Utilisation
1. Ouvrir PowerShell **à la racine** du dépôt.
2. Copier-coller le script ci-dessous.
3. Vérifier que l’arborescence est créée dans l’explorateur / VS Code.

---

## Script — Bootstrap complet

```powershell
# ============================================================
# Digicheese — Bootstrap complet (src cours + DOC + repo prof)
# - Une seule commande PowerShell
# - Pas de doublons
# - Conserve UML/ et docs_cours/
# - Prépare tests + outillage + venv
# ============================================================

# 1) Dossiers (src "cours" + doc + tests + annexes)
New-Item -ItemType Directory -Force -Path `
  "src", `
  "src\models", `
  "src\repositories", `
  "src\services", `
  "src\routes", `
  "src\conf", `
  "src\utils", `
  "tests", `
  "DOC", `
  "DOC\UTILISATION", `
  "DOC\TECH", `
  "DOC\FONC", `
  "UML", `
  "docs_cours" | Out-Null

# 2) Fichiers racine (style repo prof) + init python
New-Item -ItemType File -Force -Path `
  ".gitignore", `
  "README.md", `
  "requirements.txt", `
  ".env.example", `
  "Dockerfile", `
  "docker-compose.yml", `
  "src\__init__.py", `
  "src\models\__init__.py", `
  "src\repositories\__init__.py", `
  "src\services\__init__.py", `
  "src\routes\__init__.py", `
  "src\conf\__init__.py", `
  "src\utils\__init__.py", `
  "src\main.py" | Out-Null

# 3) Tests (choix unique : prof-like)
New-Item -ItemType File -Force -Path `
  "tests\__init__.py", `
  "tests\conftest.py", `
  "tests\test_client.py" | Out-Null

# 4) Documentation (fonctionnelle + technique + utilisation)
New-Item -ItemType File -Force -Path `
  "DOC\README.md", `
  "DOC\UTILISATION\Guide_Utilisateur.md", `
  "DOC\UTILISATION\FAQ.md", `
  "DOC\TECH\Architecture.md", `
  "DOC\TECH\Changements_CDC.md", `
  "DOC\TECH\Serveurs_Virtuels_Python.md", `
  "DOC\FONC\Contexte_Objectifs.md", `
  "DOC\FONC\Perimetre_In_Out.md", `
  "DOC\FONC\Regles_Metier.md", `
  "DOC\FONC\Parcours_Utilisateur.md", `
  "DOC\FONC\Backlog.md", `
  "UML\README.md" | Out-Null

# 5) Venv (local, à ignorer dans Git)
python -m venv .venv
