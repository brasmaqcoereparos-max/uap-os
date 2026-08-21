"""
Monitoramento de saúde do UDE.
"""


class DeviceHealth:

    def __init__(self):
        self.healthy = True
        self.message = ""
        self.metrics = {}

    def set_health(
        self,
        healthy,
        message="",
    ):
        self.healthy = bool(healthy)
        self.message = message

    def set_metric(
        self,
        name,
        value,
    ):
        self.metrics[name] = value

    def get_metric(
        self,
        name,
        default=None,
    ):
        return self.metrics.get(
            name,
            default,
        )

    def is_healthy(self):
        return self.healthy

    def to_dict(self):
        return {
            "healthy": self.healthy,
            "message": self.message,
            "metrics": dict(
                self.metrics
            ),
        }
