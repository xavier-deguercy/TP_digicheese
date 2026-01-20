from sqlalchemy import Column, Integer, DECIMAL
from .base import Base

class Poidsv(Base) :
    """Table qui représente les vignettes ( timbre ) avec leurs prix pour un certain poids."""
    __tablename__ = "t_poidsv"

    id = Column(Integer, default=None, primary_key=True)
    valmin = Column(DECIMAL, default=DECIMAL("0"), nullable=True)
    valtimbre = Column(DECIMAL, default=DECIMAL("0"), nullable=True)
   