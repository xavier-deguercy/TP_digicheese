from pydantic import BaseModel
from typing import Optional


class PoidsvBase(BaseModel):
    """Base schema for PoidsV data."""
    id: int
    valmin: float
    valmax: float

class PoidsvPost(PoidsvBase):
    """Schema for creating a new PoidsV."""
    pass


class PoidsvPatch(PoidsvBase):
    """Schema for updating an existing PoidsV."""
    valmin: Optional[float] = None
    valmax: Optional[float] = None


class PoidsvInDB(PoidsvBase):
    """Schema for PoidsV data stored in the database."""
    codPoidsV: int
    
    class Config:
        from_attributes = True