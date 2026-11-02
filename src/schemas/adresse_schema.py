from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional

class AdresseBase(BaseModel):
    """Base schema for adresse data"""
    rue: str
    compAdresse: str
    id_commune: int


class AdressePost(AdresseBase):
    """Schema for creating a new adresse."""
    id_commune: int

class AdressePatch(BaseModel):
    """Schema for updating an existing adresse."""
    rue: Optional[str] = None
    compAdresse: Optional[str] = None
    id_commune: Optional[int] = None

    @field_validator("id_commune")
    @classmethod
    def id_commune_cannot_be_null(cls, value: Optional[int]) -> int:
        if value is None:
            raise ValueError("id_commune ne peut pas etre null")
        return value


class AdresseInDB(AdresseBase):
    """Schema for adresse data stored in the database."""
    id_adresse: int

    model_config = ConfigDict(from_attributes=True)
