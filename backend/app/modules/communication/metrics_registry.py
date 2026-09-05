from app.modules.communication.metric import (
    CommunicationMetric,
)


class CommunicationMetricsRegistry:

    def __init__(self):
        self._metrics: dict[
            str,
            CommunicationMetric,
        ] = {}

    def get(
        self,
        name: str,
    ):
        return self._metrics.get(
            name
        )

    def get_or_create(
        self,
        name: str,
    ):
        metric = self.get(
            name
        )

        if metric:
            return metric

        metric = CommunicationMetric(
            name=name
        )

        self._metrics[
            name
        ] = metric

        return metric

    def increment(
        self,
        name: str,
        amount: float = 1.0,
    ):
        return (
            self.get_or_create(
                name
            )
            .increment(
                amount
            )
        )

    def snapshot(self):
        return {
            name: metric.to_dict()
            for name, metric
            in self._metrics.items()
        }

    def clear(self):
        self._metrics.clear()


communication_metrics_registry = (
    CommunicationMetricsRegistry()
      )
