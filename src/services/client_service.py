from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models.adresse import Adresse
from ..repositories.client_repository import ClientRepository
from ..schemas.client_schema import ClientPost, ClientPatch


class ClientService:
    """Service pour gérer la logique Client (avant repo)."""

    def __init__(self):
        self.repository = ClientRepository()

    def __adresse_exists(self, db: Session, id_adresse: int) -> bool:
        stmt = select(Adresse).where(Adresse.id_adresse == id_adresse)
        return db.scalars(stmt).first() is not None

    def __validate_adresses(self, db: Session, adresse1_id: Optional[int], adresse2_id: Optional[int]) -> None:
        if adresse1_id is not None and not self.__adresse_exists(db, adresse1_id):
            raise HTTPException(status_code=400, detail="adresse1_client: adresse inconnue")

        if adresse2_id is not None and not self.__adresse_exists(db, adresse2_id):
            raise HTTPException(status_code=400, detail="adresse2_client: adresse inconnue")

    def __validate_email_unique(self, db: Session, email: Optional[str], exclude_id: Optional[int] = None) -> None:
        if not email:
            return
        existing = self.repository.get_by_email(db, email)
        if existing is None:
            return
        if exclude_id is not None and existing.id_client == exclude_id:
            return
        raise HTTPException(status_code=400, detail="email_client: déjà utilisé")

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.get_all_detailed(db, skip=skip, limit=limit)
    
    def get_by_id(self, db: Session, id_client: int):
        client = self.repository.get_by_id_detailed(db, id_client)
        if client is None:
            raise HTTPException(status_code=404, detail="Client non trouvé")
        return client

    def create(self, db: Session, payload: ClientPost):
        # validations FK + email
        self.__validate_adresses(db, payload.adresse1_client, payload.adresse2_client)
        self.__validate_email_unique(db, payload.email_client)

        return self.repository.create(db, payload)

    def patch(self, db: Session, id_client: int, payload: ClientPatch):
        client = self.repository.get_by_id(db, id_client)
        if client is None:
            raise HTTPException(status_code=404, detail="Client non trouvé")

        data = payload.model_dump(exclude_unset=True)

        self.__validate_adresses(
            db,
            data.get("adresse1_client"),
            data.get("adresse2_client"),
        )

        if "email_client" in data:
            self.__validate_email_unique(db, data.get("email_client"), exclude_id=id_client)

        return self.repository.patch(db, client, payload)

    def delete(self, db: Session, id_client: int):
        client = self.repository.get_by_id(db, id_client)
        if client is None:
            raise HTTPException(status_code=404, detail="Client non trouvé")
        self.repository.delete(db, client)
        return client
