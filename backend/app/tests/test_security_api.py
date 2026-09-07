from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.security.router import (
    router as security_router,
)


app = FastAPI()

app.include_router(
    security_router
)

client = TestClient(app)


def test_security_health():
    response = client.get(
        "/security/health"
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["service"]
        == "security"
    )


def test_security_identity_api():
    response = client.post(
        "/security/identity",
        json={
            "serial_number": (
                "TEST-SERIAL"
            ),
            "board": (
                "test-board"
            ),
            "model": (
                "test-model"
            ),
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["serial_number"]
        == "TEST-SERIAL"
    )


def test_security_license_validate_api():
    response = client.post(
        "/security/license/validate",
        json={
            "device_id": (
                "missing-device"
            ),
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["validation"][
            "valid"
        ]
        is False
    )
