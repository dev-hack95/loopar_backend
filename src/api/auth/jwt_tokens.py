from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from src.services.user.service import UserService
from src.core.security import access_token, refresh_token
from src.core.security import get_password, verify_password, access_token, refresh_token
from src.schema.auth.schema import TokenPayload, TokenSchema
from src.core.config import settings
from pydantic import ValidationError
from jose import jwt
from typing import Any

authentication_router = APIRouter()

@authentication_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:  # Returns any type of value
    user = await UserService.authencate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username and password not valid")
    
    return {
        "access_token": access_token(user.user_id),
        "refresh_token": refresh_token(user.user_id)
    }


@authentication_router.post('/refresh')
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(refresh_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)

    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid token",headers={"WWW-Authenticate": "Bearer"})
    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid token for user",
        )
    
    return {
        "access_token": access_token(user.user_id),
        "refresh_token": refresh_token(user.user_id)
    }
