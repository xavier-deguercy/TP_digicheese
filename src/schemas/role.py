from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator


class RoleBase(BaseModel):
    """Schéma de base pour les données d'un rôle."""
    libelle_role: str = Field(min_length=1, max_length=50)


class RolePost(RoleBase):
    """Schéma utilisé pour la création d'un rôle."""
    pass


class RolePatch(BaseModel):
    """Schéma utilisé pour la mise à jour partielle d'un rôle."""
    libelle_role: Optional[str] = None

    @field_validator("libelle_role")
    @classmethod
    def libelle_role_cannot_be_null_or_empty(cls, value: Optional[str]) -> str:
        if value is None or not value.strip():
            raise ValueError("libelle_role ne peut pas etre null ou vide")
        return value


class RoleOut(RoleBase):
    """Schéma retourné par l'API."""
    id_role: int

    model_config = ConfigDict(from_attributes=True)
