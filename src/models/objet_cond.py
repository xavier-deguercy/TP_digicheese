from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from .base import Base


class ObjetCond(Base):
    """Table représentant la relation entre les objets et les conditionnements."""
    __tablename__ = "t_rel_cond"

    idrelcond = Column(Integer, primary_key=True)                       # identifiant de la relation
    qteobjdeb = Column(Integer, default=0)                              # quantité objet début
    qteobjfin = Column(Integer, default=0)                              # quantité objet fin
    codobj = Column(Integer, default=None)                              # code objet (clé étrangère vers t_objet)
    codcond = Column(Integer, default=None)                             # code conditionnement (clé étrangère vers t_conditionnement)

    objets = relationship("Objet", back_populates="condit")             # relation avec la table des objets
    condit = relationship("Conditionnement", back_populates="objets")   # relation avec la table des objets



