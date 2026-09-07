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


def test_distribution_status_api():
    response = client.get(
        "/deployment/distribution/status"
    )

    assert (
        response.status_code
        == 200
    )


def test_release_summary_api():
    response = client.get(
        "/deployment/release/summary"
    )

    assert (
        response.status_code
        == 200
    )


def test_boundary_install_api():
    response = client.get(
        "/deployment/boundary/install",
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
        "allowed"
        in response.json()
    )


def test_final_status_api():
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
