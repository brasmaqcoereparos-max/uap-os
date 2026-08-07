class MotionRecorder:

    def __init__(self):

        self.recording = False

        self.buffer = []

    def start(self):

        self.recording = True

        self.buffer.clear()

    def stop(self):

        self.recording = False

    def add(

        self,

        position,

    ):

        if self.recording:

            self.buffer.append(position.copy())

    def clear(self):

        self.buffer.clear()

    def positions(self):

        return list(self.buffer)


motion_recorder = MotionRecorder()
