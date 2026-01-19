# src/schemas/conditionnement_schema.py
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, condecimal, conint

PrixType = condecimal(max_digits=10, decimal_places=4, ge=0)
PoidsType = conint(ge=0)
OrdreType = conint(ge=0)


class ConditionnementBase(BaseModel):
    """Base schema for Condirtionnement data."""
    lib_condit: Optional[str] = Field(None, max_length=50)
    poids_condit: Optional[PoidsType] = None
    prix_condit: PrixType = Decimal("0")
    ordre_imp: Optional[OrdreType] = None

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
    poids_condit: Optional[PoidsType] = None
    prix_condit: Optional[PrixType] = None
    ordre_imp: Optional[OrdreType] = None


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
#

#id_condit = Column(Integer, primary_key=True, nullable=False)               # identifiant conditionnement
 #   lib_condit = Column(String(50), nullable=True)                              # libellé conditionnement
  #  poids_condit = Column(Integer, nullable=True)                               # poids conditionnement
   ## prix_condit = Column(Numeric(10, 4), nullable=False, default=0)             # prix unitaire conditionnement
   # ordre_imp = Column(Integer, nullable=True)                                  # ordre d'impression conditionnement
#relation
  #  objet_cond = relationship("ObjetCond", back_populates="condit")  