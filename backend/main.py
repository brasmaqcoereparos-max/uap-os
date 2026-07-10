from fastapi import FastAPI

from app.api.router import router
from app.core.version import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "status": "online",
    }
