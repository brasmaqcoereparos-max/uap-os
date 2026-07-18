from app.modules.simulator.programming.canvas.device_queue import (
    device_queue,
)
from app.modules.simulator.programming.canvas.device_executor import (
    device_executor,
)


class DeviceScheduler:

    def execute(self):

        while not device_queue.empty():

            task = device_queue.pop()

            device_executor.execute(

                task["device"],

                task["command"],

                *task["args"],

                **task["kwargs"],

            )

    def add(

        self,

        device,

        command,

        *args,

        **kwargs,

    ):

        device_queue.push(

            device,

            command,

            *args,

            **kwargs,

        )


device_scheduler = DeviceScheduler()
