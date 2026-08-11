class RobotPlayback:

    def __init__(self):

        self.running = False
        self.index = 0

    def start(self):

        self.running = True
        self.index = 0

    def stop(self):

        self.running = False

    def next(
        self,
        segments,
    ):

        if not self.running:
            return None

        if self.index >= len(segments):

            self.running = False

            return None

        segment = segments[
            self.index
        ]

        self.index += 1

        return segment

    def is_running(self):

        return self.running
