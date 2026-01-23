from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.commune_schema import CommuneInDB, CommunePatch, CommunePost
from src.services.commune_service import CommuneService
from src.database import get_db
from src.utils.dependencies import require_roles


""" Reference all commune-related endpoints in the FastAPI application.

Receives requestes from the commune router, transform in commune schema and process them using CommuneService"""

# create a router for communes-related endpoints
router = APIRouter(prefix="/commune", tags=["commune"], dependencies=[Depends(require_roles("Admin", "OP-colis"))])

# Initialize the commune service to have access to commune operations
service = CommuneService()

@router.get("/", status_code=200, response_model=list[CommuneInDB])
def get_communes(db: Session=Depends(get_db)):
    return service.get_all_communes(db)

@router.get("/{id_commune}", status_code=200,response_model=CommuneInDB)
def get_commune(id_commune: int, db: Session=Depends(get_db)):
    commune = service.get_commune_by_id(db,id_commune)
    if commune is None:
        raise HTTPException(status_code=404, detail="Commune non trouvé")
    return commune

@router.post("/", status_code=201, response_model= CommuneInDB)
def create_commune(donnees_commune: CommunePost, db: Session=Depends(get_db)):
    return service.create_commune(db, donnees_commune)

@router.patch("/{id_commune}", status_code=200, response_model=CommuneInDB)
def patch_commune(id_commune: int, donnees_commune: CommunePatch, db: Session=Depends(get_db)):
    commune = service.get_commune_by_id(db, id_commune)
    if commune is None:
        raise HTTPException(status_code= 404, detail="Commune non trouvé")
    return service.patch_commune(db,id_commune,donnees_commune)

@router.delete("/{id_commune}", status_code=200,response_model=CommuneInDB)
def delete_commune(id_commune: int, db: Session=Depends(get_db)):
    commune = service.get_commune_by_id(db,id_commune)
    if commune is None:
        raise HTTPException(status_code=404, detail="Commune non trouvé")
    return service.delete_commune(db, id_commune)
