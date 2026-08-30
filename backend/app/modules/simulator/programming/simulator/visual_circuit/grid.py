"""
Grade visual e sistema de snap do circuito UAP.
"""


class Grid:

    def __init__(
        self,
        spacing=20,
        enabled=True,
    ):
        self.enabled = bool(
            enabled
        )

        self.spacing = 20

        self.set_spacing(
            spacing
        )

        self.origin_x = 0.0
        self.origin_y = 0.0

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return False

    def toggle(self):
        self.enabled = (
            not self.enabled
        )

        return self.enabled

    def set_spacing(
        self,
        spacing,
    ):
        spacing = float(
            spacing
        )

        if spacing <= 0:
            raise ValueError(
                "O espaçamento da grade "
                "deve ser maior que zero."
            )

        self.spacing = spacing

        return self.spacing

    def set_origin(
        self,
        x,
        y,
    ):
        self.origin_x = float(x)
        self.origin_y = float(y)

        return (
            self.origin_x,
            self.origin_y,
        )

    def snap(
        self,
        value,
    ):
        value = float(value)

        if not self.enabled:
            return value

        return (
            round(
                value
                / self.spacing
            )
            * self.spacing
        )

    def snap_x(
        self,
        value,
    ):
        value = float(value)

        if not self.enabled:
            return value

        relative = (
            value
            - self.origin_x
        )

        return (
            round(
                relative
                / self.spacing
            )
            * self.spacing
            + self.origin_x
        )

    def snap_y(
        self,
        value,
    ):
        value = float(value)

        if not self.enabled:
            return value

        relative = (
            value
            - self.origin_y
        )

        return (
            round(
                relative
                / self.spacing
            )
            * self.spacing
            + self.origin_y
        )

    def snap_point(
        self,
        x,
        y,
    ):
        return (
            self.snap_x(x),
            self.snap_y(y),
        )

    def snap_component(
        self,
        component,
    ):
        if component is None:
            return None

        x = getattr(
            component,
            "x",
            0,
        )

        y = getattr(
            component,
            "y",
            0,
        )

        x, y = self.snap_point(
            x,
            y,
        )

        mover = getattr(
            component,
            "move_to",
            None,
        )

        if callable(mover):
            mover(
                x,
                y,
            )
        else:
            component.x = x
            component.y = y

        return component

    def to_dict(self):
        return {
            "enabled": (
                self.enabled
            ),
            "spacing": (
                self.spacing
            ),
            "origin_x": (
                self.origin_x
            ),
            "origin_y": (
                self.origin_y
            ),
        }


grid = Grid()
