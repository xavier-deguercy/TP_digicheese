from typing import Optional
from pydantic import BaseModel

class ClientBase(BaseModel):
    """Schéma de base pour les données d'un client."""
    email_client: Optional[str] = None
    nom_client: Optional[str] = None
    prenom_client: Optional[str] = None
    ville_client: Optional[str] = None
    code_postal_client: Optional[str] = None
    telephone_client: Optional[str] = None


class ClientPost(ClientBase):
    """Schéma utilisé pour la création d'un client."""
    adresse1_client: int
    adresse2_client: Optional[int] = None


class ClientPatch(BaseModel):
    """Schéma utilisé pour la mise à jour partielle d'un client."""
    email_client: Optional[str] = None
    nom_client: Optional[str] = None
    prenom_client: Optional[str] = None
    ville_client: Optional[str] = None
    code_postal_client: Optional[str] = None
    telephone_client: Optional[str] = None
    adresse1_client: Optional[int] = None
    adresse2_client: Optional[int] = None


class ClientOut(BaseModel):
    """Schéma retourné par l'API (vue simplifiée)."""
    id_client: int
    nom_client: Optional[str] = None
    prenom_client: Optional[str] = None
    email_client: Optional[str] = None

    class Config:
        from_attributes = True
