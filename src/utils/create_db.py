# src/create_db.py

from src.database import engine
from src.models.base import Base

# IMPORTANT : importer tous les modèles pour que Base.metadata connaisse les tables
from src.models.role import Role
from src.models.utilisateur import Utilisateur
from src.models.client import Client
from src.models.commune import Commune
from src.models.conditionnement import Conditionnement
from src.models.objet import Objet
from src.models.poidsv import Poidsv
from src.models.poids import Poids
from src.models.adresse import Adresse


def main() -> None:
    Base.metadata.create_all(engine)
    print("DB schema created ✅")


if __name__ == "__main__":
    main()
