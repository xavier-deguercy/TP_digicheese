

# A) UC — Système de gestion des colis (ancien système Access 2000)

## UC01 — Saisir une demande à partir du courrier *(UC_Saisie)*

* **Objectif :** saisir dans l’application Access une demande reçue par courrier (points + choix goodies + chèque) et créer une commande “en cours”.
* **Acteurs :**

  * Principal : **Opérateur colis** (interne SI)
  * Déclencheur métier : **Client final** (externe)
* **Déclencheur :** courrier reçu à traiter.
* **Préconditions :** courrier exploitable (choix + coordonnées minimales).
* **Scénario nominal :**

  1. L’opérateur lit le courrier et récupère les informations.
  2. Il identifie le client (recherche).
  3. Il saisit la demande dans Access.
  4. Le système crée/enregistre la commande “en cours”.
* **Variantes :**

  * **UC_PapierLibre** : demande formulée sur papier libre (sans collecteur).
* **Postconditions :** commande créée et liée à un client (existant ou à créer/mettre à jour).

---

## UC02 — Gérer fiche client (créer / mettre à jour) *(UC_Client)*

* **Objectif :** créer ou mettre à jour la fiche client (adresse, contact, options) pour permettre expédition et communication.
* **Acteur :** **Opérateur colis**.
* **Déclencheur :** client introuvable ou informations à corriger lors de la saisie/gestion commande.
* **Préconditions :** accès au module “clients”.
* **Scénario nominal :**

  1. Recherche du client.
  2. Création ou mise à jour de la fiche.
  3. Saisie de l’adresse (CP → ville) et informations utiles.
  4. Validation et enregistrement.
* **Postconditions :** fiche client à jour.

---

## UC03 — Enregistrer / mettre à jour la commande *(UC_Commande)*

* **Objectif :** piloter une commande (contenu, commentaires, statut) tout au long de son traitement.
* **Acteur :** **Opérateur colis**.
* **Déclencheur :** commande créée (UC01) ou avancement (préparation/expédition).
* **Préconditions :** commande existante.
* **Scénario nominal :**

  1. L’opérateur ouvre la commande.
  2. Il met à jour contenu / informations / statut.
  3. Il consulte les commandes en cours / passées du client si besoin.
  4. Le système enregistre les modifications.
* **Postconditions :** commande à jour.

---

## UC04 — Calculer conditionnement & choisir emballage *(UC_Cond)*

* **Objectif :** déterminer l’emballage compatible à partir du contenu de commande (règles min/max, cas multi-lignes).
* **Acteur :** **Opérateur colis**.
* **Déclencheur :** commande prête à être préparée.
* **Préconditions :** commande complète ; référentiel emballages/poids disponible.
* **Scénario nominal :**

  1. L’opérateur lance le calcul de conditionnement.
  2. Le système choisit un emballage compatible.
  3. Le système calcule le poids total (emballage + contenu) si nécessaire pour la suite.
* **Postconditions :** emballage retenu + données de poids prêtes pour l’affranchissement.

---

## UC05 — Calculer affranchissement (poids -> tarif) *(UC_Aff)*

* **Objectif :** calculer le coût d’affranchissement à partir du poids total et des tarifs.
* **Acteurs :**

  * Principal : **Opérateur colis**
  * Secondaire : **La Poste** (source des tarifs)
* **Déclencheur :** conditionnement réalisé (UC04) / poids total disponible.
* **Préconditions :** tarifs postaux à jour ; règles de calcul disponibles.
* **Scénario nominal :**

  1. Le système applique la grille tarifaire au poids total.
  2. Le coût d’affranchissement est calculé et enregistré sur la commande.
* **Postconditions :** affranchissement calculé et enregistré.

---

## UC06 — Expédier le colis *(UC_Exp)*

* **Objectif :** valider l’expédition via La Poste et mettre à jour l’état de la commande.
* **Acteurs :**

  * Principal : **Opérateur colis**
  * Secondaire : **La Poste**
* **Déclencheur :** colis préparé (UC04 + UC05 réalisés).
* **Préconditions :** conditionnement + affranchissement disponibles.
* **Scénario nominal :**

  1. L’opérateur valide l’expédition.
  2. Le système enregistre l’expédition (statut, date, etc.).
* **Variante :**

  * **UC_Suivi** : envoi en lettre suivie (saisie n° de suivi).
* **Postconditions :** commande expédiée / statut mis à jour.

---

## UC07 — Tracer le traitement (historisation mouvements) *(UC_Traca)*

* **Objectif :** historiser les événements de traitement (mouvements/statuts colis) pour traçabilité.
* **Acteur :** **Opérateur colis** (déclenche indirectement par ses actions).
* **Déclencheur :** création/avancement/expédition d’une commande.
* **Préconditions :** commande existante.
* **Scénario nominal :**

  1. Lors d’une action significative (saisie, préparation, expédition), le système enregistre un événement d’historisation.
* **Postconditions :** traçabilité disponible sur la commande.

---

## UC08 — Communiquer avec le client (mailing / email) *(UC_Comm)*

* **Objectif :** produire une communication client associée à une commande ou une liste (mailing fichier texte / email personnalisé).
* **Acteur :** **Opérateur colis**.
* **Préconditions :** client connu ; email disponible si email.
* **Scénario nominal :**

  1. L’opérateur sélectionne la cible.
  2. Il choisit mailing ou email personnalisé.
  3. Le système génère le support.
* **Postconditions :** support produit (et action potentiellement tracée selon l’existant).

---

### Variantes (use cases optionnels rattachés à l’exploitation)

#### UC09 — Variante : demande sur papier libre (sans collecteur) *(UC_PapierLibre)*

* **Objectif :** permettre la saisie d’une demande quand le client ne fournit pas le collecteur standard.
* **Acteur :** **Opérateur colis**.
* **Déclencheur :** courrier contenant points + choix sur papier libre.
* **Postconditions :** demande saisie comme UC01.

#### UC10 — Variante : envoi en lettre suivie (saisie n° de suivi) *(UC_Suivi)*

* **Objectif :** associer un numéro de suivi au colis expédié (dans l’existant, souvent via commentaire).
* **Acteur :** **Opérateur colis**.
* **Déclencheur :** expédition en “lettre suivie”.
* **Postconditions :** numéro de suivi enregistré.

