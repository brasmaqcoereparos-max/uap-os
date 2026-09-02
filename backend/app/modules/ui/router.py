from typing import Any

from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import Field

from app.modules.ui.enums import (
    ActionType,
    ScreenType,
    WidgetType,
)
from app.modules.ui.health import (
    ui_health,
)
from app.modules.ui.runtime_bridge import (
    ui_runtime_bridge,
)
from app.modules.ui.service import (
    UIService,
)


router = APIRouter(
    prefix="/ui",
    tags=["UI"],
)


class ScreenCreateRequest(
    BaseModel
):
    name: str
    title: str = ""
    route: str = "/"

    screen_type: (
        ScreenType
    ) = ScreenType.STANDARD


class WidgetCreateRequest(
    BaseModel
):
    name: str
    widget_type: WidgetType

    properties: (
        dict[str, Any] | None
    ) = None


class WidgetActionRequest(
    BaseModel
):
    action_type: ActionType

    action: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class ThemeCreateRequest(
    BaseModel
):
    name: str
    mode: str = "light"


class StateUpdateRequest(
    BaseModel
):
    value: Any


class StateBatchRequest(
    BaseModel
):
    values: dict[
        str,
        Any,
    ]


@router.get("/health")
def ui_health_check():
    return ui_health.check()


@router.get("/snapshot")
def ui_snapshot():
    return (
        ui_runtime_bridge
        .snapshot()
    )


@router.get("/screens")
def list_screens():
    return [
        screen.to_dict()
        for screen
        in UIService.list_screens()
    ]


@router.post("/screens")
def create_screen(
    data: ScreenCreateRequest,
):
    screen = (
        UIService.create_screen(
            name=data.name,
            title=data.title,
            route=data.route,
            screen_type=(
                data.screen_type
            ),
        )
    )

    return screen.to_dict()


@router.get(
    "/screens/{screen_id}"
)
def get_screen(
    screen_id: str,
):
    screen = (
        UIService.get_screen(
            screen_id
        )
    )

    if not screen:
        raise HTTPException(
            status_code=404,
            detail="Screen not found",
        )

    return screen.to_dict()


@router.delete(
    "/screens/{screen_id}"
)
def delete_screen(
    screen_id: str,
):
    deleted = (
        UIService.delete_screen(
            screen_id
        )
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Screen not found",
        )

    return {
        "deleted": True,
        "screen_id": screen_id,
    }


@router.post(
    "/screens/{screen_id}/widgets"
)
def add_widget(
    screen_id: str,
    data: WidgetCreateRequest,
):
    try:
        widget = (
            UIService.add_widget(
                screen_id=screen_id,
                name=data.name,
                widget_type=(
                    data.widget_type
                ),
                properties=(
                    data.properties
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return widget.to_dict()


@router.delete(
    "/screens/{screen_id}"
    "/widgets/{widget_id}"
)
def remove_widget(
    screen_id: str,
    widget_id: str,
):
    deleted = (
        UIService.remove_widget(
            screen_id,
            widget_id,
        )
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    return {
        "deleted": True,
        "widget_id": widget_id,
    }


@router.put(
    "/screens/{screen_id}"
    "/widgets/{widget_id}/action"
)
def configure_widget_action(
    screen_id: str,
    widget_id: str,
    data: WidgetActionRequest,
):
    try:
        widget = (
            UIService.configure_action(
                screen_id=screen_id,
                widget_id=widget_id,
                action_type=(
                    data.action_type
                ),
                action=data.action,
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return widget.to_dict()


@router.get("/themes")
def list_themes():
    return [
        theme.to_dict()
        for theme
        in UIService.list_themes()
    ]


@router.post("/themes")
def create_theme(
    data: ThemeCreateRequest,
):
    theme = (
        UIService.create_theme(
            name=data.name,
            mode=data.mode,
        )
    )

    return theme.to_dict()


@router.put("/state/{key}")
def update_state(
    key: str,
    data: StateUpdateRequest,
):
    value = (
        ui_runtime_bridge
        .update_state(
            key,
            data.value,
        )
    )

    return {
        "key": key,
        "value": value,
    }


@router.put("/state")
def update_state_batch(
    data: StateBatchRequest,
):
    state = (
        ui_runtime_bridge
        .update_many(
            data.values
        )
    )

    return {
        "state": state
    }
