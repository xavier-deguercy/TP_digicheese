# src/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.utils.create_db import create_tables

from src.routers.role_router import router as role_router
from src.routers.utilisateur_router import router as utilisateur_router
from src.routers.commune_router import router as commune_router
from src.routers.adresse_router import router as adresse_router
from src.routers.objet_router import router as objet_router
from src.routers.poids_router import router as poids_router
from src.routers.poidsv_router import router as poidsv_router
from src.routers.conditionnement_router import router as conditionnement_router
from src.routers.client_router import router as client_router
from src.routers.dev_router import router as dev_router

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Crée les tables au démarrage (utile si tu n'as pas encore la DB)
    create_tables()
    yield


app = FastAPI(title="DigiCheese API", version="1.0.0", lifespan=lifespan)

# CORS — indispensable pour l'IHM servie sur un autre port (ex: 5500/8000)
# DEV uniquement : en prod, restreins allow_origins à ton domaine
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(dev_router)
app.include_router(utilisateur_router)
app.include_router(role_router)
app.include_router(commune_router)
app.include_router(adresse_router)
app.include_router(client_router)
app.include_router(objet_router)
app.include_router(poids_router)
app.include_router(poidsv_router)
app.include_router(conditionnement_router)


@app.get("/health")
def health():
    return {"status": "ok"}
