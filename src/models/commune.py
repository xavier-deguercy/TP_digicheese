from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Commune(Base):
    __tablename__ = "t_commune"

    id_commune = Column(Integer, primary_key = True)
    dep = Column(String(40))
    cp = Column(String(40))
    ville = Column(String(40))


    adresses = relationship("Adresse", back_populates="commune")
