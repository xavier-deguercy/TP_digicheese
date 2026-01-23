from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Role(Base):
    """Table représentant les rôles dans le système."""
    __tablename__ = "t_role"

    id_role = Column(Integer, primary_key=True)
    libelle_role = Column(String(50), nullable=False)
    
    utilisateurs = relationship("Utilisateur", back_populates="role")
