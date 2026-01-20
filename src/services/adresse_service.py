from sqlalchemy.orm import Session
from src.repositories.adresse_repository import AdresseRepository
from src.schemas.adresse_schema import AdressePatch, AdressePost


class AdresseService:
    """Service class for managing adresse operation.
    Receive a schema from router and return a dictionary to repository."""

    def __init__(self):
        self.repository = AdresseRepository()

    def __traitement(self, adresse: dict):
        return adresse 
    
    def get_all_adresses(self, db: Session):
        return self.repository.get_all_adresses(db)

    def get_adresse_by_id(self,db: Session, id_adresse: int):
        return self.repository.get_adresse_by_id(db, id_adresse)

    def create_adresse(self,db: Session,new_adresse: AdressePost):
        new_adresse = new_adresse.model_dump()
        new_adresse = self.__traitement(new_adresse)
        return self.repository.creat_adresse(db, new_adresse)
    
    def patch_adresse(self, db: Session, id_adresse: int, adresse: AdressePatch):
        adresse = adresse.model_dump(exclude_unset = True)
        adresse = self. __traitement(adresse)
        return self.repository.patch_adresse(db, id_adresse, adresse)
    
    def delete_adresse(self, db: Session, id_adresse: int):
        return self.repository.delete_adresse(db,id_adresse)
    
