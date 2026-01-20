from sqlalchemy.orm import Session

from src.repositories.commune_repository import CommuneRepository
from src.schemas.commune_schema import CommunePatch, CommunePost
#from ..repositories import CommuneRepository
#from ..schemas import CommunePost, CommunePatch

class CommuneService:
    """Service class for managing commune operation.
    Receive a schema from router and return a dictionary to repository."""

    def __init__(self):
        self.repository = CommuneRepository()

    def __traitement(self, commune: dict):
        return commune 
    
    def get_all_communes(self, db: Session):
        return self.repository.get_all_communes(db)

    def get_commune_by_id(self,db: Session, id_commune: int):
        return self.repository.get_commune_by_id(db, id_commune)

    def create_commune(self,db: Session,new_commune: CommunePost):
        new_commune = new_commune.model_dump()
        new_commune = self.__traitement(new_commune)
        return self.repository.creat_commune(db, new_commune)
    
    def patch_commune(self, db: Session, id_commune: int, commune: CommunePatch):
        commune = commune.model_dump(exclude_unset = True)
        commune = self. __traitement(commune)
        return self.repository.patch_commune(db, id_commune, commune)
    
    def delete_commune(self, db: Session, id_commune: int):
        return self.repository.delete_commune(db,id_commune)
    
