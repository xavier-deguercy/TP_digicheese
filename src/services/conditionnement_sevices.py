# src/services/conditionnement_service.py
from sqlalchemy.orm import Session

from src.repositories.conditionnement_repository import ConditionnementRepository
from src.schemas.conditionnement_schema import ConditionnementPost, ConditionnementPatch


class ConditionnementService:
    """Service class for managing conditionnement operations.

    Receive a schema from router and return a dictionary to repository.
    """

    def __init__(self):
        self.repository = ConditionnementRepository()

    def __traitement(self, Conditionnement: dict):
        return Conditionnement
    
    def get_all_conditionnements(self, db: Session):
        return self.repository.get_all_conditionnements(db)

    def get_conditionnement_by_id(self, db: Session, condit_id: int):
        return self.repository.get_conditionnement_by_id(db, condit_id)

    def create_conditionnement(self, db: Session, payload: ConditionnementPost):
        donnees = payload.model_dump()
        donnees = self.__traitement(donnees)
        return self.repository.create_conditionnement(db, donnees)

    def patch_conditionnement(self, db: Session, condit_id: int, payload: ConditionnementPatch):
        donnees = payload.model_dump(exclude_unset=True)
        donnees = self.__traitement(donnees)
        return self.repository.patch_conditionnement(db, condit_id, donnees)

    def delete_conditionnement(self, db: Session, condit_id: int):
        return self.repository.delete_conditionnement(db, condit_id)
