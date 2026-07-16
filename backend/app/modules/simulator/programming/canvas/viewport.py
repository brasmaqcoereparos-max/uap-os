class Viewport:

    def __init__(self):

        self.width = 1920

        self.height = 1080

    def resize(
        self,
        width,
        height,
    ):

        self.width = width

        self.height = height

    def center(self):

        return {
            "x": self.width / 2,
            "y": self.height / 2,
        }

    def to_dict(self):

        return {
            "width": self.width,
            "height": self.height,
            "center": self.center(),
        }


viewport = Viewport()
