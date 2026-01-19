from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Commune(Base):
    __tablename__ = "t_commune"

    id_Commune = Column(Integer, primary_key = True)
    dep = Column(String(40))
    cp = Column(String(40))
    ville = Column(String(40))
    
  
    adresse = relationship("Adresse", back_populates="commune") 
    """ La table Adresse et Communes ont la relation: 1..n """


   

    
