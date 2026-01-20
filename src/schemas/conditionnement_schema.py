# src/schemas/conditionnement_schema.py

from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ConditionnementBase(BaseModel):
    """Base schema for Conditionnement data."""
    lib_condit: Optional[str] = Field(None, max_length=50)
    poids_condit: Optional[int] = None          # cohérent avec Integer en DB
    prix_condit: Optional[Decimal] = None       # cohérent avec Numeric(10,4)
    ordre_imp: Optional[int] = None             # cohérent avec Integer en DB


class ConditionnementPost(ConditionnementBase):
    #POST : création.
    pass


class ConditionnementPatch(ConditionnementBase):
    
    #PATCH : tout optionnel.
    
    pass


class ConditionnementInDB(ConditionnementBase):
    #OUT : réponse API (GET/POST/PATCH/DELETE).
    model_config = ConfigDict(from_attributes=True)

    id_condit: int
