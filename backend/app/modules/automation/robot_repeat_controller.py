class RobotRepeatController:

    def __init__(self):

        self.total = 1
        self.current = 0

    def set_repeat(self, repeat):

        self.total = max(1, repeat)
        self.current = 0

    def start(self):

        self.current = 0

    def next_cycle(self):

        if self.current >= self.total:
            return False

        self.current += 1

        return True

    def finished(self):

        return self.current >= self.total

    def get_current(self):

        return self.current

    def get_total(self):

        return self.total
