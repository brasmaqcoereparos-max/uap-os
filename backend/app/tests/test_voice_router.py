from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.voice.router import (
    router as voice_router,
)


app = FastAPI()

app.include_router(
    voice_router
)

client = TestClient(app)


def test_voice_router_loaded():
    routes = [
        route.path
        for route
        in app.routes
    ]

    assert any(
        path.startswith(
            "/voice"
        )
        for path in routes
    )
