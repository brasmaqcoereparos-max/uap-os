class RobotProgram:

    def __init__(
        self,
        name="Robot Program",
    ):

        self.name = name
        self.segments = []
        self.repeat = 1

    def add_segment(
        self,
        segment,
    ):

        self.segments.append(segment)

    def remove_segment(
        self,
        index,
    ):

        if 0 <= index < len(self.segments):

            self.segments.pop(index)

    def set_repeat(
        self,
        repeat,
    ):

        self.repeat = max(
            1,
            repeat,
        )

    def get_segments(self):

        return list(
            self.segments
        )
