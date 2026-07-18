from app.modules.simulator.programming.canvas.device_cache import (
    device_cache,
)
from app.modules.simulator.programming.canvas.device_metrics import (
    device_metrics,
)


class DeviceResourceManager:

    def initialize(self):

        device_cache.clear()

        device_metrics.clear()

    def cache(

        self,

        key,

        value,

    ):

        device_cache.put(

            key,

            value,

        )

    def metric(

        self,

        name,

        value=1,

    ):

        device_metrics.increment(

            name,

            value,

        )

    def status(self):

        return {

            "cache_items": device_cache.size(),

            "metrics": device_metrics.all(),

        }


device_resource_manager = DeviceResourceManager()
