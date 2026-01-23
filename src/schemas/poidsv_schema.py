from pydantic import BaseModel
from typing import Optional


class PoidsvBase(BaseModel):
    """Base schema for PoidsV data."""
    valminv: float
    valmaxv: float

class PoidsvPost(PoidsvBase):
    """Schema for creating a new PoidsV."""
    pass


class PoidsvPatch(BaseModel):
    """Schema for updating an existing PoidsV."""
    valminv: Optional[float] = None
    valmaxv: Optional[float] = None


class PoidsvInDB(PoidsvBase):
    """Schema for PoidsV data stored in the database."""
    id: int

    class Config:
        from_attributes = True
