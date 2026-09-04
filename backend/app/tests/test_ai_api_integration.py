from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

from app.modules.ai.router import (
    router as ai_router,
)


def create_test_app():
    app = FastAPI()

    app.include_router(
        ai_router
    )

    return app


app = create_test_app()

client = TestClient(app)


def test_ai_health():
    response = client.get(
        "/ai/health"
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert data[
        "service"
    ] == "ai"


def test_ai_plan_api():
    response = client.post(
        "/ai/plan",
        json={
            "title": "Teste",
            "description": (
                "Projeto de teste"
            ),
            "task_type": "general",
            "parameters": {},
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert "plan" in data


def test_ai_project_api():
    response = client.post(
        "/ai/project",
        json={
            "name": "Teste",
            "objective": (
                "Criar projeto"
            ),
            "requirements": [],
        },
    )

    assert (
        response.status_code
        == 200
    )


def test_ai_hardware_api():
    response = client.post(
        "/ai/hardware",
        json={
            "requirements": {
                "gpio": 2,
            },
            "boards": [
                {
                    "id": "board",
                    "name": "Test Board",
                    "capabilities": {
                        "gpio": 10,
                    },
                }
            ],
        },
    )

    assert (
        response.status_code
        == 200
    )


def test_ai_automation_api():
    response = client.post(
        "/ai/automation",
        json={
            "text": (
                "Criar automação"
            ),
            "objective": "Teste",
            "entities": {},
        },
    )

    assert (
        response.status_code
        == 200
    )


def test_ai_ui_api():
    response = client.post(
        "/ai/ui",
        json={
            "text": (
                "Criar interface"
            ),
            "app_type": "kiosk",
            "preferences": {},
        },
    )

    assert (
        response.status_code
        == 200
    )
