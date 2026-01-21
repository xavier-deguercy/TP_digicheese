# src/repositories/conditionnement_repository.py

from typing import Optional
from sqlalchemy.orm import Session

from src.models.conditionnement import Conditionnement


class ConditionnementRepository:
    """Repository class for managing conditionnement operations in the database.

    Receive a dictionary from service, save it to the database and return the conditionnement model.
    """

    def get_all_conditionnements(self, db: Session) -> list[Conditionnement]:
        return list(db.query(Conditionnement).all())

    def get_conditionnement_by_id(self, db: Session, id: int) -> Optional[Conditionnement]:
        # SQLAlchemy 2.x friendly
        return db.get(Conditionnement, id)

    def create_conditionnement(self, db: Session, donnees_conditionnement: dict) -> Conditionnement:
        cond = Conditionnement(**donnees_conditionnement)
        db.add(cond)
        db.commit()
        db.refresh(cond)
        return cond

    def patch_conditionnement(self, db: Session, id: int, donnees_conditionnement: dict) -> Optional[Conditionnement]:
        cond = db.get(Conditionnement, id)
        if cond is None:
            return None

        for key, value in donnees_conditionnement.items():
            setattr(cond, key, value)

        db.commit()
        db.refresh(cond)
        return cond

    def delete_conditionnement(self, db: Session, id: int) -> Optional[Conditionnement]:
        cond = db.get(Conditionnement, id)
        if cond is None:
            return None

        db.delete(cond)
        db.commit()
        return cond
