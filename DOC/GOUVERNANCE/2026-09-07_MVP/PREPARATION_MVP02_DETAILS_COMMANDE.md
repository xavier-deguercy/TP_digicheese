---
title: DigiCheese - Preparation MVP-02 Details de commande
version: 1.3.0
date: 2026-09-07
status: developpe-et-verifie
---

# MVP-02 - Details de commande

## Mandat

Le 2026-09-07, Xavier autorise la preparation de MVP-02 « Details de commande ». Ce mandat couvre l'analyse des sources, le cadrage du lot, ses criteres d'acceptation et la preparation des decisions manquantes. Il ne couvre pas le developpement, commit, push, deploiement ou AUTO_NEXT.

Le travail reste sur la branche `xavier`, au commit de reference `278003a3d70633e3ed8127984a464e8e07f0c59f`. Le working tree existant et les livrables de MVP-01 sont preserves.

## Sources et existant verifies

- MVP-01 est `ACCEPTE_AVEC_RESERVES`.
- Le backlog `US-W2-A2` demande le CRUD Detail commande, la validation des FK commande/objet et la consultation par commande.
- Le SQL Wave 2 decrit `detail_commande` avec une cle technique, `quantite`, `Colis`, `Commentaire`, `idCommande` et `idObjet`.
- Le modele applicatif actuel utilise les tables `t_commande` et `t_objet` ainsi que des champs internes en `snake_case`.
- L'API Commandes applique deja les roles Admin et OP-COLIS, le verrouillage des commandes archivees et la remise a vide de `nb_colis` lors d'un changement de conditionnement.
- L'interface active se trouve dans `digicheese-ui` a la racine du projet.

Les sources historiques restent des preuves de conception. Les noms et exemples generiques ne remplacent pas le modele applicatif reel.

## Regles deja decidees et applicables

- Une ligne reference une commande existante et un objet existant.
- `quantite` est un entier strictement positif.
- Toute creation, modification ou suppression d'une ligne remet `nb_colis` de la commande a `null`.
- Une commande archivee et ses lignes restent consultables, mais aucune ligne ne peut etre creee, modifiee ou supprimee avant desarchivage.
- Une commande qui contient au moins une ligne ne peut pas etre supprimee.
- Une reference invalide ne doit pas laisser de modification partielle en base.
- Admin et OP-COLIS peuvent gerer les details de commande dans le perimetre actuel.

## Proposition technique a valider avant developpement

### API et persistance

- Table applicative proposee : `t_detail_commande`.
- Champs minimaux certains : `id_detail_commande`, `quantite`, `id_commande`, `id_objet`.
- Route collection proposee : `/details-commandes`.
- Operations : GET collection, GET element, POST, PATCH et DELETE.
- Filtre obligatoire a fournir : `GET /details-commandes?commande_id={id}`.
- Les ecritures de ligne et la remise a vide de `nb_colis` doivent etre realisees dans une meme transaction.
- La suppression d'un objet reference par une ligne doit renvoyer un conflit `409`.

### Interface proposee

- Depuis la page Commandes, une action « Details » ouvre les lignes de la commande selectionnee.
- La vue affiche l'objet, la quantite et les actions disponibles.
- Une commande archivee affiche ses lignes en lecture seule.
- L'ajout et la modification utilisent la liste des objets existants.
- La remise a vide de `nb_colis` est signalee apres une modification de ligne.

## Decisions metier a prendre point par point

### Q-MVP02-01 - Unicite d'un objet dans une commande

Proposition : une commande ne contient qu'une seule ligne par objet. Si l'objet est deja present, l'operateur modifie la quantite de cette ligne au lieu de creer un doublon. Une contrainte unique `(id_commande, id_objet)` protege cette regle en base.

Consequences si oui : lecture plus simple, total de quantite non ambigu, interface plus claire et doublons rejetes avec un conflit `409`.

Consequences si non : plusieurs lignes du meme objet sont autorisees ; il faudra definir leur ordre, leur distinction et la facon de les regrouper a l'affichage.

Decision : `VALIDE`. Le 2026-09-07, Xavier valide une seule ligne par objet dans une meme commande. L'API doit rejeter un doublon avec `409` et la base doit porter une contrainte unique `(id_commande, id_objet)`.

### Q-MVP02-02 - Champ Colis de la ligne

Le SQL historique contient un champ texte `Colis`, mais sa signification et son lien avec `nb_colis` ne sont pas definis. Proposition : le reporter hors de MVP-02 jusqu'au cadrage explicite de l'affectation des lignes aux colis physiques.

Decision : `VALIDE`. Le champ historique `Colis` est reporte hors de MVP-02 jusqu'au cadrage de l'affectation des lignes aux colis physiques.

### Q-MVP02-03 - Commentaire de ligne

Le SQL historique contient un commentaire facultatif. Proposition : conserver un champ `commentaire` facultatif dans MVP-02, sans effet sur les calculs ni sur l'archivage.

Decision : `VALIDE`. MVP-02 conserve un champ `commentaire` facultatif, sans effet sur les calculs ou l'archivage.

### Q-MVP02-04 - Objet marque indisponible

Proposition : interdire l'ajout d'un objet dont `indisp_obj` vaut `true`, tout en laissant lisibles les anciennes lignes qui le referencent. Une ancienne ligne devenue indisponible peut conserver une modification de quantite ou de commentaire, mais ne peut pas etre remplacee par un autre objet indisponible.

Decision : `VALIDE` pour le lot complet le 2026-09-07.

## Criteres d'acceptation prepares

- CRUD complet et documente dans OpenAPI.
- Liste filtrable par commande.
- Rejets explicites pour commande ou objet inconnu, quantite invalide, doublon selon decision et commande archivee.
- Transactions coherentes entre la ligne et la remise a vide de `nb_colis`.
- Suppression d'une commande ou d'un objet reference bloquee par `409`.
- Interface de gestion et lecture seule archivee verifiee dans un navigateur reel.
- Tests nominaux, erreurs, roles Admin/OP-COLIS, SQLite et MySQL reel.
- Non-regression de la suite existante et conservation des preuves MVP-01.

## Point exact de reprise

Les quatre decisions sont validees. Par sa reponse « Y pour le lot complet » du 2026-09-07, Xavier a autorise le developpement de bout en bout de MVP-02 dans ce perimetre. Le lot est maintenant developpe et verifie ; le point de reprise est son acceptation metier, sans AUTO_NEXT vers MVP-03.

Aucun commit, push ou deploiement n'est inclus dans cette autorisation.
