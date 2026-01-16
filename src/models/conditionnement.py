from sqlalchemy import Column, ForeignKey, Integer, String, Numeric     
from sqlalchemy.orm import relationship
from .base import Base


class Conditionnement(Base):

    __tablename__ = "t_conditionnement"                                         # table des conditionnements
#attributs
    id_condit = Column(Integer, primary_key=True, nullable=False)               # identifiant conditionnement
    lib_condit = Column(String(50), nullable=True)                              # libellé conditionnement
    poids_condit = Column(Integer, nullable=True)                               # poids conditionnement
    prix_condit = Column(Numeric(10, 4), nullable=False, default=0)             # prix unitaire conditionnement
    ordre_imp = Column(Integer, nullable=True)                                  # ordre d'impression conditionnement
#relation
    objet_cond = relationship("ObjetCond", back_populates="condit")             # relation avec la table des objets
#pas de methode ici, ce sera dans les routes