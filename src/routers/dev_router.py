from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.utilisateur import Utilisateur

router = APIRouter(prefix="/dev", tags=["Dev"])


@router.get("/api-key/{user_id}")
def get_api_key(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Utilisateur).filter(Utilisateur.id_user == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user.id_user, "api_key": user.api_key}
