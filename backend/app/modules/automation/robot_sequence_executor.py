class RobotSequenceExecutor:

    def __init__(self):

        self.sequence = []
        self.index = 0
        self.running = False

    def load(self, poses):

        self.sequence = list(poses)
        self.index = 0

    def start(self):

        if not self.sequence:
            return False

        self.index = 0
        self.running = True

        return True

    def next(self):

        if not self.running:
            return None

        if self.index >= len(self.sequence):

            self.running = False

            return None

        pose = self.sequence[self.index]

        self.index += 1

        return pose

    def stop(self):

        self.running = False

    def get_index(self):

        return self.index

    def is_running(self):

        return self.running
