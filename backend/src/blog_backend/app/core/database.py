from dotenv import load_dotenv
import os
import asyncio,asyncpg
from fastapi import Request

load_dotenv()
dsn = os.getenv("DSN")

async def create_app_pool():
    try:
        pool = await asyncpg.create_pool(dsn=dsn)
    except Exception as e:
        raise ConnectionError("failed to create pool")
    return pool

async def get_conn(request:Request):
    pool = request.app.state.pool
    async with pool.acquire() as conn:
        yield conn