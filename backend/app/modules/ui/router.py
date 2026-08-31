from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel

from app.modules.ui.enums import (
    ScreenType,
    WidgetType,
)
from app.modules.ui.service import (
    UIService,
)


router = APIRouter(
    prefix="/ui",
    tags=["UI"],
)


class ScreenCreateRequest(BaseModel):
    name: str
    title: str = ""
    route: str = "/"
    screen_type: ScreenType = (
        ScreenType.STANDARD
    )


class WidgetCreateRequest(BaseModel):
    name: str
    widget_type: WidgetType


class ThemeCreateRequest(BaseModel):
    name: str
    mode: str = "light"


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
    screen = UIService.create_screen(
        name=data.name,
        title=data.title,
        route=data.route,
        screen_type=data.screen_type,
    )

    return screen.to_dict()


@router.get(
    "/screens/{screen_id}"
)
def get_screen(
    screen_id: str,
):
    screen = UIService.get_screen(
        screen_id
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
        widget = UIService.add_widget(
            screen_id=screen_id,
            name=data.name,
            widget_type=(
                data.widget_type
            ),
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
    theme = UIService.create_theme(
        name=data.name,
        mode=data.mode,
    )

    return theme.to_dict()
