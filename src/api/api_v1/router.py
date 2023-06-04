from fastapi import APIRouter
from src.api.api_v1.handlers import user
from src.api.api_v1.handlers.blog_crud import blog_router
from src.api.auth.jwt_tokens import authentication_router
router = APIRouter()

router.include_router(user.user_router, prefix="/users", tags=['users'])
router.include_router(authentication_router, prefix="/authentication", tags=['authentication'])
router.include_router(blog_router, prefix="/blog", tags=['blog'])