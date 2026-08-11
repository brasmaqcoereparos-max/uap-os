class WorkFrame:

    def __init__(
        self,
        name="Work Area",
    ):

        self.name = name

        self.origin = {
            "x": 0,
            "y": 0,
            "z": 0,
        }

    def set_origin(
        self,
        x,
        y,
        z,
    ):

        self.origin = {
            "x": x,
            "y": y,
            "z": z,
        }

    def get_origin(self):

        return dict(
            self.origin
        )
