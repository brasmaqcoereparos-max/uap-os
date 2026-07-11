from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import router
from app.core.version import APP_NAME, APP_VERSION
from app.database.base import Base
from app.database.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria automaticamente todas as tabelas do banco
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    lifespan=lifespan,
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "status": "online",
    }
