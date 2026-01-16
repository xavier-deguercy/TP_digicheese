from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# create a router for communes-related endpoints
router = APIRouter(prefix="/commune", tags=["commune"])
