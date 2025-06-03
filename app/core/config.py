# app/core/config.py

import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Aplikasi
    APP_NAME: str = "FastAPI App"
    API_PREFIX: str = "/api"

    # Keamanan
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Database
    DATABASE_URL: str = "sqlite:///./app.db"

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")  # bisa override dengan ENV_FILE
        env_file_encoding = "utf-8"
        case_sensitive = True


config = Settings()
