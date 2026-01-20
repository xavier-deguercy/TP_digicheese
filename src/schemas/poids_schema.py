from pydantic import BaseModel
from typing import Optional


class PoidsBase(BaseModel):
    """Base schema for Poids data."""
    id: int
    valmin: float
    valmax: float

class PoidsPost(PoidsBase):
    """Schema for creating a new Poids."""
    pass


class PoidsPatch(PoidsBase):
    """Schema for updating an existing Poids."""
    valmin: Optional[float] = None
    valmax: Optional[float] = None


class PoidsInDB(PoidsBase):
    """Schema for Poids data stored in the database."""
    codPoids: int
    
    class Config:
        from_attributes = True