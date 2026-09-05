from dataclasses import dataclass


@dataclass
class CommunicationTimeoutPolicy:
    connect_timeout_seconds: float = 5.0

    read_timeout_seconds: float = 10.0

    write_timeout_seconds: float = 10.0

    idle_timeout_seconds: float = 60.0

    def to_dict(self):
        return {
            "connect_timeout_seconds": (
                self.connect_timeout_seconds
            ),
            "read_timeout_seconds": (
                self.read_timeout_seconds
            ),
            "write_timeout_seconds": (
                self.write_timeout_seconds
            ),
            "idle_timeout_seconds": (
                self.idle_timeout_seconds
            ),
        }
