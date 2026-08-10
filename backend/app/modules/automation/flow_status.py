from enum import Enum


class FlowStatus(Enum):

    CREATED = "created"

    READY = "ready"

    RUNNING = "running"

    PAUSED = "paused"

    STOPPED = "stopped"

    ERROR = "error"


class FlowStatusManager:

    def __init__(self):

        self.status = FlowStatus.CREATED

        self.message = ""

    def set(
        self,
        status,
        message="",
    ):

        self.status = status
        self.message = message

    def get(self):

        return self.status


flow_status = FlowStatusManager()
