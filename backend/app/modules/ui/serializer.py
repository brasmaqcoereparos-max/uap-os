from __future__ import annotations

import json
from typing import Any

from app.modules.ui.enums import (
    ActionType,
    LayoutType,
    ScreenType,
    WidgetType,
)
from app.modules.ui.layout import (
    UILayout,
)
from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.theme import (
    UITheme,
)
from app.modules.ui.widget import (
    UIWidget,
)


class UISerializer:

    @staticmethod
    def widget_to_dict(
        widget: UIWidget,
    ) -> dict[str, Any]:
        return widget.to_dict()

    @staticmethod
    def widget_from_dict(
        data: dict[str, Any],
    ) -> UIWidget:
        if not isinstance(data, dict):
            raise TypeError(
                "Widget data must be a dict"
            )

        widget_id = str(
            data.get(
                "id",
                "",
            )
        ).strip()

        name = str(
            data.get(
                "name",
                "",
            )
        ).strip()

        if not widget_id:
            raise ValueError(
                "Widget id is required"
            )

        if not name:
            raise ValueError(
                "Widget name is required"
            )

        widget_type = WidgetType(
            data.get(
                "widget_type",
                WidgetType.CUSTOM.value,
            )
        )

        action_type = ActionType(
            data.get(
                "action_type",
                ActionType.NONE.value,
            )
        )

        return UIWidget(
            id=widget_id,
            name=name,
            widget_type=widget_type,
            x=float(
                data.get(
                    "x",
                    0,
                )
            ),
            y=float(
                data.get(
                    "y",
                    0,
                )
            ),
            width=max(
                1.0,
                float(
                    data.get(
                        "width",
                        100,
                    )
                ),
            ),
            height=max(
                1.0,
                float(
                    data.get(
                        "height",
                        40,
                    )
                ),
            ),
            visible=bool(
                data.get(
                    "visible",
                    True,
                )
            ),
            enabled=bool(
                data.get(
                    "enabled",
                    True,
                )
            ),
            value=data.get(
                "value"
            ),
            properties=dict(
                data.get(
                    "properties",
                    {},
                )
                or {}
            ),
            style=dict(
                data.get(
                    "style",
                    {},
                )
                or {}
            ),
            action_type=action_type,
            action=dict(
                data.get(
                    "action",
                    {},
                )
                or {}
            ),
        )

    @staticmethod
    def layout_to_dict(
        layout: UILayout,
    ) -> dict[str, Any]:
        return layout.to_dict()

    @staticmethod
    def layout_from_dict(
        data: dict[str, Any],
    ) -> UILayout:
        if not isinstance(data, dict):
            raise TypeError(
                "Layout data must be a dict"
            )

        layout = UILayout(
            id=str(
                data.get(
                    "id",
                    "",
                )
            ),
            name=str(
                data.get(
                    "name",
                    "Layout",
                )
            ),
            layout_type=LayoutType(
                data.get(
                    "layout_type",
                    LayoutType.FREE.value,
                )
            ),
            width=float(
                data.get(
                    "width",
                    1280,
                )
            ),
            height=float(
                data.get(
                    "height",
                    720,
                )
            ),
            gap=float(
                data.get(
                    "gap",
                    0,
                )
            ),
            padding=float(
                data.get(
                    "padding",
                    0,
                )
            ),
            properties=dict(
                data.get(
                    "properties",
                    {},
                )
                or {}
            ),
        )

        for widget_data in (
            data.get(
                "widgets",
                [],
            )
            or []
        ):
            layout.add_widget(
                UISerializer
                .widget_from_dict(
                    widget_data
                )
            )

        return layout

    @staticmethod
    def screen_to_dict(
        screen: UIScreen,
    ) -> dict[str, Any]:
        return screen.to_dict()

    @staticmethod
    def screen_from_dict(
        data: dict[str, Any],
    ) -> UIScreen:
        if not isinstance(data, dict):
            raise TypeError(
                "Screen data must be a dict"
            )

        screen_id = str(
            data.get(
                "id",
                "",
            )
        ).strip()

        name = str(
            data.get(
                "name",
                "",
            )
        ).strip()

        if not screen_id:
            raise ValueError(
                "Screen id is required"
            )

        if not name:
            raise ValueError(
                "Screen name is required"
            )

        layout_data = data.get(
            "layout"
        )

        layout = (
            UISerializer
            .layout_from_dict(
                layout_data
            )
            if isinstance(
                layout_data,
                dict,
            )
            else None
        )

        return UIScreen(
            id=screen_id,
            name=name,
            title=str(
                data.get(
                    "title",
                    "",
                )
            ),
            screen_type=ScreenType(
                data.get(
                    "screen_type",
                    ScreenType.STANDARD.value,
                )
            ),
            route=str(
                data.get(
                    "route",
                    "/",
                )
            ),
            layout=layout,
            visible=bool(
                data.get(
                    "visible",
                    True,
                )
            ),
            enabled=bool(
                data.get(
                    "enabled",
                    True,
                )
            ),
            requires_auth=bool(
                data.get(
                    "requires_auth",
                    False,
                )
            ),
            metadata=dict(
                data.get(
                    "metadata",
                    {},
                )
                or {}
            ),
            properties=dict(
                data.get(
                    "properties",
                    {},
                )
                or {}
            ),
        )

    @staticmethod
    def screen_to_json(
        screen: UIScreen,
    ) -> str:
        return json.dumps(
            UISerializer
            .screen_to_dict(
                screen
            ),
            ensure_ascii=False,
            indent=2,
        )

    @staticmethod
    def screen_from_json(
        payload: str,
    ) -> UIScreen:
        data = json.loads(
            payload
        )

        return UISerializer.screen_from_dict(
            data
        )

    @staticmethod
    def theme_to_dict(
        theme: UITheme,
    ) -> dict[str, Any]:
        return theme.to_dict()

    @staticmethod
    def theme_from_dict(
        data: dict[str, Any],
    ) -> UITheme:
        if not isinstance(data, dict):
            raise TypeError(
                "Theme data must be a dict"
            )

        return UITheme(
            id=str(
                data.get(
                    "id",
                    "",
                )
            ),
            name=str(
                data.get(
                    "name",
                    "Theme",
                )
            ),
            mode=str(
                data.get(
                    "mode",
                    "light",
                )
            ),
            primary_color=str(
                data.get(
                    "primary_color",
                    "#2563EB",
                )
            ),
            secondary_color=str(
                data.get(
                    "secondary_color",
                    "#64748B",
                )
            ),
            background_color=str(
                data.get(
                    "background_color",
                    "#FFFFFF",
                )
            ),
            surface_color=str(
                data.get(
                    "surface_color",
                    "#F8FAFC",
                )
            ),
            text_color=str(
                data.get(
                    "text_color",
                    "#0F172A",
                )
            ),
            muted_text_color=str(
                data.get(
                    "muted_text_color",
                    "#64748B",
                )
            ),
            success_color=str(
                data.get(
                    "success_color",
                    "#16A34A",
                )
            ),
            warning_color=str(
                data.get(
                    "warning_color",
                    "#D97706",
                )
            ),
            error_color=str(
                data.get(
                    "error_color",
                    "#DC2626",
                )
            ),
            border_radius=int(
                data.get(
                    "border_radius",
                    8,
                )
            ),
            font_family=str(
                data.get(
                    "font_family",
                    "sans-serif",
                )
            ),
            metadata=dict(
                data.get(
                    "metadata",
                    {},
                )
                or {}
            ),
        )

    @staticmethod
    def theme_to_json(
        theme: UITheme,
    ) -> str:
        return json.dumps(
            UISerializer
            .theme_to_dict(
                theme
            ),
            ensure_ascii=False,
            indent=2,
        )

    @staticmethod
    def theme_from_json(
        payload: str,
    ) -> UITheme:
        return (
            UISerializer
            .theme_from_dict(
                json.loads(
                    payload
                )
            )
        )
