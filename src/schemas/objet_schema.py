from pydantic import BaseModel
from typing import Optional


# ObjetBase : champs communs
class ObjetBase(BaseModel):
    libobj: Optional[str] = None
    tailleobj: Optional[str] = None
    puobj: Optional[float] = 0.0
    poidsobj: Optional[float] = 0.0
    indispobj: Optional[int] = 0
    o_imp: Optional[int] = 0
    o_aff: Optional[int] = 0
    o_cartp: Optional[int] = 0
    o_ordre_aff: Optional[int] = 0

# ObjetPost : création (sans codobj)
class ObjetPost(ObjetBase):
    pass

# ObjetPatch : update partiel (tous optionnels)
class ObjetPatch(ObjetBase):
    libobj: Optional[str] = None
    tailleobj: Optional[str] = None
    puobj: Optional[float] = None
    poidsobj: Optional[float] = None
    indispobj: Optional[int] = None
    o_imp: Optional[int] = None
    o_aff: Optional[int] = None
    o_cartp: Optional[int] = None
    o_ordre_aff: Optional[int] = None

# ObjetOut : réponse (avec codobj)
class ObjetOut(ObjetBase):
    codobj: int


#Validations à faire ici :

#libobj max 50 (Pydantic le fera si tu utilises max_length=50)

puobj >= 0, poidsobj >= 0, points >= 0, o_ordre_aff >= 0 (minimum)