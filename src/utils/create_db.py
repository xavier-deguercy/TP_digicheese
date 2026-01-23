from sqlalchemy.orm import Session
from sqlalchemy import select
import secrets

from src.database import engine, SessionLocal
from src.models.base import Base
from src.utils.password import hash_password

from src.models.role import Role
from src.models.utilisateur import Utilisateur
from src.models.client import Client
from src.models.commune import Commune
from src.models.adresse import Adresse
from src.models.poids import Poids
from src.models.poidsv import Poidsv
from src.models.conditionnement import Conditionnement
from src.models.objet import Objet

DEFAULT_ROLES = ["Admin", "OP-COLIS", "OP-STOCK"]


def create_tables():
    Base.metadata.create_all(bind=engine)


def seed_roles_and_admin():
    db: Session = SessionLocal()
    try:
        # roles
        for libelle in DEFAULT_ROLES:
            exists = db.scalars(select(Role).where(Role.libelle_role == libelle)).first()
            if not exists:
                db.add(Role(libelle_role=libelle))
        db.commit()

        # admin
        admin_role = db.scalars(select(Role).where(Role.libelle_role == "Admin")).first()
        existing_admin = db.scalars(
            select(Utilisateur).where(Utilisateur.id_role == admin_role.id_role)
        ).first()

        if not existing_admin:
            admin = Utilisateur(
                nom_user="Admin",
                prenom_user="Root",
                username="admin",
                hashed_password=hash_password("admin"),
                id_role=admin_role.id_role,
                api_key=secrets.token_hex(32),
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
            print(f"Veuillez coller ceci dans Swagger : {admin.api_key}")

    finally:
        db.close()
