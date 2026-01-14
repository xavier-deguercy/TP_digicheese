

## 1) Données à recueillir pour construire le diagramme de classes

### A. Données Client (qui reçoit le colis)

* Identifiant client (technique)
* Nom / prénom (ou raison sociale si tu veux rester extensible)
* Adresse : ligne1, ligne2, code postal, ville
* Email (optionnel mais cité dans les fonctionnalités)
* Historique : commandes passées (relation, pas un champ)

➡️ Source : “gestion des clients”, “email personnalisé”, “code postal → ville proposée”.

### B. Données Demande / Commande (dossier métier)

Il faut distinguer **Demande** (courrier reçu, brut) et **Commande** (objet suivi en SI).
Dans ton fonctionnement, tu peux simplifier : **la saisie du courrier crée directement une Commande**.
Mais si ton prof aime la traçabilité “courrier”, tu peux avoir une classe `Demande`.

Données minimales d’une **Commande** :

* Identifiant commande
* Date de création
* Statut (EN_COURS, EXPEDIEE, EN_ATTENTE…)
* Montant affranchissement (ou par colis si multi-colis)
* Commentaires / note opérateur
* Mode d’expédition : standard / lettre suivie (si tu le gardes)
* Lignes de commande (goodies + quantités)

### C. Ligne de commande (contenu)

* Quantité
* Référence goodie
* (Optionnel) points nécessaires ? → c’est plutôt côté marketing / fidélité, mais tu peux l’indiquer si c’est dans le sujet initial.

### D. Colis (si split)

Ton scénario dit : **une commande peut être splittée** → donc une commande peut avoir **1..n colis**.
Données d’un **Colis** :

* Identifiant colis
* Poids total
* Emballage choisi
* Montant affranchissement (par colis)
* Numéro de suivi (optionnel)
* Statut colis (PREPARE, DEPOSE, EXPEDIE…)

### E. Emballage (référentiel)

* Id emballage
* Libellé
* Poids de l’emballage
* Contraintes (min/max) : selon ton texte “min/max par article et cas multi-lignes”.
  Pour un diagramme de classes simple, tu peux modéliser :

  * `poidsMax` (ou `poidsMaxContenu`) + éventuellement `poidsMin`
  * ou une règle plus complexe (mais pas nécessaire au niveau débutant)

### F. Goodie / Article (référentiel)

* Id goodie
* Nom
* Poids unitaire
* (Optionnel) volume / fragilité / catégorie, si utile pour conditionnement

### G. Tarifs postaux (référentiel)

Représentation simple :

* Une **GrilleTarifaire** annuelle
* Des **TranchesTarif** (poidsMin, poidsMax, prix)

➡️ Ça suffit pour justifier le calcul `poids -> tarif`.

### H. Traçabilité / Historisation des mouvements

Tu as explicitement “historisation mouvements”.
Donc une classe :

* `MouvementCommande` ou `HistoriqueCommande`
* avec date, type de mouvement / statut, commentaire, opérateur (optionnel)

---

## 2) Proposition de modèle de classes “gestion des colis” (cœur métier)

### Classes cœur

* `Client`
* `Commande`
* `LigneCommande`
* `Colis`
* `MouvementCommande`

### Référentiels

* `Goodie`
* `Emballage`
* `GrilleTarifaire`
* `TrancheTarif`

### Associations clés

* **Client 1 — 0..*** Commande
* **Commande 1 — 1..*** LigneCommande
* **LigneCommande * — 1** Goodie
* **Commande 1 — 1..*** Colis *(si tu autorises multi-colis, sinon 0..1)*
* **Colis * — 1** Emballage
* **Commande 1 — 0..*** MouvementCommande
* **GrilleTarifaire 1 — 1..*** TrancheTarif

### Énumérations utiles

* `StatutCommande { EN_COURS, EN_ATTENTE, EXPEDIEE }`
* `ModeExpedition { STANDARD, LETTRE_SUIVIE }` (si tu le gardes)

---

## 3) Ce qu’il me manque pour figer définitivement le diagramme (et éviter d’inventer)

Tu m’as demandé “recueillir les data nécessaires”. Donc je te liste **les décisions à prendre** (tu peux répondre en 2 minutes avec des choix simples) :

1. **Commande vs Demande (courrier)** : tu veux une classe `DemandeCourrier` ou tu simplifies en “la commande représente la demande” ?
la commande représente la demande , il n'y a rien dans le systeme avan la reception du courrier
2. **Multi-colis** : tu confirmes `Commande 1..* Colis` (recommandé vu ton scénario) ?
oui
3. **Affranchissement** : tu le stockes :

   * au niveau **Colis** seulement (plus logique)
   * ou aussi au niveau **Commande** (somme des colis) ?
   au niveau **Colis** seulement
4. **Traçabilité** : tu veux historiser :

   * uniquement les statuts de commande


---

## 4) Si tu veux, je passe directement au diagramme de classes PlantUML

Dès que tu me dis tes choix (même juste : “1) pas de Demande, 2) oui multi-colis, 3) affranchissement au colis, 4) traçabilité commande”), je te fournis :

* le **diagramme de classes complet en PlantUML**
* avec cardinalités propres
* * une version “simple” si ton prof préfère éviter les référentiels tarifaires détaillés.
