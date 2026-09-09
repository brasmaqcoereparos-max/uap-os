from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.vision.vision_router import (
    router as vision_router,
)


app = FastAPI()

app.include_router(
    vision_router
)

client = TestClient(app)


def test_vision_router_loaded():
    routes = [
        route.path
        for route
        in app.routes
    ]

    assert len(
        routes
    ) > 0
