# backend/app/core/config.py

from pydantic import BaseModel
from datetime import timedelta


class Settings(BaseModel):
    PROJECT_NAME: str = "English Placement Test API"

    # JWT
    JWT_SECRET_KEY: str = "CHANGE_ME_SUPER_SECRET"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


settings = Settings()
