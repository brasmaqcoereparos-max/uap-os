class TeachRecordService:

    def __init__(self):

        self.recording = False
        self.recorded = []

    def start(self):

        self.recording = True
        self.recorded.clear()

    def record(self, pose):

        if not self.recording:
            return False

        self.recorded.append(pose)

        return True

    def stop(self):

        self.recording = False

    def get(self):

        return list(self.recorded)

    def clear(self):

        self.recorded.clear()
