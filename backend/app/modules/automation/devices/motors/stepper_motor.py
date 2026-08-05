from app.modules.automation.devices.motors.motor_base import (
    MotorBase,
)


class StepperMotor(MotorBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.position = 0

    def move_steps(

        self,

        steps,

    ):

        self.position += steps
