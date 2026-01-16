from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from .base import Base


class Objet(Base):
    """Table représentant les objets disponibles dans la fromagerie."""
    
    __tablename__ = "t_objet"

    codobj = Column(Integer, primary_key=True)                       # code objet
    libobj = Column(String(50), nullable=False)                     # nom objet
    tailleobj = Column(String(50), nullable=True)                   # taille objet
    puobj = Column(Numeric(10, 4), nullable=False, default=0)       # prix unitaire objet
    poidsobj = Column(Numeric(10, 4), nullable=False, default=0)    # poids objet
    indispobj = Column(Integer, nullable=False, default=0)          # 0/1
    points = Column(Integer, nullable=False, default=0)             #  
        
    o_imp = Column(Integer, nullable=False, default=0)              # 0/1
    o_aff = Column(Integer, nullable=False, default=0)              # 0/1
    o_cartp = Column(Integer, nullable=False, default=0)            # 0/1
    o_ordre_aff = Column(Integer, nullable=False, default=0)        # ordre d'affichage des objets dans la fromagerie

    condit = relationship("objet_cond", back_populates="objets") # relation avec la table des conditionnements
