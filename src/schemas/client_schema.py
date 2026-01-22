from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ClientBase(BaseModel):
    """Schéma de base pour les données d'un client."""
    email_client: Optional[EmailStr] = None
    nom_client: Optional[str] = Field(default=None, max_length=40)
    prenom_client: Optional[str] = Field(default=None, max_length=30)

    # FK vers t_adresse
    adresse1_client: Optional[int] = None
    adresse2_client: Optional[int] = None

    ville_client: Optional[str] = Field(default=None, max_length=50)
    code_postal_client: Optional[str] = Field(default=None, max_length=5)
    telephone_client: Optional[str] = Field(default=None, max_length=10)


class ClientPost(ClientBase):
    """Schéma utilisé pour la création d'un client."""
    # Dans votre modèle, adresse1_client est NOT NULL
    adresse1_client: int


class ClientPatch(BaseModel):
    """Schéma utilisé pour la mise à jour partielle d'un client."""
    email_client: Optional[EmailStr] = None
    nom_client: Optional[str] = Field(default=None, max_length=40)
    prenom_client: Optional[str] = Field(default=None, max_length=30)

    adresse1_client: Optional[int] = None
    adresse2_client: Optional[int] = None

    ville_client: Optional[str] = Field(default=None, max_length=50)
    code_postal_client: Optional[str] = Field(default=None, max_length=5)
    telephone_client: Optional[str] = Field(default=None, max_length=10)


class ClientOut(ClientBase):
    """Schéma retourné par l'API."""
    id_client: int

    class Config:
        from_attributes = True
