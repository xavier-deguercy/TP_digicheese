from sqlalchemy.orm import Session
from src.models.commune import Commune

class CommuneRepository:
    """Repository class for managing commune operations in the database.

    Receive a dictionary from service, save it to the database and return the commune model to service."""
    
    def get_all_communes(self, db: Session):
        return list(db.query(Commune).all())
    
    def get_commune_by_id(self, db: Session, id: int):
        return db.query(Commune).get(id)
    
    def create_commune(self, db: Session, donnees_commune: dict):
        commune = Commune(**donnees_commune)
        db.add(commune)
        db.commit()
        db.refresh(commune)
        return commune
    
    def patch_commune(self,db: Session, id: int, donnees_commune: dict):
        commune = db.query(Commune).get(id)
        for key, value in donnees_commune.items():
            setattr(commune, key, value)
        db.commit()
        db.refresh(commune)
        return commune
    
    def delete_commune(self, db: Session, id: int):
        commune = db.query(Commune).get(id)
        db.delete(commune)
        db.commit
        return commune
    