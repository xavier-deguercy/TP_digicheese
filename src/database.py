from sqlalchemy import create_engine
from src.models.base import Base

# IMPORTANT : importer les modèles pour enregistrer les tables dans Base.metadata
from src.models.role import Role
from src.models.utilisateur import Utilisateur
from src.models.client import Client
from src.models.commune import Commune
from src.models.conditionnement import Conditionnement
from src.models.objet import Objet
from src.models.poids_v import Poidsv
from src.models.poids import Poids
from src.models.adresse import Adresse

DATABASE_URL = "mysql+pymysql://group2:digicheese@localhost:3308/digicheese"

engine = create_engine(DATABASE_URL, echo=True)

def main() -> None:
    Base.metadata.create_all(engine)
    print("Tables created ✅")

if __name__ == "__main__":
    main()
