from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.detail_commande import DetailCommande


class DetailCommandeRepository:
    @staticmethod
    def get_all(
        db: Session,
        commande_id: int | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[DetailCommande]:
        stmt = select(DetailCommande).order_by(
            DetailCommande.id_detail_commande
        )
        if commande_id is not None:
            stmt = stmt.where(DetailCommande.id_commande == commande_id)
        stmt = stmt.offset(skip).limit(limit)
        return list(db.scalars(stmt).all())

    @staticmethod
    def get_by_id(
        db: Session,
        id_detail_commande: int,
    ) -> Optional[DetailCommande]:
        return db.get(DetailCommande, id_detail_commande)

    @staticmethod
    def get_by_commande_and_objet(
        db: Session,
        id_commande: int,
        id_objet: int,
        exclude_id: int | None = None,
    ) -> Optional[DetailCommande]:
        stmt = select(DetailCommande).where(
            DetailCommande.id_commande == id_commande,
            DetailCommande.id_objet == id_objet,
        )
        if exclude_id is not None:
            stmt = stmt.where(
                DetailCommande.id_detail_commande != exclude_id
            )
        return db.scalars(stmt).first()

    @staticmethod
    def create(db: Session, data: dict) -> DetailCommande:
        detail = DetailCommande(**data)
        db.add(detail)
        return detail

    @staticmethod
    def patch(detail: DetailCommande, data: dict) -> DetailCommande:
        for field, value in data.items():
            setattr(detail, field, value)
        return detail

    @staticmethod
    def delete(db: Session, detail: DetailCommande) -> None:
        db.delete(detail)
