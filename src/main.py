from fastapi import FastAPI
from src.routers.role_router import router as role_router
from src.routers.utilisateur_router import router as utilisateur_router
from src.routers.poids_router import router as poids_router
from src.routers.poidsv_router import router as poidsv_router

app = FastAPI(
    title="DigiCheese API",
    version="0.1.0",
)

app.include_router(role_router)
app.include_router(utilisateur_router)
app.include_router(poids_router)
app.include_router(poidsv_router)
