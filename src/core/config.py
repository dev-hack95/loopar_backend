from pydantic import BaseSettings, AnyHttpUrl
from typing import List
from decouple import config

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1" #Endpoints
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 30 * 24 * 60  # 60 days of long lived token
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = "LOOPAR_BACKEND"

    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)

    class Config:
        case_sensitive = True

settings = Settings()