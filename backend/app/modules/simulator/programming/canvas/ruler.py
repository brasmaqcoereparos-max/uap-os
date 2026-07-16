class CanvasRuler:

    def __init__(self):

        self.enabled = True

        self.unit = "px"

        self.origin_x = 0

        self.origin_y = 0

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def set_origin(self, x, y):

        self.origin_x = x
        self.origin_y = y

    def move_origin(self, dx, dy):

        self.origin_x += dx
        self.origin_y += dy

    def to_dict(self):

        return {
            "enabled": self.enabled,
            "unit": self.unit,
            "origin_x": self.origin_x,
            "origin_y": self.origin_y,
        }


ruler = CanvasRuler()
