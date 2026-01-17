

## Acteurs principaux (cœur “gestion des colis”)

acteurs                         role
_                               _ 
_ Opérateur colis               _ Acteurs principaux 
_ clients particuliers          _ Acteurs principaux 
_ Administrateur du système     _ Acteurs principaux 


_ Opérateur stock               _ Acteurs secondaire 

_ La Poste                      _ Acteurs secondaire 
_ Site vitrine / site marketing _ Acteurs secondaire 

_ Direction                     _ Acteurs secondaire 



Acteurs principaux (périmètre : gestion des colis)

1) Client final (particulier)

Rôle : initier une demande de goodies en envoyant un courrier à la fromagerie.

Ce qu’il fait :

découpe les points de fidélité, choisit un goodies, joint un chèque pour les frais de port et envoie l’ensemble par courrier ;

consulte le site vitrine pour télécharger le collecteur ou vérifier la liste de goodies/points à jour.

Pourquoi je le considère comme acteur : même s’il n’utilise pas l’application interne, il déclenche le flux métier (entrée des demandes).

2) Opérateur colis

Rôle : traiter les courriers entrants, saisir/mettre à jour les données et piloter la préparation et l’expédition des colis.

Ce qu’il fait :

réceptionne et traite manuellement les courriers ;

utilise le module “gestion des colis” : gestion clients, commandes, conditionnement (calcul final), choix d’emballages, historisation des mouvements, statistiques, mailing, emails personnalisés, impressions.

Pourquoi je le considère comme acteur : c’est l’utilisateur principal du système sur le périmètre “colis”.

3) Administrateur du système (profil admin)

Rôle : administrer et maintenir les référentiels nécessaires au bon fonctionnement.

Ce qu’il fait :

paramètre les emballages, les données de calcul d’affranchissement, les poids des articles, les référentiels associés.

Pourquoi je le considère comme acteur : il garantit la cohérence des référentiels et la fiabilité des calculs utilisés par les opérateurs.

Acteurs connexes (impact indirect sur le périmètre “colis”)

4) Opérateur stock

Rôle : gérer les stocks de goodies et les inventaires (fonction présente dans l’outil historique).

Ce qu’il fait :

suit les niveaux de stock et réalise les inventaires.

Pourquoi je le considère comme acteur : les disponibilités goodies peuvent impacter le traitement des commandes (même si les règles de rupture ne sont pas détaillées dans le document).

5) Direction / management

Rôle : exploiter les indicateurs et piloter le besoin de reporting.

Ce qu’elle fait :

consulte les statistiques, impressions et rapports selon les besoins de pilotage.

Pourquoi je le considère comme acteur : c’est une partie prenante “décideur” et “consommateur” des sorties du système, même si l’usage n’est pas quotidien.

Acteurs / systèmes externes (environnement)

6) La Poste

Rôle : assurer l’acheminement et fournir les informations nécessaires à l’expédition.

Ce qu’elle apporte :

les tarifs postaux (mis à jour annuellement) ;

le numéro de suivi en cas de “lettre suivie”.

Pourquoi je le considère comme acteur externe : le système dépend de La Poste pour l’affranchissement et le suivi.

7) Site vitrine / marketing

Rôle : mettre à disposition des clients les supports et informations à jour.

Ce qu’il permet :

téléchargement du collecteur ;

consultation de la liste goodies/points à jour.

Pourquoi je le considère comme système externe : il intervient en amont du processus, côté client, comme source d’information/support.


