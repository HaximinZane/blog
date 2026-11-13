from fastapi import FastAPI
from .routers import health,posts,agent,tags
from fastapi.middleware.cors import CORSMiddleware
from .core.database import create_app_pool
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app : FastAPI):
    app.state.pool = await create_app_pool()
    try:
        yield
    finally:
        await app.state.pool.close()




app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
app.include_router(posts.router)
app.include_router(agent.router)
app.include_router(tags.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500","http://localhost:5500","http://127.0.0.1:8000","http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




