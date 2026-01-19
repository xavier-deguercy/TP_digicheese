# creation du service pour les objets
from sqlalchemy.orm import Session
from ..repositories import objet_repository as objet_repo
from ..schemas import objet_schema as objet_schema
from typing import Optional


class ObjetService:
    def __init__(self, db: Session):
        self.repository = objet_repo.ObjetRepository(db)

    def __traitement(self, client: dict):
        return client
    
    def get_objet(self, objet_id: int) -> Optional[objet_schema.ObjetOut]:
        objet = self.repository.get_objet(objet_id)
        if objet:
            return objet_schema.ObjetOut.from_orm(objet)
        return None

    def create_objet(self, objet_data: objet_schema.ObjetPost) -> objet_schema.ObjetOut:
        new_objet = self.repository.create_objet(objet_data)
        return objet_schema.ObjetOut.from_orm(new_objet)

    
       
    def create_objet(self, db: Session, new_objet: ClientPost):
        new_objet = new_objet.model_dump()
        new_objet = self.__traitement(new_objet)
        return self.repository.create_objet(db, new_objet)    

    def delete_objet(self, objet_id: int) -> bool:
        return self.repository.delete_objet(objet_id)