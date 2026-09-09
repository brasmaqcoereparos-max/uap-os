from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.automation.router import (
    router as automation_router,
)


app = FastAPI()

app.include_router(
    automation_router
)

client = TestClient(app)


def test_automation_router_loaded():
    routes = [
        route.path
        for route
        in app.routes
    ]

    assert len(routes) > 0
