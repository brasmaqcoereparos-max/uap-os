from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.deployment.router import (
    router as deployment_router,
)


app = FastAPI()

app.include_router(
    deployment_router
)

client = TestClient(app)


def test_deployment_summary():
    response = client.get(
        "/deployment/summary"
    )

    assert (
        response.status_code
        == 200
    )


def test_deployment_final_status():
    response = client.get(
        "/deployment/final-status",
        params={
            "target": (
                "generic-linux"
            ),
            "root_path": (
                ".uap-test"
            ),
        },
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()[
            "block"
        ][
            "name"
        ]
        == "deployment"
    )


def test_deployment_service_command():
    response = client.get(
        (
            "/deployment/service/"
            "uap-os/command/status"
        )
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["action"]
        == "status"
    )


def test_deployment_lifecycle_versions():
    response = client.get(
        "/deployment/lifecycle/versions"
    )

    assert (
        response.status_code
        == 200
    )

    assert isinstance(
        response.json(),
        list,
    )
