
## 1) Scénario textuel — Administration & Pilotage (scénario nominal)

### Objectif

Assurer le bon fonctionnement de la gestion des colis en maintenant les référentiels (emballages, goodies, tarifs postaux), en pilotant les stocks/inventaires, et en produisant des rapports destinés à la Direction (via l’Admin/PMO).

### Acteurs / systèmes impliqués

* **Administrateur (PMO)** (interne SI) : paramétrage + reporting + transmission à la direction
* **Opérateur stock** (connexe) : mise à jour stock + inventaires
* **La Poste** (externe) : source des tarifs postaux annuels
* **Direction / management** (connexe) : consomme les rapports via l’Admin/PMO
* **Système Access 2000** : stockage des référentiels, calculs, reporting

### Déclencheurs (exemples)

* Mise à jour annuelle des **tarifs postaux** (nouvelle grille La Poste)
* Ajout/modification d’un **goodie** (poids/caractéristiques)
* Mise à jour du référentiel **emballages** (nouveaux formats/règles)
* Besoin périodique de **reporting** (mensuel/annuel)
* Réalisation d’un **inventaire** (périodique) ou correction de stock

### Préconditions

* Droits admin disponibles pour l’Administrateur
* Accès au référentiel La Poste (tarifs) pour l’Admin
* Données de commandes/expéditions existantes pour le reporting

### Scénario nominal (Happy path)

1. L’Administrateur (PMO) ouvre le module d’administration.
2. Il met à jour les référentiels :

   * emballages,
   * goodies (poids),
   * tarifs postaux annuels (selon La Poste).
3. Le système enregistre et rend ces paramètres disponibles à l’exploitation.
4. L’Opérateur stock met à jour le stock goodies et réalise un inventaire si prévu.
5. L’Administrateur génère un reporting (mois/année) depuis les données du système.
6. Il fournit le rapport à la Direction (export/impression/transmission).

### Postconditions

* Référentiels à jour (emballages, goodies, tarifs)
* Stocks/inventaires enregistrés
* Rapports disponibles et transmis à la Direction via Admin/PMO

---

## 2) Diagramme de séquence — Administration & Pilotage (PlantUML)

```plantuml
@startuml
title DIGICHEESE — Séquence : Administration & Pilotage (scénario nominal)
autonumber
skinparam shadowing false

actor "Administrateur (PMO)" as Admin
actor "Opérateur stock" as Stock
actor "Direction" as Dir
participant "SI Gestion des colis\n(Access 2000)" as SI
participant "La Poste" as Poste

== Administration / Paramétrage ==
Admin -> SI : Ouvrir administration (UC11)

Admin -> SI : Mettre à jour référentiel emballages (UC12)
SI --> Admin : Référentiel emballages enregistré

Admin -> SI : Mettre à jour référentiel goodies (poids, caractéristiques) (UC13)
SI --> Admin : Référentiel goodies enregistré

Admin -> Poste : Obtenir / consulter tarifs postaux annuels
Poste --> Admin : Grille tarifs postaux

Admin -> SI : Mettre à jour tarifs postaux (UC14)
SI --> Admin : Tarifs postaux enregistrés

== Stocks / Inventaire (connexe) ==
Stock -> SI : Mettre à jour stocks goodies (UC15)
SI --> Stock : Stock mis à jour

opt Inventaire planifié
  Stock -> SI : Réaliser inventaire (UC16)
  SI --> Stock : Inventaire enregistré / écarts traités
end

== Reporting / Pilotage ==
Admin -> SI : Générer statistiques / reporting (UC17)
SI --> Admin : Rapport généré (impression / export)

Admin -> Dir : Fournir le rapport à la Direction (UC18)
Dir --> Admin : Accusé de réception / questions (hors SI)

@enduml
```

✅ Points clés :

* La **Direction** ne touche pas le SI.
* La Poste intervient uniquement pour **fournir les tarifs** (source).
* L’inventaire est modélisé en **opt** (optionnel / périodique).

---

## 3) Diagramme d’activité — Administration & Pilotage (PlantUML)

```plantuml
@startuml
title DIGICHEESE — Activité : Administration & Pilotage (workflow)
skinparam shadowing false

start

:Ouvrir module d'administration (UC11);

fork
  :Mettre à jour référentiel emballages (UC12);
fork again
  :Mettre à jour référentiel goodies\n(poids, caractéristiques) (UC13);
fork again
  :Récupérer tarifs postaux annuels\nauprès de La Poste;
  :Mettre à jour tarifs postaux (UC14);
end fork

:Paramétrage enregistré\net disponible pour l'exploitation;

if (Besoin de mise à jour stock ?) then (Oui)
  :Mettre à jour stocks goodies (UC15);

  if (Inventaire planifié ?) then (Oui)
    :Réaliser inventaire (UC16);
  endif
endif

if (Besoin de reporting ?) then (Oui)
  :Générer statistiques / reporting (UC17);
  :Fournir le rapport à la Direction\n(via Admin/PMO) (UC18);
endif

stop
@enduml
```

✅ Points clés :

* Les mises à jour référentiels peuvent être vues comme **parallélisables** (fork), ce qui rend le diagramme très lisible.
* Stock/inventaire et reporting apparaissent comme **conditions** (périodiques, “selon besoin”).

