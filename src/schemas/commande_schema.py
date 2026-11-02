from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class CommandeBase(BaseModel):
    date_commande: date
    timbre_client: Optional[str] = Field(default=None, max_length=100)
    timbre_code: Optional[str] = Field(default=None, max_length=100)
    nb_colis: Optional[int] = Field(default=None, ge=1)
    b_archive: bool = False
    id_client: int
    id_conditionnement: Optional[int] = None


class CommandePost(CommandeBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "date_commande": "2026-09-07",
                "timbre_client": None,
                "timbre_code": None,
                "nb_colis": None,
                "b_archive": False,
                "id_client": 1,
                "id_conditionnement": None,
            }
        }
    )


class CommandePatch(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id_conditionnement": 2,
                "nb_colis": None,
            }
        }
    )

    date_commande: Optional[date] = None
    timbre_client: Optional[str] = Field(default=None, max_length=100)
    timbre_code: Optional[str] = Field(default=None, max_length=100)
    nb_colis: Optional[int] = Field(default=None, ge=1)
    b_archive: Optional[bool] = None
    id_client: Optional[int] = None
    id_conditionnement: Optional[int] = None

    @model_validator(mode="after")
    def required_fields_cannot_be_null(self):
        for field in ("date_commande", "b_archive", "id_client"):
            if field in self.model_fields_set and getattr(self, field) is None:
                raise ValueError(f"{field} ne peut pas être null")
        return self


class CommandeOut(CommandeBase):
    model_config = ConfigDict(from_attributes=True)

    id_commande: int
