from sqlalchemy import column, Integer, DECIMAL
from .base import Base

class Poidsv(Base) :
    """Table qui représente les vignettes ( timbre ) avec leurs prix pour un certain poids."""
    __tablename__ = "t_poidsv"

    id = column(Integer, default=None, primary_key=True)
    valmin = column(DECIMAL, default=DECIMAL("0"), nullable=True)
    valtimbre = column(DECIMAL, default=DECIMAL("0"), nullable=True)
   