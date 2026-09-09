from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.simulator.router import (
    router as simulator_router,
)
from app.modules.simulator.codegen.router import (
    router as codegen_router,
)
from app.modules.simulator.programming.canvas.router import (
    router as canvas_router,
)
from app.modules.simulator.programming.router import (
    router as programming_router,
)


app = FastAPI()

app.include_router(
    simulator_router
)

app.include_router(
    programming_router
)

app.include_router(
    canvas_router
)

app.include_router(
    codegen_router
)

client = TestClient(app)


def test_simulator_routes_loaded():
    routes = [
        route.path
        for route
        in app.routes
    ]

    assert len(routes) > 0
