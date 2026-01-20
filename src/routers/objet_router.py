# src/routers/objet_router.py

"""
Endpoints Objets (Admin) — DIGICHEESE
Router (HTTP) -> Service (métier) -> Repository (DB)
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.schemas.objet_schema import ObjetBase, ObjetPatch, ObjetOut
from src.services.objet_services import ObjetService

router = APIRouter(prefix="/api/v1/admin/objets", tags=["Admin - Objets"])


@router.get("/", response_model=list[ObjetOut], status_code=200)
def get_objets(db: Session = Depends(get_db)):
    """
    Liste tous les objets.
    """
    service = ObjetService()
    return service.get_all_objet(db)


@router.get("/{objet_id}", response_model=ObjetOut, status_code=200)
def get_objet(objet_id: int, db: Session = Depends(get_db)):
    """
    Récupère un objet par son id.
    """
    service = ObjetService()
    objet = service.get_objet(db, objet_id)
    if objet is None:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return objet


@router.post("/", status_code=201, response_model=ObjetOut)
def create_objet(payload: ObjetBase, db: Session = Depends(get_db)):
    """
    Crée un nouvel objet.
    """
    service = ObjetService()
    return service.create_objet(db, payload)

@router.patch("/{objet_id}", response_model=ObjetOut, status_code=200)
def patch_objet(objet_id: int, payload: ObjetPatch, db: Session = Depends(get_db)):
    """
    Met à jour partiellement un objet.
    """
    service = ObjetService()
    # 
    objet = service.get_objet_by_id(db, objet_id) 
    if objet is None:
        raise HTTPException(status_code=404, detail="Objet non trouvé")

    return service.patch_objet(db, objet_id, payload)


@router.delete("/{objet_id}", response_model=ObjetOut, status_code=200)
def delete_objet(objet_id: int, db: Session = Depends(get_db)):
    """
    Supprime un objet.
    """
    service = ObjetService()
    objet = service.get_objet_by_id(db, objet_id)
    if objet is None:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    return service.delete_objet(db, objet_id)
