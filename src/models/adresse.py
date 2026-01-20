from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Adresse(Base):
    __tablename__ = "t_adresse"

    id_adresse = Column(Integer, primary_key = True)
    rue = Column(String(100))
    compAdresse = Column(String(100))
    id_commune = Column(Integer, ForeignKey("t_commune.id_commune"), nullable=False)

    commune = relationship("Commune", back_populates="adresse")

    