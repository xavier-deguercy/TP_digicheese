from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Client(Base):
    """Table représentant les clients de la fidélisation de la fromagerie."""
    __tablename__ = "t_client"

    id_client = Column(Integer, primary_key=True)
    email_client = Column(String(255), nullable=True, index=True)
    nom_client = Column(String(40), nullable=True)
    prenom_client = Column(String(30), nullable=True)
    adresse1_client = Column(Integer, ForeignKey("t_adresse.id_adresse"), nullable=False)
    adresse2_client = Column(Integer, ForeignKey("t_adresse.id_adresse"), nullable=True)
    ville_client = Column(String(50), nullable=True)
    code_postal_client = Column(String(5), nullable=True)
    telephone_client = Column(String(10), nullable=True)

    adresse1 = relationship("Adresse", foreign_keys=[adresse1_client], back_populates="clients_adresse1")
    adresse2 = relationship("Adresse", foreign_keys=[adresse2_client], back_populates="clients_adresse2")
