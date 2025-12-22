from fastapi import APIRouter

from app.api.v1 import auth, exams, results, history

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(exams.router)
api_router.include_router(results.router)
api_router.include_router(history.router)
