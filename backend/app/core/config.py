from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "English Placement Test"

    DATABASE_URL: str = "sqlite:///./english.db"

    class Config:
        env_file = ".env"


settings = Settings()
