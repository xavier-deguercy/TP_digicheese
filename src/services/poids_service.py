from sqlmodel import Session
from src.repositories.poids_repository import PoidsRepository
from src.schemas.poids_schema import PoidsPatch, PoidsPost


class PoidsService:
    """Service class for managing poids operations.
    
    Receive a schema from router and return a dictionary to repository."""

    def __init__(self):
        self.repository = PoidsRepository()
    
    def __traitement(self, poids: dict):
        return poids
    
    
    def get_all_poids(self, db: Session):
        return self.repository.get_all_poids(db)
    
    
    def get_poids_by_id(self, db: Session, poids_id: int):
        return self.repository.get_poids_by_id(db, poids_id)
    
    
    def create_poids(self, db: Session, new_poids: PoidsPost):
        new_poids = new_poids.model_dump()
        new_poids = self.__traitement(new_poids)
        return self.repository.create_poids(db, new_poids)
    
    
    def patch_poids(self, db: Session, poids_id: int, poids: PoidsPatch):
        poids = poids.model_dump(exclude_unset=True)
        poids = self.__traitement(poids)
        return self.repository.patch_poids(db, poids_id, poids)
    
    
    def delete_poids(self, db: Session, poids_id: int):
        return self.repository.delete_poids(db, poids_id)