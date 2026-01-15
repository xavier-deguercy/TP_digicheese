# Changements vs Cahier des Charges (adaptation TP7)

## Objectif
Tracer explicitement les écarts entre :
- le **mini cahier des charges** (application intranet complète)
- la **réalisation TP7** (API backend + Swagger + tests)

---

## 1) IHM / Front
- CDC : application intranet “pratique et esthétique” (interfaces admin, colis, stock).
- TP7 : **IHM non développée** ; simulation via **Swagger/OpenAPI**.

---

## 2) Fonctionnel livré (réduction de périmètre)
### Livré (TP7)
- CRUD **Admin** sur : users (si retenu), communes, objets, conditionnements, poids, poids-vignette.
- (Option) CRUD **Clients** (OP-colis).

### Non livré (TP7) — conservé en évolutions
- Commandes complètes (CRUD + calcul), mailing, stats, impression, historisation colis.
- Module OP-stocks complet (inventaire, bouton annuel, etc.).

---

## 3) Justification des changements
- Le TP7 impose un livrable concentré sur : API + Swagger + tests + MySQL + documentation, en 5 jours.
- Le backlog retient donc le “minimum viable” attendu en soutenance.

---

## 4) Traçabilité
Toute décision de périmètre doit être reportée aussi dans :
- `DOC/FONC/Perimetre_In_Out.md`
- `DOC/FONC/Backlog.md`
