from pydantic import BaseModel
from typing import Optional

class AdresseBase(BaseModel):
    """Base schema for adresse data"""
    rue: str
    compAdresse: str
   

class AdressePost(AdresseBase):
    """Schema for creating a new adresse."""
    id_commune = int

class AdressePatch(BaseModel):
    """Schema for updating an existing adresse."""
    rue: Optional[str] = None
    compAdresse: Optional[str] = None
   

class AdresseInDB(AdresseBase):
    """Schema for adresse data stored in the database."""
    id_adresse: int
    
    class Config:
        from_attributes = True
