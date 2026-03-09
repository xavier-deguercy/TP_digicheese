@startuml
left to right direction
skinparam actorStyle awesome
skinparam shadowing false
skinparam wrapWidth 220

title DIGICHEESE — UC Exploitation (Gestion des colis) — Access 2000

'========================
' Acteurs
'========================
actor "Client final\n(externe)" as A_Client
actor "Opérateur colis\n(interne SI)" as A_OpColis
actor "La Poste\n(système externe)" as A_Poste
actor "Opérateur stock\n(connexe)" as A_Stock

'========================
' Système de gestion des colis
'========================
rectangle "Système de gestion des colis\n(ancien système Access 2000)" {

  '--- UC principaux (exploitation)
  usecase "Saisir une demande\nà partir du courrier" as UC01_Saisie
  usecase "Gérer fiche client\n(créer / mettre à jour)" as UC02_Client
  usecase "Enregistrer / mettre à jour\nla commande" as UC03_Commande
  usecase "Calculer conditionnement\n& choisir emballage" as UC04_Cond
  usecase "Calculer affranchissement\n(poids -> tarif)" as UC05_Aff
  usecase "Expédier le colis" as UC06_Exp
  usecase "Tracer le traitement\n(historisation mouvements)" as UC07_Traca
  usecase "Communiquer avec le client\n(mailing / email)" as UC08_Comm

  '--- Variantes (optionnelles)
  usecase "Variante : demande sur papier libre\n(sans collecteur)" as UC09_PapierLibre
  usecase "Variante : envoi en lettre suivie\n(saisie n° de suivi)" as UC10_Suivi
}

'========================
' Associations acteurs -> UC
'========================
A_Client --> UC01_Saisie

A_OpColis --> UC01_Saisie
A_OpColis --> UC03_Commande
A_OpColis --> UC04_Cond
A_OpColis --> UC06_Exp
A_OpColis --> UC08_Comm

A_Poste --> UC05_Aff
A_Poste --> UC06_Exp

' Connexe : consultation disponibilité lors du traitement de commande
A_Stock --> UC03_Commande

'========================
' Liens include / extend (peu nombreux, lisibles)
'========================

' Quand on saisit une demande, on doit pouvoir créer/mettre à jour client et commande
UC01_Saisie ..> UC02_Client : <<include>>
UC01_Saisie ..> UC03_Commande : <<include>>

' Conditionnement inclut le calcul d'affranchissement
UC04_Cond ..> UC05_Aff : <<include>>

' Expédier suppose qu'on a conditionné (et donc affranchi)
UC06_Exp ..> UC04_Cond : <<include>>

' Traçabilité : expédition génère une trace (au minimum)
UC06_Exp ..> UC07_Traca : <<include>>

' Communication : optionnelle (selon besoin)
UC08_Comm ..> UC03_Commande : <<extend>>

' Variantes spécifiques
UC09_PapierLibre ..> UC01_Saisie : <<extend>>
UC10_Suivi ..> UC06_Exp : <<extend>>

@enduml
