# src/schemas/conditionnement_schema.py
from decimal import Decimal
from typing import Optional, Optional
from pydantic import BaseModel, ConfigDict, Field

class ConditionnementBase(BaseModel):
    """Base schema for Condirtionnement data."""
    lib_condit: Optional[str] = Field(None, max_length=50)
    poids_condit: Optional[float] = None
    prix_condit: Optional[float ] = None
    ordre_imp: Optional[bool] = None

class ConditionnementPost(ConditionnementBase):
    """
    POST : création.
    -> lib_condit optionnel (nullable=True en DB)
    -> poids_condit optionnel (nullable=True en DB)
    -> prix_condit requis (default=0 en DB)
    -> ordre_imp optionnel (nullable=True en DB)
    """
    pass

class ConditionnementPatch(ConditionnementBase):
    """
    PATCH : tout optionnel.
    On utilisera model_dump(exclude_unset=True) dans le service.
    """
    lib_condit: Optional[str] = Field(None, max_length=50)
    poids_condit: Optional[float] = None
    prix_condit: Optional[float ] = None
    ordre_imp: Optional[bool] = None


class ConditionnementInDB(ConditionnementBase):
    """
    OUT : réponse API (GET/POST/PATCH/DELETE).
    """
    model_config = ConfigDict(from_attributes=True)

    id_condit: int
    lib_condit: Optional[str]
    poids_condit: Optional[int]
    prix_condit: Decimal
    ordre_imp: Optional[int]
 