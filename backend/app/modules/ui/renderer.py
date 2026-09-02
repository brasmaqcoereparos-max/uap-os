from app.modules.ui.render_node import (
    UIRenderNode,
)
from app.modules.ui.render_tree import (
    UIRenderTree,
)
from app.modules.ui.screen import (
    UIScreen,
)


class UIRenderer:

    @staticmethod
    def widget_node(widget):
        return UIRenderNode(
            id=widget.id,
            node_type=(
                widget.widget_type.value
            ),
            properties={
                "name": widget.name,
                "x": widget.x,
                "y": widget.y,
                "width": widget.width,
                "height": widget.height,
                "visible": (
                    widget.visible
                ),
                "enabled": (
                    widget.enabled
                ),
                "value": widget.value,
                "properties": dict(
                    widget.properties
                ),
            },
            style=dict(
                widget.style
            ),
        )

    @classmethod
    def render_screen(
        cls,
        screen: UIScreen,
        width: float = 1280,
        height: float = 720,
    ):
        root = UIRenderNode(
            id=f"{screen.id}:root",
            node_type="screen",
            properties={
                "name": screen.name,
                "title": screen.title,
                "route": screen.route,
            },
        )

        if screen.layout:
            for widget in (
                screen.layout.widgets
            ):
                if not widget.visible:
                    continue

                root.add_child(
                    cls.widget_node(
                        widget
                    )
                )

        return UIRenderTree(
            screen_id=screen.id,
            width=width,
            height=height,
            root=root,
        )


ui_renderer = UIRenderer()
