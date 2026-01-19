from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

import os
import time
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables d'environnement pour la base de données
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

CONNECTION_STRING = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

max_retries = 10
retry_delay = 3  # secondes

# Try to create the database engine with retries
engine = None
for attempt in range(max_retries):
    try:
        engine = create_engine(CONNECTION_STRING, echo=True)
        # Teste la connexion
        with engine.connect() as conn:
            print("Connexion à la base de données réussie !")
        break
    except OperationalError:
        print(f"Connexion échouée (tentative {attempt + 1}/{max_retries}), nouvelle tentative dans {retry_delay}s...")
        time.sleep(retry_delay)
else:
    raise Exception("Impossible de se connecter à la base de données après plusieurs tentatives.")

# Create a session bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Yield a database session for use in FastAPI endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
