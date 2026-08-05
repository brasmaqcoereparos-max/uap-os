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

        self.microstep = 1

        self.rpm = 60

    def move_steps(

        self,

        steps,

    ):

        self.position += steps

    def home(self):

        self.position = 0

    def set_microstep(

        self,

        value,

    ):

        self.microstep = value

    def set_rpm(

        self,

        rpm,

    ):

        self.rpm = rpm
