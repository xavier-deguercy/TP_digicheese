from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class UtilisateurBase(BaseModel):
    """Base schema pour utilisateur."""
    nom_user: Optional[str] = None
    prenom_user: Optional[str] = None
    username: Optional[str] = None
    id_role: int


class UtilisateurPost(UtilisateurBase):
    """Créer un utilisateur."""
    password: str = Field(min_length=1)  # mot de passe en clair à la création


class UtilisateurPatch(BaseModel):
    """Schema for update un utilisateur"""
    nom_user: Optional[str] = None
    prenom_user: Optional[str] = None
    username: Optional[str] = None
    id_role: Optional[int] = None
    password: Optional[str] = None

    @field_validator("password")
    @classmethod
    def password_cannot_be_null_or_empty(cls, value: Optional[str]) -> str:
        if value is None or value == "":
            raise ValueError("password ne peut pas etre null ou vide")
        return value


class UtilisateurOut(UtilisateurBase):
    """Schema retourné par l'API."""
    id_user: int
    date_insc_user: datetime

    model_config = ConfigDict(from_attributes=True)

class UtilisateurOutWithApiKey(UtilisateurOut):
    """Schéma retourné par l'API avec la clé API."""
    api_key: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class UtilisateurInDB(UtilisateurOut):
    """MDP haché en base de données."""
    hashed_password: str

    model_config = ConfigDict(from_attributes=True)
