from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Adresse(Base):
    __tablename__ = "t_adresse"

    id_Adresse = Column(Integer, primary_key = True)
    rue = Column(String(100))
    compAdresse = Column(String(100))
    id_Commune = Column(Integer, ForeignKey("t_commune.id"), nullable=False)

    commune = relationship("Commune", back_populates="adresse")
