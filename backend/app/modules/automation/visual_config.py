class VisualConfig:

    def __init__(self):

        self.label = ""
        self.icon = ""
        self.category = ""
        self.color = ""
        self.position = {
            "x": 0,
            "y": 0,
        }

    def set_position(
        self,
        x,
        y,
    ):

        self.position = {
            "x": x,
            "y": y,
        }

    def set_label(
        self,
        label,
    ):

        self.label = label
