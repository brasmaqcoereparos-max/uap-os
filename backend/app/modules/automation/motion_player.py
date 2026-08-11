class MotionPlayer:

    def __init__(self):

        self.playing = False
        self.current_index = 0

    def start(self):

        self.playing = True
        self.current_index = 0

    def stop(self):

        self.playing = False

    def next_position(
        self,
        positions,
    ):

        if not self.playing:
            return None

        if self.current_index >= len(positions):

            self.playing = False

            return None

        position = positions[
            self.current_index
        ]

        self.current_index += 1

        return position

    def is_playing(self):

        return self.playing
