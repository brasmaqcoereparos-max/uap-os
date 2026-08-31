from app.modules.ui.widget import (
    UIWidget,
)


class UIDistribution:

    @staticmethod
    def horizontal(
        widgets: list[UIWidget],
    ):
        if len(widgets) < 3:
            return widgets

        ordered = sorted(
            widgets,
            key=lambda widget: widget.x,
        )

        first = ordered[0]
        last = ordered[-1]

        occupied = sum(
            widget.width
            for widget in ordered
        )

        total_width = (
            last.x
            + last.width
            - first.x
        )

        gap = (
            total_width - occupied
        ) / (
            len(ordered) - 1
        )

        cursor = first.x

        for widget in ordered:
            widget.x = cursor

            cursor += (
                widget.width
                + gap
            )

        return ordered

    @staticmethod
    def vertical(
        widgets: list[UIWidget],
    ):
        if len(widgets) < 3:
            return widgets

        ordered = sorted(
            widgets,
            key=lambda widget: widget.y,
        )

        first = ordered[0]
        last = ordered[-1]

        occupied = sum(
            widget.height
            for widget in ordered
        )

        total_height = (
            last.y
            + last.height
            - first.y
        )

        gap = (
            total_height - occupied
        ) / (
            len(ordered) - 1
        )

        cursor = first.y

        for widget in ordered:
            widget.y = cursor

            cursor += (
                widget.height
                + gap
            )

        return ordered
