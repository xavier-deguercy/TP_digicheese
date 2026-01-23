from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.client_schema import ClientOutDetailed, ClientOut, ClientPost, ClientPatch
from ..services.client_service import ClientService
from src.utils.dependencies import require_roles

router = APIRouter(prefix="/clients", tags=["Clients"], dependencies=[Depends(require_roles("Admin", "OP-colis"))])
service = ClientService()

# Get clients

@router.get("/", response_model=List[ClientOutDetailed])
def get_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip=skip, limit=limit)

# Get client by id

@router.get("/{id_client}", response_model=ClientOutDetailed)
def get_client(id_client: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, id_client)

# Create client

@router.post("/", response_model=ClientOut, status_code=201)
def create_client(payload: ClientPost, db: Session = Depends(get_db)):
    return service.create(db, payload)

# Modifier client

@router.patch("/{id_client}", response_model=ClientOut)
def patch_client(id_client: int, payload: ClientPatch, db: Session = Depends(get_db)):
    return service.patch(db, id_client, payload)

# Supprimer client

@router.delete("/{id_client}", response_model=ClientOut)
def delete_client(id_client: int, db: Session = Depends(get_db)):
    return service.delete(db, id_client)
