from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.modules.ui.router import (
    router as ui_router,
)
from app.modules.ui.studio_router import (
    router as ui_studio_router,
)


def create_test_app():
    app = FastAPI()

    app.include_router(
        ui_router
    )

    app.include_router(
        ui_studio_router
    )

    return app


app = create_test_app()

client = TestClient(app)


def test_ui_health_route():
    response = client.get(
        "/ui/health"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        dict,
    )


def test_ui_snapshot_route():
    response = client.get(
        "/ui/snapshot"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        dict,
    )


def test_studio_initialize():
    response = client.post(
        "/ui/studio/initialize"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        dict,
    )

    assert "panels" in data
    assert "dock" in data
    assert "palette" in data


def test_studio_snapshot():
    client.post(
        "/ui/studio/initialize"
    )

    response = client.get(
        "/ui/studio/snapshot"
    )

    assert response.status_code == 200

    data = response.json()

    assert "studio" in data
    assert "state" in data


def test_studio_palette():
    client.post(
        "/ui/studio/initialize"
    )

    response = client.get(
        "/ui/studio/palette"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        list,
    )

    assert len(data) > 0


def test_studio_palette_search():
    client.post(
        "/ui/studio/initialize"
    )

    response = client.post(
        "/ui/studio/palette/search",
        json={
            "query": "button",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        list,
    )


def test_create_screen():
    response = client.post(
        "/ui/screens",
        json={
            "name": (
                "integration-screen"
            ),
            "title": (
                "Integration Screen"
            ),
            "route": (
                "/integration"
            ),
            "screen_type": (
                "standard"
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data[
        "name"
    ] == "integration-screen"

    assert "id" in data


def test_screen_widget_flow():
    screen_response = (
        client.post(
            "/ui/screens",
            json={
                "name": (
                    "widget-screen"
                ),
                "title": (
                    "Widget Screen"
                ),
                "route": (
                    "/widget-test"
                ),
                "screen_type": (
                    "standard"
                ),
            },
        )
    )

    assert (
        screen_response
        .status_code
        == 200
    )

    screen = (
        screen_response.json()
    )

    screen_id = screen["id"]

    widget_response = (
        client.post(
            (
                f"/ui/screens/"
                f"{screen_id}"
                "/widgets"
            ),
            json={
                "name": (
                    "test-button"
                ),
                "widget_type": (
                    "button"
                ),
                "properties": {
                    "text": (
                        "Test"
                    )
                },
            },
        )
    )

    assert (
        widget_response
        .status_code
        == 200
    )

    widget = (
        widget_response.json()
    )

    assert widget[
        "name"
    ] == "test-button"

    assert widget[
        "widget_type"
    ] == "button"


def test_studio_hierarchy_flow():
    screen_response = (
        client.post(
            "/ui/screens",
            json={
                "name": (
                    "hierarchy-screen"
                ),
                "title": (
                    "Hierarchy Screen"
                ),
                "route": (
                    "/hierarchy-test"
                ),
                "screen_type": (
                    "standard"
                ),
            },
        )
    )

    assert (
        screen_response
        .status_code
        == 200
    )

    screen_id = (
        screen_response
        .json()["id"]
    )

    response = client.get(
        (
            "/ui/studio/"
            f"hierarchy/{screen_id}"
        )
    )

    assert response.status_code == 200

    data = response.json()

    assert data[
        "screen_id"
    ] == screen_id

    assert "roots" in data
    assert "nodes" in data


def test_unknown_screen_returns_404():
    response = client.get(
        (
            "/ui/screens/"
            "screen-that-does-not-exist"
        )
    )

    assert response.status_code == 404
