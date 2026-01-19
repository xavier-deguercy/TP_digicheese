from pydantic import BaseModel
from typing import Optional

from sqlalchemy import Column


# ObjetBase : champs communs
class ObjetBase(BaseModel):
    nom_obj: Optional[str] = None
    taille_obj: Optional[str] = None
    prix_obj: Optional[float] = 0.0
    poids_obj: Optional[float] = 0.0
    indisp_obj: Optional[int] = 0
    


    # nom_obj = Column(String(50), nullable=False)                     # nom objet
    # taille_obj = Column(String(50), nullable=True)                   # taille objet
    # prix_obj = Column(Numeric(10, 4), nullable=False, default=0)       # prix unitaire objet
    # poids_obj = Column(Numeric(10, 4), nullable=False, default=0)    # poids objet
    # indisp_obj = Column(Boolean, nullable=False, default=0)          # 0/1
    # points = Column(Integer, nullable=False, default=0)             #  



# ObjetPost : création (sans codobj)
class ObjetPost(ObjetBase):
    pass

# ObjetPatch : update partiel (tous optionnels)
class ObjetPatch(ObjetBase):
    pass # tous les champs sont optionnels pour le patch

# ObjetOut : réponse (avec codobj)
class ObjetOut(ObjetBase):
    codobj: int


#Validations à faire ici :

#libobj max 50 (Pydantic le fera si tu utilises max_length=50)

#puobj >= 0, poidsobj >= 0, points >= 0, o_ordre_aff >= 0 (minimum)