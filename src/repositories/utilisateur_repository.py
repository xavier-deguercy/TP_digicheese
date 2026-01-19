from sqlalchemy.orm import Session
from ..models.utilisateur import Utilisateur


class UtilisateurRepository:
    """Repository pour gérer les opérations DB sur les utilisateurs."""

    def get_all(self, db: Session):
        return list(db.query(Utilisateur).all())

    def get_by_id(self, db: Session, user_id: int):
        return db.get(Utilisateur, user_id)

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
