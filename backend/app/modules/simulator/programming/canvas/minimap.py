class MiniMap:

    def __init__(self):

        self.enabled = True

        self.width = 240

        self.height = 160

        self.scale = 0.10

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def to_dict(self):

        return {
            "enabled": self.enabled,
            "width": self.width,
            "height": self.height,
            "scale": self.scale,
        }


minimap = MiniMap()
