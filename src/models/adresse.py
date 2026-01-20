from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Adresse(Base):
    __tablename__ = "t_adresse"

    id_adresse = Column(Integer, primary_key = True)
    rue = Column(String(100))
    compAdresse = Column(String(100))
    id_commune = Column(Integer, ForeignKey("t_commune.id_commune"), nullable=False)

    commune = relationship("Commune", back_populates="adresses")
    clients_adresse1 = relationship("Client", foreign_keys="Client.adresse1_client", back_populates="adresse1")
    clients_adresse2 = relationship("Client", foreign_keys="Client.adresse2_client", back_populates="adresse2")
