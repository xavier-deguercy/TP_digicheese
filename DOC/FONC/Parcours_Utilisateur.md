# Parcours utilisateur (sans IHM) — utilisation via Swagger

## Principe
L’IHM n’est pas développée dans le TP7.  
Les parcours sont donc validés via **Swagger UI** (OpenAPI), qui simule le front.

---

## Parcours 1 — Admin : gérer un référentiel (CRUD “Objets”)
### Acteur
Administrateur

### Préconditions
- API en cours d’exécution
- Base MySQL accessible
- Endpoint `/api/v1/admin/objets` disponible dans Swagger

### Scénario nominal
1. L’admin ouvre Swagger UI.
2. Il consulte la liste des objets (GET).
3. Il crée un nouvel objet (POST) avec les champs requis.
4. Il vérifie la présence du nouvel objet dans la liste (GET).
5. Il met à jour l’objet (PUT/PATCH).
6. Il supprime l’objet (DELETE) ou le rend indisponible (si suppression logique choisie).

### Postconditions
- Les données sont persistées en base.
- Les réponses HTTP sont cohérentes (200/201/204, 400/404…).

---

## Parcours 2 — Admin : gérer les communes (CRUD “Communes”)
Même structure que Parcours 1, appliquée à `/api/v1/admin/communes`.

---

## Parcours 3 — OP-colis (option) : créer et maintenir un client
### Acteur
Opérateur colis

### Préconditions
- Option “CRUD Clients” activée
- Endpoint `/api/v1/op-colis/clients` disponible

### Scénario nominal
1. L’opérateur ouvre Swagger UI.
2. Il crée un client (POST) avec identité + contact + adresse.
3. Il recherche le client (GET avec filtres éventuels).
4. Il met à jour les coordonnées (PUT/PATCH).
5. (option) Il supprime/désactive le client (DELETE/flag).

---

## Critères de validation (parcours)
- L’ensemble des parcours est testable “bout-à-bout” via Swagger.
- Chaque endpoint a un exemple de payload request/response (Swagger).
