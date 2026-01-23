# src/routers/objet_router.py

"""
Endpoints Objets (Admin) — DIGICHEESE
Router (HTTP) -> Service (métier) -> Repository (DB)
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.objet_schema import ObjetCreate, ObjetPatch, ObjetOut
from src.services.objet_services import ObjetService
from src.utils.dependencies import require_roles

# Create a router for objet-related endpoints
router = APIRouter(
    prefix="/objets",
    tags=["CRUD Objets (Admin)"],
    dependencies=[Depends(require_roles("Admin"))]
)
# Initialize the objet service to have access to objet operations
service = ObjetService()

@router.get("/", response_model=list[ObjetOut], status_code=200)
def get_objets(db: Session = Depends(get_db)):

    """
    Liste tous les objets.
    """
    return service.get_all_objet(db)


@router.get("/{objet_id}",status_code=200, response_model=ObjetOut)
def get_objet(objet_id: int, db: Session = Depends(get_db)):

    # Récupère un objet par son id.

    objet = service.get_objet_by_id(db, objet_id)
    if objet is None:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return objet

@router.post("/", status_code=201, response_model=ObjetOut)
def create_objet(payload: ObjetCreate, db: Session = Depends(get_db)):
    """
    Crée un nouvel objet.
    """
    return service.create_objet(db, payload)

@router.patch("/{objet_id}", response_model=ObjetOut, status_code=200)
def patch_objet(objet_id: int, payload: ObjetPatch, db: Session = Depends(get_db)):
    """
    Met à jour partiellement un objet.
    """
    objet = service.get_objet_by_id(db, objet_id)
    if objet is None:
        raise HTTPException(status_code=404, detail="Objet non trouvé")

    return service.patch_objet(db, objet_id, payload)


@router.delete("/{objet_id}", response_model=ObjetOut, status_code=200)
def delete_objet(objet_id: int, db: Session = Depends(get_db)):
    """
    Supprime un objet.
    """
    objet = service.get_objet_by_id(db, objet_id)
    if objet is None:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return service.delete_objet(db, objet_id)
