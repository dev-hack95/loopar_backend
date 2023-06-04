from src.models.user_models import User
from src.models.blog_models import Blog
from src.schema.blog.schema import BlogCreate, BlogResponse, BlogUpdate
from typing import List
from uuid import UUID

class BlogService:
    @staticmethod
    async def list_blogs(user: User) -> List[Blog]:
        blogs = await Blog.find(Blog.owner.id == user.user_id).to_list()
        return blogs
    
    @staticmethod
    async def create_blogs(user: User, data: BlogCreate) -> Blog:
        blog = Blog(**data.dict(), owner=user)
        return await blog.insert()
    
    @staticmethod
    async def get_blog(current_user: User, blog_id: UUID):
        blog = await Blog.find_one(Blog.blog_id == blog_id)
        return blog
    
    @staticmethod
    async def delete_blog(current_user: User, blog_id: UUID):
        blog = await Blog.delete(Blog.blog_id == blog_id)
        return blog
    
