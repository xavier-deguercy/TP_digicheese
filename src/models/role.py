from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Role(Base):
    __tablename__ = "t_role"

    id_role = Column(int, primary_key=True)
    libelle_role = Column(String)
    utilisateurs = relationship("Utilisateur", back_populates="role")
