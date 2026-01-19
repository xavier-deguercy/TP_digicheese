from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UtilisateurBase(BaseModel):
    """Base schema pour utilisateur."""
    nom_user: Optional[str] = None
    prenom_user: Optional[str] = None
    username: Optional[str] = None
    id_role: int


class UtilisateurPost(UtilisateurBase):
    """Créer un utilisateur."""
    password: str  # mot de passe en clair UNIQUEMENT à la création


class UtilisateurPatch(BaseModel):
    """Schema for update un utilisateur"""
    nom_user: Optional[str] = None
    prenom_user: Optional[str] = None
    username: Optional[str] = None
    id_role: Optional[int] = None
    password: Optional[str] = None


class UtilisateurOut(UtilisateurBase):
    """Schema retourné par l'API."""
    id_user: int
    date_insc_user: datetime

    class Config:
        from_attributes = True


class UtilisateurInDB(UtilisateurOut):
    """MDP haché en base de données."""
    hashed_password: str

    class Config:
        from_attributes = True
