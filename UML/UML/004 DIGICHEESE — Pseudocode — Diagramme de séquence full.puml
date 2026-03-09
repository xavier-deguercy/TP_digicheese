@startuml
title DIGICHEESE — Séquence : gestion des colis (Access 2000)
autonumber
skinparam shadowing false
skinparam sequenceMessageAlign center

actor "Client final\n(externe)" as A_Client
actor "Opérateur colis\n(interne SI)" as A_OpColis

participant "IHM Access\n(Formulaires)" as UI
participant "Logique applicative\n(VBA / requêtes)" as APP
database "BD Access\n(Tables)" as DB

participant "La Poste\n(système externe)" as Poste

'===================================================================================
== Déclenchement (hors SI) ==
A_Client -> A_OpColis : Envoie un courrier\n(points + choix + chèque)
note right of A_OpColis
Réceptionne et ouvre le courrier,
relève les informations utiles
end note

'===================================================================================
== Saisie / création ==

A_OpColis -> UI : Rechercher client (nom/adresse)
activate UI
UI -> APP : rechercherClient(critères)
activate APP
APP -> DB : SELECT client WHERE critères
activate DB
DB --> APP : résultat (trouvé ? + fiche client)
deactivate DB

alt Client existant
  APP --> UI : fiche client
  UI --> A_OpColis : Afficher fiche client
else Nouveau client
  APP --> UI : client introuvable
  UI --> A_OpColis : Demander création fiche client

  A_OpColis -> UI : Créer / compléter fiche client
  UI -> APP : enregistrerFicheClient(données client)
  APP -> DB : INSERT/UPDATE Client(...)
  activate DB
  DB --> APP : idClient + OK
  deactivate DB
  APP --> UI : Confirmation création/MAJ client
  UI --> A_OpColis : Afficher fiche client créée
end

A_OpColis -> UI : Saisir demande + créer/compléter commande
UI -> APP : creerOuMajCommande(idClient, lignes)
APP -> DB : INSERT/UPDATE Commande + LignesCommande
activate DB
DB --> APP : idCommande + statut=EN_COURS
deactivate DB
APP --> UI : Confirmation enregistrement commande
UI --> A_OpColis : Commande enregistrée (id, statut)

deactivate APP
deactivate UI

'===================================================================================
== Conditionnement & affranchissement ==

A_OpColis -> UI : Lancer calcul conditionnement
activate UI
UI -> APP : calculerConditionnement(idCommande)
activate APP

APP -> DB : SELECT lignes commande + poids goodies
activate DB
DB --> APP : lignes + poids unitaires
deactivate DB

APP -> DB : SELECT référentiel emballages + règles
activate DB
DB --> APP : emballages + règles
deactivate DB

APP -> APP : choisirEmballage()\ncalculerPoidsTotal()
APP -> DB : UPDATE Commande SET emballage=?, poids_total=?
activate DB
DB --> APP : OK
deactivate DB

APP --> UI : Emballage + poids total calculés
deactivate APP
UI --> A_OpColis : Afficher emballage + poids total
deactivate UI

A_OpColis -> UI : Lancer calcul affranchissement
activate UI
UI -> APP : calculerAffranchissement(idCommande, poids_total)
activate APP

APP -> DB : SELECT tarifs postaux (poids -> tarif)
activate DB
DB --> APP : grille tarifs
deactivate DB

APP -> APP : calculTarif(poids_total)
APP -> DB : UPDATE Commande SET affranchissement=?
activate DB
DB --> APP : OK
deactivate DB

APP --> UI : Montant affranchissement enregistré
deactivate APP
UI --> A_OpColis : Afficher montant affranchissement
deactivate UI
'--- Calculs (logique applicative)
APP -> APP : choisirEmballage()\ncalculerPoidsTotal()

alt Emballage compatible trouvé
  '--- Persistences résultat conditionnement
  APP -> DB : UPDATE Commande SET emballage=?, poids_total=?
  activate DB
  DB --> APP : OK
  deactivate DB

  '--- Calcul affranchissement (à partir des tarifs stockés)
  APP -> DB : SELECT tarifs postaux (poids -> tarif)
  activate DB
  DB --> APP : grille tarifs
  deactivate DB

  APP -> APP : calculTarif(poids_total)

  alt Tarif trouvé (poids dans la grille)
    APP -> DB : UPDATE Commande SET affranchissement=?
    activate DB
    DB --> APP : OK
    deactivate DB

    APP --> UI : Emballage + poids total + affranchissement calculés
  else Tarif manquant (colis trop lourd / hors grille)
    note right of APP
    Règle : si le poids dépasse la grille tarifaire,
    on split la commande en plusieurs colis
    (au moins 1 goodie par colis).
    end note

    APP -> APP : splitCommandeEnColis()\n(recalcul par colis)
    APP -> DB : INSERT Colis/LignesColis\n+ MAJ Commande (multi-colis)
    activate DB
    DB --> APP : OK
    deactivate DB

    APP -> APP : recalculerConditionnementEtTarifs(par colis)

    APP --> UI : Commande splittée en plusieurs colis\n(tarifs calculés par colis)
  end

else Aucun emballage compatible
  note right of APP
  Règle : si aucun emballage n'est compatible,
  on split la commande en plusieurs colis
  (au moins 1 goodie par colis).
  end note

  APP -> APP : splitCommandeEnColis()\n(recalcul par colis)
  APP -> DB : INSERT Colis/LignesColis\n+ MAJ Commande (multi-colis)
  activate DB
  DB --> APP : OK
  deactivate DB

  APP -> APP : recalculerConditionnementEtTarifs(par colis)

  APP --> UI : Commande splittée en plusieurs colis\n(conditionnement + tarifs par colis)
end

'===================================================================================
== Expédition ==

A_OpColis -> Poste : Déposer le colis\n(acheminement La Poste)
activate Poste

opt Lettre suivie
  Poste --> A_OpColis : Fournir n° de suivi
  note right of A_OpColis
  Conserver le n° de suivi
  pour saisie dans Access
  end note
end

Poste --> A_OpColis : Preuve de dépôt (optionnelle)
deactivate Poste

A_OpColis -> UI : Valider expédition dans Access
activate UI
UI -> APP : enregistrerExpedition(idCommande)
activate APP

opt Lettre suivie
  A_OpColis -> UI : Saisir n° de suivi
  UI -> APP : enregistrerSuivi(idCommande, tracking)
  APP -> DB : UPDATE Commande SET tracking=?
  activate DB
  DB --> APP : OK
  deactivate DB
end

APP -> DB : INSERT Mouvement(statut=EXPEDIEE, date, idCommande)
activate DB
DB --> APP : OK
deactivate DB

APP -> DB : UPDATE Commande SET statut=EXPEDIEE
activate DB
DB --> APP : OK
deactivate DB

APP --> UI : Confirmation expédition enregistrée
deactivate APP
UI --> A_OpColis : Statut commande = expédiée
deactivate UI

@enduml
