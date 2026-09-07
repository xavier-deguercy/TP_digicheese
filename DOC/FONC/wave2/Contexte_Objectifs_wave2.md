# Contexte & objectifs - DIGICHEESE Wave 2

## 1) Contexte
La Wave 1 a fourni un socle API backend avec CRUD admin principaux et une base exploitee en production.
La Wave 2 etend ce socle pour couvrir les cas metier non livres en priorite:
- commandes
- details de commandes
- prix et relations conditionnement
- stock et mouvements

Le cadre reste:
- API backend
- Swagger pour simulation front
- tests automatises
- livraison additive

---

## 2) Objectifs metier Wave 2
- Finaliser le parcours operationnel colis.
- Ajouter la gestion des flux stock sans casser l'existant.
- Renforcer la coherence des relations de donnees (FK et contraintes).

---

## 3) Objectifs techniques Wave 2
- Implementer les nouveaux CRUD metier planifies.
- Maintenir la compatibilite des routes deja en prod.
- Couvrir les nouveaux flux par tests CRUD + integration.
- Produire des KPI de suivi par sprint (tests, couverture, latence, erreurs).

---

## 4) Criteres de succes
- Flux commande complet executable via Swagger.
- Flux stock principal executable via Swagger.
- Non-regression verte sur CRUD deja en production.
- Documentation FONC/TECH/UTILISATION alignee sur Wave 2.

---

## 5) References
- `DOC/FONC/Backlog_wave2.md`
- `database/modelisation_base_digicheese_wave2.md`
- `database/modelisation_base_digicheese_wave2.sql`
