from sqlmodel import SQLModel, Field, Relationship
from typing import List
from datetime import date
from decimal import Decimal

class Departement(SQLModel, table=True):
    """Table représentant les départements français."""
    
    __tablename__ = "t_dept"
    
    code_dept: str = Field(primary_key=True, max_length=2)
    nom_dept: str | None = Field(default=None, max_length=50, nullable=True)
    ordre_aff_dept: int = Field(default=0)
    
    communes: List["Commune"] = Relationship(back_populates="departement")

class Commune(SQLModel, table=True):
    """Table représentant les communes associées à un département."""
    
    __tablename__ = "t_communes"
    
    id: int | None = Field(default=None, primary_key=True)
    dep: str = Field(foreign_key="t_dept.code_dept", max_length=2, nullable=False)
    cp: str | None = Field(default=None, max_length=5, nullable=True)
    ville: str | None = Field(default=None, max_length=50, nullable=True)
    
    departement: Departement | None = Relationship(back_populates="communes")

class Client(SQLModel, table=True):
    """Table représentant les clients de la fidélisation de la fromagerie."""
    
    __tablename__ = "t_client"
    
    codcli: int | None = Field(default=None, primary_key=True)
    genrecli: str | None = Field(default=None, max_length=8, nullable=True)
    nomcli: str | None = Field(default=None, max_length=40, index=True, nullable=True)
    prenomcli: str | None = Field(default=None, max_length=30, nullable=True)
    adresse1cli: str | None = Field(default=None, max_length=50, nullable=True)
    adresse2cli: str | None = Field(default=None, max_length=50, nullable=True)
    adresse3cli: str | None = Field(default=None, max_length=50, nullable=True)
    villecli_id: int | None = Field(default=None, foreign_key="t_communes.id", nullable=True)
    telcli: str | None = Field(default=None, max_length=10, nullable=True)
    emailcli: str | None = Field(default=None, max_length=255, nullable=True)
    portcli: str | None = Field(default=None, max_length=10, nullable=True)
    newsletter: int | None = Field(default=None, nullable=True)

class Commande(SQLModel, table=True):
    """Table représentant les commandes passées par les clients."""
    
    __tablename__ = "t_entcde"
    
    codcde: int | None = Field(default=None, primary_key=True)
    datcde: date | None = Field(default=None, nullable=True)
    codcli: int | None = Field(default=None, foreign_key="t_client.codcli", nullable=True)
    timbrecli: float | None = Field(default=None, nullable=True)
    timbrecde: float | None = Field(default=None, nullable=True)
    nbcolis: int = Field(default=1)
    cheqcli: float | None = Field(default=None, nullable=True)
    idcondit: int = Field(default=0)
    cdeComt: str | None = Field(default=None, max_length=255, nullable=True)
    barchive: int = Field(default=0)
    bstock: int = Field(default=0)

class Conditionnement(SQLModel, table=True):
    """Table représentant les conditionnements disponibles pour les objets."""

    __tablename__ = "t_conditionnement"
    
    idcondit: int | None = Field(default=None, primary_key=True)
    libcondit: str | None = Field(default=None, max_length=50, nullable=True)
    poidscondit: int | None = Field(default=None, nullable=True)
    prixcond: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    ordreimp: int | None = Field(default=None, nullable=True)
    
    objets: List["ObjetCond"] = Relationship(back_populates="condit")

class Objet(SQLModel, table=True):
    """Table représentant les objets disponibles dans la fromagerie."""
    
    __tablename__ = "t_objet"
    
    codobj: int | None = Field(default=None, primary_key=True)
    libobj: str | None = Field(default=None, max_length=50, nullable=True)
    tailleobj: str | None = Field(default=None, max_length=50, nullable=True)
    puobj: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    poidsobj: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    indispobj: int = Field(default=0)
    o_imp: int = Field(default=0)
    o_aff: int = Field(default=0)
    o_cartp: int = Field(default=0)
    points: int = Field(default=0)
    o_ordre_aff: int = Field(default=0)
    
    condit: List["ObjetCond"] = Relationship(back_populates="objets")

class ObjetCond(SQLModel, table=True):
    """Table représentant la relation entre les objets et les conditionnements."""
    
    __tablename__ = "t_rel_cond"
    
    idrelcond: int | None = Field(default=None, primary_key=True, index=True)
    qteobjdeb: int = Field(default=0)
    qteobjfin: int = Field(default=0)
    codobj: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)
    codcond: int | None = Field(default=None, foreign_key="t_conditionnement.idcondit", nullable=True)
    
    objets: Objet | None = Relationship(back_populates="condit")
    condit: Conditionnement | None = Relationship(back_populates="objets")

class Detail(SQLModel, table=True):
    """Table représentant les détails des commandes."""
    
    __tablename__ = "t_dtlcode"
    
    id: int | None = Field(default=None, primary_key=True) 
    codcde: int | None = Field(default=None, foreign_key="t_entcde.codcde", index=True, nullable=True)
    qte: int = Field(default=1)
    colis: int = Field(default=1)
    commentaire: str | None = Field(default=None, max_length=100, nullable=True)

class DetailObjet(SQLModel, table=True):
    """Table représentant les détails des objets associés aux commandes."""
    
    __tablename__ = "t_dtlcode_codobj"
    
    id: int | None = Field(default=None, primary_key=True)
    detail_id: int | None = Field(default=None, foreign_key="t_dtlcode.id", nullable=True)
    objet_id: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)

class Enseigne(SQLModel, table=True):
    """Table représentant les enseignes que la société travaille avec."""
    
    __tablename__ = "t_enseigne"
    
    id_enseigne: int | None = Field(default=None, primary_key=True)
    lb_enseigne: str | None = Field(default=None, max_length=50, nullable=True)
    ville_enseigne: str | None = Field(default=None, max_length=50, nullable=True)
    dept_enseigne: int = Field(default=0)

class Poids(SQLModel, table=True):
    """Table représentant les poids et timbres associés aux commandes."""
    
    __tablename__ = "t_poids"
    
    id: int | None = Field(default=None, primary_key=True)
    valmin: Decimal | None = Field(default=Decimal("0"), nullable=True)
    valtimbre: Decimal | None = Field(default=Decimal("0"), nullable=True)
    
class Vignette(SQLModel, table=True):
    """Table représentant les vignettes (timbre) avec leurs prix pour un certain poids."""
    
    __tablename__ = "t_poidsv"
    
    id: int | None = Field(default=None, primary_key=True)
    valmin: Decimal | None = Field(default=Decimal("0"), nullable=True)
    valtimbre: Decimal | None = Field(default=Decimal("0"), nullable=True)


class Role(SQLModel, table=True):
    """Table représentant les rôles dans le système."""
    
    __tablename__ = "t_role"
    
    codrole: int | None = Field(default=None, primary_key=True)
    librole: str | None = Field(default=None, max_length=25, nullable=True)

class Utilisateur(SQLModel, table=True):
    """Table représentant les utilisateurs dans le système."""
    
    __tablename__ = "t_utilisateur"
    
    code_utilisateur: int | None = Field(default=None, primary_key=True)
    nom_utilisateur: str | None = Field(default=None, max_length=50, nullable=True)
    prenom_utilisateur: str | None = Field(default=None, max_length=50, nullable=True)
    username: str | None = Field(default=None, max_length=50, nullable=True)
    couleur_fond_utilisateur: int = Field(default=0)
    date_insc_utilisateur: date | None = Field(default=None, nullable=True)

class RoleUtilisateur(SQLModel, table=True):
    """Table d'association entre les utilisateurs et leurs rôles."""
    
    __tablename__ = "t_utilisateur_role"
    
    id: int | None = Field(default=None, primary_key=True)
    utilisateur_id: int | None = Field(default=None, foreign_key="t_utilisateur.code_utilisateur", nullable=True)
    role_id: int | None = Field(default=None, foreign_key="t_role.codrole", nullable=True)
