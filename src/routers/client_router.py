from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.client_schema import ClientOut, ClientPost, ClientPatch
from ..services.client_service import ClientService

router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)

service = ClientService()


@router.get("/", response_model=List[ClientOut])
def get_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip=skip, limit=limit)


@router.get("/{id_client}", response_model=ClientOut)
def get_client(id_client: int, db: Session = Depends(get_db)):
    client = service.get_by_id(db, id_client)
    if client is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client


@router.post("/", response_model=ClientOut, status_code=201)
def create_client(payload: ClientPost, db: Session = Depends(get_db)):
    return service.create(db, payload)


@router.patch("/{id_client}", response_model=ClientOut)
def patch_client(id_client: int, payload: ClientPatch, db: Session = Depends(get_db)):
    return service.patch(db, id_client, payload)


@router.delete("/{id_client}", response_model=ClientOut)
def delete_client(id_client: int, db: Session = Depends(get_db)):
    return service.delete(db, id_client)
