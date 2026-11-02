---
title: DigiCheese - Migration du dispositif équipe projet DSI V2
version: 0.2.0
date: 2026-09-05
status: migration-v2-terminee-regularisation-j2-j4-en-attente
---

# DigiCheese — Migration du dispositif équipe projet DSI V2

Cette migration fait évoluer le pilotage de DigiCheese sans redémarrer le projet, rejouer J1, réécrire les décisions humaines ni remplacer les backlogs métier par les exemples génériques du paquet.

## 1. Sources et version chargée

| Élément | Constat |
|---|---|
| Source canonique | `C:/Users/xavie/Documents/Codex/2026-09-03/bo/outputs/equipe-agents-generique-v2.0.0` |
| Skill réellement chargé | `C:/Users/xavie/.codex/skills/equipe-projet-dsi/SKILL.md` |
| Version déclarée | `2.0.0`, importée le 2026-09-05 |
| Références canoniques | 43 fichiers dans `references/equipe` |
| Concordance live | 43/43 chemins et empreintes SHA-256 identiques à la source canonique |
| Adaptations Codex préservées | `SKILL.md`, `agents/openai.yaml`, `references/import-manifest.json` |
| Ancienne version du dispositif | 1.2.0, 29 fichiers dans la source historique |

Le chemin `C:/Users/xavie.codex/...` fourni dans la demande ne correspond pas au chemin installé observé. Le chemin effectif contient `/.codex/` et il est utilisé sans déplacer le skill.

## 2. Comparaison 1.2.0 vers 2.0.0

| Catégorie | Résultat |
|---|---|
| Inchangés | 12 fichiers |
| Modifiés par la V2 | 17 fichiers |
| Ajoutés par la V2 | 14 fichiers |
| Supprimés | Aucun |
| Remplacement à effectuer dans le skill | Aucun : l'installation correspond déjà à la V2 canonique |

Les ajouts V2 présents sont `HEPHAESTOS-DEV`, `HEPHAESTOS-FIX`, `CERBERUS-TECH`, `CERBERUS-FONCTIONNEL`, `CERBERUS-CYBER`, `AUTONOMOUS_DELIVERY`, `TEST_STRATEGY`, `CYBER_SOURCE_REGISTER`, l'enveloppe d'autonomie, le modèle d'élément de backlog et les rapports techniques, fonctionnels, cyber et d'itération.

## 3. Éléments DigiCheese préservés

- Branche `xavier` et HEAD `6790d40902c32f207923c8d174169e280cddadc9`.
- Travail local non commité : WP-01, réorganisation Wave 1, documents Wave 2, Obsidian, SQL, PDF et extractions.
- Dossier J1 et son contrôle documentaire, sans réexécution ni validation rétroactive.
- Décision D-06 / H0 : fusion minimale Data + DevOps, baseline Admin + Clients, stabilisation avant commandes, front hors H0, Wave 2 futur backlog non validé et rôles cumulables sous migration IAM séparée.
- Autorisation locale du 2026-09-05 limitée à la réalisation et aux contrôles locaux de WP-01 ; aucun commit, push, déploiement ou service distant.
- Résultats WP-01 : 51 tests réussis, 16 avertissements préexistants, Ruff et `pip check` réussis, réserve AC-11 sur GitHub Actions/MySQL/healthcheck.
- Inconnues, responsabilités, PPM, tolérances et validations institutionnelles laissés `À_CONFIRMER`.

Les documents J1, J2 et J5 antérieurs restent des traces historiques. La migration ajoute cette couche V2 sans attribuer rétroactivement leurs travaux aux nouveaux spécialistes.

## 4. Jalons reconstitués

| Jalon | État conservé après migration |
|---|---|
| J1 | Étude livrée et vérifiée documentairement |
| J2 | `GO_AVEC_RÉSERVES` décidé le 2026-09-05 |
| J3 | `ATTEINT_AVEC_RÉSERVES` constaté le 2026-09-05 ; Xavier décideur et pilote formel |
| J4 | `REPORTÉ` ; mode `SPRINTS` retenu ; mandat WP-01 consommé ; aucune nouvelle enveloppe |
| J5 | Preuves WP-01 préparées ; décision humaine `EN_ATTENTE` |
| J6 | `EN_ATTENTE`, aucun déploiement autorisé |
| J7 | `EN_ATTENTE` |
| J8 | `EN_ATTENTE` |

## 5. Rôles et séparation V2

| Flux V2 | Application au projet |
|---|---|
| HEPHAESTOS-DEV | Produit un élément `READY` et retourne `DEV_COMPLETE` sans s'auto-valider |
| CERBERUS-TECH | Rejoue séparément installation, lint, tests, intégration et non-régression applicables |
| CERBERUS-FONCTIONNEL | Vérifie séparément les critères et comportements observables sans déclarer l'acceptation business |
| CERBERUS-CYBER | Intervient seulement avec sources, cible et autorisation adaptées |
| CERBERUS | Consolide les portes pour une même version candidate |
| HEPHAESTOS-FIX | Corrige un rejet reproductible dans la limite de l'enveloppe, puis déclenche par ZEUS le rejeu technique et les contrôles impactés |

Le travail WP-01 a historiquement été produit par HEPHAESTOS et contrôlé par CERBERUS monolithique. Ses preuves restent utilisables, mais la migration ne les renomme pas rétroactivement en verdicts spécialisés V2.

## 6. Modes et boucle d'exécution

- `CYCLE_V` est disponible pour une séquence fortement dépendante suivie de campagnes de tests.
- `SPRINTS` est disponible pour des éléments indépendants suivant chacun le micro-cycle V2.
- Le mode DigiCheese reste `À_CONFIRMER`. Les mentions historiques de sprints ne valent pas décision, et le plan Wave 2 appartient à un backlog non validé.

Boucle désormais applicable à tout futur élément autorisé :

```text
READY
  -> HEPHAESTOS-DEV / DEV_COMPLETE
  -> CERBERUS-TECH
  -> CERBERUS-FONCTIONNEL
  -> CERBERUS-CYBER si applicable et autorisé
  -> CERBERUS / porte consolidée
  -> HEPHAESTOS-FIX puis rejeu en cas de rejet
  -> AUTO_NEXT seulement si toutes les portes passent pour la même version
```

L'[enveloppe H0](ENVELOPPE_AUTONOMIE_H0.md) décrit les permissions et limites actuelles. Elle ne crée aucune autorisation nouvelle.

## 7. Backlog et point de reprise

| Élément | État migré | Suite permise |
|---|---|---|
| WP-01 — configuration et tests reproductibles | Développement local achevé ; preuves historiques disponibles ; porte historique `PASS_WITH_RESERVATIONS` | Rejouer les contrôles locaux séparés couverts ; conserver AC-11 externe `À_CONFIRMER` |
| WP-02 — IAM | Candidat `PROPOSÉ`, critères et liste fermée incomplets | Aucun développement : non `READY` et non autorisé |
| Wave 1 | Backlog historique sans statut fiable élément par élément | Ne pas convertir les US en `DONE` sans preuve |
| Wave 2 | Futur backlog non validé | Aucun élément `READY` |

`AUTO_NEXT` n'est pas émis au moment de la migration : l'enveloppe multiélément n'est pas validée, aucun prochain élément n'est `READY` et autorisé, et les portes V2 séparées de WP-01 ne sont pas encore toutes consignées.

## 8. Cyber et contrôles obligatoires

- Sources cyber utilisateur : **`À_FOURNIR`**.
- Aucun verdict cyber formel n'est repris ou inventé.
- Aucun test intrusif, offensif, externe ou destructif n'est autorisé.
- Si un verdict cyber formel devient obligatoire avant adoption des sources et autorisations, le résultat attendu est `CYBER_BLOCKED`.
- Le screening SSI reste `EN_COURS` et distinct d'une campagne cyber.

## 9. Contrôles de migration

| Contrôle | Résultat |
|---|---|
| Validateur V2 | Version 2.0.0 ; 37 contrôles réussis ; 0 échec |
| Références internes du skill | 37/37 : aucune référence interne non résolue |
| UTF-8 et U+FFFD | 46 fichiers du skill et 43 fichiers source valides ; aucun U+FFFD |
| Plan comportemental V2 | 28 scénarios / 56 exécutions planifiées ; aucune exécution prouvée |
| CERBERUS-TECH WP-01 | `TECH_VERIFIED` sur `wp01-7d113810cc2d0216` ; rapport dédié produit |
| CERBERUS-FONCTIONNEL WP-01 | `FUNCTIONAL_VERIFIED` sur la même candidate ; aucune acceptation business déduite |
| CERBERUS-CYBER WP-01 | Aucun verdict demandé ou émis ; sources `À_FOURNIR` |
| Porte consolidée V2 | `NEEDS_DECISION` ; `QUALITY_GATE_PASSED` non émis ; `AUTO_NEXT` non autorisé |

Le validateur chargé explicitement en UTF-8 retourne **Version 2.0.0, Passed 37, Failed 0**. L'appel direct sous Windows PowerShell 5.1 peut interpréter le script UTF-8 sans BOM comme ANSI et produire un faux échec ; ce point de compatibilité amont reste `À_CONFIRMER` et le fichier canonique n'est pas modifié localement.

Version candidate WP-01 reprise sous V2 : `wp01-7d113810cc2d0216`, calculée à partir des contenus des neuf fichiers matériels du lot et de l'état de retrait de `.env` de l'index, sans inclure le contenu du secret local.

Rapports spécialisés : [technique](RAPPORT_TECHNIQUE_WP01.md), [fonctionnel](RAPPORT_FONCTIONNEL_WP01.md) et [porte consolidée](RAPPORT_PORTE_WP01.md).

## 10. Résultat de la reprise V2

CERBERUS a consolidé les rapports portant sur la même candidate :

```text
TECH_VERIFIED
+ FUNCTIONAL_VERIFIED
+ aucune régression critique détectée
+ périmètre inchangé
+ aucun verdict cyber applicable
+ AC-11 externe à-confirmer
= NEEDS_DECISION
```

`QUALITY_GATE_PASSED` et `AUTO_NEXT` ne sont pas émis. Aucune correction HEPHAESTOS-FIX n'est requise, car aucun défaut WP-01 n'a été observé. La limite provient des décisions et preuves manquantes, pas d'un échec applicatif.

## 11. Fichiers de migration ajoutés

| Fichier | Usage |
|---|---|
| `MIGRATION_DISPOSITIF_V2.md` | Comparaison, préservation, jalons, rôles, contrôles et point de reprise |
| `ENVELOPPE_AUTONOMIE_H0.md` | Transposition des permissions et limites, sans autorisation nouvelle |
| `RAPPORT_TECHNIQUE_WP01.md` | Verdict indépendant `TECH_VERIFIED` |
| `RAPPORT_FONCTIONNEL_WP01.md` | Verdict indépendant `FUNCTIONAL_VERIFIED` sans acceptation business |
| `RAPPORT_PORTE_WP01.md` | Consolidation `NEEDS_DECISION` et blocage `AUTO_NEXT` |

Aucun fichier du skill, du produit, du backlog métier ou des dossiers historiques J1/J2/J5 n'est remplacé par cette migration.

## 12. Prochaine décision utile

J2, J3 et J4 ont été régularisés sans effet rétroactif le 2026-09-05. Les contrôles AC-11 MySQL local et cyber minimal ont ensuite été exécutés sous autorisation ciblée. Le point de reprise est maintenant une nouvelle décision J5 sur WP-01. Le mandat local limité à WP-01 est consommé et `AUTO_NEXT` reste non autorisé.

Le [dossier de régularisation](../2026-09-05_REGULARISATION_J2_J3_J4/REGULARISATION_J2_J3_J4.md) et la [demande de décision consolidée](../2026-09-05_REGULARISATION_J2_J3_J4/DEMANDE_DECISION_CONSOLIDEE.md) détaillent les décisions distinctes, l'indépendance des contrôles, AC-11, l'applicabilité cyber et les options J5.
