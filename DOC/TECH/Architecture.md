# Architecture — DIGICHEESE (TP7)

## 1) Objectif
Décrire l’architecture retenue pour livrer une API :
- maintenable
- testable
- documentée (Swagger)
- compatible avec une IHM future (hors scope TP7)

---

## 2) Architecture logique (couches)
### routes/
- Expose les endpoints REST (FastAPI)
- Convertit request -> appels service
- Gère codes HTTP + schémas de réponse

### services/
- Contient les règles métiers applicatives
- Orchestration : validations métier, enchaînements, transactions simples

### repositories/
- Accès aux données (CRUD DB)
- Isole la persistance (SQLModel / sessions)

### models/
- Modèles SQLModel (tables)
- Schémas de données (si séparés)

### conf/
- Gestion configuration (.env, variables, DB URL, timezone)
- Paramètres runtime

### utils/
- Helpers (pagination, erreurs standardisées, logs)

---

## 3) Contrat d’API (préparation IHM)
- Versionnement : `/api/v1/...`
- Ressources : `communes`, `objets`, `conditionnements`, `poids`, `poids-vignettes`
- (option) `clients`
- Swagger : exemples request/response pour simuler l’IHM

---

## 4) Gestion erreurs (convention)
- 400 : validation / payload invalide
- 404 : ressource inexistante
- 409 : conflit (si besoin)
- 500 : erreurs internes (non exposer de détails sensibles)

---

## 5) Tests (stratégie minimale)
- Tests “smoke” : `/health`
- Tests CRUD : nominal + erreur (ex: 404 sur id inconnu)
- Outillage : pytest + httpx

---

## 6) Sécurité / RGPD / monitoring (TP7)
- Validation stricte des entrées
- Journalisation contrôlée (pas de données sensibles en clair)
- KPIs à définir (temps réponse, taux erreurs) + alertes (documentées)
