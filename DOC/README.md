# Documentation — DIGICHEESE (TP7)

## Objectif de cette documentation
Ce dossier centralise la documentation du projet **DIGICHEESE** réalisé dans le cadre du **TP7 Diginamic** :
- formaliser le **besoin** (fonctionnel)
- cadrer le **périmètre** (IN/OUT) et les **règles métier**
- définir un **backlog** exécutable en 5 jours
- documenter l’**architecture** et l’**environnement d’exécution**
- fournir un **guide d’utilisation** (sans IHM, via Swagger)

> Rappel TP7 : API Backend Python + base MySQL, Swagger pour simuler le front, tests (pytest/unittest), branches (test/dev/prod/master + 1 branche par dev).  
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

## Équipe & rôles (à compléter)
> Objectif : clarifier “qui fait quoi” (attendu TP7).

| Membre | Rôle projet | Responsabilités principales | Branche |
|-------|-------------|----------------------------|--------|
| [Nom1] | Lead / Intégration | conventions, merges, CI locale | feature/nom1 |
| [Nom2] | Dev API | endpoints admin / clients | feature/nom2 |
| [Nom3] | QA / Doc | tests, doc, checklist livrables | feature/nom3 |

---

## Point d’entrée
- **Fonctionnel** : commencer par `DOC/FONC/Contexte_Objectifs.md`
- **Technique** : `DOC/TECH/Serveurs_Virtuels_Python.md`
- **Utilisation** : `DOC/UTILISATION/Guide_Utilisateur.md`
