from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.communication.router import (
    router as communication_router,
)


app = FastAPI()

app.include_router(
    communication_router
)

client = TestClient(app)


def test_communication_health():
    response = client.get(
        "/communication/health"
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["service"]
        == "communication"
    )


def test_transports_api():
    response = client.get(
        "/communication/transports"
    )

    assert (
        response.status_code
        == 200
    )

    assert isinstance(
        response.json(),
        list,
    )


def test_open_memory_connection():
    response = client.post(
        "/communication/connections",
        json={
            "transport": "memory",
            "destination": "test",
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["connection"][
            "state"
        ]
        == "connected"
    )


def test_publish_api():
    response = client.post(
        "/communication/publish",
        json={
            "topic": "test.topic",
            "source": "api-test",
            "payload": {
                "value": 1,
            },
        },
    )

    assert (
        response.status_code
        == 200
    )
