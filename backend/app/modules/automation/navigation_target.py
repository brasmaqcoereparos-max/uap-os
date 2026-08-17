class NavigationTarget:

    def __init__(
        self,
        x=0,
        y=0,
        tolerance=0.1,
    ):

        self.x = x
        self.y = y
        self.tolerance = tolerance

    def set(
        self,
        x,
        y,
        tolerance=None,
    ):

        self.x = x
        self.y = y

        if tolerance is not None:

            self.tolerance = tolerance

    def get(self):

        return {
            "x": self.x,
            "y": self.y,
            "tolerance": self.tolerance,
        }

    def reached(
        self,
        x,
        y,
    ):

        distance_x = abs(
            self.x - x
        )

        distance_y = abs(
            self.y - y
        )

        return (
            distance_x <= self.tolerance
            and
            distance_y <= self.tolerance
        )
