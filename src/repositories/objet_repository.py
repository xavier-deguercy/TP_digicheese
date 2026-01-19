from ..models import Objet # import the Objet model
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional 


class ObjetRepository:
    def __init__(self, session):
        self.session = session

    def get_objet(self, objet_id: int) -> Optional[Objet]:
        return self.session.query(Objet).filter(Objet.id_objet == objet_id).first()

    def create_objet(self, objet_data: BaseModel) -> Objet:
        new_objet = Objet(**objet_data.dict())
        self.session.add(new_objet)
        self.session.commit()
        self.session.refresh(new_objet)
        return new_objet

    def update_objet(self, objet_id: int, objet_data: BaseModel) -> Optional[Objet]:
        objet = self.get_objet(objet_id)
        if objet:
            for key, value in objet_data.dict(exclude_unset=True).items():
                setattr(objet, key, value)
            self.session.commit()
            self.session.refresh(objet)
        return objet

    def delete_objet(self, objet_id: int) -> bool:
        objet = self.get_objet(objet_id)
        if objet:
            self.session.delete(objet)
            self.session.commit()
            return True
        return False
