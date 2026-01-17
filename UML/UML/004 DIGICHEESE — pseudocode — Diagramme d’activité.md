

« Dans le diagramme d’activité, j’ai regroupé Formulaires, logique VBA et base Access dans une seule swimlane, car ils constituent une seule responsabilité fonctionnelle : le système d’information. La séparation technique est traitée dans le diagramme de séquence, pas dans le workflow métier. »

## 3) Diagramme d’activité (PlantUML) — workflow + décisions

@startuml
title DIGICHEESE — Diagramme d’activité (gestion des colis)
skinparam shadowing false
skinparam activityBorderColor black
skinparam activityBackgroundColor white


start
:Réceptionner le courrier;
:Ouvrir et lire le courrier;

if (Informations minimales\nprésentes ?) then (Oui)
else (Non)
  :Mettre en attente\n+ commentaire / blocage;
  stop
endif


:Rechercher le client;
if (Client trouvé ?) then (Oui)
  :Ouvrir fiche client;
else (Non)
  :Créer / compléter\nla fiche client;
endif

:Créer / compléter\nla commande (EN_COURS);

'=========================================================
' Boucle : on répète tant que la commande n'est pas expédiable.
'=========================================================
repeat
  :Calculer conditionnement\n(emballage + poids total);

  if (Emballage compatible ?) then (Oui)
    :OK conditionnement;
  else (Non)
    :Splitter la commande\nen plusieurs colis;
    :Recalculer conditionnement\n(par colis);
  endif

  :Calculer affranchissement\n(poids -> tarif);

  if (Tarif trouvé ?) then (Oui)
    :Enregistrer emballage,\npoids et affranchissement;
  else (Non)
    :Splitter la commande\nen plusieurs colis;
    :Recalculer conditionnement\net affranchissement\n(par colis);
    :Enregistrer résultats\nmulti-colis;
    
  endif

repeat while (Commande expédiable ?) is (Non)

:Préparer le(s) colis;
:Déposer le(s) colis à La Poste;

if (Lettre suivie ?) then (Oui)
  :Récupérer le n° de suivi;
  :Enregistrer le n° de suivi;
endif
:Valider l’expédition;
:Historiser le mouvement;
:Mettre à jour statut\n(EXPEDIEE);

stop
@enduml
