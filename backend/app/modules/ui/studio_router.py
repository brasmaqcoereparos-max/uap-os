from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.ui.drop_payload import (
    UIDropPayload,
)
from app.modules.ui.palette_service import (
    ui_palette_service,
)
from app.modules.ui.property_inspector import (
    ui_property_inspector,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.studio_api_models import (
    UIStudioDropRequest,
    UIStudioPaletteSearchRequest,
    UIStudioPreviewRequest,
    UIStudioPropertyUpdateRequest,
    UIStudioSelectRequest,
    UIStudioWidgetSelectRequest,
)
from app.modules.ui.studio_facade import (
    ui_studio_facade,
)


router = APIRouter(
    prefix="/ui/studio",
    tags=["UI Studio"],
)


@router.post("/initialize")
def initialize_studio():
    return (
        ui_studio_facade.initialize()
    )


@router.get("/snapshot")
def studio_snapshot():
    return (
        ui_studio_facade.snapshot()
    )


@router.post("/select/screen")
def select_screen(
    data: UIStudioSelectRequest,
):
    try:
        screen = (
            ui_studio_facade
            .select_screen(
                data.screen_id
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return screen.to_dict()


@router.post("/select/widget")
def select_widget(
    data: (
        UIStudioWidgetSelectRequest
    ),
):
    try:
        return (
            ui_studio_facade
            .select_widget(
                data.screen_id,
                data.widget_id,
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.get(
    "/hierarchy/{screen_id}"
)
def hierarchy(
    screen_id: str,
):
    try:
        return (
            ui_studio_facade
            .hierarchy(
                screen_id
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.get("/palette")
def palette(
    category: str | None = None,
):
    return (
        ui_studio_facade
        .palette(category)
    )


@router.post("/palette/search")
def search_palette(
    data: (
        UIStudioPaletteSearchRequest
    ),
):
    return (
        ui_palette_service
        .search(
            data.query
        )
    )


@router.post("/drop")
def drop_widget(
    data: UIStudioDropRequest,
):
    try:
        widget = (
            ui_palette_service.drop(
                UIDropPayload(
                    palette_item_id=(
                        data
                        .palette_item_id
                    ),
                    x=data.x,
                    y=data.y,
                    screen_id=(
                        data.screen_id
                    ),
                    properties=(
                        data.properties
                    ),
                )
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return widget.to_dict()


@router.put("/properties")
def update_properties(
    data: (
        UIStudioPropertyUpdateRequest
    ),
):
    screen = (
        ui_registry.get_screen(
            data.screen_id
        )
    )

    if (
        not screen
        or not screen.layout
    ):
        raise HTTPException(
            status_code=404,
            detail="Screen not found",
        )

    widget = (
        screen.layout.get_widget(
            data.widget_id
        )
    )

    if not widget:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    ui_property_inspector.update_widget(
        widget,
        data.values,
    )

    return widget.to_dict()


@router.post("/preview")
def preview(
    data: UIStudioPreviewRequest,
):
    try:
        result = (
            ui_studio_facade
            .preview(
                screen_id=(
                    data.screen_id
                ),
                profile_id=(
                    data.profile_id
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return result.to_dict()
