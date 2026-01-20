from sqlalchemy.orm import Session
from src.models import poidsv
from src.repositories.poidsv_repository import PoidsvRepository
from src.schemas.poidsv_schema import PoidsvPatch, PoidsvPost



class PoidsvService:
    """Service class for managing poids-Vignettes operations.
    
    Receive a schema from router and return a dictionary to repository."""

    def __init__(self):
        self.repository = PoidsvRepository()
    
    def __traitement(self, poidsv: dict):
        return poidsv
    
    
    def get_all_poidsv(self, db: Session):
        return self.repository.get_all_poidsv(db)
    
    
    def get_poidsv_by_id(self, db: Session, poidsv_id: int):
        return self.repository.get_poidsv_by_id(db, poidsv_id)
    
    
    def create_poidsv(self, db: Session, new_poidsv: PoidsvPost):
        data = new_poidsv.model_dump()
        data = self.__traitement(data)
        return self.repository.create_poidsv(db,data)
    
    
    def patch_poidsv(self, db: Session, poidsv_id: int, poids: PoidsvPatch):
        data = poidsv.model_dump(exclude_unset=True)
        data = self.__traitement(data)
        return self.repository.patch_poidsv(db, poidsv_id, data)
    
    def delete_poidsv(self, db: Session, poidsv_id: int):
        return self.repository.delete_poidsv(db, poidsv_id)