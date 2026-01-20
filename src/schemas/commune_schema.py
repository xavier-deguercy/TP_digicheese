from pydantic import BaseModel
from typing import Optional

class CommuneBase(BaseModel):
    """Base schema for commune data"""
    dep: str
    cp: str
    ville: str

class CommunePost(CommuneBase):
    """Schema for creating a new commune."""
    pass

class CommunePatch(CommuneBase):
    """Schema for updating an existing commune."""
    dept: Optional[str] = None
    cp: Optional[str] = None
    ville: Optional[str] = None

class CommuneInDB(CommuneBase):
    """Schema for commune data stored in the database."""
    id_commune: int
    
    class Config:
        from_attributes = True

        

