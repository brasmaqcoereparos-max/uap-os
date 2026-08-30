"""
Canvas do Visual Circuit Engine do UAP.
"""


class Canvas:

    MIN_ZOOM = 0.1
    MAX_ZOOM = 5.0

    def __init__(
        self,
        width=10000,
        height=10000,
    ):
        self.width = float(
            width
        )

        self.height = float(
            height
        )

        self.zoom = 1.0

        self.offset_x = 0.0
        self.offset_y = 0.0

        self.grid_enabled = True
        self.grid_size = 20

    def set_size(
        self,
        width,
        height,
    ):
        width = float(width)
        height = float(height)

        if (
            width <= 0
            or height <= 0
        ):
            raise ValueError(
                "Dimensões do canvas "
                "devem ser positivas."
            )

        self.width = width
        self.height = height

        return (
            self.width,
            self.height,
        )

    def set_zoom(
        self,
        zoom,
    ):
        zoom = float(zoom)

        self.zoom = max(
            self.MIN_ZOOM,
            min(
                self.MAX_ZOOM,
                zoom,
            ),
        )

        return self.zoom

    def zoom_in(
        self,
        step=0.1,
    ):
        return self.set_zoom(
            self.zoom
            + float(step)
        )

    def zoom_out(
        self,
        step=0.1,
    ):
        return self.set_zoom(
            self.zoom
            - float(step)
        )

    def reset_zoom(self):
        self.zoom = 1.0
        return self.zoom

    def move(
        self,
        dx,
        dy,
    ):
        self.offset_x += float(
            dx
        )

        self.offset_y += float(
            dy
        )

        return (
            self.offset_x,
            self.offset_y,
        )

    def set_offset(
        self,
        x,
        y,
    ):
        self.offset_x = float(x)
        self.offset_y = float(y)

        return (
            self.offset_x,
            self.offset_y,
        )

    def reset_view(self):
        self.zoom = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0

        return True

    def enable_grid(self):
        self.grid_enabled = True

    def disable_grid(self):
        self.grid_enabled = False

    def set_grid_size(
        self,
        size,
    ):
        size = int(size)

        if size <= 0:
            raise ValueError(
                "Grid deve ser maior "
                "que zero."
            )

        self.grid_size = size

        return self.grid_size

    def screen_to_world(
        self,
        x,
        y,
    ):
        return (
            (
                float(x)
                - self.offset_x
            )
            / self.zoom,
            (
                float(y)
                - self.offset_y
            )
            / self.zoom,
        )

    def world_to_screen(
        self,
        x,
        y,
    ):
        return (
            (
                float(x)
                * self.zoom
            )
            + self.offset_x,
            (
                float(y)
                * self.zoom
            )
            + self.offset_y,
        )

    def contains(
        self,
        x,
        y,
    ):
        return (
            0
            <= float(x)
            <= self.width
            and 0
            <= float(y)
            <= self.height
        )

    def to_dict(self):
        return {
            "width": self.width,
            "height": self.height,
            "zoom": self.zoom,
            "offset_x": (
                self.offset_x
            ),
            "offset_y": (
                self.offset_y
            ),
            "grid_enabled": (
                self.grid_enabled
            ),
            "grid_size": (
                self.grid_size
            ),
        }


canvas = Canvas()
