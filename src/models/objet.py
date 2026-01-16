from sqlalchemy import Column, Integer, String, Numeric,Boolean
from sqlalchemy.orm import relationship
from .base import Base


class Objet(Base):
    """Table représentant les objets disponibles dans la fromagerie."""
    
    __tablename__ = "t_objet" # table des objets
#attributs
    id_objet = Column(Integer, primary_key=True)                      # code objet
    nom_obj = Column(String(50), nullable=False)                     # nom objet
    taille_obj = Column(String(50), nullable=True)                   # taille objet
    prix_obj = Column(Numeric(10, 4), nullable=False, default=0)       # prix unitaire objet
    poids_obj = Column(Numeric(10, 4), nullable=False, default=0)    # poids objet
    indisp_obj = Column(Boolean, nullable=False, default=0)          # 0/1
    points_obj = Column(Integer, nullable=False, default=0)             #  
        

# on ne prend pas en compte les o_ ( c'est pour la config) dans cette version
    # o_imp = Column(Integer, nullable=False, default=0)              # 0/1
    # o_aff = Column(Integer, nullable=False, default=0)              # 0/1
    # o_cartp = Column(Integer, nullable=False, default=0)            # 0/1
    # o_ordre_aff = Column(Integer, nullable=False, default=0)        # ordre d'affichage des objets dans la fromagerie

#relation
    condit = relationship("objet_cond", back_populates="objets")    # relation avec la table des conditionnements
#pas de methode ici, ce sera dans les routes
