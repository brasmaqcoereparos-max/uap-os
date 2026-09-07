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


def test_protection_status():
    response = client.get(
        "/security/protection/status"
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["service"]
        == "security-protection"
    )


def test_create_security_session():
    response = client.post(
        "/security/sessions",
        params={
            "principal_id": (
                "test-user"
            )
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["principal_id"]
        == "test-user"
    )


def test_access_check():
    response = client.get(
        "/security/access/check",
        params={
            "principal_id": (
                "test-access-user"
            )
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


def test_security_events():
    response = client.get(
        "/security/events"
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        "events"
        in response.json()
  )
