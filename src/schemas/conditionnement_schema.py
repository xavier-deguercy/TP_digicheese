from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.models.base import Base

# SQLAlchemy base

class ConditionnementBase(BaseModel):
    id_condit: Optional[int] = None
    lib_condit: Optional[str] = None
    poids_condit: Optional[int] = None
    prix_condit: Optional[float] = 0.0
    ordre_imp: Optional[int] = None

# ConditionnementPost : création (sans id_condit)
class ConditionnementPost(ConditionnementBase):
    pass

# ConditionnementPatch : update partiel (tous optionnels)
class ConditionnementPatch(ConditionnementBase):
    pass # tous les champs sont optionnels pour le patch


# ConditionnementOut : réponse (avec id_condit)
class ConditionnementOut(ConditionnementBase):
    id_condit: int




