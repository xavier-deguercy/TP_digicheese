## 1) Scénario textuel — Gestion des colis (scénario nominal)

les acteurs de ce scenarion:
"Client final (externe)" 
"Opérateur colis (interne SI)" 
"La Poste (système externe)" 
"Opérateur stock (connexe)" 


### Objectif

Traiter une demande client reçue par courrier et expédier le colis via La Poste, avec traçabilité.

### Acteurs / systèmes impliqués

* **Client final** (externe) : déclenche la demande par courrier
* **Opérateur colis** (interne SI) : saisie, préparation, expédition
* **Système Access 2000** : enregistrement, calculs, historisation
* **La Poste** (externe) : transport + tarifs (et suivi si lettre suivie)

### Déclencheur

Réception d’un courrier client contenant points + choix goodies + chèque (frais de port).

### Préconditions

* Le courrier est lisible (choix + coordonnées minimales)
* Les référentiels (emballages, poids goodies, tarifs postaux) sont à jour

### Scénario nominal (Happy path)

1. L’opérateur colis ouvre le courrier et relève les informations (client, adresse, choix goodies, éléments de paiement).


2. Dans Access, il recherche le client :

   * s’il existe : il ouvre la fiche
   * sinon : il crée la fiche client.
      mise a jours de la BDD
3. L’opérateur saisit la demande et crée/complète la commande “en cours” (lignes goodies, commentaires).
    si les information et le payement sont bon, il passe a la suite
    sinon, il s'arrete et envoye une erreur
4. Il lance le calcul de conditionnement :

   * le système détermine l’emballage,
   * calcule le poids total (emballage + contenu).

5. Le système calcule l’affranchissement à partir des tarifs postaux.

6. L’opérateur prépare le colis et valide l’expédition.

7. Le système enregistre l’expédition et historise le mouvement (traçabilité).

8. La commande est mise à jour (statut “expédiée” / clôture selon règles).


### Postconditions

* Commande expédiée et tracée
* Données consultables (commande + historisation + éventuels rapports)

-