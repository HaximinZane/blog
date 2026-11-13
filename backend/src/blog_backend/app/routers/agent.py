from fastapi import APIRouter,Depends,HTTPException
from ..agent.service import generate_text,llm_read_post
from ..core.database import get_conn
from ..services.post_service import get_public_post

router = APIRouter(prefix="/api/v1/agent",tags=["Agent"])

@router.post("/text")
async def agent_text(message:dict[str,str]):
    return await generate_text(message=message)

@router.post("/posts/{post_id}/ask")
async def agent_post_ask(message:dict[str,str],post_id:int,conn=Depends(get_conn)):
    try:
        row = await get_public_post(conn,post_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    if row is None:
        raise HTTPException(status_code=404, detail="文章不存在")
    message["user"] += '\n' + str(row)
    result =  await llm_read_post(message=message)
    return {"ok":True,"data":result}