class MapCell:

    FREE = "free"
    OCCUPIED = "occupied"
    UNKNOWN = "unknown"

    def __init__(
        self,
        x,
        y,
        state=UNKNOWN,
    ):

        self.x = x
        self.y = y
        self.state = state

    def set_state(self, state):

        self.state = state

    def is_free(self):

        return self.state == self.FREE

    def is_occupied(self):

        return self.state == self.OCCUPIED

    def to_dict(self):

        return {
            "x": self.x,
            "y": self.y,
            "state": self.state,
        }
