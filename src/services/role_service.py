from sqlalchemy.orm import Session
from ..repositories.role_repository import RoleRepository
from ..schemas.role import RolePost, RolePatch


class RoleService:
    """Service pour gérer la logique role (avant repo)."""

    def __init__(self):
        self.repository = RoleRepository()

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, role_id: int):
        return self.repository.get_by_id(db, role_id)

    def create(self, db: Session, new_role: RolePost):
        data = new_role.model_dump()
        return self.repository.create(db, data)

    def patch(self, db: Session, role_id: int, role: RolePatch):
        data = role.model_dump(exclude_unset=True)
        return self.repository.patch(db, role_id, data)

    def delete(self, db: Session, role_id: int):
        return self.repository.delete(db, role_id)
