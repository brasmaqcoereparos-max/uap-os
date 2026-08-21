"""
Processador de eventos do simulador UAP.
"""


class EventProcessor:

    def __init__(self):

        self.processed = 0

    def process(
        self,
        event,
    ):

        if event is None:
            return False

        self.processed += 1

        handler = getattr(
            event,
            "handle",
            None,
        )

        if callable(handler):
            handler()

        return True

    def reset(self):

        self.processed = 0
