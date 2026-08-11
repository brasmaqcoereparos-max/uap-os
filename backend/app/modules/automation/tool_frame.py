class ToolFrame:

    def __init__(
        self,
        name="Tool",
    ):

        self.name = name

        self.offset = {
            "x": 0,
            "y": 0,
            "z": 0,
        }

    def set_offset(
        self,
        x,
        y,
        z,
    ):

        self.offset = {
            "x": x,
            "y": y,
            "z": z,
        }

    def get_offset(self):

        return dict(
            self.offset
        )
