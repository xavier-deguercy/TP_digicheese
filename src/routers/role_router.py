from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..services.role_service import RoleService
from ..schemas.role import RolePost, RolePatch, RoleOut
from src.utils.dependencies import require_roles

router = APIRouter(prefix="/roles", tags=["admin-roles"], dependencies=[Depends(require_roles("Admin"))])
service = RoleService()

# Get roles

@router.get("/", response_model=list[RoleOut])
def get_roles(db: Session = Depends(get_db)):
    return service.get_all(db)

# Get role par id

@router.get("/{role_id}", response_model=RoleOut)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = service.get_by_id(db, role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Rôle non trouvé")
    return role

# Créer role

@router.post("/", status_code=201, response_model=RoleOut)
def create_role(payload: RolePost, db: Session = Depends(get_db)):
    return service.create(db, payload)

# Modifier role

@router.patch("/{role_id}", response_model=RoleOut)
def patch_role(role_id: int, payload: RolePatch, db: Session = Depends(get_db)):
    role = service.get_by_id(db, role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Rôle non trouvé")
    return service.patch(db, role_id, payload)

# Supprimer role

@router.delete("/{role_id}", response_model=RoleOut)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = service.get_by_id(db, role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Rôle non trouvé")
    return service.delete(db, role_id)
