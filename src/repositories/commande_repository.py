from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.commande import Commande
from src.schemas.commande_schema import CommandePost


class CommandeRepository:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Commande]:
        stmt = select(Commande).order_by(Commande.id_commande).offset(skip).limit(limit)
        return list(db.scalars(stmt).all())

    @staticmethod
    def get_by_id(db: Session, id_commande: int) -> Optional[Commande]:
        stmt = select(Commande).where(Commande.id_commande == id_commande)
        return db.scalars(stmt).first()

    @staticmethod
    def create(db: Session, payload: CommandePost) -> Commande:
        commande = Commande(**payload.model_dump())
        db.add(commande)
        db.commit()
        db.refresh(commande)
        return commande

    @staticmethod
    def patch(db: Session, commande: Commande, data: dict) -> Commande:
        for field, value in data.items():
            setattr(commande, field, value)
        db.commit()
        db.refresh(commande)
        return commande

    @staticmethod
    def delete(db: Session, commande: Commande) -> None:
        db.delete(commande)
        db.commit()
