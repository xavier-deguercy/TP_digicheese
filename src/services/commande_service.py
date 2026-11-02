from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.client import Client
from src.models.conditionnement import Conditionnement
from src.models.detail_commande import DetailCommande
from src.repositories.commande_repository import CommandeRepository
from src.schemas.commande_schema import CommandePatch, CommandePost


class CommandeService:
    def __init__(self) -> None:
        self.repository = CommandeRepository()

    @staticmethod
    def _client_exists(db: Session, id_client: int) -> bool:
        return db.scalar(select(Client.id_client).where(Client.id_client == id_client)) is not None

    @staticmethod
    def _conditionnement_exists(db: Session, id_conditionnement: int) -> bool:
        stmt = select(Conditionnement.id_condit).where(
            Conditionnement.id_condit == id_conditionnement
        )
        return db.scalar(stmt) is not None

    def _validate_references(
        self,
        db: Session,
        id_client: int | None,
        id_conditionnement: int | None,
    ) -> None:
        if id_client is not None and not self._client_exists(db, id_client):
            raise HTTPException(status_code=400, detail="id_client: client inconnu")
        if id_conditionnement is not None and not self._conditionnement_exists(
            db, id_conditionnement
        ):
            raise HTTPException(
                status_code=400,
                detail="id_conditionnement: conditionnement inconnu",
            )

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return self.repository.get_all(db, skip=skip, limit=limit)

    def get_by_id(self, db: Session, id_commande: int):
        commande = self.repository.get_by_id(db, id_commande)
        if commande is None:
            raise HTTPException(status_code=404, detail="Commande non trouvée")
        return commande

    def create(self, db: Session, payload: CommandePost):
        self._validate_references(db, payload.id_client, payload.id_conditionnement)
        return self.repository.create(db, payload)

    def patch(self, db: Session, id_commande: int, payload: CommandePatch):
        commande = self.get_by_id(db, id_commande)
        data = payload.model_dump(exclude_unset=True)

        if commande.b_archive and data != {"b_archive": False}:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Une commande archivée doit être désarchivée avant modification",
            )

        self._validate_references(
            db,
            data.get("id_client"),
            data.get("id_conditionnement"),
        )

        if (
            "id_conditionnement" in data
            and data["id_conditionnement"] != commande.id_conditionnement
        ):
            data["nb_colis"] = None

        return self.repository.patch(db, commande, data)

    def delete(self, db: Session, id_commande: int):
        commande = self.get_by_id(db, id_commande)
        if commande.b_archive:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Une commande archivée ne peut pas être supprimée",
            )
        detail_id = db.scalar(
            select(DetailCommande.id_detail_commande)
            .where(DetailCommande.id_commande == id_commande)
            .limit(1)
        )
        if detail_id is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Une commande contenant des lignes ne peut pas etre supprimee",
            )
        self.repository.delete(db, commande)
        return commande
