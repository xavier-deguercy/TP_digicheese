````md
# Process Git & rituels Agile — DIGICHEESE (TP7)

## Objectif
Standardiser notre manière de travailler à plusieurs :
- éviter les erreurs de branche (push/merge au mauvais endroit)
- garder `main` **propre**
- centraliser le développement sur `dev`
- isoler la documentation / fonctionnel dans `func/<prenom>`
- adopter un rythme Agile simple (daily + point midi + clôture journée)

---

# 1) Stratégie de branches (règles)

## Branches “longue durée”
- `main` : **stable / livrable** (propre, démontrable)
- `dev` : **intégration développement** (code + tests en cours)
- `test` : **stabilisation** (optionnel, quand on veut valider avant `main`)

## Branches personnelles
### Développement (code)
- `dev/<prenom>` : branche personnelle de dev **qui part de `dev`**
  - ex : `dev/xavier`, `dev/stan`, `dev/hien`, `dev/imen`

### Fonctionnel (docs, backlog, UML, guides, etc.)
- `func/<prenom>` : branche personnelle de documentation / fonctionnel **qui part de `main`**
  - ex : `func/xavier`

> Justification :  
> - le code se consolide sur `dev` (intégration) ;  
> - la doc “fonctionnelle” peut aller vers `main` sans risque de casser l’exécutable ;  
> - pour éviter la divergence, **on réinjecte ensuite la doc de `main` vers `dev`** (voir §5.3).

---

# 2) Commandes “anti-erreur” (à faire systématiquement)

## Vérifier où je suis (branche + état)
```bash
git status
git branch --show-current
````

## Vérifier d’où vient ma branche + si elle suit un remote

```bash
git remote -v
git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null || echo "⚠️ Pas d'upstream configuré"
```

## Voir rapidement l’historique (comprendre ce qu’on va pousser/merger)

```bash
git log --oneline --decorate -n 10
```

---

# 3) Initialisation (une fois par personne)

## 3.1 Créer une branche DEV personnelle : `dev/<prenom>` (depuis `dev`)

```bash
# Se placer à la racine du repo
cd /chemin/vers/TP_digicheese

# Récupérer l’état distant
git fetch --all --prune

# Mettre dev à jour
git checkout dev
git pull origin dev

# Créer ta branche perso de dev
git checkout -b dev/<prenom>

# Publier la branche (upstream)
git push -u origin dev/<prenom>
```

## 3.2 Créer une branche FUNC personnelle : `func/<prenom>` (depuis `main`)

```bash
git fetch --all --prune

# Mettre main à jour
git checkout main
git pull origin main

# Créer ta branche perso fonctionnelle (docs)
git checkout -b func/<prenom>

# Publier la branche (upstream)
git push -u origin func/<prenom>
```

---

# 4) Routines de synchronisation (matin / midi / soir)

> Deux variantes possibles : **REBASE (propre)** ou **MERGE (simple)**.
> L’équipe choisit **une seule** variante et s’y tient pour éviter des surprises.

## Variante A (recommandée) — REBASE

### 4.1 Routine “MATIN” (avant de coder)

Objectif : repartir sur une base à jour, sans divergence.

#### Si je travaille sur du DEV (code)

```bash
git fetch --all --prune

git checkout dev
git pull origin dev

git checkout dev/<prenom>
git rebase dev

git push --force-with-lease
```

#### Si je travaille sur du FUNC (docs)

```bash
git fetch --all --prune

git checkout main
git pull origin main

git checkout func/<prenom>
git rebase main

git push --force-with-lease
```

### 4.2 Routine “MIDI” (checkpoint)

Objectif : sécuriser et limiter les conflits.

#### DEV (code)

```bash
git status
git add .
git commit -m "WIP: <courte-description>"
git push

git fetch --all --prune
git checkout dev
git pull origin dev
git checkout dev/<prenom>
git rebase dev
git push --force-with-lease
```

#### FUNC (docs)

```bash
git status
git add .
git commit -m "docs: <courte-description>"
git push

git fetch --all --prune
git checkout main
git pull origin main
git checkout func/<prenom>
git rebase main
git push --force-with-lease
```

### 4.3 Routine “SOIR” (fin de journée)

Objectif : tout est commité, poussé, et prêt pour PR/merge.

#### DEV (code)

```bash
git status
git add .
git commit -m "feat: <résumé clair>"
git push

git fetch --all --prune
git checkout dev
git pull origin dev
git checkout dev/<prenom>
git rebase dev
git push --force-with-lease
```

#### FUNC (docs)

```bash
git status
git add .
git commit -m "docs: <résumé clair>"
git push

git fetch --all --prune
git checkout main
git pull origin main
git checkout func/<prenom>
git rebase main
git push --force-with-lease
```

---

## Variante B (plus simple) — MERGE

### 4.4 Matin / Midi / Soir en MERGE (DEV)

```bash
git fetch --all --prune
git checkout dev
git pull origin dev

git checkout dev/<prenom>
git merge dev
git push
```

### 4.5 Matin / Midi / Soir en MERGE (FUNC)

```bash
git fetch --all --prune
git checkout main
git pull origin main

git checkout func/<prenom>
git merge main
git push
```

---

# 5) Push “sécurisé” (être sûr de pousser au bon endroit)

## 5.1 Vérification avant push (obligatoire)

```bash
git branch --show-current
git status
```

## 5.2 Push recommandé : pousser uniquement sa branche perso

```bash
git push
```

## 5.3 Push explicite (si tu veux être sûr à 100%)

> Utile quand tu veux éviter toute erreur de destination.

### DEV (depuis `dev/<prenom>`)

```bash
git branch --show-current
git push origin HEAD:dev/<prenom>
```

### FUNC (depuis `func/<prenom>`)

```bash
git branch --show-current
git push origin HEAD:func/<prenom>
```

⚠️ Règle : on évite de pousser directement sur `dev` / `main`.
On met à jour `dev` / `main` via PR ou merge contrôlé (section 6).

---

# 6) Merge (intégration) — mettre à jour dev/main proprement

## 6.1 Règles

* `main` reste propre : merge uniquement via **PR** (recommandé) ou merge contrôlé.
* `dev` sert à intégrer le code des branches `dev/<prenom>`.
* `func/<prenom>` (doc) merge vers `main`, puis on réinjecte la doc dans `dev` pour éviter la divergence.

## 6.2 Intégrer le DEV (code) : `dev/<prenom>` -> `dev`

### Variante PR (recommandée)

* PR : `dev/<prenom>` → `dev`, puis merge.

### Variante “merge local” (si PR impossible)

```bash
git checkout dev
git pull origin dev

git merge --no-ff dev/<prenom> -m "merge: dev/<prenom> -> dev"
git push origin dev
```

## 6.3 Intégrer le FUNC (docs) : `func/<prenom>` -> `main`

### Variante PR (recommandée)

* PR : `func/<prenom>` → `main`, puis merge.

### Variante “merge local” (si PR impossible)

```bash
git checkout main
git pull origin main

git merge --no-ff func/<prenom> -m "merge: func/<prenom> -> main"
git push origin main
```

## 6.4 Réinjecter la doc de `main` dans `dev` (important)

Après un merge docs dans `main`, synchroniser `dev` :

```bash
git checkout dev
git pull origin dev
git merge main
git push origin dev
```

---

# 7) Gestion des conflits (commande réflexe)

## Si rebase bloque

```bash
git status
# résoudre les conflits, puis :
git add .
git rebase --continue

# annuler si besoin :
# git rebase --abort
```

## Si merge bloque

```bash
git status
# résoudre les conflits, puis :
git add .
git commit
git push
```

---

# 8) Rituels Agile (cadence simple)

## Daily (15 minutes, matin)

Chacun répond :

1. Ce que j’ai fait hier
2. Ce que je fais aujourd’hui
3. Mes blocages / besoins

## Point “midi” (5–10 minutes)

* conflits en vue ?
* ticket bloqué ?
* besoin d’aide / revue PR ?

## Clôture (soir, 10 minutes max)

* push fin de journée (branche perso)
* mise à jour du Kanban
* note de suivi (voir §9)

---

# 9) Journal de suivi (recommandé)

Créer : `DOC/UTILISATION/Journal_Suivi.md`

Format (1 entrée / jour) :

* Date :
* Avancement (tickets fermés / PR) :
* Blocages :
* Décisions prises :
* Prochaines actions :

---

# 10) Bonnes pratiques

* Un ticket = une branche perso = une PR (quand possible)
* Commits petits et lisibles
* Toujours `fetch` + `pull` avant de commencer
* Toujours vérifier la branche avant `push` :

  * `git branch --show-current`
* Toujours pousser sur `dev/<prenom>` ou `func/<prenom>`
* `dev` / `main` ne se mettent à jour que via PR ou merge contrôlé

```
```
