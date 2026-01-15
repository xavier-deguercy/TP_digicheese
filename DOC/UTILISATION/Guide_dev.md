# A. Github

- main / prod / dev / test : on n’y touche jamais directement

- chacun travaille sur sa branche personnelle

- on envoie une Pull Request vers dev

### 1. Récupérer les branches du repo

Après le clone ou quand de nouvelles branches ont été push :

```bash
git fetch
git branch -a
```
Se placer sur dev :

```bash
git checkout dev
git pull origin dev
```

### (Optionnel) Naviguer entre les branches

Afficher les branches locales :

```bash
git branch
```

Changer de branche

```bash
git checkout nom-de-la-branche
```

### 2. Créer une branche de travail

##### ⚠️ Toujours créer sa branche depuis dev.

```bash
git checkout dev
git pull origin dev
git checkout -b feature/prenom
```

> Puis soit:
>
> on l'envoie directement sur GitHub
>
```bash
git push -u origin feature/prenom
```

> Soit :
>

### 3. Cycle de travail

On code notre feature, puis :

```bash
git add .
git commit -m "feat: description courte"
git push
```
### 4. Méthodologie Git

**1 branche = 1 feature**

**Ne jamais travailler directement sur :**

- *main*
- *prod*
- *test*
- *dev*

> Nommage des branches :
>
> feature/prenom
>
> feature/crud-commune

##### Pull Request (PR)

**Pourquoi ?**

- relire le code
- éviter de casser le projet
- garder un historique propre

**Comment ?**

- depuis GitHub :

source : feature/...

cible : dev

attendre la validation avant merge par le GitMaster

## Résumé : Je crée ma branche → je code → je push → je fais une PR vers dev

---------------------------------------
