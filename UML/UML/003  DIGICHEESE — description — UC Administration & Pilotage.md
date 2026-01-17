

# B) UC — Administration & Pilotage (référentiels + reporting via Admin/PMO)

## UC11 — Administrer / paramétrer le système *(UC_Admin)*

* **Objectif :** garantir la cohérence des référentiels et paramètres indispensables au traitement des commandes.
* **Acteur :** **Administrateur (profil admin + interface PMO)**.
* **Déclencheur :** mise à jour périodique (ex : annuelle) ou correction nécessaire.
* **Préconditions :** droits admin.
* **Scénario nominal :**

  1. L’admin met à jour les référentiels (emballages, goodies, tarifs…).
  2. Le système enregistre et rend disponible pour l’exploitation.
* **Postconditions :** paramètres opérationnels.

---

## UC12 — Gérer référentiel emballages *(UC_Emb)*

* **Objectif :** maintenir la liste des emballages et règles associées (utilisées par UC_Cond).
* **Acteur :** **Administrateur**.
* **Postconditions :** référentiel emballages à jour.

---

## UC13 — Gérer référentiel goodies (poids, caractéristiques) *(UC_Goodies)*

* **Objectif :** maintenir les données goodies nécessaires au calcul (poids, caractéristiques).
* **Acteur :** **Administrateur**.
* **Postconditions :** référentiel goodies à jour.

---

## UC14 — Mettre à jour tarifs postaux (annuels) *(UC_Tarifs)*

* **Objectif :** maintenir les tarifs postaux annuels utilisés pour l’affranchissement (UC_Aff).
* **Acteurs :**

  * Principal : **Administrateur**
  * Secondaire : **La Poste**
* **Postconditions :** tarifs à jour.

---

## UC15 — Gérer stocks goodies *(UC_Stocks)*

* **Objectif :** maintenir la disponibilité des goodies.
* **Acteur :** **Opérateur stock** (principal), **Admin** éventuellement.
* **Postconditions :** stock à jour.

---

## UC16 — Réaliser inventaire *(UC_Inventaire)*

* **Objectif :** réaliser une opération d’inventaire pour fiabiliser le stock.
* **Acteur :** **Opérateur stock**.
* **Postconditions :** inventaire enregistré / stock ajusté.

---

## UC17 — Générer statistiques / reporting *(UC_Reporting)*

* **Objectif :** produire indicateurs/rapports (mois/année) et impressions.
* **Acteur :** **Administrateur (PMO)** et/ou **Opérateur colis** (consultation selon organisation).
* **Postconditions :** rapports générés.

---

## UC18 — Fournir un rapport à la Direction *(UC_Fournir)*

* **Objectif :** transmettre les rapports à la Direction (la Direction ne manipule pas le SI directement).
* **Acteurs :**

  * Principal : **Administrateur (PMO)**
  * Consommateur : **Direction / management**
* **Postconditions :** rapport transmis / exploitable.

