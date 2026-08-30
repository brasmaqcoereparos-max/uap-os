"""
Processador de eventos do simulador UAP.
"""


class EventProcessor:

    def __init__(self):
        self.processed = 0
        self.failed = 0

        self.last_event = None
        self.last_error = None

    def process(
        self,
        event,
    ):
        if event is None:
            return False

        self.last_event = event

        try:
            handler = getattr(
                event,
                "handle",
                None,
            )

            if callable(handler):
                handler()

            elif callable(event):
                event()

            self.processed += 1
            self.last_error = None

            return True

        except Exception as exc:
            self.failed += 1
            self.last_error = str(exc)

            raise

    def process_many(
        self,
        events,
        stop_on_error=False,
    ):
        results = []

        for event in events or []:
            try:
                results.append(
                    self.process(event)
                )

            except Exception:
                results.append(False)

                if stop_on_error:
                    raise

        return results

    def reset(self):
        self.processed = 0
        self.failed = 0

        self.last_event = None
        self.last_error = None

    def status(self):
        return {
            "processed": (
                self.processed
            ),
            "failed": self.failed,
            "last_error": (
                self.last_error
            ),
        }

    def to_dict(self):
        return self.status()
