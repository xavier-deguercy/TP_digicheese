Exercice 2.1 : Étude de cas – Identifier les types de tests

Objectif : Appliquer les concepts de tests statiques, dynamiques, et d'acceptation à un scénario concret.
Consigne détaillée : Vous travaillez sur un projet de développement d'une application mobile de gestion de tâches. Voici une liste d'activités liées aux tests. Pour chacune, précisez :
● Type de test : Statique, Dynamique, ou Acceptation.
definition:
    ● Statique : Test effectué sans exécuter le code, souvent par revue de documents ou analyse de code.
    ● Dynamique : Test effectué en exécutant le code pour vérifier son comportement.
    ● Acceptation : Test réalisé pour valider que le système répond aux exigences et attentes des utilisateurs finaux

● Justification : Pourquoi ce type de test est-il adapté à cette activité ?
● Responsable : Qui devrait réaliser ce test (développeur, testeur, utilisateur final) ?
Liste des activités :
1. Revue des spécifications fonctionnelles pour vérifier leur clarté et leur exhaustivité.
statique
2. Exécution de tests automatisés pour valider le bon fonctionnement de la fonctionnalité "ajout d'une tâche".
3. Validation par les utilisateurs finaux que l'application répond à leurs besoins.
4. Analyse du code source pour détecter des erreurs de syntaxe ou des violations des bonnes pratiques.
5. Test manuel de l'interface utilisateur pour vérifier l'ergonomie et la facilité d'utilisation. 


Réponses attendues :
1. Type de test : Statique
   Justification : La revue des spécifications fonctionnelles ne nécessite pas l'exécution du code, elle consiste à examiner les documents pour s'assurer qu'ils sont complets et compréhensibles.
   Responsable : Analyste métier ou chef de projet.


2. Type de test : Dynamique
   Justification : L'exécution de tests automatisés implique l'exécution du code pour vérifier que la fonctionnalité fonctionne comme prévu.
   Responsable : Testeur ou développeur.


3. Type de test : Acceptation
   Justification : La validation par les utilisateurs finaux vise à s'assurer que l'application répond à leurs besoins et attentes, ce qui est l'objectif principal des tests d'acceptation.
   Responsable : Utilisateurs finaux ou clients.


4. Type de test : Statique
   Justification : L'analyse du code source est une activité de test statique car elle consiste à examiner le code sans l'exécuter, afin de détecter des erreurs potentielles.
   Responsable : Développeur ou équipe de revue de code.


5. Type de test : Dynamique
   Justification : Le test manuel de l'interface utilisateur nécessite l'exécution de l'application pour évaluer l'ergonomie et la facilité d'utilisation.
   Responsable : Testeur ou utilisateur final.
Test manuel de l'interface utilisateur pour vérifier l'ergonomie et la facilité d'utilisation. si ihm deja deveoppée, c'est dynamique
Test manuel de l'interface utilisateur pour vérifier l'ergonomie et la facilité d'utilisation. si ihm a l'etat de maquette, c'est statique







## Exercice 2.2 : Distinguer erreurs, défauts et défaillances
Objectif : Appliquer les définitions théoriques d'erreurs, défauts et défaillances à des scénarios concrets.
Consigne détaillée :
Pour chaque scénario décrit ci-dessous, identifiez s'il s'agit d'une erreur, d'un défaut ou d'une défaillance. Justifiez votre choix en expliquant pourquoi ce scénario correspond à
cette catégorie.

definissions :  
# une erreur est une action humaine qui produit un résultat incorrect
# un défaut est une erreur dans le code source ou la documentation qui peut potentiellement causer une défaillance
# une défaillance est un comportement incorrect observé lors de l'exécution du système, résultant d'un défaut   



Scénario 1 : Oubli de gestion d'erreur
Contexte : Lors du développement d'une application de gestion de tâches, un développeur
oublie d'inclure une gestion d'erreur pour le cas où un utilisateur essaie de supprimer une
tâche qui n'existe pas.
● Question : S'agit-il d'une erreur, d'un défaut ou d'une défaillance ?




Scénario 2 : Plantage de l'application
Contexte : Lors de l'utilisation d'une application bancaire, un utilisateur saisit un caractère
spécial dans le champ "Montant du virement". L'application plante immédiatement et affiche
un message d'erreur système.
● Question : S'agit-il d'une erreur, d'un défaut ou d'une défaillance ?




Scénario 3 : Spécification incomplète
Contexte : Dans le cahier des charges d'une application de réservation de billets de train, il
est mentionné que les utilisateurs doivent pouvoir rechercher des trajets, mais le format des
données d'entrée (ex : date, heure) n'est pas précisé.
● Question : S'agit-il d'une erreur, d'un défaut ou d'une défaillance ?




Scénario 4 : Bug de calcul
Contexte : Dans une application de gestion de notes pour les étudiants, un bug est
découvert : la moyenne des notes est calculée en ignorant les coefficients des matières.
● Question : S'agit-il d'une erreur, d'un défaut ou d'une défaillance ?



Scénario 5 : Problème d'interface utilisateur
Contexte : Lors de l'utilisation d'une application mobile, les utilisateurs remarquent que le
bouton "Valider" ne répond pas quand ils cliquent dessus, empêchant la validation d'une
commande.
● Question : S'agit-il d'une erreur, d'un défaut ou d'une défaillance ?



Scénario 6 : Mauvaise compréhension des exigences
Contexte : Lors de la conception d'une application de gestion de projets, l'équipe de
développement interprète mal une exigence concernant la priorisation des tâches, ce qui
conduit à une implémentation incorrecte.
● Question : S'agit-il d'une erreur, d'un défaut ou d'une défaillance ?
