from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.adresse_schema import AdresseInDB, AdressePatch, AdressePost
from src.services.adresse_service import AdresseService
from src.database import get_db
from src.utils.dependencies import require_roles

router = APIRouter(prefix="/adresse", tags=["adresse"], dependencies=[Depends(require_roles("Admin", "OP-colis"))])
service = AdresseService()

@router.get("/", status_code=200, response_model=list[AdresseInDB])
def get_adresses(db: Session=Depends(get_db)):
    return service.get_all_adresses(db)

@router.get("/{id_adresse}", status_code=200,response_model=AdresseInDB)
def get_adresse(id_adresse: int, db: Session=Depends(get_db)):
    adresse = service.get_adresse_by_id(db,id_adresse)
    if adresse is None:
        raise HTTPException(status_code=404, detail="Adresse non trouvé")
    return adresse

@router.post("/", status_code=201, response_model= AdresseInDB)
def create_adresse(donnees_adresse: AdressePost, db: Session=Depends(get_db)):
    return service.create_adresse(db, donnees_adresse)

@router.patch("/{id_adresse}", status_code=200, response_model=AdresseInDB)
def patch_adresse(id_adresse: int, donnees_adresse: AdressePatch, db: Session=Depends(get_db)):
    adresse = service.get_adresse_by_id(db, id_adresse)
    if adresse is None:
        raise HTTPException(status_code= 404, detail="Adresse non trouvé")
    return service.patch_adresse(db,id_adresse,donnees_adresse)

@router.delete("/{id_adresse}", status_code=200,response_model=AdresseInDB)
def delete_adresse(id_adresse: int, db: Session=Depends(get_db)):
    adresse = service.get_adresse_by_id(db,id_adresse)
    if adresse is None:
        raise HTTPException(status_code=404, detail="Adresse non trouvé")
    return service.delete_adresse(db, id_adresse)
