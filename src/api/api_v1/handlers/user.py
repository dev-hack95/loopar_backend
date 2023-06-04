from fastapi import APIRouter, HTTPException, status, Depends
from src.schema.user.schema import UserAuth, UserResponse
from src.services.user.service import UserService, UserUpdate, User
from src.api.deps.deps import get_current_user
from pymongo import errors

user_router = APIRouter()

@user_router.post("/create", response_model=UserResponse)
async def create_user(data: UserAuth):
      try:
          return await UserService.create_user(data)
      except errors.DuplicateKeyError:
           raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already present in database")
      