from fastapi import FastAPI

from database import init_db
from user_controller import user_router

app = FastAPI(
    title="Asyncpg example",
    description="Create users with asyncpg",
    version="0.0.1",
)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def index():
    return {"message": "Api is running"}

app.include_router(user_router, prefix="/api/v1")