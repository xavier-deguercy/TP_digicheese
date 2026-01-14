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

## Objectifs pédagogiques
- Modéliser un besoin métier (acteurs, cas d’utilisation, scénarios)
- Produire des diagrammes UML (use case, séquence, activité, classes / ERD selon sujet)
- Structurer un projet comme un vrai dépôt de développement :
  - séparation des responsabilités (routes / services / repositories)
  - configuration
  - tests automatisés de base

## Périmètre (à adapter au sujet exact du TP)
- Modélisation et conception autour de processus métier DIGICHEESE
- Réalisation des livrables UML
- Mise en place d’un squelette applicatif Python (éventuellement API)

## Hors périmètre (exemples)
- Application complète industrialisée
- Gestion complète de la sécurité (auth, droits, etc.)
- Déploiement production

## Arborescence
- `src/` : code source
  - `routes/` : endpoints / contrôleurs
  - `services/` : logique métier
  - `repositories/` : accès données
  - `models/` : modèles et schémas
  - `conf/` : configuration
  - `utils/` : utilitaires
- `tests/` : tests automatisés
- `UML/` : livrables UML (diagrammes + exports)
- `docs/` : documents de cadrage (scénarios, règles de gestion, etc.)
- `scripts/` : scripts utilitaires (initialisation, seed, etc.)

## Pré-requis
- Python 3.x
- Git

## Installation (Windows / Git Bash ou PowerShell)
Créer l’environnement virtuel :
```bash
python -m venv .venv
