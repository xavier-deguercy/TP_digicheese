from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.models.commande import Commande
from src.models.objet import Objet
from src.repositories.detail_commande_repository import DetailCommandeRepository
from src.schemas.detail_commande_schema import (
    DetailCommandePatch,
    DetailCommandePost,
)


class DetailCommandeService:
    def __init__(self) -> None:
        self.repository = DetailCommandeRepository()

    @staticmethod
    def _get_commande(db: Session, id_commande: int) -> Commande:
        commande = db.get(Commande, id_commande)
        if commande is None:
            raise HTTPException(status_code=404, detail="Commande non trouvee")
        return commande

    @staticmethod
    def _get_objet(db: Session, id_objet: int) -> Objet:
        objet = db.get(Objet, id_objet)
        if objet is None:
            raise HTTPException(status_code=404, detail="Objet non trouve")
        return objet

    @staticmethod
    def _ensure_commande_writable(commande: Commande) -> None:
        if commande.b_archive:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Une commande archivee doit etre desarchivee avant modification de ses lignes",
            )

    def _ensure_unique(
        self,
        db: Session,
        id_commande: int,
        id_objet: int,
        exclude_id: int | None = None,
    ) -> None:
        existing = self.repository.get_by_commande_and_objet(
            db,
            id_commande,
            id_objet,
            exclude_id=exclude_id,
        )
        if existing is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Cet objet est deja present dans la commande",
            )

    def get_all(
        self,
        db: Session,
        commande_id: int | None = None,
        skip: int = 0,
        limit: int = 100,
    ):
        if commande_id is not None:
            self._get_commande(db, commande_id)
        return self.repository.get_all(
            db,
            commande_id=commande_id,
            skip=skip,
            limit=limit,
        )

    def get_by_id(self, db: Session, id_detail_commande: int):
        detail = self.repository.get_by_id(db, id_detail_commande)
        if detail is None:
            raise HTTPException(
                status_code=404,
                detail="Detail de commande non trouve",
            )
        return detail

    def create(self, db: Session, payload: DetailCommandePost):
        commande = self._get_commande(db, payload.id_commande)
        self._ensure_commande_writable(commande)
        objet = self._get_objet(db, payload.id_objet)
        if objet.indisp_obj:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Un objet indisponible ne peut pas etre ajoute",
            )
        self._ensure_unique(db, payload.id_commande, payload.id_objet)

        try:
            detail = self.repository.create(db, payload.model_dump())
            commande.nb_colis = None
            db.commit()
            db.refresh(detail)
            return detail
        except IntegrityError as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Cet objet est deja present dans la commande",
            ) from exc

    def patch(
        self,
        db: Session,
        id_detail_commande: int,
        payload: DetailCommandePatch,
    ):
        detail = self.get_by_id(db, id_detail_commande)
        commande = self._get_commande(db, detail.id_commande)
        self._ensure_commande_writable(commande)
        data = payload.model_dump(exclude_unset=True)
        if not data:
            return detail

        new_objet_id = data.get("id_objet", detail.id_objet)
        if new_objet_id != detail.id_objet:
            objet = self._get_objet(db, new_objet_id)
            if objet.indisp_obj:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Un objet indisponible ne peut pas etre ajoute",
                )
            self._ensure_unique(
                db,
                detail.id_commande,
                new_objet_id,
                exclude_id=detail.id_detail_commande,
            )

        try:
            self.repository.patch(detail, data)
            commande.nb_colis = None
            db.commit()
            db.refresh(detail)
            return detail
        except IntegrityError as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Cet objet est deja present dans la commande",
            ) from exc

    def delete(self, db: Session, id_detail_commande: int):
        detail = self.get_by_id(db, id_detail_commande)
        commande = self._get_commande(db, detail.id_commande)
        self._ensure_commande_writable(commande)
        self.repository.delete(db, detail)
        commande.nb_colis = None
        db.commit()
        return detail
