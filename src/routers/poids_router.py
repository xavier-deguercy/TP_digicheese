"""
References all client-related endpoints in the FastAPI application.

Receives requests from the client router, transform in client schema and processes them using the ClientService.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.DB.database import get_db
from src.schemas.poids_schema import PoidsInDB, PoidsPatch, PoidsPost
from src.services.poids_service import PoidsService


# Create a router for poids-related endpoints
router = APIRouter(prefix="/poids", tags=["poids"])

# Initialize the poids service to have access to poids operations
service = PoidsService()

@router.get("/", status_code=200, response_model=list[PoidsInDB])
def get_poids(db: Session=Depends(get_db)):
    return service.get_all_poids(db)
    

@router.get("/{poids_id}", status_code=200, response_model=PoidsInDB)
def get_poids(poids_id: int, db: Session=Depends(get_db)):
    poids = service.get_poids_by_id(db, poids_id)
    if poids is None:
        raise HTTPException(status_code=404, detail="Poids non trouvé")
    return poids


@router.post("/", status_code=201, response_model=PoidsInDB)
def create_poids(donnees_poids: PoidsPost, db: Session=Depends(get_db)):
    return service.create_poids(db, donnees_poids)


@router.patch("/{poids_id}", status_code=200, response_model=PoidsInDB)
def patch_poids(poids_id: int, donnees_poids: PoidsPatch, db: Session=Depends(get_db)):
    poids = service.get_poids_by_id(db, poids_id)
    if poids is None:
        raise HTTPException(status_code=404, detail="Poids non trouvé")
    return service.patch_poids(db, poids_id, donnees_poids)


@router.delete("/{poids_id}", status_code=200, response_model=PoidsInDB)
def delete_poids(poids_id: int, db: Session=Depends(get_db)):
    poids = service.get_poids_by_id(db, poids_id)
    if poids is None:
        raise HTTPException(status_code=404, detail="Poids non trouvé")
    return service.delete_poids(db, poids_id)