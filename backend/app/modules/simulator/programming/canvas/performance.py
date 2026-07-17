from datetime import datetime


class CanvasPerformance:

    def __init__(self):

        self.started = datetime.now()

        self.frames = 0

        self.operations = 0

    def frame(self):

        self.frames += 1

    def operation(self):

        self.operations += 1

    def reset(self):

        self.started = datetime.now()

        self.frames = 0

        self.operations = 0

    def to_dict(self):

        return {

            "started": self.started.isoformat(),

            "frames": self.frames,

            "operations": self.operations,

        }


performance = CanvasPerformance()
