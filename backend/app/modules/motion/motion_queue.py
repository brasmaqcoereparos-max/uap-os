class MotionQueue:

    def __init__(self):

        self.queue = []

    def add(

        self,

        sequence,

    ):

        self.queue.append(sequence)

    def next(self):

        if self.queue:

            return self.queue.pop(0)

        return None

    def clear(self):

        self.queue.clear()

    def size(self):

        return len(self.queue)


motion_queue = MotionQueue()
