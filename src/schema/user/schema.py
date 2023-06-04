from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserAuth(BaseModel):
    email: EmailStr = Field(...)
    username: str = Field(..., min_length=5, max_length=32)
    password: str = Field(..., min_length=8, max_length=32)

class UserResponse(BaseModel):
    user_id: UUID
    email: EmailStr
    username: str

class UserUpdate(BaseModel):
    email: EmailStr