from sqlalchemy.orm import Session
from src.models.poidsv import Poidsv


class PoidsvRepository:
    """Repository class for managing poids-vignettes operations in the database.

    Receive a dictionary from service, save it to the database and return the poids-vignettes model to service."""
    
    def get_all_poidsv(self, db: Session):
        return list(db.query(Poidsv).all())
    
    def get_poidsv_by_id(self, db: Session, id: int):
        return db.get(Poidsv,id)
    
    def create_poidsv(self, db: Session, donnees_poidsv: dict):
        poidsv = Poidsv(**donnees_poidsv)
        db.add(poidsv)
        db.commit()
        db.refresh(poidsv)
        return poidsv
    
    def patch_poidsv(self, db: Session, id: int, donnees_poidsv: dict):
        poidsv = db.get(Poidsv,id)
        if not poidsv:
            return None
        for key, value in donnees_poidsv.items():
            setattr(poidsv, key, value)
        db.commit()
        db.refresh(poidsv)
        return poidsv
    
    def delete_poidsv(self, db: Session, id: int):
        poidsv = db.get(Poidsv,id)
        if not poidsv:
            return None
        db.delete(poidsv)
        db.commit()
        return poidsv