from sqlalchemy.orm import Session
from ..models.role import Role


class RoleRepository:
    """Repository pour gérer les opérations DB sur les rôles."""

    def get_all(self, db: Session):
        return list(db.query(Role).all())

    def get_by_id(self, db: Session, role_id: int):
        return db.get(Role, role_id)

    def create(self, db: Session, data: dict):
        role = Role(**data)
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def patch(self, db: Session, role_id: int, data: dict):
        role = db.get(Role, role_id)
        if not role:
            return None
        for key, value in data.items():
            setattr(role, key, value)
        db.commit()
        db.refresh(role)
        return role

    def delete(self, db: Session, role_id: int):
        role = db.get(Role, role_id)
        if not role:
            return None
        db.delete(role)
        db.commit()
        return role
