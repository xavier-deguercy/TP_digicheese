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
- Le conditionnement est optionnel a la creation et peut etre renseigne pendant la preparation.
- `bArchive` indique l'etat actif/archive de la commande. Une commande archivee reste consultable, mais doit etre desarchivee avant modification.
- L'archivage d'une commande incomplete est autorise et ne confirme pas son expedition.
- Une commande archivee ne peut pas etre supprimee. Une commande active peut etre supprimee tant qu'elle ne contient aucune ligne de detail.
- `nbColis` designe le nombre de colis physiques a expedier. Il est saisi manuellement, reste vide tant qu'il est inconnu et doit etre strictement positif lorsqu'il est renseigne.
- Toute modification du conditionnement ou des lignes de commande remet `nbColis` a vide.
- Un client ou un conditionnement reference par une commande ne peut pas etre supprime.

### 2.2 Detail commande
- Un detail commande reference une commande existante et un objet existant.
- `quantite` est strictement positive.
- Un detail invalide ne doit pas casser la coherence globale de la commande.
- Un meme objet ne peut apparaitre qu'une fois dans une commande ; un doublon est rejete avec `409`.
- Le commentaire de ligne est facultatif et n'a pas d'effet sur les calculs ou l'archivage.
- Le champ historique `Colis` est reporte hors de MVP-02.
- Un objet indisponible ne peut pas etre ajoute. Une ligne existante dont l'objet devient indisponible reste lisible et sa quantite ou son commentaire peut etre corrige.
- Les lignes d'une commande archivee sont en lecture seule jusqu'au desarchivage.
- Toute creation, modification ou suppression de ligne remet `nbColis` a vide dans la meme transaction.
- Une commande ou un objet reference par une ligne ne peut pas etre supprime.

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
