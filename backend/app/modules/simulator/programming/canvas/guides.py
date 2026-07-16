class GuideManager:

    def __init__(self):

        self.vertical = []

        self.horizontal = []

    def add_vertical(
        self,
        x,
    ):

        self.vertical.append(x)

    def add_horizontal(
        self,
        y,
    ):

        self.horizontal.append(y)

    def clear(self):

        self.vertical.clear()
        self.horizontal.clear()

    def to_dict(self):

        return {
            "vertical": self.vertical,
            "horizontal": self.horizontal,
        }


guides = GuideManager()
