# Perimetre IN/OUT - DIGICHEESE Wave 2

## Principe de cadrage
Wave 2 etend une API deja en production.
Le perimetre est strictement additif et centre sur les CRUD metier restants.

---

## 1) IN (Wave 2)

### 1.1 Ressources metier prioritaires
- `commandes`
- `details-commandes`
- `prix`
- `relations-conditionnement`
- `utilisateur-roles`

### 1.2 Ressources stock
- `stocks`
- `stock-lignes`
- `mises-a-jour`
- `boutiques`

### 1.3 Cadre technique
- API Python (FastAPI)
- Swagger/OpenAPI
- Base MySQL
- Tests automatises (CRUD, integration, non-regression)

---

## 2) OUT (Wave 2)
- Refonte globale des conventions API.
- Front web complet.
- Migration cassante des endpoints existants.
- Changement du mode d'authentification global.

---

## 3) Regles de compatibilite
- Conserver les routes existantes telles qu'elles sont exposees.
- Ajouter les nouvelles routes sans supprimer l'existant.
- Garder les roles actuels et etendre le controle d'acces.
- Documenter les ecarts de nomenclature (modele actuel vs modele wave2).

---

## 4) Dependances fonctionnelles
- `commande` depend de `client` + `conditionnement`
- `detail_commande` depend de `commande` + `objet`
- `prix` depend de `objet`
- `rel_cond` depend de `objet` + `conditionnement`
- `stock_ligne` depend de `stock` + `objet`
- `mise_a_jour` depend de `objet`
- `boutique` depend de `objet`
