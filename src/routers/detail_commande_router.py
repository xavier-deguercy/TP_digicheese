from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.detail_commande_schema import (
    DetailCommandeOut,
    DetailCommandePatch,
    DetailCommandePost,
)
from src.services.detail_commande_service import DetailCommandeService
from src.utils.dependencies import require_roles
from src.utils.roles import ROLE_ADMIN, ROLE_OP_COLIS


router = APIRouter(
    prefix="/details-commandes",
    tags=["CRUD Details commandes (OP-Colis, Admin)"],
    dependencies=[Depends(require_roles(ROLE_ADMIN, ROLE_OP_COLIS))],
)
service = DetailCommandeService()


@router.get("/", response_model=list[DetailCommandeOut])
def get_details_commandes(
    commande_id: int | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return service.get_all(
        db,
        commande_id=commande_id,
        skip=skip,
        limit=limit,
    )


@router.get("/{id_detail_commande}", response_model=DetailCommandeOut)
def get_detail_commande(
    id_detail_commande: int,
    db: Session = Depends(get_db),
):
    return service.get_by_id(db, id_detail_commande)


@router.post("/", response_model=DetailCommandeOut, status_code=201)
def create_detail_commande(
    payload: DetailCommandePost,
    db: Session = Depends(get_db),
):
    return service.create(db, payload)


@router.patch("/{id_detail_commande}", response_model=DetailCommandeOut)
def patch_detail_commande(
    id_detail_commande: int,
    payload: DetailCommandePatch,
    db: Session = Depends(get_db),
):
    return service.patch(db, id_detail_commande, payload)


@router.delete("/{id_detail_commande}", response_model=DetailCommandeOut)
def delete_detail_commande(
    id_detail_commande: int,
    db: Session = Depends(get_db),
):
    return service.delete(db, id_detail_commande)
