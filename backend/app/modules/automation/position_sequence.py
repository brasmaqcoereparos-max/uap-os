class PositionSequence:

    def __init__(self, name="Sequence"):

        self.name = name
        self.positions = []

    def add_position(
        self,
        position,
        speed=0,
        wait=0,
    ):

        self.positions.append(
            {
                "position": position,
                "speed": speed,
                "wait": wait,
            }
        )

    def remove_position(
        self,
        index,
    ):

        if 0 <= index < len(self.positions):
            self.positions.pop(index)

    def clear(self):

        self.positions.clear()

    def get_positions(self):

        return list(self.positions)
