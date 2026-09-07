# Regles metier - DIGICHEESE Wave 2

## 1) Roles et droits (cible Wave 2)
- Admin: CRUD complet sur toutes les ressources wave 2.
- OP-COLIS: travail principal sur commandes et details.
- OP-STOCK: travail principal sur stock, stock_ligne, mise_a_jour, boutique.

Principe:
- Toute route metier doit explicitement definir ses roles autorises.

---

## 2) Regles metier Commandes

### 2.1 Commande
- Une commande reference un client existant.
- Le conditionnement peut etre obligatoire ou optionnel selon la regle retenue dans l'API.
- `bArchive` indique l'etat actif/archive de la commande.
- `nbColis` doit rester coherent avec les details de commande.

### 2.2 Detail commande
- Un detail commande reference une commande existante et un objet existant.
- `quantite` est strictement positive.
- Un detail invalide ne doit pas casser la coherence globale de la commande.

### 2.3 Prix
- Un objet ne peut avoir qu'un prix actif (contrainte unique 1-1 par objet).

### 2.4 Relation conditionnement
- `rel_cond` relie objet et conditionnement avec une quantite associee.
- Les deux FK doivent exister au moment de l'insertion.

---

## 3) Regles metier Stock

### 3.1 Stock / Stock ligne
- Une ligne de stock reference un stock et un objet.
- `quantiteStock` doit etre un entier valide.
- `dateDeb/dateFin` doivent etre coherentes quand presentes.

### 3.2 Mise a jour stock
- Toute mise a jour doit pointer un objet existant.
- La date de mouvement est obligatoire.

### 3.3 Boutique
- Une sortie boutique reference un objet.
- La quantite doit etre coherente avec les regles de gestion definies par l'equipe.

---

## 4) Integrite et qualite de donnees
- Respect des FK obligatoires.
- Validation stricte des payloads.
- Erreurs explicites (`400/403/404`) en cas de donnees invalides ou interdites.
- Tracabilite des regles importantes dans la documentation et les tests.
