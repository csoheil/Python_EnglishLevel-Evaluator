# backend/app/core/config.py

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "English Placement Test"
    ENVIRONMENT: str = "development"

    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/placement_test"

    JWT_SECRET_KEY: str = "CHANGE_ME"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
