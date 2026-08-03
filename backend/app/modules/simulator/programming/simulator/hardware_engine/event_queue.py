class EventQueue:

    def __init__(self):

        self.queue = []

    def push(

        self,

        event,

    ):

        self.queue.append(event)

    def pop(self):

        if self.queue:

            return self.queue.pop(0)

        return None

    def clear(self):

        self.queue.clear()


event_queue = EventQueue()
