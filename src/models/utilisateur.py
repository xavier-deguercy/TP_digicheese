from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime, timezone

class Utilisateur(Base):
    """Table représentant les utilisateurs dans le système."""
    __tablename__ = "t_utilisateur"

    id_user = Column(Integer, primary_key=True)
    nom_user = Column(String(40), index = True)
    prenom_user = Column(String(40))
    username = Column(String(50))
    hashed_password = Column(String(255), nullable=False)
    date_insc_user = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    id_role = Column(Integer, ForeignKey("t_role.id_role"), nullable=False)

    role = relationship("Role", back_populates="utilisateurs")
