class MotionRecorder:

    def __init__(self):

        self.recording = False
        self.positions = []

    def start(self):

        self.positions.clear()
        self.recording = True

    def record(
        self,
        pose,
    ):

        if not self.recording:
            return False

        self.positions.append(pose)

        return True

    def stop(self):

        self.recording = False

    def get_recording(self):

        return list(self.positions)

    def clear(self):

        self.positions.clear()
