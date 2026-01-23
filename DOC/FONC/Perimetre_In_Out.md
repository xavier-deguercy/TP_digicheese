# Périmètre IN/OUT — DIGICHEESE (TP7)

## Principe de cadrage
Le cahier des charges décrit un **site interne** avec une IHM.  
Dans le cadre du **TP7**, on livre **uniquement le backend API** et on **simule le front via Swagger**.

---

## 1) IN (périmètre réalisé dans le TP7)

### 1.1 API Backend (obligatoire)
- API **Python (FastAPI)** exposant des endpoints REST.
- Documentation via **Swagger/OpenAPI**.
- Base de données **MySQL**.
- Tests automatisés (**pytest** ou **unittest**).

### 1.2 Fonctionnalités “Admin” (obligatoire TP7)
CRUD (ajout / modification / suppression / consultation) sur :
- utilisateurs (si retenu)
- **communes**
- **objets (articles / goodies)**
- **conditionnements**
- **poids**
- **poids vignette**

> Note : ces éléments sont explicitement listés dans la description “Admin” du mini CDC.

### 1.3 Fonctionnalités “OP-colis” (option TP7)
- **CRUD Clients** (gestion des clients) — option explicitement mentionnée dans la fiche TP7.

---

## 2) OUT (hors scope TP7 – conservé en “évolutions”)
- **IHM / Front web** (interfaces utilisateur).
- Gestion complète des commandes (CRUD + calcul), mailing, stats, impression papier, historisation colis, etc.
- Module complet “OP-stocks” (gestion des stocks).
- Fonction “mise à jour annuelle des stocks”, impressions.

---

## 3) Hypothèses & décisions de cadrage
- L’IHM est **hors scope** mais tous les “points d’entrée” nécessaires à une IHM future sont préparés :
  - endpoints stables
  - schémas (request/response) clairs
  - exemples dans Swagger
- Les règles de sécurité / RGPD / monitoring seront traitées à un niveau proportionné au TP7 (documentation + mesures simples).

---

## 4) Liste des points d’entrée (préparation IHM)

**Base URL : `/`** (routes à la racine — pas de préfixe global `/api/v1`).

> Note : dans Swagger, certains endpoints sont regroupés sous des tags « Admin - … ».
> Il s’agit d’une **classification documentaire** ; ce n’est **pas** un segment d’URL.

### Référentiels / back-office (Admin)
- Objets : `GET /objets/` · `POST /objets/` · `GET /objets/{objet_id}` · `PATCH /objets/{objet_id}` · `DELETE /objets/{objet_id}`
- Les autres référentiels suivent le **même pattern CRUD** (chemins exacts visibles dans Swagger) :
  - conditionnements
  - poids
  - poidsv
  - communes
  - adresses
  - rôles
  - utilisateurs
  - clients (si exposé)

### Technique
- `/health` (disponibilité du service)
- `/version` (version applicative)

