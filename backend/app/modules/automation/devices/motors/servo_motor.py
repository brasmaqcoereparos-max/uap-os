from app.modules.automation.devices.motors.motor_base import (
    MotorBase,
)


class ServoMotor(MotorBase):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.angle = 0

    def set_angle(

        self,

        angle,

    ):

        self.angle = max(

            0,

            min(

                180,

                angle,

            ),

        )
