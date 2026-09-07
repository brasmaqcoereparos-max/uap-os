from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.security.final_status import (
    security_final_status,
)
from app.modules.security.router import (
    router as security_router,
)


app = FastAPI()

app.include_router(
    security_router
)

client = TestClient(app)


def test_security_final_status():
    result = (
        security_final_status
        .snapshot()
    )

    assert (
        result["block"]["ready"]
        is True
    )


def test_security_final_status_api():
    response = client.get(
        "/security/final-status"
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["block"]["ready"]
        is True
    )


def test_security_summary_api():
    response = client.get(
        "/security/summary"
    )

    assert (
        response.status_code
        == 200
    )


def test_security_boundary_runtime_api():
    response = client.get(
        "/security/boundary/runtime",
        params={
            "device_id": (
                "unknown-device"
            )
        },
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()[
            "allowed"
        ]
        is False
    )
