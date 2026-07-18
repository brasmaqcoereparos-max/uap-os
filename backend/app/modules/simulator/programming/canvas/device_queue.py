from collections import deque


class DeviceQueue:

    def __init__(self):

        self.queue = deque()

    def push(
        self,
        device,
        command,
        *args,
        **kwargs,
    ):

        self.queue.append(

            {

                "device": device,

                "command": command,

                "args": args,

                "kwargs": kwargs,

            }

        )

    def pop(self):

        if not self.queue:

            return None

        return self.queue.popleft()

    def clear(self):

        self.queue.clear()

    def size(self):

        return len(self.queue)

    def empty(self):

        return len(self.queue) == 0


device_queue = DeviceQueue()
