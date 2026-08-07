import time


class MotionRecorder:

    def __init__(self):

        self.recording = False

        self.buffer = []

        self.start_time = None

    def start(self):

        self.recording = True

        self.buffer.clear()

        self.start_time = time.time()

    def stop(self):

        self.recording = False

    def add(

        self,

        position,

    ):

        if not self.recording:

            return

        self.buffer.append(

            {

                "time": time.time() - self.start_time,

                "position": position.copy(),

            }

        )

    def clear(self):

        self.buffer.clear()

    def positions(self):

        return list(self.buffer)


motion_recorder = MotionRecorder()
