from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Commande(Base):
    """Commande client préparée par un opérateur colis."""

    __tablename__ = "t_commande"

    id_commande = Column(Integer, primary_key=True, autoincrement=True, index=True)
    date_commande = Column(Date, nullable=False)
    timbre_client = Column(String(100), nullable=True)
    timbre_code = Column(String(100), nullable=True)
    nb_colis = Column(Integer, nullable=True)
    b_archive = Column(Boolean, nullable=False, default=False)
    id_client = Column(Integer, ForeignKey("t_client.id_client"), nullable=False, index=True)
    id_conditionnement = Column(
        Integer,
        ForeignKey("t_conditionnement.id_condit"),
        nullable=True,
        index=True,
    )

    client = relationship("Client")
    conditionnement = relationship("Conditionnement")
