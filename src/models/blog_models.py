from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from src.models.user_models import User

class Blog(Document):
    blog_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Indexed(str)
    context: str = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]
    
    def __repr__(self) -> str:
        return f"<Blog {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Blog):
            return self.blog_id == other.blog_id
        return False
    
    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at = datetime.utcnow()
        
    
    class Collection:
        name = "blogs"