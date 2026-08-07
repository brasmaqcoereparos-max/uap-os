class MotionDriverBase:

    def __init__(self):

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def enable(self):

        pass

    def disable(self):

        pass

    def move(self, target):

        raise NotImplementedError

    def stop(self):

        raise NotImplementedError
