from sqlalchemy.orm import Session
from src.models.adresse import Adresse

class AdresseRepository:
    """Repository class for managing adresse operations in the database.

    Receive a dictionary from service, save it to the database and return the adresse model to service."""
    
    def get_all_adresses(self, db: Session):
        return list(db.query(Adresse).all())
    
    def get_adresse_by_id(self, db: Session, id_adresse: int):
        return db.get(Adresse, id_adresse)
    
    def create_adresse(self, db: Session, donnees_adresse: dict):
        adresse = Adresse(**donnees_adresse)
        db.add(adresse)
        db.commit()
        db.refresh(adresse)
        return adresse
    
    def patch_adresse(self,db: Session, id_adresse: int, donnees_adresse: dict):
        adresse = db.get(Adresse, id_adresse)
        if not adresse:
            return None
        for key, value in donnees_adresse.items():
            setattr(adresse, key, value)
        db.commit()
        db.refresh(adresse)
        return adresse
    
    def delete_adresse(self, db: Session, id_adresse: int):
        adresse = db.get(Adresse, id_adresse)
        db.delete(adresse)
        db.commit()
        return adresse
    