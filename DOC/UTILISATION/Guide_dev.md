# A. Github

- main / prod / dev / test : on n’y touche jamais directement

- chacun travaille sur sa branche personnelle

- on envoie une Pull Request vers dev

### 1. Récupérer les branches du repo

Après le clone ou quand de nouvelles branches ont été push :

```bash
git fetch                   # récupérer les mises à jour
git branch -a               # lister les branches locales et distantes
```
Se placer sur dev :

```bash
git checkout dev            # basculer sur dev
git pull origin dev         # mettre dev à jour
```

### (Optionnel) Naviguer entre les branches

Afficher les branches locales :

```bash
git branch                 # lister les branches locales
```

Changer de branche

```bash
git checkout nom-de-la-branche # basculer sur une autre branche
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

<<<<<<< HEAD
attendre la validation avant merge par le GitMaster

## Résumé : Je crée ma branche → je code → je push → je fais une PR vers dev

---------------------------------------
=======
attendre la validation avant merge par le GitMaster 
>>>>>>> 63710e8e174f58272ab6743aa4f34010fa92c338
