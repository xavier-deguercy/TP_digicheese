# src/schemas/objet_schema.py
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


#class ObjetPost(BaseModel):
class ObjetCreate(BaseModel):
    nom_obj: str = Field(..., max_length=50)
    taille_obj: Optional[str] = Field(None, max_length=50)
    prix_obj: Decimal = Decimal("0")
    poids_obj: Decimal = Decimal("0")
    indisp_obj: bool = False
    points_obj: int = 0                                                  

class ObjetPatch(BaseModel):
    """
    Schéma pour PATCH (mise à jour partielle).
    -> tout optionnel
    -> on utilisera model_dump(exclude_unset=True) côté service.
    """
    nom_obj: Optional[str] = Field(None, max_length=50)
    taille_obj: Optional[str] = Field(None, max_length=50)

    prix_obj: Optional[float] = None 
    poids_obj: Optional[float] = None 

    indisp_obj: Optional[bool] = None
    points_obj: Optional[int] = None

class ObjetOut(BaseModel):
    """
    Schéma de sortie (GET/POST/PATCH/DELETE).
    from_attributes=True permet de sérialiser directement un objet SQLAlchemy.
    """
    model_config = ConfigDict(from_attributes=True)

    id_objet: int
    nom_obj: str
    taille_obj: Optional[str]

    prix_obj: float
    poids_obj: float

    indisp_obj: bool
    points_obj: int
    
    