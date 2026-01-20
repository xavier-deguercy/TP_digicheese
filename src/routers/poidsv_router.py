"""
References all client-related endpoints in the FastAPI application.

Receives requests from the client router, transform in client schema and processes them using the ClientService.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.DB.database import get_db
from src.schemas.poidsv_schema import PoidsvInDB, PoidsvPatch, PoidsvPost
from src.services.poidsv_service import PoidsvService


# Create a router for poids-Vignettes-related endpoints
router = APIRouter(prefix="/poidsv", tags=["poidsv"])

# Initialize the poids-vignettes service to have access to poids-vignettes operations
service = PoidsvService()

@router.get("/", status_code=200, response_model=list[PoidsvInDB])
def get_poidsv_list(db: Session=Depends(get_db)):
    return service.get_all_poidsv(db)
    

@router.get("/{poidsv_id}", status_code=200, response_model=PoidsvInDB)
def get_poidsv_by_id(poidsv_id: int, db: Session=Depends(get_db)):
    poidsv = service.get_poidsv_by_id(db, poidsv_id)
    if poidsv is None:
        raise HTTPException(status_code=404, detail="Poids des vignettes non trouvé")
    return poidsv


@router.post("/", status_code=201, response_model=PoidsvInDB)
def create_poidsv(donnees_poidsv: PoidsvPost, db: Session=Depends(get_db)):
    return service.create_poidsv(db, donnees_poidsv)


@router.patch("/{poidsv_id}", status_code=200, response_model=PoidsvInDB)
def patch_poidsv(poidsv_id: int, donnees_poids: PoidsvPatch, db: Session=Depends(get_db)):
    poidsv = service.get_poidsv_by_id(db, poidsv_id)
    if poidsv is None:
        raise HTTPException(status_code=404, detail="Poids des vignettes non trouvé")
    return service.patch_poidsv(db, poidsv_id, donnees_poidsv)


@router.delete("/{poidsv_id}", status_code=200, response_model=PoidsvInDB)
def delete_poidsv(poidsv_id: int, db: Session=Depends(get_db)):
    poidsv = service.get_poidsv_by_id(db, poidsv_id)
    if poidsv is None:
        raise HTTPException(status_code=404, detail="Poids des vignettes non trouvé")
    return service.delete_poidsv(db, poidsv_id)