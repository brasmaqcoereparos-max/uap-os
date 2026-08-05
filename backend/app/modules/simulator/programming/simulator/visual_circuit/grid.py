class Grid:

    def __init__(self):

        self.enabled = True

        self.spacing = 20

    def snap(

        self,

        value,

    ):

        if not self.enabled:

            return value

        return round(value / self.spacing) * self.spacing


grid = Grid()
