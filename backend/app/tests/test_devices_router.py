from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.api.routes import devices


app = FastAPI()

app.include_router(
    devices.router
)

client = TestClient(app)


def test_devices_router_loaded():
    routes = [
        route.path
        for route
        in app.routes
    ]

    assert len(routes) > 0
