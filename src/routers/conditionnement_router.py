# src/routers/conditionnement_router.py

"""
Endpoints Conditionnements (Admin) — DIGICHEESE
Router (HTTP) -> Service (métier) -> Repository (DB)
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.database import get_db                                                  
from ..schemas.conditionnement_schema import (
    ConditionnementPost,
    ConditionnementPatch,
    ConditionnementInDB ,
)
from ..services.conditionnement_sevices import ConditionnementService

# Create a router for conditionnement-related endpoints
router = APIRouter(
    prefix="/conditionnements",
    tags=["Admin - Conditionnements"]
)

# Initialize the conditionnement service to have access to client operations
service = ConditionnementService()


@router.get("/", response_model=list[ConditionnementInDB], status_code=200)
def get_conditionnements(db: Session = Depends(get_db)):
    return service.get_all_conditionnements(db)


@router.get("/{condit_id}", response_model=ConditionnementInDB, status_code=200)
def get_conditionnement(condit_id: int, db: Session = Depends(get_db)):
    cond = service.get_conditionnement_by_id(db, condit_id)
    if cond is None:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    return cond


@router.post("/", response_model=ConditionnementInDB, status_code=201)
def create_conditionnement(payload: ConditionnementPost, db: Session = Depends(get_db)):
    return service.create_conditionnement(db, payload)


@router.patch("/{condit_id}", response_model=ConditionnementInDB, status_code=200)
def patch_conditionnement(condit_id: int, payload: ConditionnementPatch, db: Session = Depends(get_db)):
    cond = service.get_conditionnement_by_id(db, condit_id)
    if cond is None:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    return service.patch_conditionnement(db, condit_id, payload)


@router.delete("/{condit_id}", response_model=ConditionnementInDB, status_code=200)
def delete_conditionnement(condit_id: int, db: Session = Depends(get_db)):
    cond = service.get_conditionnement_by_id(db, condit_id)
    if cond is None:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    return service.delete_conditionnement(db, condit_id)
