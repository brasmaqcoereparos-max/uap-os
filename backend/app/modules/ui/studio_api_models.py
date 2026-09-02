from typing import Any

from pydantic import BaseModel


class UIStudioSelectRequest(
    BaseModel
):
    screen_id: str


class UIStudioWidgetSelectRequest(
    BaseModel
):
    screen_id: str
    widget_id: str


class UIStudioPreviewRequest(
    BaseModel
):
    screen_id: str
    profile_id: str = "desktop"


class UIStudioPaletteSearchRequest(
    BaseModel
):
    query: str


class UIStudioPropertyUpdateRequest(
    BaseModel
):
    screen_id: str
    widget_id: str
    values: dict[
        str,
        Any,
    ]


class UIStudioDropRequest(
    BaseModel
):
    palette_item_id: str

    screen_id: str

    x: float
    y: float

    properties: dict[
        str,
        Any,
    ] = {}
