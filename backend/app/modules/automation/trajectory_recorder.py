class TrajectoryRecorder:

    def __init__(self):

        self.recording = False
        self.points = []

    def start(self):

        self.points.clear()
        self.recording = True

    def record(self, point):

        if not self.recording:
            return False

        self.points.append(point)

        return True

    def stop(self):

        self.recording = False

    def clear(self):

        self.points.clear()

    def get_points(self):

        return list(self.points)

    def is_recording(self):

        return self.recording
