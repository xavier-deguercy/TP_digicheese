import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.main import app
from src.database import get_db
from src.models.base import Base

# IMPORTANT : importer les modèles pour que Base.metadata connaisse les tables
from src.models.role import Role
from src.models.utilisateur import Utilisateur
from src.models.client import Client
from src.models.commune import Commune
from src.models.adresse import Adresse
from src.models.poids import Poids
from src.models.poidsv import Poidsv
from src.models.conditionnement import Conditionnement
from src.models.objet import Objet


# Base SQLite en mémoire (rapide)
SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # garde la même connexion en mémoire
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """Crée les tables avant chaque test, puis nettoie."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    """Injecte une session de test dans les dépendances FastAPI."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client():
    """Client HTTP de test."""
    return TestClient(app)
