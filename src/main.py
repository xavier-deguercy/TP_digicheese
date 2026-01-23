# src/main.py
from fastapi import FastAPI
from src.utils.create_db import init_db
from contextlib import asynccontextmanager
from dotenv import load_dotenv
load_dotenv()

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

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="DigiCheese API", version="1.0.0", lifespan=lifespan)

app.include_router(role_router)
app.include_router(utilisateur_router)
app.include_router(commune_router)
app.include_router(adresse_router)
app.include_router(objet_router)
app.include_router(poids_router)
app.include_router(poidsv_router)
app.include_router(conditionnement_router)
app.include_router(client_router)
app.include_router(dev_router)

@app.get("/health")
def health():
    return {"status": "ok"}
