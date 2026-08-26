from app.modules.vision.events.event_dispatcher import (
    event_dispatcher,
)

from app.modules.vision.events.vision_monitor import (
    vision_monitor,
)


class VisionEventService:

    def subscribe(
        self,
        event_type,
        listener,
    ):

        return event_dispatcher.subscribe(
            event_type,
            listener,
        )

    def unsubscribe(
        self,
        event_type,
        listener,
    ):

        return event_dispatcher.unsubscribe(
            event_type,
            listener,
        )

    def process(
        self,
        camera_id,
        analysis,
    ):

        events = vision_monitor.process(
            camera_id,
            analysis,
        )

        return [
            event.to_dict()
            for event in events
        ]

    def latest(self):

        return vision_monitor.latest()

    def list(self):

        return vision_monitor.events()

    def count(self):

        return vision_monitor.count()


vision_event_service = VisionEventService()
