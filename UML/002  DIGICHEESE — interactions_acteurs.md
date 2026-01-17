@startuml
left to right direction
skinparam componentStyle rectangle
skinparam shadowing false
skinparam wrapWidth 220
title DIGICHEESE — Schéma global (périmètre : Gestion des colis)

'============================================================
' Objectif du schéma (réponse à la question)
' - Montrer les ACTEURS + les GRANDES FONCTIONNALITÉS (macro-modules)
' - Montrer les INTERACTIONS des acteurs (liens acteur -> module)
' - Rester dans le périmètre "gestion des colis" (pas une vue SI complète)
'============================================================

'============================================================
' ACTEURS
' NB : distinction entre acteurs INTERNES (utilisateurs du SI) et
'      acteurs EXTERNES (hors SI mais interagissant avec le processus)
'============================================================


package "Digichesse" as DG {
'========================
' acteurs internes  
'========================
actor "Opérateur colis" as A_OpColis
actor "Administrateur du système\n(profil admin)\n+ interface PMO" as A_Admin
actor "Opérateur stock\n(connexe)" as A_OpStock
actor "Direction / management\n(connexe)" as A_Direction


'============================================================
' GRANDES FONCTIONNALITÉS (macro-modules) — périmètre projet
' Chaque composant représente un bloc fonctionnel (pas du détail technique).
'============================================================
package "Système de gestion des colis" as SYS_GestionColis {

  component "Gestion des commandes" as C_Commandes
  component "Gestion des clients" as C_Clients
  component "Conditionnement / Emballages\n(incl. affranchissement)" as C_Cond
  component "Communication client" as C_Comm
  component "Statistiques\n(incl. reporting)" as C_Stats
  component "Gestion des emplacements" as C_Empl
  component "Gestion des stocks" as C_Stock
  component "Administration / paramétrage" as C_AdminParam
  'le site est un composant statique 
  component "Site vitrine / marketing"  as EXT_Site
  }
}
'========================
' acteurs externes
'========================

actor "Client final\n(particulier)" as A_Client
actor "la Poste" as A_Poste

'============================================================
' INTERACTIONS DES ACTEURS (acteur -> fonctionnalité)
'============================================================

'--- Client final : agit hors SI mais déclenche le processus métier ---
A_Client -up- EXT_Site : consulter / télécharger\n(collecteur, liste goodies/points)
A_Client -- C_Commandes : déclencher demande\n(courrier : points + choix + chèque)

'--- Opérateur colis : utilisateur principal du SI sur le périmètre colis ---
A_OpColis -- C_Commandes : saisir / suivre commandes
A_OpColis -- C_Clients : créer / MAJ fiche client
A_OpColis -- C_Cond : lancer conditionnement\n& calcul affranchissement
A_OpColis -- C_Comm : mailing / emails
A_OpColis -- C_Stats : consulter / produire stats
A_OpColis -- C_Empl : renseigner / consulter\n(si activé)

'--- Opérateur stock : connexe, alimente/contrôle les disponibilités goodies ---
A_OpStock -- C_Stock : gérer stocks & inventaires

'--- Administrateur : paramétrage + production de reporting (rôle “PMO”) ---
A_Admin -- C_AdminParam : maintenir référentiels\n(règles, poids, tarifs, etc.)
A_Admin -- C_Stats : extraire / produire\nrapports pour la Direction

'--- Direction : ne manipule pas le SI directement, passe par l’Admin ---
' (On relie la Direction aux Statistiques avec une précision "via Admin")
'A_Direction -- C_Stats : consulter indicateurs\n(via Administrateur)
A_Direction -- A_Admin : demander / consulter\nindicateurs & rapports
'============================================================
' DÉPENDANCES EXTERNES STRUCTURANTES
' (sans entrer dans le détail technique)
'============================================================

' Conditionnement/affranchissement dépend de La Poste (tarifs + suivi)
C_Cond -up- A_Poste : tarifs annuels\n+ n° de suivi (lettre suivie)
A_Poste -- C_Comm : envoi notifications\n(suivi colis)
@enduml
