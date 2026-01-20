from ..models.objet import Objet # import the Objet model
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

from src.models import objet 


class ObjetRepository:
    def __init__(self, session):
        self.session = session

    def get_all_objet(self, db: Session):
        return list(db.query(Objet).all())
    
    def get_objet_by_id(self, db: Session, id: int):
        return db.query(Objet).get(id)

    
    def create_objet(self, db: Session, objet_data: BaseModel) -> Objet:
        new_objet = Objet(**objet_data)
        db.add(new_objet)
        db.commit()
        db.refresh(new_objet)
        return new_objet

    def update_objet(self, db: Session, objet_id: int, objet_data: BaseModel) -> Optional[Objet]:
        objet = self.get_objet(objet_id)
        if objet:
            for key, value in objet_data.dict(exclude_unset=True).items():
                setattr(objet, key, value)
            db.commit()
            db.refresh(objet)
        return objet

    def delete_objet(self, db: Session, id: int):
        objet = db.query(Objet).get(id)
        db.delete(objet)
        db.commit()
        return objet