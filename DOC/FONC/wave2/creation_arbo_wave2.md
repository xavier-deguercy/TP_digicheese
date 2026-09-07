# Creation arborescence Wave 2 (extensions metier)

## Objectif
Ajouter la structure minimale pour la Wave 2 sans impacter la base existante:
- nouvelles ressources commandes
- nouvelles ressources stock
- docs wave 2

---

## Script PowerShell (structure uniquement)

```powershell
# Dossiers code Wave 2 (si absents)
New-Item -ItemType Directory -Force -Path `
  "src\models", `
  "src\schemas", `
  "src\repositories", `
  "src\services", `
  "src\routers", `
  "tests" | Out-Null

# Fichiers code Wave 2
New-Item -ItemType File -Force -Path `
  "src\models\commande.py", `
  "src\models\detail_commande.py", `
  "src\models\prix.py", `
  "src\models\rel_cond.py", `
  "src\models\stock.py", `
  "src\models\stock_ligne.py", `
  "src\models\mise_a_jour.py", `
  "src\models\boutique.py", `
  "src\models\utilisateur_role.py", `
  "src\schemas\commande_schema.py", `
  "src\schemas\detail_commande_schema.py", `
  "src\schemas\prix_schema.py", `
  "src\schemas\rel_cond_schema.py", `
  "src\schemas\stock_schema.py", `
  "src\schemas\stock_ligne_schema.py", `
  "src\schemas\mise_a_jour_schema.py", `
  "src\schemas\boutique_schema.py", `
  "src\schemas\utilisateur_role_schema.py", `
  "src\repositories\commande_repository.py", `
  "src\repositories\detail_commande_repository.py", `
  "src\repositories\prix_repository.py", `
  "src\repositories\rel_cond_repository.py", `
  "src\repositories\stock_repository.py", `
  "src\repositories\stock_ligne_repository.py", `
  "src\repositories\mise_a_jour_repository.py", `
  "src\repositories\boutique_repository.py", `
  "src\repositories\utilisateur_role_repository.py", `
  "src\services\commande_service.py", `
  "src\services\detail_commande_service.py", `
  "src\services\prix_service.py", `
  "src\services\rel_cond_service.py", `
  "src\services\stock_service.py", `
  "src\services\stock_ligne_service.py", `
  "src\services\mise_a_jour_service.py", `
  "src\services\boutique_service.py", `
  "src\services\utilisateur_role_service.py", `
  "src\routers\commande_router.py", `
  "src\routers\detail_commande_router.py", `
  "src\routers\prix_router.py", `
  "src\routers\rel_cond_router.py", `
  "src\routers\stock_router.py", `
  "src\routers\stock_ligne_router.py", `
  "src\routers\mise_a_jour_router.py", `
  "src\routers\boutique_router.py", `
  "src\routers\utilisateur_role_router.py", `
  "tests\test_commande.py", `
  "tests\test_detail_commande.py", `
  "tests\test_prix.py", `
  "tests\test_rel_cond.py", `
  "tests\test_stock.py", `
  "tests\test_stock_ligne.py", `
  "tests\test_mise_a_jour.py", `
  "tests\test_boutique.py", `
  "tests\test_utilisateur_role.py" | Out-Null

# Dossiers de suivi documentaire
New-Item -ItemType Directory -Force -Path `
  "DOC\FONC\wave1", `
  "DOC\FONC\wave2" | Out-Null
```

---

## Notes
- Ce script prepare la structure; l'implementation reste guidee par `Backlog_wave2.md`.
- Conserver les conventions de routes existantes pour la compatibilite prod.
