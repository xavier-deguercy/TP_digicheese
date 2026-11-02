# Backlog Wave 2 - DIGICHEESE

## 1) Contexte Wave 2
La Wave 1 est en production avec un socle API stable et les CRUD Admin principaux deja livres.
La Wave 2 etend ce socle sans rupture de service pour couvrir les CRUD metier restants.

Objectif principal:
- Priorite "commandes d'abord", puis dependances directes et modules stock.
- Livraison additive, sans casser les endpoints deja exposes en production.
- Planification en 2 sprints.

---

## 2) Perimetre

### Perimetre IN
- Commande (`commande`)
- Detail de commande (`detail_commande`)
- Prix (`prix`)
- Relation objet-conditionnement (`rel_cond`)
- Liaison utilisateur-role (`utilisateur_role`)
- Stock (`stock`)
- Ligne de stock (`stock_ligne`)
- Mise a jour de stock (`mise_a_jour`)
- Sortie boutique (`boutique`)

### Perimetre OUT
- Refonte API globale.
- Changement de conventions de routes deja en production.
- Migration cassante des structures existantes.
- Changement de strategie d'authentification globale.

---

## 3) Compatibilite prod stricte

Regles de compatibilite:
- Conserver les conventions actuelles de routes (pas de prefixe global nouveau).
- Conserver le modele d'authentification et les roles existants, ajouter seulement ce qui manque.
- Ajouter les nouvelles ressources de facon additive.
- Interdire tout renommage destructif des ressources deja en prod.

US transverse de coherence:
- `US-W2-C2 Normalisation nomenclature`: documenter et appliquer une strategie de mapping entre nomenclature existante (`t_*`, snake_case courant) et modele database Wave 2 (`commande`, `detail_commande`, etc.), sans rupture publique.

---

## 4) DoD commun Wave 2
Une User Story est "Done" si tous les points ci-dessous sont valides:
- Endpoint CRUD implemente (GET collection, GET item, POST, PATCH, DELETE).
- Validations de payload appliquees et erreurs geres.
- Statuts HTTP conformes: `200`, `201`, `400`, `403`, `404`.
- Persistance DB fonctionnelle avec contraintes FK respectees.
- Swagger/OpenAPI a jour pour les endpoints et schemas.
- Tests presents: nominal + erreur + autorisation.
- Documentation impactee mise a jour.

---

## 5) Public APIs / interfaces ciblees

Ressources API planifiees:
- `/commandes`
- `/details-commandes`
- `/prix`
- `/relations-conditionnement`
- `/stocks`
- `/stock-lignes`
- `/mises-a-jour`
- `/boutiques`
- `/utilisateur-roles`

Convention CRUD par ressource:
- `GET /ressource`
- `GET /ressource/{id}`
- `POST /ressource`
- `PATCH /ressource/{id}`
- `DELETE /ressource/{id}`

Regles de roles (cible backlog):
- Admin: CRUD complet sur toutes les ressources Wave 2.
- OP-COLIS: CRUD sur commandes/details + lecture relation conditionnement/prix.
- OP-STOCK: CRUD sur stock, stock_ligne, mise_a_jour, boutique + lecture commandes.

---

## 6) Dependances explicites
- `commande` depend de `client` + `conditionnement`.
- `detail_commande` depend de `commande` + `objet`.
- `prix` depend de `objet`.
- `rel_cond` depend de `objet` + `conditionnement`.
- `stock_ligne` depend de `stock` + `objet`.
- `mise_a_jour` depend de `objet`.
- `boutique` depend de `objet`.
- `utilisateur_role` depend de `utilisateur` + `role`.

Ordre de livraison recommande:
1. `commande`
2. `detail_commande`
3. `prix`
4. `rel_cond`
5. `utilisateur_role`
6. `stock`
7. `stock_ligne`
8. `mise_a_jour`
9. `boutique`

---

## 7) Epics / User Stories

### [~] EPIC W2-A - Commandes

`US-W2-A1` CRUD Commande

Statut MVP-01 : `ACCEPTE_AVEC_RESERVES` le 2026-09-07. La reserve sur la suppression d'une commande contenant des lignes sera traitee avec `US-W2-A2`.

- Taches:
- [x] Model + schema + repository + service + router `commande`.
- [x] Validations: FK client, FK conditionnement optionnelle, type/date, `bArchive`.
- [x] Swagger examples pour create/update/get.
- Criteres d'acceptation:
1. CRUD complet operationnel.
2. Erreurs `400/404` sur payload/FK invalides.
3. Regles role OP-COLIS et Admin appliquees.

`US-W2-A2` CRUD Detail commande

Statut MVP-02 : `DEVELOPPE_ET_VERIFIE — ACCEPTATION_METIER_A_CONFIRMER`.

Regle validee : une seule ligne par couple commande/objet ; doublon rejete avec `409` et contrainte unique en base.

- Taches:
- [x] Implementer `detail_commande` avec FK `idCommande` et `idObjet`.
- [x] Validation de quantite et coherence FK.
- [x] Endpoint liste par commande.
- Criteres d'acceptation:
1. CRUD complet operationnel.
2. Recuperation des details d'une commande possible.
3. Erreurs `404` sur commande/objet inexistants.

`US-W2-A3` Regles archive et `nbColis`
- Taches:
- [x] Definir la saisie et le controle `nbColis` pour le MVP.
- [x] Definir regles d'archivage (`bArchive`) et mise a jour securisee.
- [x] Ajouter tests de flux "creation + archive".
- Criteres d'acceptation:
1. `nbColis` coherent avec les details.
2. Archivage protege et traçable.

`US-W2-A4` CRUD Relation conditionnement (`rel_cond`)
- Taches:
- [ ] Implementer CRUD `rel_cond` (objet-conditionnement + quantiteObjet).
- [ ] Validations FK objet/conditionnement.
- [ ] Exposer endpoint de recherche par objet et par conditionnement.
- Criteres d'acceptation:
1. Relation consultable et modifiable sans incoherence FK.
2. Erreurs `400/404` sur references invalides.

`US-W2-A5` CRUD Prix
- Taches:
- [ ] Implementer CRUD `prix`.
- [ ] Garantir contrainte 1-1 sur `idObjet` (unique).
- [ ] Ajouter endpoints de consultation "prix par objet".
- Criteres d'acceptation:
1. Un seul prix par objet.
2. Erreur `400` si tentative de doublon.

### [ ] EPIC W2-B - Stock

`US-W2-B1` CRUD Stock
- Taches:
- [ ] Implementer entite `stock`.
- [ ] CRUD complet avec regles de libelle.
- [ ] Swagger + tests.
- Criteres d'acceptation:
1. CRUD stable.
2. Controle role OP-STOCK/Admin.

`US-W2-B2` CRUD Stock ligne
- Taches:
- [ ] Implementer `stock_ligne` (FK stock + objet).
- [ ] Validation dates `dateDeb/dateFin` et quantite.
- [ ] Endpoint de consultation par stock.
- Criteres d'acceptation:
1. Insertion et mise a jour coherentes.
2. Erreurs `400` si intervalle date invalide.

`US-W2-B3` CRUD Mise a jour stock (`mise_a_jour`)
- Taches:
- [ ] Implementer journal de mise a jour stock par objet.
- [ ] Validation quantite/date.
- [ ] Endpoint historique par objet.
- Criteres d'acceptation:
1. Historique consultable.
2. FK objet respectee.

`US-W2-B4` CRUD Boutique
- Taches:
- [ ] Implementer `boutique` (sortie/quantite/date par objet).
- [ ] Validation quantite/date.
- [ ] Endpoint de consultation par objet et periode.
- Criteres d'acceptation:
1. CRUD complet operationnel.
2. Integrable aux flux stock.

### [ ] EPIC W2-C - Securite et coherence

`US-W2-C1` CRUD Utilisateur-role
- Taches:
- [ ] Implementer `utilisateur_role` (N-N).
- [ ] Verifier coherence role principal/existant.
- [ ] Ajouter controles d'autorisation.
- Criteres d'acceptation:
1. Affectation de roles multi-profils possible.
2. Pas de doublon utilisateur-role.

`US-W2-C2` Normalisation nomenclature
- Taches:
- [ ] Produire une matrice de mapping "modele existant vs database Wave 2".
- [ ] Fixer conventions de nommage internes sans rupture API.
- [ ] Ajouter notes de compatibilite dans documentation technique.
- Criteres d'acceptation:
1. Nommage coherent et documente.
2. Aucun endpoint existant casse.

### [ ] EPIC W2-D - Qualite, non-regression, KPI

`US-W2-D1` Tests Wave 2
- Taches:
- [ ] Tests unitaires service/repository pour chaque nouvelle entite.
- [ ] Tests API CRUD par ressource (nominal + erreur).
- [ ] Tests d'autorisation par role.
- Criteres d'acceptation:
1. Tous les nouveaux modules testes.
2. Statuts HTTP attendus verifies.

`US-W2-D2` Tests d'integration metier
- Taches:
- [ ] Creation commande avec details.
- [ ] Calcul/controle `nbColis`.
- [ ] Archivage commande.
- [ ] Mise a jour stock suite operations.
- Criteres d'acceptation:
1. Flux de bout en bout stable.
2. Donnees coherentes entre tables.

`US-W2-D3` Non-regression prod existante
- Taches:
- [ ] Relancer tests CRUD deja en prod: `utilisateurs`, `commune`, `objet`, `conditionnement`, `poids`, `poidsv`, `client`.
- [ ] Ajouter suite smoke automatique.
- Criteres d'acceptation:
1. Aucun comportement critique degrade.

`US-W2-D4` Observabilite KPI
- Taches:
- [ ] Suivre KPI par sprint: pass rate, couverture, erreurs API, latence endpoints metier.
- [ ] Consolider rapports sprint.
- Criteres d'acceptation:
1. KPI disponibles en fin de sprint.
2. Actions correctives decidees si seuils en baisse.

---

## 8) Plan 2 sprints

### Sprint 1 - Commandes et dependances directes
Objectif:
- Livrer le coeur commandes sans rupture API.

Contenu:
1. `US-W2-A1` CRUD commande
2. `US-W2-A2` CRUD detail_commande
3. `US-W2-A3` Regles archive/nbColis
4. `US-W2-A4` CRUD rel_cond
5. `US-W2-A5` CRUD prix
6. `US-W2-D1` et `US-W2-D2` (tests integration commande)
7. `US-W2-C2` demarrage matrice de nomenclature

Livrables Sprint 1:
- Endpoints commandes + details + prix + rel_cond en Swagger.
- Tests CRUD et integration commande.
- Rapport KPI sprint.

### Sprint 2 - Stock, coherence et stabilisation
Objectif:
- Couvrir le bloc stock + finaliser qualite et documentation.

Contenu:
1. `US-W2-B1` CRUD stock
2. `US-W2-B2` CRUD stock_ligne
3. `US-W2-B3` CRUD mise_a_jour
4. `US-W2-B4` CRUD boutique
5. `US-W2-C1` CRUD utilisateur_role
6. `US-W2-D3` non-regression complete
7. `US-W2-D4` observabilite KPI
8. Finalisation `US-W2-C2` (normalisation nomenclature)

Livrables Sprint 2:
- Endpoints stock + utilisateur_role en prod-ready.
- Campagne de non-regression verte.
- Documentation wave 2 finalisee.

---

## 9) Plan de test Wave 2

Couverture demandee:
- Tests unitaires service/repository pour chaque nouvelle entite.
- Tests API CRUD pour chaque ressource (nominal + erreurs).
- Tests d'integration de flux:
1. creation commande avec details
2. calcul/controle `nbColis`
3. archivage commande
4. mise a jour stock suite operations
- Tests non-regression obligatoires sur:
1. `utilisateurs`
2. `commune`
3. `objet`
4. `conditionnement`
5. `poids`
6. `poidsv`
7. `client`

KPI de suivi par sprint:
- Taux de succes tests (pass rate).
- Couverture de code.
- Taux d'erreurs API.
- Latence des endpoints metier.

---

## 10) Risques et parades
- Risque: divergence nomenclature DB/API.
- Parade: `US-W2-C2` priorisee, matrice de mapping et conventions bloquees.

- Risque: regression sur CRUD deja en prod.
- Parade: `US-W2-D3` obligatoire avant release wave 2.

- Risque: incoherences FK dans flux commande/detail/stock.
- Parade: validations service + tests integration multi-tables.

- Risque: derive de scope.
- Parade: perimetre OUT explicite et livraison en 2 sprints fermes.

---

## 11) Assumptions figees
- Langue du document: francais.
- Emplacement du fichier: `DOC/FONC/Backlog_wave2.md`.
- Horizon: 2 sprints.
- Priorite: commandes d'abord.
- Strategie de livraison: additive, sans rupture des endpoints deja en production.
