from app.modules.simulator.programming.simulator.hardware_engine.event_queue import (
    event_queue,
)


class EventProcessor:

    def process(self):

        while True:

            event = event_queue.pop()

            if event is None:

                break


event_processor = EventProcessor()
