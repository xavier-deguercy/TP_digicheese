from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Optional
from ..models.utilisateur import Utilisateur


class UtilisateurRepository:
    """Repository pour gérer les opérations DB sur les utilisateurs."""

    def get_all(self, db: Session):
        return list(db.query(Utilisateur).all())

    @staticmethod
    def get_by_id(self, db: Session, user_id: int):
        return db.get(Utilisateur, user_id)

    @staticmethod
    def get_by_api_key(db: Session, api_key: str) -> Optional[Utilisateur]:
        stmt = select(Utilisateur).where(Utilisateur.api_key == api_key)
        return db.scalars(stmt).first()

    def create(self, db: Session, data: dict):
        user = Utilisateur(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def patch(self, db: Session, user_id: int, data: dict):
        user = db.get(Utilisateur, user_id)
        if not user:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user_id: int):
        user = db.get(Utilisateur, user_id)
        if not user:
            return None
        db.delete(user)
        db.commit()
        return user
