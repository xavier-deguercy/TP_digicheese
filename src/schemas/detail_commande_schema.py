from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class DetailCommandePost(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "quantite": 2,
                "commentaire": "Sans substitution",
                "id_commande": 1,
                "id_objet": 3,
            }
        }
    )

    quantite: int = Field(ge=1)
    commentaire: Optional[str] = Field(default=None, max_length=1000)
    id_commande: int
    id_objet: int


class DetailCommandePatch(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "quantite": 3,
                "commentaire": "Quantite corrigee",
            }
        }
    )

    quantite: Optional[int] = Field(default=None, ge=1)
    commentaire: Optional[str] = Field(default=None, max_length=1000)
    id_objet: Optional[int] = None

    @model_validator(mode="after")
    def required_fields_cannot_be_null(self):
        for field in ("quantite", "id_objet"):
            if field in self.model_fields_set and getattr(self, field) is None:
                raise ValueError(f"{field} ne peut pas etre null")
        return self


class DetailCommandeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_detail_commande: int
    quantite: int
    commentaire: Optional[str]
    id_commande: int
    id_objet: int
