from sqlalchemy import Column, Integer, String, DECIMAL
from .base import Base

class Poids(Base) :
    """Table représentant les poids et timbres associés aux commandes."""
    __tablename__ = "t_poids"

    id = Column(Integer, default=None, primary_key=True)
    valmin = Column(DECIMAL, default=DECIMAL("0"), nullable=True)
    valtimbre = Column(DECIMAL, default=DECIMAL("0"), nullable=True)
