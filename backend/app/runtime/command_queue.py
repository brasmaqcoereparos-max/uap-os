from queue import Queue, Empty


class CommandQueue:

    def __init__(self):
        self.queue = Queue()

    def put(
        self,
        command: dict,
    ):
        self.queue.put(command)

    def get(self):
        try:
            return self.queue.get_nowait()
        except Empty:
            return None

    def size(self):
        return self.queue.qsize()

    def clear(self):
        while not self.queue.empty():
            self.queue.get()


command_queue = CommandQueue()
