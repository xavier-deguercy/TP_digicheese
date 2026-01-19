from sqlmodel import Session
from src.models.poids import Poids


class PoidsRepository:
    """Repository class for managing poids operations in the database.

    Receive a dictionary from service, save it to the database and return the poids model to service."""
    
    def get_all_poids(self, db: Session):
        return list(db.query(Poids).all())
    
    def get_poids_by_id(self, db: Session, id: int):
        return db.query(Poids).get(id)
    
    def create_poids(self, db: Session, donnees_poids: dict):
        poids = Poids(**donnees_poids)
        db.add(poids)
        db.commit()
        db.refresh(poids)
        return poids
    
    def patch_poids(self, db: Session, id: int, donnees_poids: dict):
        poids = db.query(Poids).get(id)
        for key, value in donnees_poids.items():
            setattr(poids, key, value)
        db.commit()
        db.refresh(poids)
        return poids
    
    def delete_poids(self, db: Session, id: int):
        poids = db.query(Poids).get(id)
        db.delete(poids)
        db.commit()
        return poids