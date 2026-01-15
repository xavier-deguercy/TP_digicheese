# Règles métier — DIGICHEESE (TP7)

## 1) Rôles et responsabilités (règles d’accès)
Le système est centré sur 3 rôles (cumulables) :
- **Admin** : gère users + référentiels (communes, objets, conditionnements, poids, poids vignette).
- **Opérateur colis** : gère (cible CDC) clients, commandes, mailing, stats, impression (dans TP7 : clients optionnel).
- **Opérateur stock** : gestion des stocks (hors scope TP7).

> Dans le TP7, le périmètre implémenté est prioritairement “Admin” (CRUD) + “Clients” en option.

---

## 2) Référentiels et cohérence des données (règles de gestion)
### 2.1 Communes / Départements
- Une **commune** appartient à un **département**.
- Une commune peut être utilisée comme référence d’adresse d’un client.
- Suppression d’une commune : à sécuriser (interdite si utilisée par un client, ou suppression logique).

### 2.2 Clients (si option activée)
- Un client peut avoir : civilité/genre, nom/prénom, adresses, téléphone, email, commune de rattachement.
- Champs obligatoires (minimum recommandé) : nom + prénom OU nom (selon choix), commune (si modélisée), email/téléphone (au moins 1 moyen de contact).

### 2.3 Objets (goodies) et conditionnements
- Un **objet** (goodie) est un article disponible à la commande.
- Un **conditionnement** représente un emballage/format possible.
- La relation objet–conditionnement peut être portée par une table de relation (ex : `t_rel_cond`) avec des quantités min/max.

### 2.4 Poids / Poids-vignette
- Les tables de poids et poids-vignette servent à porter des seuils et des coûts associés (d’après les modèles fournis).
- Les valeurs monétaires doivent rester en type décimal (éviter float pour l’argent).

---

## 3) Configuration “standard européenne” (règles d’affichage / conventions)
- Timezone : `Europe/Paris`
- Format date (côté UI future) : `JJ/MM/AAAA`
- Monnaie : `EUR`
- Stockage en base/API : formats standards (ISO pour date si exposée), décimaux pour prix.
