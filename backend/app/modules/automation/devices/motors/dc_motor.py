from app.modules.automation.devices.motors.motor_base import (
    MotorBase,
)

from app.modules.automation.devices.motors.pid_controller import (
    PIDController,
)

from app.modules.automation.devices.motors.energy_monitor import (
    EnergyMonitor,
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

        self.pid = PIDController()

        self.energy = EnergyMonitor()

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

    def pid_output(self):

        return self.pid.update(

            self.target_speed,

            self.speed,

        )
