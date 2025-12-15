# backend/app/main.py

from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="English Placement Test API",
    version="1.0.0",
    description="Production-ready REST API for English placement testing"
)


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "environment": settings.ENVIRONMENT
    }
