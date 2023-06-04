from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class BlogCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=255)
    context: str = Field(..., max_length=999999)
    author: str = Field(..., max_length=55)
    published: Optional[bool] = True

class BlogUpdate(BaseModel):
    title: Optional[str] = Field(..., title='Title', max_length=255)
    context: Optional[str] = Field(..., max_length=999999)
    author: Optional[str] = Field(..., max_length=55)
    published: Optional[bool] = True

class BlogResponse(BaseModel):
    blog_id: UUID
    published: bool
    title: str
    context: str
    created_at: datetime