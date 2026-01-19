# src/schemas/conditionnement_schema.py
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, condecimal, conint

PrixType = condecimal(max_digits=10, decimal_places=4, ge=0)
PoidsType = conint(ge=0)
OrdreType = conint(ge=0)


class ConditionnementPost(BaseModel):
    """
    POST (création) : pas d'id_condit (auto).
    Champs nullable en DB -> optionnels ici.
    prix_condit non-null en DB -> défaut 0.
    """
    lib_condit: Optional[str] = Field(None, max_length=50)
    poids_condit: Optional[PoidsType] = None
    prix_condit: PrixType = Decimal("0")
    ordre_imp: Optional[OrdreType] = None


class ConditionnementPatch(BaseModel):
    """
    PATCH : tout optionnel.
    On utilisera model_dump(exclude_unset=True) dans le service.
    """
    lib_condit: Optional[str] = Field(None, max_length=50)
    poids_condit: Optional[PoidsType] = None
    prix_condit: Optional[PrixType] = None
    ordre_imp: Optional[OrdreType] = None


class ConditionnementOut(BaseModel):
    """
    OUT : réponse API (GET/POST/PATCH/DELETE).
    """
    model_config = ConfigDict(from_attributes=True)

    id_condit: int
    lib_condit: Optional[str]
    poids_condit: Optional[int]
    prix_condit: Decimal
    ordre_imp: Optional[int]
