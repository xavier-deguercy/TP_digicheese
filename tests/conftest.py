# ruff: noqa: E402, F401
# DATABASE_URL doit être défini avant les imports applicatifs ; les modèles sont
# importés pour enregistrer leurs tables dans Base.metadata.
import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# La configuration doit exister avant l'import de l'application.
SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///:memory:"
os.environ["DATABASE_URL"] = SQLALCHEMY_DATABASE_URL

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

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # garde la même connexion en mémoire
)


@event.listens_for(engine, "connect")
def enable_sqlite_foreign_keys(dbapi_connection, connection_record):
    """Aligne les tests SQLite sur les contraintes FK actives dans MySQL."""
    del connection_record
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True, scope="session")
def disable_auth_for_tests():
    os.environ["DISABLE_AUTH"] = "true"
    yield
    os.environ.pop("DISABLE_AUTH", None)


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
