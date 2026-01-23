import secrets
from sqlalchemy.orm import Session
from ..repositories.utilisateur_repository import UtilisateurRepository
from ..schemas.utilisateur import UtilisateurPost, UtilisateurPatch
from src.utils.password import hash_password



class UtilisateurService:
    """Service pour gérer la logique utilisateur (avant repo)."""

    def __init__(self):
        self.repository = UtilisateurRepository()

    def __traitement_create(self, data: dict) -> dict:
        pwd = data.pop("password")
        data["hashed_password"] = hash_password(pwd)
        data["api_key"] = secrets.token_hex(32)
        return data

    def __traitement_patch(self, data: dict) -> dict:
        if "password" in data:
            password = data.pop("password")
            data["hashed_password"] = hash_password(password)
        return data

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, user_id: int):
        return self.repository.get_by_id(db, user_id)

    def create(self, db: Session, new_user: UtilisateurPost):
        data = new_user.model_dump()
        data = self.__traitement_create(data)
        return self.repository.create(db, data)

    def patch(self, db: Session, user_id: int, user: UtilisateurPatch):
        data = user.model_dump(exclude_unset=True)
        data = self.__traitement_patch(data)
        return self.repository.patch(db, user_id, data)

    def delete(self, db: Session, user_id: int):
        return self.repository.delete(db, user_id)
