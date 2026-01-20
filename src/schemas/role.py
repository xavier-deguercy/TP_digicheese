from typing import Optional
from pydantic import BaseModel


class RoleBase(BaseModel):
    """Schéma de base pour les données d'un rôle."""
    libelle_role: Optional[str] = None


class RolePost(RoleBase):
    """Schéma utilisé pour la création d'un rôle."""
    pass


class RolePatch(BaseModel):
    """Schéma utilisé pour la mise à jour partielle d'un rôle."""
    libelle_role: Optional[str] = None


class RoleOut(RoleBase):
    """Schéma retourné par l'API."""
    id_role: int

    class Config:
        from_attributes = True
