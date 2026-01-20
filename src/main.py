from src.models.base import Base
from fastapi import FastAPI
from .models import *
from .database import engine
from .routers import commune_router

# Create the FastAPI app and include the router
app = FastAPI()
app.include_router(commune_router)

# Import the models to create the tables in the database
Base.metadata.create_all(engine)

#Define a simple root endpoints to check the connection
@app.get("/")
def read_root():
    return{"message": "Connected to the database"}
