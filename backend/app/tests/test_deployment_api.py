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


def test_deployment_health():
    response = client.get(
        "/deployment/health"
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()[
            "service"
        ]
        == "deployment"
    )


def test_deployment_preflight_api():
    response = client.post(
        "/deployment/preflight",
        json={
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


def test_deployment_installation_plan_api():
    response = client.post(
        "/deployment/installation/plan",
        json={
            "target": (
                "uap-box"
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


def test_deployment_release_api():
    response = client.post(
        "/deployment/release/prepare",
        json={
            "name": "uap-os",
            "version": "0.1.0",
            "target": "uap-box",
            "architecture": "arm64",
            "artifacts": [],
            "include_paths": [],
            "output_path": (
                "dist/uap-os.zip"
            ),
            "base_image": "",
            "packages": [],
        },
    )

    assert (
        response.status_code
        == 200
          )
