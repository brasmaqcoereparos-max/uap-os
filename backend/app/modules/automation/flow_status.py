from enum import Enum


class FlowStatus(
    str,
    Enum,
):
    CREATED = "created"
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"
    COMPLETED = "completed"
    ERROR = "error"

    @classmethod
    def normalize(
        cls,
        value,
    ):
        if isinstance(value, cls):
            return value

        text = str(
            value
        ).strip().lower()

        for item in cls:
            if item.value == text:
                return item

        raise ValueError(
            f"Status inválido: {value}"
        )


class FlowStatusManager:
    def __init__(self):
        self.status = (
            FlowStatus.CREATED
        )

        self.message = ""

        self.error = None

        self.metadata = {}

    def set(
        self,
        status,
        message="",
        error=None,
        metadata=None,
    ):
        self.status = (
            FlowStatus.normalize(
                status
            )
        )

        self.message = str(
            message
        )

        self.error = error

        if metadata is not None:
            self.metadata = dict(
                metadata
            )

        return self.status

    def ready(
        self,
        message="",
    ):
        return self.set(
            FlowStatus.READY,
            message,
        )

    def running(
        self,
        message="",
    ):
        return self.set(
            FlowStatus.RUNNING,
            message,
        )

    def pause(
        self,
        message="",
    ):
        return self.set(
            FlowStatus.PAUSED,
            message,
        )

    def stop(
        self,
        message="",
    ):
        return self.set(
            FlowStatus.STOPPED,
            message,
        )

    def complete(
        self,
        message="",
    ):
        return self.set(
            FlowStatus.COMPLETED,
            message,
        )

    def fail(
        self,
        error,
        message="",
    ):
        return self.set(
            FlowStatus.ERROR,
            message=message
            or str(error),
            error=error,
        )

    def get(self):
        return self.status

    def is_running(self):
        return (
            self.status
            == FlowStatus.RUNNING
        )

    def to_dict(self):
        return {
            "status": (
                self.status.value
            ),
            "message": self.message,
            "error": (
                str(self.error)
                if self.error
                is not None
                else None
            ),
            "metadata": dict(
                self.metadata
            ),
        }


flow_status = FlowStatusManager()
