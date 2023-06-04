from fastapi import APIRouter, Depends
from src.schema.blog.schema import BlogResponse, BlogCreate, BlogUpdate
from src.services.user.service import User
from src.api.deps.deps import get_current_user
from src.models.blog_models import Blog
from src.services.blog.service import BlogService
from uuid import UUID

blog_router = APIRouter()

@blog_router.get("/", response_model=BlogResponse)
async def list(current_user: User = Depends(get_current_user)):
    return await BlogService.list_blogs(current_user)

@blog_router.post("/create", response_model=BlogResponse)
async def create_blog(data: BlogCreate, current_user: User = Depends(get_current_user)):
    return await BlogService.create_blogs(data, current_user)


@blog_router.get("/{blog_id}", response_model=BlogResponse)
async def get_blog(blog_id: UUID, current_user: User = Depends(get_current_user)):
    return await BlogService.get_blog(current_user, blog_id)

@blog_router.delete("/{blog_id}", response_model=BlogResponse)
async def delete_blog(blog_id: UUID, current_user: User = Depends(get_current_user)):
    return await BlogService.delete_blog(current_user, blog_id)

