# src\services\objet_services.py
# # creation du service pour les objets
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models.detail_commande import DetailCommande
from ..repositories.objet_repository import ObjetRepository 
from ..schemas.objet_schema import ObjetCreate, ObjetPatch



class ObjetService:
    def __init__(self):
        self.repository = ObjetRepository()

    def __traitement(self, objet: dict):
        return objet
    
    def get_all_objet(self, db: Session):
        return self.repository.get_all_objet(db)
    
    def get_objet_by_id(self, db: Session, objet_id: int):
        return self.repository.get_objet_by_id(db, objet_id)   

    def create_objet(self, db: Session, new_objet: ObjetCreate):
        new_objet = new_objet.model_dump()
        new_objet = self.__traitement(new_objet)
        return self.repository.create_objet(db, new_objet)    

    def patch_objet(self, db: Session, objet_id: int, objet: ObjetPatch):
        objet = objet.model_dump(exclude_unset=True)
        objet = self.__traitement(objet)
        return self.repository.patch_objet(db, objet_id, objet)

    def delete_objet(self, db: Session, objet_id: int):
        detail_id = db.scalar(
            select(DetailCommande.id_detail_commande)
            .where(DetailCommande.id_objet == objet_id)
            .limit(1)
        )
        if detail_id is not None:
            raise HTTPException(
                status_code=409,
                detail="Objet utilise par une ligne de commande",
            )
        return self.repository.delete_objet(db, objet_id)
