from app.modules.ui.layout import (
    UILayout,
)


class UILayerManager:

    @staticmethod
    def bring_to_front(
        layout: UILayout,
        widget_id: str,
    ):
        widget = layout.get_widget(
            widget_id
        )

        if not widget:
            return False

        layout.widgets.remove(widget)
        layout.widgets.append(widget)

        return True

    @staticmethod
    def send_to_back(
        layout: UILayout,
        widget_id: str,
    ):
        widget = layout.get_widget(
            widget_id
        )

        if not widget:
            return False

        layout.widgets.remove(widget)
        layout.widgets.insert(
            0,
            widget,
        )

        return True

    @staticmethod
    def move_forward(
        layout: UILayout,
        widget_id: str,
    ):
        widget = layout.get_widget(
            widget_id
        )

        if not widget:
            return False

        index = layout.widgets.index(
            widget
        )

        if index >= (
            len(layout.widgets) - 1
        ):
            return True

        layout.widgets[index], (
            layout.widgets[index + 1]
        ) = (
            layout.widgets[index + 1],
            layout.widgets[index],
        )

        return True

    @staticmethod
    def move_backward(
        layout: UILayout,
        widget_id: str,
    ):
        widget = layout.get_widget(
            widget_id
        )

        if not widget:
            return False

        index = layout.widgets.index(
            widget
        )

        if index <= 0:
            return True

        layout.widgets[index], (
            layout.widgets[index - 1]
        ) = (
            layout.widgets[index - 1],
            layout.widgets[index],
        )

        return True
