from passlib.context import CryptContext
from typing import Any
from datetime import datetime, timedelta
from src.core.config import settings
from jose import jwt

password_ctx = CryptContext(schemes=["bcrypt"])

def get_password(password: str) -> str:
    return password_ctx.hash(password)

def verify_password(password: str, hash_pass: str) -> bool:
    return password_ctx.verify(password, hash_pass)

def access_token(sub: Any, expires_by: int = None) -> str:
    if expires_by is not None:
        expires_by = datetime.utcnow() + expires_by
    else:
        expires_by = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_by, "sub": str(sub)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt

def refresh_token(sub: Any, expires_by: int = None) -> str:
    if expires_by is not None:
        expires_by = datetime.utcnow() + expires_by
    else:
        expires_by = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_by, "sub": str(sub)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt    