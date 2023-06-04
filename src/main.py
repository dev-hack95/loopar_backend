from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings
from src.models.user_models import User
from src.models.blog_models import Blog
from src.api.api_v1.router import router

app = FastAPI( 
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def startup():
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).loopardb

    await init_beanie(
        database=client,
        document_models=[
            User,
            Blog
        ]
    )

app.include_router(router=router, prefix=settings.API_V1_STR)