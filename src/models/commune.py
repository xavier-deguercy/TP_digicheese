from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Communes(Base):
    __tablename__ = "t_communes"

    id = Column(Integer, primary_key = True)
    dep = Column(String(40))
    cp = Column(String(40))
    ville = Column(String(40))
    """ajoute la Foreignkey adresse_id"""
    #adresse_id =  Column(Integer, ForeignKey("adresse_id", ondelete="CASCADE"), index=True, nullable=False)
    """ajoute la relation entre deux table: Adresse et Communes"""
    #adress = relationship("Adresse", back_populates="Communes")

    """ La table Adresse et Communes ont la relation: 1..n """


   

    
