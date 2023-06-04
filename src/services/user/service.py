from src.schema.user.schema import UserAuth
from src.models.user_models import User
from src.core.security import get_password, verify_password
from src.schema.user.schema import UserUpdate
from typing import Optional
from uuid import UUID
from pymongo import errors

class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_data = User(
            username = user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        await user_data.save()
        return user_data
    
    @staticmethod
    async def authencate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hash_pass=user.hashed_password):
            return None
        
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user
    
    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id  == id)
        return user
    
    @staticmethod
    async def update_user(id: UUID, data: UserUpdate) -> User:
        user = await User.find_one(User.user_id == id)
        if not user:
            raise errors.OperationFailure("User not found")
    
        await user.update({"$set": data.dict(exclude_unset=True)})
        return user
