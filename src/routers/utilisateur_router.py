from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.utilisateur_service import UtilisateurService
from ..schemas.utilisateur import UtilisateurPost, UtilisateurPatch, UtilisateurOut, UtilisateurOutWithApiKey
from src.utils.dependencies import require_roles

router = APIRouter(prefix="/utilisateurs", tags=["admin-utilisateurs"], dependencies=[Depends(require_roles("Admin"))])
service = UtilisateurService()


@router.get("/", response_model=list[UtilisateurOut])
def get_users(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{user_id}", response_model=UtilisateurOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = service.get_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user


@router.post("/", status_code=201, response_model=UtilisateurOutWithApiKey)
def create_user(payload: UtilisateurPost, db: Session = Depends(get_db)):
    return service.create(db, payload)


@router.patch("/{user_id}", response_model=UtilisateurOut)
def patch_user(user_id: int, payload: UtilisateurPatch, db: Session = Depends(get_db)):
    user = service.get_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return service.patch(db, user_id, payload)


@router.delete("/{user_id}", response_model=UtilisateurOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = service.get_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return service.delete(db, user_id)
