class CanvasGrid:

    def __init__(self):

        self.enabled = True

        self.visible = True

        self.size = 20

        self.snap = True

    def to_dict(self):

        return {
            "enabled": self.enabled,
            "visible": self.visible,
            "size": self.size,
            "snap": self.snap,
        }

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def show(self):

        self.visible = True

    def hide(self):

        self.visible = False

    def set_size(self, size):

        if size < 5:
            size = 5

        self.size = size

    def enable_snap(self):

        self.snap = True

    def disable_snap(self):

        self.snap = False


grid = CanvasGrid()
