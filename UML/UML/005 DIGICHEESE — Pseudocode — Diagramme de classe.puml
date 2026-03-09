@startuml
title DIGICHEESE — Diagramme de classes (gestion des colis — Access 2000)
skinparam style strictuml
skinparam classAttributeIconSize 0

'========================
' Énumérations
'========================
enum StatutCommande {
  EN_COURS
  EN_ATTENTE
  EXPEDIEE
}

enum ModeExpedition {
  STANDARD
  LETTRE_SUIVIE
}

'========================
' Classes coeur métier
'========================
class Client {
  +idClient: int
  +nom: string
  +prenom: string
  +codePostal: string
  +ville: string
  
  +adresse1: string
  +adresse2: string [0..1]
  +email: string [0..1]


  +majCoordonnees(): void
}

class Commande {
  +idCommande: int
  +dateCreation: Date
  +statut: StatutCommande
  +commentaire: String
  +modeExpedition: ModeExpedition

  +ajouterLigne(goodie: Goodie, quantite: int): void
  +changerStatut(nouveauStatut: StatutCommande): void
  +splitterEnColis(): void
}

class LigneCommande {
  +idLigne: int
  +quantite: int
  +commentaire: String

  +calculerPoidsLigne(): decimal
}

class Colis {
  +idColis: int
  +poidsTotal: decimal
  +affranchissement: decimal
  +numeroSuivi: String

  +calculerPoidsTotal(): decimal
  +enregistrerSuivi(tracking: String): void
}

class MouvementCommande {
  +idMouvement: int
  +dateMouvement: DateTime
  +statut: StatutCommande
  +commentaire: String
}

'========================
' Référentiels
'========================
class Goodie {
  +idGoodie: int
  +libelle: String
  +poidsUnitaire: decimal
}

class Emballage {
  +idEmballage: int
  +libelle: String
  +poidsEmballage: decimal
  +poidsMax: decimal
  +poidsMin: decimal

  +estCompatible(poidsContenu: decimal): boolean
}

class GrilleTarifaire {
  +annee: int
  +dateMAJ: Date

  +trouverTarif(poids: decimal): decimal
}

class TrancheTarif {
  +idTranche: int
  +poidsMin: decimal
  +poidsMax: decimal
  +tarif: decimal

  +contient(poids: decimal): boolean
}

'========================
' Associations & cardinalités
'========================
Client "1" -- "0..*" Commande : passe >

Commande "1" o-- "1..*" LigneCommande : contient >
LigneCommande "1" --> "1" Goodie : concerne >

Commande "1" o-- "1..*" Colis : découpée en >
Colis "1" --> "1" Emballage : utilise >

Commande "1" o-- "0..*" MouvementCommande : historise >

GrilleTarifaire "1" o-- "1..*" TrancheTarif : définit >
Colis ..> GrilleTarifaire : calculeTarif(poidsTotal)

@enduml
