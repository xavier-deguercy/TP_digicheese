# src/schemas/objet_schema.py
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, condecimal, conint

# Types réutilisables (lisibilité + cohérence)
PrixType = condecimal(max_digits=10, decimal_places=4, ge=0)
PoidsType = condecimal(max_digits=10, decimal_places=4, ge=0)
PointsType = conint(ge=0)


class ObjetPost(BaseModel):
    """
    Schéma pour POST (création).
    -> nom_obj requis (car nullable=False en DB)
    -> le reste a des défauts propres et validés.
    """
    nom_obj: Optional[str] = Field(None, max_length=50)
    taille_obj: Optional[str] = Field(None, max_length=50)

    prix_obj: Optional[condecimal(max_digits=10, decimal_places=4, ge=0)] = None                
    poids_obj: Optional[condecimal(max_digits=10, decimal_places=4, ge=0)] = None               
    indisp_obj: Optional[bool] = None
    points_obj: Optional[conint(ge=0)] = None                                                  


class ObjetPatch(BaseModel):
    """
    Schéma pour PATCH (mise à jour partielle).
    -> tout optionnel
    -> on utilisera model_dump(exclude_unset=True) côté service.
    """
    nom_obj: Optional[str] = Field(None, max_length=50)
    taille_obj: Optional[str] = Field(None, max_length=50)

    prix_obj: Optional[PrixType] = None 
    poids_obj: Optional[PoidsType] = None 

    indisp_obj: Optional[bool] = None
    points_obj: Optional[PointsType] = None


class ObjetOut(BaseModel):
    """
    Schéma de sortie (GET/POST/PATCH/DELETE).
    from_attributes=True permet de sérialiser directement un objet SQLAlchemy.
    """
    model_config = ConfigDict(from_attributes=True)

    id_objet: int
    nom_obj: str
    taille_obj: Optional[str]

    prix_obj: Decimal
    poids_obj: Decimal

    indisp_obj: bool
    points_obj: int
