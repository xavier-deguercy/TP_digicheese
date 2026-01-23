from sqlalchemy.orm import Session
from sqlalchemy import select
from src.database import engine, SessionLocal
from src.models.base import Base
import time
from sqlalchemy import text
from src.utils.password import hash_password
import secrets

from src.models.role import Role
from src.models.utilisateur import Utilisateur
from src.models.client import Client
from src.models.commune import Commune
from src.models.conditionnement import Conditionnement
from src.models.objet import Objet
from src.models.poidsv import Poidsv
from src.models.poids import Poids
from src.models.adresse import Adresse


DEFAULT_ROLES = ["Admin", "OP-COLIS", "OP-STOCK"]

def wait_for_db(engine, retries=10, delay=1):
    for i in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return
        except Exception:
            time.sleep(delay)
    raise RuntimeError("DB not ready")

def init_db():
    wait_for_db(engine)
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        for libelle in DEFAULT_ROLES:
            exists = db.scalars(
                select(Role).where(Role.libelle_role == libelle)
            ).first()
            if not exists:
                db.add(Role(libelle_role=libelle))
        db.commit()

        admin_role = db.scalars(select(Role).where(Role.libelle_role == "Admin")).first()
        existing_admin = db.scalars(select(Utilisateur).where(Utilisateur.id_role == admin_role.id_role)).first()

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

            print("Seed admin created: username=admin password=admin api_key=", admin.api_key)

    finally:
        db.close()
