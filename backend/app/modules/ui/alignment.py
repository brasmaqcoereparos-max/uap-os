from app.modules.ui.widget import (
    UIWidget,
)


class UIAlignment:

    @staticmethod
    def left(
        widgets: list[UIWidget],
    ):
        if not widgets:
            return []

        target = min(
            widget.x
            for widget in widgets
        )

        for widget in widgets:
            widget.x = target

        return widgets

    @staticmethod
    def right(
        widgets: list[UIWidget],
    ):
        if not widgets:
            return []

        target = max(
            widget.x + widget.width
            for widget in widgets
        )

        for widget in widgets:
            widget.x = (
                target - widget.width
            )

        return widgets

    @staticmethod
    def top(
        widgets: list[UIWidget],
    ):
        if not widgets:
            return []

        target = min(
            widget.y
            for widget in widgets
        )

        for widget in widgets:
            widget.y = target

        return widgets

    @staticmethod
    def bottom(
        widgets: list[UIWidget],
    ):
        if not widgets:
            return []

        target = max(
            widget.y + widget.height
            for widget in widgets
        )

        for widget in widgets:
            widget.y = (
                target - widget.height
            )

        return widgets

    @staticmethod
    def center_horizontal(
        widgets: list[UIWidget],
    ):
        if not widgets:
            return []

        centers = [
            widget.x
            + widget.width / 2
            for widget in widgets
        ]

        target = (
            sum(centers)
            / len(centers)
        )

        for widget in widgets:
            widget.x = (
                target
                - widget.width / 2
            )

        return widgets

    @staticmethod
    def center_vertical(
        widgets: list[UIWidget],
    ):
        if not widgets:
            return []

        centers = [
            widget.y
            + widget.height / 2
            for widget in widgets
        ]

        target = (
            sum(centers)
            / len(centers)
        )

        for widget in widgets:
            widget.y = (
                target
                - widget.height / 2
            )

        return widgets
