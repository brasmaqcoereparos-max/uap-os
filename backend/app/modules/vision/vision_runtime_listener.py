from app.runtime.runtime_events import (
    runtime_events,
)


class VisionRuntimeListener:

    def __init__(self):
        self.enabled = True
        self.last_event = None

        runtime_events.subscribe(
            "vision.decision",
            self.on_decision,
        )

    def on_decision(self, event):

        if not self.enabled:
            return None

        self.last_event = event

        return {
            "received": True,
            "event": event.to_dict()
            if hasattr(
                event,
                "to_dict",
            )
            else event,
        }

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def status(self):

        return {
            "enabled": self.enabled,
            "last_event": self.last_event,
        }


vision_runtime_listener = (
    VisionRuntimeListener()
  )
