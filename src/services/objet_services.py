# creation du service pour les objets
from sqlalchemy.orm import Session
from ..repositories.objet_repository import ObjetRepository 
from ..schemas.objet_schema import ObjetBase, ObjetPatch



class ObjetService:
    def __init__(self, db: Session):
        self.repository = ObjetRepository(db)

    def __traitement(self, objet: dict):
        return objet
    
    def get_all_objet(self, db: Session):
        return self.repository.get_all_objet(db)
    
    def get_objet_by_id(self, db: Session, objet_id: int):
        return self.repository.get_objet_by_id(db, objet_id)   
  
    def create_objet(self, db: Session, new_objet: ObjetBase):
        new_objet = new_objet.model_dump()
        new_objet = self.__traitement(new_objet)
        return self.repository.create_objet(db, new_objet)    

    def patch_objet(self, db: Session, objet_id: int, objet: ObjetPatch):
        objet = objet.model_dump(exclude_unset=True)
        objet = self.__traitement(objet)
        return self.repository.patch_objet(db, objet_id, objet)

    def delete_objet(self, db: Session, objet_id: int):
        return self.repository.delete_objet(db, objet_id)
