# DIGICHEESE — TP Diginamic (UML + socle dev)

## Contexte
DIGICHEESE est une fromagerie régionale (≈ 130 salariés), entreprise familiale de plus d’un siècle,
qui vend ses produits :
- aux grands distributeurs
- aux particuliers qui se rendent physiquement à la boutique de l’usine

Ce dépôt est réalisé dans le cadre d’un **TP de la formation Diginamic**.
L’objectif est de produire des livrables structurés (UML, scénarios, conception) et de préparer un socle
de développement exploitable (architecture, tests, exécution).

> Statut : TP pédagogique (prioritaire) + socle dev (évolutif)

---

## Objectifs pédagogiques
- Modéliser un besoin métier (acteurs, cas d’utilisation, scénarios)
- Produire des diagrammes UML (use case, séquence, activité, classes / ERD selon sujet)
- Structurer un projet comme un vrai dépôt de développement :
  - séparation des responsabilités (routes / services / repositories)
  - configuration
  - tests automatisés de base
  - documentation (fonctionnelle, technique et d’utilisation)

---

## Livrables attendus (rappel consignes)
- Code Python structuré par projet (**src/** + scripts associés si besoin)
- Tests : scénarios + scripts (dossier **tests/** + éventuellement scripts d’exécution)
- Documentation :
  - **DOC/** : documentation technique + documentation d’utilisation (avec un README équipe/rôles)
  - **DOC/TECH/** : architecture, éléments modifiés selon le cahier des charges, description des environnements Python

---

## Arborescence (principale)
- `src/` : code source (structure imposée par le cours)
  - `routes/` : endpoints / contrôleurs
  - `services/` : logique métier
  - `repositories/` : accès données
  - `models/` : modèles et structures
  - `conf/` : configuration
  - `utils/` : utilitaires
- `tests/` : tests automatisés (pytest)
- `DOC/` : documentation projet (évolutive)
  - `DOC/README.md` : doc centrale + équipe / rôles + index
  - `DOC/FONC/` : documentation fonctionnelle (contexte, périmètre, règles métier, parcours, backlog)
  - `DOC/UTILISATION/` : documentation d’utilisation (guide, FAQ)
  - `DOC/TECH/` : documentation technique (architecture, changements CDC, environnements Python)
- `UML/` : livrables UML + exports (peut contenir des éléments d’un autre cours)
- `docs_cours/` : supports / notes / documents liés aux cours

➡️ Point d’entrée documentation : **`DOC/README.md`**

---

## Pré-requis
- Python 3.x
- Git

---

## Installation (Windows — PowerShell / Git Bash)
Créer l’environnement virtuel :
```bash
python -m venv .venv
```
------------------------------------

# Organisation projet API

## 1. Résumé du projet

- Backend API Python + MySQL
- CRUD (Create Read Update Delete)
- Documentation Swagger
- Tests via Pytest / unittest

> **MVP attendu**:
>
> CRUD Admin (swagger)
>
> CRUD Operateur Colis (Gestion client)
>
> Une branche par développeur et les branches : test, dev, prod et master
>
> Sources python par projet (SOURCES PYTHON, Scripts, Mysql)
>
> Un dossier avec la documentation technique et d’utilisation (Dans un README.md avec présentation de l’équipe et leur rôle)
>
> Un dossier contenant les scénarii de tests et les scripts
>
> Un dossier contenant la documentation technique (contenant l’architecture, les éléments changés selon le cahier des charges fournis, la description des serveurs virtuels python)

## 2. Mise en place

1. setup GitHub
2. Création de branches par dev
3. Création d'autres branches (dev etc..)
4. Définition des besoins clients
5. Définition de l'env de travail (bibliotheque, technologies, etc.. )
6. Création d'un backlog (tout ce qui est nécessaire a réaliser le projet)
7. Relevé des paramètres (classes, methodes)
8. Définir les étapes de devs
9. Assignation des taches (sprint backlog)
