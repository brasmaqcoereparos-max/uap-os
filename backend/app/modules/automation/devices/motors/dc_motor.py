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

        self.pwm = 0

    def set_pwm(

        self,

        pwm,

    ):

        self.pwm = max(

            0,

            min(

                100,

                pwm,

            ),

        )

    def brake(self):

        self.speed = 0

        self.target_speed = 0
