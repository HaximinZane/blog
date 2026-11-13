from fastapi import APIRouter,Depends
from ..core.database import get_conn
from ..services import tag_service


router = APIRouter(prefix="/api/v1/tags",tags=["tags"])

@router.get("/")
async def tags(conn = Depends(get_conn)):
    return await tag_service.list_tags(conn=conn)