from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.communication.final_status import (
    communication_final_status,
)
from app.modules.communication.router import (
    router as communication_router,
)


app = FastAPI()

app.include_router(
    communication_router
)

client = TestClient(app)


def test_final_status_ready():
    status = (
        communication_final_status
        .snapshot()
    )

    assert (
        status["block"]["ready"]
        is True
    )


def test_final_status_api():
    response = client.get(
        "/communication/final-status"
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


def test_provider_health_api():
    response = client.get(
        "/communication/providers/health"
    )

    assert (
        response.status_code
        == 200
    )

    assert isinstance(
        response.json(),
        list,
    )


def test_inbound_status_api():
    response = client.get(
        "/communication/inbound/status"
    )

    assert (
        response.status_code
        == 200
    )


def test_dead_letter_api():
    response = client.get(
        "/communication/dead-letter"
    )

    assert (
        response.status_code
        == 200
    )


def test_ack_api():
    response = client.get(
        "/communication/acks"
    )

    assert (
        response.status_code
        == 200
    )


def test_integration_api():
    response = client.get(
        "/communication/integration"
    )

    assert (
        response.status_code
        == 200
    )


def test_observability_api():
    response = client.get(
        "/communication/observability"
    )

    assert (
        response.status_code
        == 200
  )
