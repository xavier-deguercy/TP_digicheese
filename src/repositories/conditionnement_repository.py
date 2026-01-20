# src/repositories/conditionnement_repository.py
from sqlalchemy.orm import Session

from src.models.conditionnement import Conditionnement


class ConditionnementRepository:
    """Repository class for managing conditionnement operations in the database.

    Receive a dictionary from service, save it to the database and return the conditionnement model.
    """

    def get_all_conditionnements(self, db: Session):
        return list(db.query(Conditionnement).all())

    def get_conditionnement_by_id(self, db: Session, id: int):
        return db.query(Conditionnement).get(id)

    def create_conditionnement(self, db: Session, donnees_conditionnement: dict):
        cond = Conditionnement(**donnees_conditionnement)
        db.add(cond)
        db.commit()
        db.refresh(cond)
        return cond

    def patch_conditionnement(self, db: Session, id: int, donnees_conditionnement: dict):
        cond = db.query(Conditionnement).get(id)
        for key, value in donnees_conditionnement.items():
            setattr(cond, key, value)
        db.commit()
        db.refresh(cond)
        return cond

    def delete_conditionnement(self, db: Session, id: int):
        cond = db.query(Conditionnement).get(id)
        db.delete(cond)
        db.commit()
        return cond
