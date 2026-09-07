# Parcours utilisateur Wave 2 (sans IHM, via Swagger)

## Principe
Les parcours Wave 2 sont valides par appels API dans Swagger:
- URL: `http://127.0.0.1:8000/docs`

Objectif:
- demontrer les flux metier commandes et stock sans front.

---

## Parcours 1 - OP-COLIS: creer et archiver une commande

### Preconditions
- API lancee
- Authentification active
- Client, objet, conditionnement existants

### Scenario nominal
1. Creer une commande (`POST /commandes`).
2. Ajouter des details (`POST /details-commandes`).
3. Verifier la commande (`GET /commandes/{id}`).
4. Verifier les details (`GET /details-commandes?commande_id=...`).
5. Archiver la commande (`PATCH /commandes/{id}` avec `bArchive=true`).

### Resultat attendu
- La commande est persistante.
- Les details sont relies a la commande.
- Le statut archive est visible en lecture.

---

## Parcours 2 - OP-STOCK: mettre a jour le stock

### Preconditions
- API lancee
- Objet existant
- Stock existant

### Scenario nominal
1. Creer une ligne de stock (`POST /stock-lignes`).
2. Ajouter un mouvement (`POST /mises-a-jour`).
3. Enregistrer une sortie boutique (`POST /boutiques`).
4. Relire les lignes et mouvements associes.

### Resultat attendu
- Les mouvements sont historises.
- Les FK stock/objet restent coherentes.

---

## Criteres de validation de parcours
- Reussite des appels nominaux avec statuts `200/201`.
- Rejet des cas invalides avec `400/404`.
- Rejet des appels non autorises avec `403`.
- Cohabitation sans regression avec les routes deja en production.
