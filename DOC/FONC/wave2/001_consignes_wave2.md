# Diginamic - Consignes Wave 2

## 1) Objectif
Cette wave 2 prolonge une base deja en production.
Le but est de livrer les CRUD metier restants sans rupture API.

Priorites:
- commandes d'abord
- compatibilite prod stricte
- execution en 2 sprints

---

## 2) Organisation de travail
- Travail en equipe sur board unique (Jira ou GitHub Projects).
- Decoupage en epics, user stories, taches.
- Chaque tache doit avoir un responsable et un statut.
- Daily courte avec avancement, blocages, priorite du jour.

Colonnes recommandees:
- Backlog
- Ready
- In Progress
- Code Review
- Done

---

## 3) Livrables minimum Wave 2
- `DOC/FONC/Backlog_wave2.md`
- `DOC/FONC/Contexte_Objectifs_wave2.md`
- `DOC/FONC/Perimetre_In_Out_wave2.md`
- `DOC/FONC/Regles_Metier_wave2.md`
- `DOC/FONC/Parcours_Utilisateur_wave2.md`
- Preuves de tests et non-regression
- Documentation Swagger mise a jour

---

## 4) Definition of Done (rappel)
Une story est terminee si:
- CRUD implemente avec validations
- statuts HTTP attendus (`200/201/400/403/404`)
- tests nominal + erreur + autorisation
- Swagger a jour
- documentation impactee a jour

---

## 5) Contraintes de compatibilite
- Ne pas casser les endpoints deja exposes en production.
- Ne pas imposer de refonte globale de conventions.
- Ajouter les nouvelles ressources de facon additive.
- Tracer les ecarts de nomenclature dans la doc wave 2.
