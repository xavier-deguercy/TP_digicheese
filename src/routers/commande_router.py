from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.commande_schema import CommandeOut, CommandePatch, CommandePost
from src.services.commande_service import CommandeService
from src.utils.dependencies import require_roles
from src.utils.roles import ROLE_ADMIN, ROLE_OP_COLIS


router = APIRouter(
    prefix="/commandes",
    tags=["CRUD Commandes (OP-Colis, Admin)"],
    dependencies=[Depends(require_roles(ROLE_ADMIN, ROLE_OP_COLIS))],
)
service = CommandeService()


@router.get("/", response_model=list[CommandeOut])
def get_commandes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip=skip, limit=limit)


@router.get("/{id_commande}", response_model=CommandeOut)
def get_commande(id_commande: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, id_commande)


@router.post("/", response_model=CommandeOut, status_code=201)
def create_commande(payload: CommandePost, db: Session = Depends(get_db)):
    return service.create(db, payload)


@router.patch("/{id_commande}", response_model=CommandeOut)
def patch_commande(
    id_commande: int,
    payload: CommandePatch,
    db: Session = Depends(get_db),
):
    return service.patch(db, id_commande, payload)


@router.delete("/{id_commande}", response_model=CommandeOut)
def delete_commande(id_commande: int, db: Session = Depends(get_db)):
    return service.delete(db, id_commande)
