from fastapi import APIRouter,Query,Depends
from ..services import post_service
from typing import Annotated
from ..core.database import get_conn
from ..models.post import PostCreate

router = APIRouter(tags=["posts"],prefix="/api/v1/posts")

@router.get("/")
async def list_posts(conn = Depends(get_conn),skip:int = 0,limit: Annotated[int,Query(le=50)] = 10):
    return await post_service.list_public_posts(conn,skip,limit)

@router.get("/{post_id}")
async def get_post(post_id : int,conn = Depends(get_conn)):
    return await post_service.get_public_post(conn,post_id)

@router.post("/")
async def create_post(post : PostCreate,conn = Depends(get_conn)):
    return await post_service.create_post(conn,post)
        