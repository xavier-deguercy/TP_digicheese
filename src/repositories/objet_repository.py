# src/repositories/objet_repository.py
from ..models.objet import Objet # import the Objet model
from sqlalchemy.orm import Session
from typing import Optional



class ObjetRepository:



    def get_all_objet(self, db: Session) -> list[Objet]:
        return list(db.query(Objet).all())

    def get_objet_by_id(self, db: Session, id: int) -> Optional[Objet]:
        return db.get(Objet, id)

    
    def create_objet(self, db: Session, objet_data: dict) -> Objet:
        objet = Objet(**objet_data)
        db.add(objet)
        db.commit()
        db.refresh(objet)
        return objet
    
    def patch_objet(self, db: Session, id: int, donnees_objet: dict) -> Optional[Objet]:
        """
        Met à jour partiellement un objet (PATCH).

        Version robuste :
        - on refuse de modifier certains champs sensibles (ex. identifiant),
        - on limite les champs modifiables à une liste blanche (optionnel mais conseillé),
        - on rollback en cas d'erreur SQL (évite de "casser" la session).
        """

        objet = db.get(Objet, id)
        if objet is None:
            return None

        # --- Option de robustesse (proposée pour éviter les mises à jour "trop permissives") ---
        # Sans filtrage, n'importe quelle clé du dict serait appliquée via setattr().
        # Dans un TP, ça passe souvent. En prod, on préfère verrouiller :
        # - Empêcher la modification de la PK / champs système
        # - Ne mettre à jour que les champs explicitement autorisés
        allowed_fields = {
            "nom_obj",
            "taille_obj",
            "prix_obj",
            "poids_obj",
            "indisp_obj",
            "points_obj",
        }

        # On ne touche jamais à la clé primaire (au cas où elle arrive dans le payload)
        donnees_objet.pop("id_obj", None)
        donnees_objet.pop("id", None)

        # On applique uniquement les champs autorisés + ceux qui ne sont pas None
        # (si tu veux autoriser de mettre un champ à None, supprime le test "is not None")
        for key, value in donnees_objet.items():
            if key in allowed_fields and value is not None:
                setattr(objet, key, value)

        try:
            db.commit()
        except Exception:
            # Option de robustesse : on rollback pour éviter de laisser la session dans un état invalide
            db.rollback()
            raise

        db.refresh(objet)
        return objet


#def patch_objet originelle (moins robuste)

#    def patch_objet(self, db: Session, id: int, donnees_objet: dict) -> Optional[Objet]:
#        objet = db.get(Objet, id)
#        if objet is None:
#            return None

#        for key, value in donnees_objet.items():
#            setattr(objet, key, value)

#        db.commit()
#        db.refresh(objet)
#        return objet

    def delete_objet(self, db: Session, id: int) -> Optional[Objet]:
        objet = db.get(Objet, id)
        if objet is None:
            return None

        db.delete(objet)
        db.commit()
        return objet