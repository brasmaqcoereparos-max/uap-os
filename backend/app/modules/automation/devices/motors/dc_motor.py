from app.modules.automation.devices.motors.motor_base import (
    MotorBase,
)


class DCMotor(MotorBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )
