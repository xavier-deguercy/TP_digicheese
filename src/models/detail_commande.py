from sqlalchemy import Column, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import Base


class DetailCommande(Base):
    """Ligne d'objet rattachee a une commande."""

    __tablename__ = "t_detail_commande"
    __table_args__ = (
        UniqueConstraint(
            "id_commande",
            "id_objet",
            name="uq_detail_commande_commande_objet",
        ),
    )

    id_detail_commande = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    quantite = Column(Integer, nullable=False)
    commentaire = Column(Text, nullable=True)
    id_commande = Column(
        Integer,
        ForeignKey("t_commande.id_commande"),
        nullable=False,
        index=True,
    )
    id_objet = Column(
        Integer,
        ForeignKey("t_objet.id_objet"),
        nullable=False,
        index=True,
    )

    commande = relationship("Commande")
    objet = relationship("Objet")
