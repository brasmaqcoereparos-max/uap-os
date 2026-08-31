from app.modules.ui.screen import (
    UIScreen,
)


class UIValidator:

    def validate_screen(
        self,
        screen: UIScreen,
    ):
        errors: list[str] = []

        if not screen.id:
            errors.append(
                "Screen id is required"
            )

        if not screen.name:
            errors.append(
                "Screen name is required"
            )

        if not screen.route:
            errors.append(
                "Screen route is required"
            )

        if not screen.layout:
            errors.append(
                "Screen layout is required"
            )

            return errors

        widget_ids: set[str] = set()

        for widget in (
            screen.layout.widgets
        ):
            if not widget.id:
                errors.append(
                    "Widget id is required"
                )

                continue

            if widget.id in widget_ids:
                errors.append(
                    "Duplicate widget id: "
                    f"{widget.id}"
                )

            widget_ids.add(widget.id)

            if widget.width < 0:
                errors.append(
                    f"Invalid width: "
                    f"{widget.id}"
                )

            if widget.height < 0:
                errors.append(
                    f"Invalid height: "
                    f"{widget.id}"
                )

        return errors

    def is_valid(
        self,
        screen: UIScreen,
    ):
        return not self.validate_screen(
            screen
        )


ui_validator = UIValidator()
