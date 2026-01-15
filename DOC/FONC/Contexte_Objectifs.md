# Contexte & objectifs — DIGICHEESE (TP7)

## 1) Contexte
La fromagerie **DIGICHEESE** souhaite refondre une application interne ancienne :
- l’existant est centralisé sur **Microsoft Access (Office 2000) + VBA**, avec des limites fortes (instabilité, maintenance difficile, faible évolutivité, ergonomie dépassée).  
- la cible exprimée dans le cahier des charges est un **site interne (Intranet)** structuré par rôles : Authentification, Administration, Gestion des colis, Gestion des stocks.

> Dans le TP7, la livraison attendue est une **API backend** (Python) avec **Swagger** pour simuler l’IHM, une base **MySQL**, et des **tests automatisés**.  

## 2) Objectifs métier (côté “client”)
- Disposer d’un socle plus robuste et maintenable que l’existant Access/VBA.
- Structurer l’application autour de **rôles** (Admin / OP-colis / OP-stocks).
- Centraliser des référentiels nécessaires au fonctionnement (communes, objets, conditionnements, poids, poids-vignette).

## 3) Objectifs pédagogiques (TP7)
- Produire une API backend documentée (Swagger/OpenAPI) et testée.
- Structurer le dépôt : couches (routes/services/repositories/models), documentation (FONC/TECH/UTILISATION), scénarios de tests.
- Respecter les livrables attendus : requirements.txt, branches (test/dev/prod/master + 1 branche par développeur), dossier doc technique, etc.

## 4) Références documentaires
- MiniCahierDesChargesFromagerieDigiCheese.pdf (besoin & périmètre)
- PROJETTP7_API_WEB_2026_Data.pdf (livrables TP7)
- consignes_projet_dev_2026.pdf (critères d’évaluation : sécurité, RGPD, monitoring, qualité, tests)
