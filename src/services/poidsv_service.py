from sqlmodel import Session
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
    
    
    def create_poidsv(self, db: Session, new_poids: PoidsvPost):
        new_poidsv = new_poidsv.model_dump()
        new_poidsv = self.__traitement(new_poidsv)
        return self.repository.create_poidsv(db, new_poidsv)
    
    
    def patch_poidsv(self, db: Session, poidsv_id: int, poids: PoidsvPatch):
        poidsv = poidsv.model_dump(exclude_unset=True)
        poidsv = self.__traitement(poidsv)
        return self.repository.patch_poidsv(db, poidsv_id, poidsv)
    
    
    def delete_poidsv(self, db: Session, poidsv_id: int):
        return self.repository.delete_poidsv(db, poidsv_id)