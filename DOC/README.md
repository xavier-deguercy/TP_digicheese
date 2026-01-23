Doc/README.md
# Documentation — DIGICHEESE (TP7)

## Objectif de cette documentation
Ce dossier centralise la documentation du projet **DIGICHEESE** réalisé dans le cadre du **TP7 Diginamic** :
- formaliser le **besoin** (fonctionnel)
- cadrer le **périmètre** (IN/OUT) et les **règles métier**
- définir un **backlog** exécutable en 5 jours
- documenter l’**architecture** et l’**environnement d’exécution**
- fournir un **guide d’utilisation** (sans IHM, via Swagger)

> Rappel TP7 : API Backend Python + base MySQL, Swagger pour simuler le front, tests (pytest, branches (test/dev/prod/master + 1 branche par dev).  
> Sources : PROJETTP7_API_WEB_2026_Data.pdf ; consignes_projet_dev_2026.pdf ; MiniCahierDesChargesFromagerieDigiCheese.pdf.

---

## Index

### 1) Documentation fonctionnelle (`DOC/FONC/`)
- [Contexte & objectifs](./FONC/Contexte_Objectifs.md)
- [Périmètre IN/OUT (IHM hors scope)](./FONC/Perimetre_In_Out.md)
- [Règles métier](./FONC/Regles_Metier.md)
- [Parcours utilisateur (via Swagger)](./FONC/Parcours_Utilisateur.md)
- [Backlog (épics, US, priorités, DoD)](./FONC/Backlog.md)
- [Arborescence & organisation documentaire](./FONC/creation_arbo.md)

### 2) Documentation technique (`DOC/TECH/`)
- [Architecture (couches, modules, conventions)](./TECH/Architecture.md)
- [Changements vs Cahier des Charges (TP7)](./TECH/Changements_CDC.md)
- [Serveurs virtuels Python / environnement (venv, Docker, config)](./TECH/Serveurs_Virtuels_Python.md)

### 3) Documentation d’utilisation (`DOC/UTILISATION/`)
- [Guide utilisateur (tests via Swagger)](./UTILISATION/Guide_Utilisateur.md)
- [Guide développeur (setup, branches, qualité, tests)](./UTILISATION/Guide_dev.md)
- [FAQ](./UTILISATION/FAQ.md)

---

## Équipe & rôles
> Objectif : clarifier “qui a porté quoi” sur le TP7.  
> Lecture : les responsabilités ci-dessous reflètent la **dominante** par membre ; **tout le monde a contribué aux scripts** (seed, utilitaires, etc.).

### Convention de branches (choix d’équipe)
- Format retenu : `prenom_sujet` (underscore), simple à lire et à suivre
- Exemples : `xavier_test`, `stanislas_env`, `eman_api`, `titouan_db`

| Membre | Rôle projet (dominante) | Responsabilités principales (dominantes) | Branche de dev |
|-------|--------------------------|------------------------------------------|--------|
| Stanislas DELANNOY | Lead / Environnement & intégration | Mise en place de l’environnement (setup, conventions repo), cadrage d’intégration et support sur la structuration (merge / cohérence globale) | `stanislas_dev` |
| Imen KHAMMASSI | Développement | Développement d’API (endpoints + logique associée), participation aux éléments base de données et scripts nécessaires au fonctionnement | `eman_dev` |
| Thi Thu Hien NGUYEN | Développement | Développement (API + base de données) et scripts (initialisation, utilitaires) | `titouan_dev` |
| Xavier DEGUERCY | Fonctionnel / coordination | Contribution fonctionnelle (périmètre, règles, parcours Swagger), coordination et support à la structuration ; contribution scripts et validation des scénarios d’usage | `xavier_dev` |


---

## Point d’entrée
- **Fonctionnel** : commencer par `DOC/FONC/Contexte_Objectifs.md`
- **Technique** : `DOC/TECH/Serveurs_Virtuels_Python.md`
- **Utilisation** : `DOC/UTILISATION/Guide_Utilisateur.md`

---