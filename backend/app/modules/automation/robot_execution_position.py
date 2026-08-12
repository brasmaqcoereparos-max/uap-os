class RobotExecutionPosition:

    def __init__(self):

        self.current = None
        self.target = None

    def set_target(self, pose):

        self.target = pose

    def set_current(self, pose):

        self.current = pose

    def get_target(self):

        return self.target

    def get_current(self):

        return self.current
