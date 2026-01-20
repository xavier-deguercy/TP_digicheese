from sqlalchemy.orm import Session
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
        data = new_poids.model_dump()
        data = self.__traitement(data)
        return self.repository.create_poids(db,data)
    
    
    def patch_poids(self, db: Session, poids_id: int, poids: PoidsPatch):
        data = poids.model_dump(exclude_unset=True)
        data = self.__traitement(data)
        return self.repository.patch_poids(db, poids_id, data)
    
    
    def delete_poids(self, db: Session, poids_id: int):
        return self.repository.delete_poids(db, poids_id)