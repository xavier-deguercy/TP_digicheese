from sqlalchemy import create_engine
from src.models.base import Base

# IMPORTANT : importer tous les modèles pour que SQLAlchemy connaisse les tables
from src.models.role import Role
from src.models.utilisateur import Utilisateur
from src.models.client import Client
# ... ajoute ici Client, Adresse, Commune, etc.

DATABASE_URL = "mysql+pymysql://group2:digicheese@localhost:3308/digicheese"

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

print("DB schema created ✅")
