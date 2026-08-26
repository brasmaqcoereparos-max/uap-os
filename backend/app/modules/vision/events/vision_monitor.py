from app.modules.vision.events.event_buffer import (
    event_buffer,
)

from app.modules.vision.events.event_detector import (
    event_detector,
)

from app.modules.vision.events.event_dispatcher import (
    event_dispatcher,
)


class VisionMonitor:

    def process(
        self,
        camera_id,
        analysis,
    ):

        events = event_detector.detect(
            camera_id,
            analysis,
        )

        for event in events:

            event_buffer.add(
                event
            )

            event_dispatcher.dispatch(
                event
            )

        return events

    def latest(self):

        event = event_buffer.latest()

        if event is None:
            return None

        return event.to_dict()

    def events(self):

        return [
            event.to_dict()
            for event in event_buffer.list()
        ]

    def count(self):

        return event_buffer.count()


vision_monitor = VisionMonitor()
