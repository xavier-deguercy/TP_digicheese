from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ClientBase(BaseModel):
    """Schéma de base pour les données d'un client."""
    email_client: Optional[EmailStr] = None
    nom_client: Optional[str] = Field(default=None, max_length=40)
    prenom_client: Optional[str] = Field(default=None, max_length=30)
    adresse1_client: Optional[int] = None
    adresse2_client: Optional[int] = None
    telephone_client: Optional[str] = Field(default=None, max_length=10)


class ClientPost(ClientBase):
    """Schéma utilisé pour la création d'un client."""
    adresse1_client: int


class ClientPatch(BaseModel):
    """Schéma utilisé pour la mise à jour partielle d'un client."""
    email_client: Optional[EmailStr] = None
    nom_client: Optional[str] = Field(default=None, max_length=40)
    prenom_client: Optional[str] = Field(default=None, max_length=30)
    adresse1_client: Optional[int] = None
    adresse2_client: Optional[int] = None
    telephone_client: Optional[str] = Field(default=None, max_length=10)

class ClientOut(ClientBase):
    """Schéma retourné par l'API."""
    id_client: int

    class Config:
        from_attributes = True

class CommuneOut(BaseModel):
    id_commune: int
    dep: Optional[str] = None
    cp: Optional[str] = Field(default=None, max_length=5)

    class Config:
        from_attributes = True

class AdresseOut(BaseModel):
    id_adresse: int
    rue: Optional[str] = None
    compAdresse: Optional[str] = None
    commune: Optional[CommuneOut] = None

    class Config:
        from_attributes = True

class ClientOutDetailed(BaseModel):
    id_client: int
    email_client: Optional[EmailStr] = None
    nom_client: Optional[str] = Field(default=None, max_length=40)
    prenom_client: Optional[str] = Field(default=None, max_length=30)
    adresse1_client: Optional[int] = None
    adresse2_client: Optional[int] = None
    telephone_client: Optional[str] = Field(default=None, max_length=10)
    adresse1: Optional[AdresseOut] = None
    adresse2: Optional[AdresseOut] = None

    class Config:
        from_attributes = True
