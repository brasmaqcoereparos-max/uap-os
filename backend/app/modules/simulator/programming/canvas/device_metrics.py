class DeviceMetrics:

    def __init__(self):

        self.metrics = {}

    def increment(

        self,

        metric,

        value=1,

    ):

        self.metrics[metric] = (

            self.metrics.get(

                metric,

                0,

            )

            + value

        )

    def set(

        self,

        metric,

        value,

    ):

        self.metrics[metric] = value

    def get(

        self,

        metric,

        default=0,

    ):

        return self.metrics.get(

            metric,

            default,

        )

    def all(self):

        return self.metrics.copy()

    def clear(self):

        self.metrics.clear()


device_metrics = DeviceMetrics()
