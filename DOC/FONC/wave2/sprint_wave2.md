# Sprint plan - Wave 2 (solo)

## 1) Cadre de pilotage
- Contexte: je suis seul pour la fin de projet.
- Regle de cadence: `1 CRUD principal = 1 sprint`.
- Strategie: livraison additive (sans rupture API prod) + refactor IHM HTML/CSS en parallele.
- Duree cible: 1 sprint = 1 semaine (adaptable selon charge).

---

## 2) Definition of Done par sprint
- [ ] CRUD principal livre (GET liste, GET id, POST, PATCH, DELETE).
- [ ] Validations + statuts HTTP (`200/201/400/403/404`) operationnels.
- [ ] Swagger mis a jour.
- [ ] Tests du CRUD (nominal + erreur + autorisation).
- [ ] UI raccordee au CRUD (liste, creation, edition, suppression).
- [ ] Documentation impactee mise a jour.

---

## 3) Roadmap sprint par sprint

### [ ] Sprint 0 - Refactor IHM et architecture front (base Wave 2)
US cibles:
- `US-W2-C2` Normalisation nomenclature (partie UI/API mapping)
- `US-W2-D1` socle tests front/back minimal

CRUD principal:
- Aucun (sprint de fondation technique UI)

Taches:
- [ ] Auditer l'existant UI (`UML/digicheese-ui`) et lister ce qui est obsolete.
- [ ] Definir nouvelle architecture IHM HTML/CSS (layout, composants, pages).
- [ ] Poser une base CSS refactorisee (tokens, grille, composants, responsive).
- [ ] Poser une structure JS propre (config, api client, modules metier, utilitaires).
- [ ] Definir conventions de nommage UI pour alignement avec API wave 2.
- [ ] Documenter l'architecture IHM dans la doc fonctionnelle/technique.

Sortie attendue:
- [ ] Base front propre et reutilisable pour tous les CRUD wave 2.

---

### [ ] Sprint 1 - CRUD `commande`
US cibles:
- `US-W2-A1` CRUD Commande
- `US-W2-A3` Regles archive/nbColis (partie initiale)

CRUD principal:
- `commandes`

Taches backend:
- [ ] Model/schema/repository/service/router `commande`.
- [ ] Validation FK `client` + `conditionnement`.
- [ ] Gestion `bArchive`.
- [ ] Swagger + exemples payload.
- [ ] Tests CRUD API + autorisation.

Taches UI:
- [ ] Ecran liste commandes.
- [ ] Formulaire creation/edition commande.
- [ ] Action archivage commande.
- [ ] Etats UI: loading, erreur, vide.

Sortie attendue:
- [ ] CRUD `commandes` demonstrable de bout en bout.

---

### [ ] Sprint 2 - CRUD `detail_commande`
US cibles:
- `US-W2-A2` CRUD Detail commande
- `US-W2-A3` Regles archive/nbColis (suite)

CRUD principal:
- `details-commandes`

Taches backend:
- [ ] Model/schema/repository/service/router `detail_commande`.
- [ ] Validation FK `idCommande` + `idObjet`.
- [ ] Endpoint de consultation par commande.
- [ ] Recalcul/controle `nbColis` apres modifications de details.
- [ ] Tests CRUD + tests integration commande/details.

Taches UI:
- [ ] Ecran details d'une commande.
- [ ] Ajout/modification/suppression ligne detail.
- [ ] Affichage coherence `nbColis`.

Sortie attendue:
- [ ] Flux commande + details stable.

---

### [ ] Sprint 3 - CRUD `prix`
US cibles:
- `US-W2-A5` CRUD Prix

CRUD principal:
- `prix`

Taches backend:
- [ ] Model/schema/repository/service/router `prix`.
- [ ] Regle 1-1 prix/objet (contrainte unique).
- [ ] Endpoint prix par objet.
- [ ] Tests CRUD + contrainte de doublon.

Taches UI:
- [ ] Ecran gestion des prix.
- [ ] Recherche/filtre par objet.
- [ ] Gestion des erreurs de doublon.

Sortie attendue:
- [ ] CRUD `prix` operationnel et coherent.

---

### [ ] Sprint 4 - CRUD `rel_cond`
US cibles:
- `US-W2-A4` CRUD Relation conditionnement

CRUD principal:
- `relations-conditionnement`

Taches backend:
- [ ] Model/schema/repository/service/router `rel_cond`.
- [ ] Validation FK `objet` + `conditionnement`.
- [ ] Endpoints de recherche (par objet/par conditionnement).
- [ ] Tests CRUD + tests erreurs FK.

Taches UI:
- [ ] Ecran mapping objet-conditionnement.
- [ ] Gestion quantiteObjet.
- [ ] Filtres objet/conditionnement.

Sortie attendue:
- [ ] CRUD `rel_cond` livre et exploitable.

---

### [ ] Sprint 5 - CRUD `utilisateur_role`
US cibles:
- `US-W2-C1` CRUD Utilisateur-role

CRUD principal:
- `utilisateur-roles`

Taches backend:
- [ ] Model/schema/repository/service/router `utilisateur_role`.
- [ ] Regle anti-doublon utilisateur-role.
- [ ] Tests CRUD + tests autorisation admin.

Taches UI:
- [ ] Ecran affectation des roles utilisateur.
- [ ] Liste des affectations existantes.
- [ ] Creation/suppression d'affectation.

Sortie attendue:
- [ ] Gestion des role mappings operationnelle.

---

### [ ] Sprint 6 - CRUD `stock`
US cibles:
- `US-W2-B1` CRUD Stock

CRUD principal:
- `stocks`

Taches backend:
- [ ] Model/schema/repository/service/router `stock`.
- [ ] Regles de validation du libelle.
- [ ] Tests CRUD + droits OP-STOCK/Admin.

Taches UI:
- [ ] Ecran liste des stocks.
- [ ] Formulaire creation/edition stock.
- [ ] Actions suppression securisee.

Sortie attendue:
- [ ] CRUD `stocks` stable.

---

### [ ] Sprint 7 - CRUD `stock_ligne`
US cibles:
- `US-W2-B2` CRUD Stock ligne

CRUD principal:
- `stock-lignes`

Taches backend:
- [ ] Model/schema/repository/service/router `stock_ligne`.
- [ ] Validations FK stock/objet + dates + quantite.
- [ ] Endpoint de consultation par stock.
- [ ] Tests CRUD + erreurs de date.

Taches UI:
- [ ] Ecran lignes de stock.
- [ ] Filtres par stock et objet.
- [ ] Alertes UI sur dates invalides.

Sortie attendue:
- [ ] CRUD `stock-lignes` valide.

---

### [ ] Sprint 8 - CRUD `mise_a_jour`
US cibles:
- `US-W2-B3` CRUD Mise a jour stock

CRUD principal:
- `mises-a-jour`

Taches backend:
- [ ] Model/schema/repository/service/router `mise_a_jour`.
- [ ] Validation quantite/date + FK objet.
- [ ] Endpoint historique par objet.
- [ ] Tests CRUD + integration stock.

Taches UI:
- [ ] Ecran historique des mises a jour stock.
- [ ] Ajout d'un mouvement.
- [ ] Visualisation chronologique.

Sortie attendue:
- [ ] CRUD `mises-a-jour` operationnel.

---

### [ ] Sprint 9 - CRUD `boutique`
US cibles:
- `US-W2-B4` CRUD Boutique

CRUD principal:
- `boutiques`

Taches backend:
- [ ] Model/schema/repository/service/router `boutique`.
- [ ] Validation quantite/date + FK objet.
- [ ] Endpoint consultation par periode.
- [ ] Tests CRUD + integration stock/boutique.

Taches UI:
- [ ] Ecran sorties boutique.
- [ ] Filtre par periode.
- [ ] Raccordement avec les ecrans stock.

Sortie attendue:
- [ ] CRUD `boutiques` stable et raccorde.

---

### [ ] Sprint 10 - Stabilisation finale Wave 2
US cibles:
- `US-W2-D2` integration metier
- `US-W2-D3` non-regression prod
- `US-W2-D4` observabilite KPI
- `US-W2-C2` finalisation nomenclature

CRUD principal:
- Aucun (sprint de consolidation)

Taches:
- [ ] Campagne non-regression complete sur CRUD deja en prod.
- [ ] Revue des flux bout-en-bout commande -> stock -> boutique.
- [ ] Stabilisation UI (navigation, coherence visuelle, responsive).
- [ ] Nettoyage front (legacy, fichiers inutiles, consolidation CSS/JS).
- [ ] Consolidation KPI (pass rate, couverture, erreurs API, latence).
- [ ] Documentation finale wave 2.

Sortie attendue:
- [ ] Wave 2 prete pour livraison et suivi.

---

## 4) Vue rapide des sprints CRUD
- Sprint 1: `commandes`
- Sprint 2: `details-commandes`
- Sprint 3: `prix`
- Sprint 4: `relations-conditionnement`
- Sprint 5: `utilisateur-roles`
- Sprint 6: `stocks`
- Sprint 7: `stock-lignes`
- Sprint 8: `mises-a-jour`
- Sprint 9: `boutiques`

---

## 5) Notes de suivi solo
- [ ] Mettre a jour l'etat `[ ]/[x]` a la fin de chaque sprint.
- [ ] Taguer chaque livrable sprint dans Git.
- [ ] Ne pas ouvrir le sprint suivant tant que DoD du sprint courant n'est pas valide.
