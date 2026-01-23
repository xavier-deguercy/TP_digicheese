from typing import Optional, List
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select

from src.models.client import Client
from src.models.adresse import Adresse
from src.schemas.client_schema import ClientPost, ClientPatch


class ClientRepository:

    @staticmethod
    def get_all_detailed(db: Session, skip: int = 0, limit: int = 100) -> List[Client]:
        stmt = (
            select(Client)
            .offset(skip)
            .limit(limit)
            .options(
                selectinload(Client.adresse1).selectinload(Adresse.commune),
                selectinload(Client.adresse2).selectinload(Adresse.commune),
            )
        )
        return list(db.scalars(stmt).all())

    @staticmethod
    def get_by_id(db: Session, id_client: int) -> Optional[Client]:
        stmt = select(Client).where(Client.id_client == id_client)
        return db.scalars(stmt).first()

    @staticmethod
    def get_by_email(db: Session, email_client: str) -> Optional[Client]:
        stmt = select(Client).where(Client.email_client == email_client)
        return db.scalars(stmt).first()

    @staticmethod
    def get_by_id_detailed(db: Session, id_client: int) -> Optional[Client]:
        stmt = (
            select(Client)
            .where(Client.id_client == id_client)
            .options(
                selectinload(Client.adresse1).selectinload(Adresse.commune),
                selectinload(Client.adresse2).selectinload(Adresse.commune),
            )
        )
        return db.scalars(stmt).first()

    @staticmethod
    def create(db: Session, payload: ClientPost) -> Client:
        client = Client(**payload.model_dump())
        db.add(client)
        db.commit()
        db.refresh(client)
        return client

    @staticmethod
    def patch(db: Session, client: Client, payload: ClientPatch) -> Client:
        data = payload.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(client, key, value)

        db.commit()
        db.refresh(client)
        return client

    @staticmethod
    def delete(db: Session, client: Client) -> None:
        db.delete(client)
        db.commit()
