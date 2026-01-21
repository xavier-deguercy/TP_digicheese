# Parcours utilisateur (sans IHM) — validation via Swagger

## Principe
Dans le cadre du TP7, l’IHM n’est pas développée.  
Les parcours sont donc **validés via Swagger UI** (OpenAPI), qui simule les appels du front.

- Swagger : `http://127.0.0.1:8000/docs`

> Remarque importante : certains endpoints sont regroupés sous des tags Swagger (ex. « Admin - Objets »).
> Ce sont des **tags de documentation** ; les **URLs** restent à la racine (ex. `/objets/`).

---

## Parcours 1 — Admin : gérer un référentiel (CRUD “Objets”)

### Acteur
Administrateur

### Préconditions
- API en cours d’exécution
- Base MySQL accessible
- Endpoints Objets visibles dans Swagger :
  - `GET /objets/`
  - `POST /objets/`
  - `GET /objets/{objet_id}`
  - `PATCH /objets/{objet_id}`
  - `DELETE /objets/{objet_id}`

### Scénario nominal (démo “phare”)
1. **Lister** les objets : `GET /objets/`  
2. **Créer** un objet : `POST /objets/` (payload ci-dessous)  
3. **Relire** l’objet créé : `GET /objets/{objet_id}`  
4. **Mettre à jour partiellement** : `PATCH /objets/{objet_id}` (ex. points + indisponible)  
5. **Supprimer** : `DELETE /objets/{objet_id}`  
6. **Contrôle post-suppression** : relancer `GET /objets/{objet_id}` → attendu : **404**

### Exemples de payload (Swagger)
**POST /objets/**
```json
{
  "nom_obj": "Mug DigiCheese",
  "taille_obj": "Standard",
  "prix_obj": 9.90,
  "poids_obj": 0.25,
  "indisp_obj": false,
  "points_obj": 120
}
```

**PATCH /objets/{objet_id}**
```json
{
  "points_obj": 150,
  "indisp_obj": true
}
```

### Critères de validation (parcours)
- Le parcours est exécutable “bout-à-bout” via Swagger.
- Les codes HTTP attendus sont cohérents (200/201/204, 404 en cas d’ID inexistant).
- Les schémas request/response sont exposés (Swagger) et exploitables par un front ultérieur.

---

## Parcours optionnels (si exposés dans Swagger)
Selon l’avancement, d’autres ressources peuvent être démontrées avec le **même pattern CRUD** (référentiels : conditionnements, poids, communes, adresses, utilisateurs, rôles…).

> Pour la soutenance, la démo se concentre sur **Objets** (parcours 1) afin de rester fiable et maîtrisée.
