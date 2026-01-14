@startuml
left to right direction
skinparam actorStyle awesome
skinparam shadowing false
skinparam wrapWidth 220
title DIGICHEESE — UC Administration & Pilotage — Access 2000

'========================
' Acteurs
'========================
actor "Administrateur (PMO)\n(interne SI)" as A_Admin
actor "Opérateur stock\n(connexe)" as A_Stock
actor "La Poste\n(système externe)" as A_Poste
actor "Direction / management\n(connexe)" as A_Direction

'========================
' Système : Administration & Pilotage
'========================
rectangle "Système de gestion des colis\n(ancien système Access 2000)" {

  usecase "nAdministrer / paramétrer\nle système" as UC11_Admin

  usecase "nGérer référentiel emballages" as UC12_Emb
  usecase "nGérer référentiel goodies\n(poids, caractéristiques)" as UC13_Goodies
  usecase "nMettre à jour tarifs postaux\n(annuels)" as UC14_Tarifs

  usecase "nGérer stocks goodies" as UC15_Stocks
  usecase "nRéaliser inventaire" as UC16_Inventaire

  usecase "Générer statistiques /\nreporting" as UC17_Reporting
  usecase "Fournir un rapport\nà la Direction" as UC18_Fournir
}

'========================
' Associations acteurs -> UC
'========================
A_Admin --> UC11_Admin
A_Admin --> UC17_Reporting
A_Admin --> UC18_Fournir

A_Stock --> UC15_Stocks
A_Stock --> UC16_Inventaire

A_Poste --> UC14_Tarifs

' La Direction ne manipule pas le SI : elle reçoit le rapport via l'Admin/PMO
A_Direction --> UC18_Fournir

'========================
' Liens include / extend (structurants, peu nombreux)
'========================

' Le paramétrage inclut la mise à jour des référentiels
UC11_Admin ..> UC12_Emb : <<include>>
UC11_Admin ..> UC13_Goodies : <<include>>
UC11_Admin ..> UC14_Tarifs : <<include>>

' L'inventaire est un cas particulier/une activité qui s'appuie sur la gestion de stock
UC16_Inventaire ..> UC15_Stocks : <<include>>

' Produire un reporting inclut la fourniture d'un rapport exploitable pour la Direction
UC17_Reporting ..> UC18_Fournir : <<include>>

@enduml
