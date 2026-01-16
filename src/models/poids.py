from sqlalchemy import column, Integer, String, DECIMAL
from .base import Base

class Poids(Base) :
    """Table représentant les poids et timbres associés aux commandes."""
    __tablename__ = "t_poids"

    id = column(Integer, default=None, primary_key=True)
    valmin = column(DECIMAL, default=DECIMAL("0"), nullable=True)
    valtimbre = column(DECIMAL, default=DECIMAL("0"), nullable=True)


