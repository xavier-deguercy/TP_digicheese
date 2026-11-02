---
title: DigiCheese - Perimetre MVP valide
version: 1.14.0
date: 2026-09-07
status: mvp-02-developpe-a-valider
---

# Périmètre MVP

## Décision humaine

Le 2026-09-07, Xavier valide le périmètre MVP proposé dans la conversation par sa réponse « Y ». Cette décision porte sur le contenu de la première version démontrable. Les identifiants MVP ci-dessous désignent le découpage proposé et ne renumérotent pas les WP historiques.

| Lot | Contenu retenu | Préparation |
|---|---|---|
| MVP-01 | Commandes : API, liste/formulaire, client, conditionnement et archivage initial | ACCEPTÉ_AVEC_RÉSERVES |
| MVP-02 | Détails : lignes, objets, quantités et consultation par commande | DÉVELOPPÉ_ET_VÉRIFIÉ — ACCEPTATION_MÉTIER_À_CONFIRMER |
| MVP-03 | Règles métier : nbColis, archivage et cohérence commande/détails | DÉCISIONS_MÉTIER_À_CONFIRMER |
| MVP-04 | Relations objet-conditionnement ; réutilisation du prix de l'objet dans l'écran Objets | À_PRÉPARER |
| MVP-05 | Parcours UI complet, gestion des erreurs et états vides | À_PRÉPARER |
| MVP-06 | Stabilisation, tests API/UI/MySQL, non-régression, documentation et démonstration | À_PRÉPARER |

Les règles de MVP-03 nécessaires aux premiers lots doivent être décidées avant leur développement. Le découpage ne reporte pas ces arbitrages après l'implémentation. MVP-05 consolide les écrans livrés dans les lots précédents.

## Après le MVP

Stocks, lignes de stock, journal des mouvements, sorties boutique, rôles multiples, WP-02 IAM et renforcement sécurité sont reportés après le MVP. Les contrôles d'accès existants restent en place. Les réserves et preuves déjà produites sont conservées ; les sources cyber formelles restent À_FOURNIR.

Le référentiel Prix séparé et son API CRUD dédiée sont également reportés après le MVP par D-MVP-09. Le prix existant sur l'objet reste la référence unique du MVP.

## Règles métier décidées

- D-MVP-02 — Conditionnement : le 2026-09-07, Xavier valide par « Y » la création d'une commande sans conditionnement, avec possibilité de le renseigner ensuite lors de sa préparation. Cette décision lève l'inconnue sur son caractère obligatoire à la création. Une éventuelle obligation à une étape ultérieure reste À_CONFIRMER.

- D-MVP-03 — Archivage : le 2026-09-07, Xavier valide par « Y » qu'une commande archivée reste consultable, mais que sa modification et celle de ses lignes sont bloquées. Le désarchivage est nécessaire pour reprendre les modifications. Les règles de suppression restent à décider séparément.

- D-MVP-04 — Suppression : le 2026-09-07, Xavier valide par « Y » la suppression définitive uniquement pour une commande non archivée et sans ligne de détail. Une commande contenant des lignes doit être archivée pour être retirée du travail courant. Cette décision complète D-MVP-03 sans modifier sa règle de verrouillage des commandes archivées.

- D-MVP-05 — Signification de nbColis : le 2026-09-07, Xavier valide par « Y » que nbColis représente le nombre de colis physiques à expédier, et non la somme des quantités d'objets. Exemple validé : trois objets regroupés dans un seul emballage comptent pour un colis. Cette décision ne valide pas encore une formule de calcul ou un mode de saisie.

- D-MVP-06 — Saisie de nbColis : le 2026-09-07, Xavier valide par « Y » une saisie manuelle lors de la préparation. Le champ reste vide lorsque le nombre est inconnu ; toute valeur renseignée doit être un entier strictement positif. Aucun calcul automatique de regroupement n'est retenu pour le MVP. Cette décision complète D-MVP-05 et remplace, pour le MVP, les tâches historiques de recalcul automatique de nbColis.

- D-MVP-07 — Invalidation de nbColis : le 2026-09-07, Xavier valide par « Y » que toute modification des lignes de commande (ajout, modification ou suppression) ou du conditionnement remet nbColis à vide. Le nombre de colis doit alors être vérifié et renseigné à nouveau. Le verrouillage des commandes archivées défini par D-MVP-03 reste applicable.

- D-MVP-08 — Archivage incomplet : le 2026-09-07, Xavier valide par « Y » que l'archivage est autorisé même lorsque le conditionnement ou nbColis ne sont pas renseignés, notamment pour retirer une commande abandonnée du travail courant. L'archivage ne vaut pas confirmation d'expédition. Les règles de consultation et de verrouillage de D-MVP-03 restent applicables.

- D-MVP-09 — Prix : le 2026-09-07, Xavier valide par « Y » l'ajustement de MVP-04 : conserver le prix de chaque objet comme référence unique, géré dans l'écran Objets, et reporter le référentiel Prix séparé après le MVP. Le CRUD Prix dédié du backlog Wave 2 n'est donc pas à réaliser dans le MVP. Les relations objet-conditionnement restent dans MVP-04.

- D-MVP-10 — Autorisation MVP-01 : le 2026-09-07, Xavier autorise explicitement le développement de bout en bout de MVP-01 « Commandes ». Cette autorisation couvre les modifications locales de conception, API, interface, tests et documentation nécessaires au lot. Elle ne couvre pas commit, push, déploiement ni AUTO_NEXT.

- D-MVP-11 — Acceptation MVP-01 : le 2026-09-07, Xavier accepte explicitement MVP-01 avec les réserves consignées dans sa fiche d'exécution. Le lot est clos fonctionnellement au statut `ACCEPTÉ_AVEC_RÉSERVES`. Cette décision ne lève pas les réserves, n'autorise pas AUTO_NEXT et n'ouvre pas le développement de MVP-02.

- D-MVP-12 — Préparation MVP-02 : le 2026-09-07, Xavier autorise par « Y » la préparation de MVP-02 « Détails de commande ». Cette décision couvre le cadrage et la préparation des décisions, mais pas le développement, commit, push, déploiement ou AUTO_NEXT.

- D-MVP-13 — Unicité des lignes : le 2026-09-07, Xavier valide par « Y » qu'un même objet ne peut apparaître qu'une fois dans une commande. La quantité se modifie sur la ligne existante ; une tentative de doublon doit renvoyer `409` et une contrainte unique `(id_commande, id_objet)` protège la règle en base.

- D-MVP-14 — Champ Colis : le 2026-09-07, Xavier valide pour le lot complet le report du champ historique `Colis` hors de MVP-02, jusqu'au cadrage de l'affectation des lignes aux colis physiques.

- D-MVP-15 — Commentaire de ligne : le 2026-09-07, Xavier valide pour le lot complet un commentaire facultatif sur chaque ligne, sans effet sur les calculs ou l'archivage.

- D-MVP-16 — Objet indisponible : le 2026-09-07, Xavier valide pour le lot complet l'interdiction d'ajouter un objet indisponible. Une ligne existante devenue indisponible reste lisible et peut conserver une correction de quantité ou de commentaire.

- D-MVP-17 — Autorisation MVP-02 : le 2026-09-07, la réponse « Y pour le lot complet » autorise le développement de bout en bout de MVP-02 dans le périmètre préparé. Cette autorisation couvre les modifications locales API, UI, tests et documentation ; elle n'inclut pas commit, push, déploiement ou AUTO_NEXT.

## Inconnues et reprise

L'articulation du référentiel Prix séparé avec le prix de l'objet sera étudiée après le MVP. Charge globale, dates et enveloppe des lots suivants : À_CONFIRMER.

MVP-01 est accepté avec réserves. MVP-02 est développé et vérifié localement ; la réserve de MVP-01 sur la suppression d'une commande contenant des lignes est maintenant couverte techniquement. Le point exact de reprise est l'acceptation métier de MVP-02 ; aucun passage automatique à MVP-03 n'est autorisé.

## Sources conservées

- [Backlog Wave 2](../../FONC/wave2/Backlog_wave2.md)
- [Plan solo Wave 2](../../FONC/wave2/sprint_wave2.md)
- [Clôture WP-03 à WP-05](../2026-09-06_POST_WP01/RAPPORT_LOT_REVUE_REFACTOR_UI.md)

Les anciens plans restent des sources historiques. Ni leurs durées ni leur périmètre complet ne deviennent des engagements du MVP par cette décision.
