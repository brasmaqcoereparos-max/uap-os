from __future__ import annotations

from app.modules.devices.actuator_manager import (
    ActuatorManager,
)
from app.modules.devices.motor_manager import (
    MotorManager,
)
from app.modules.devices.servo_manager import (
    ServoManager,
)
from app.modules.devices.digital_output_manager import (
    DigitalOutputManager,
)
from app.modules.devices.pwm_manager import (
    PWMManager,
)


class ActuatorHub:
    """
    Centro universal de atuadores do UAP.

    Reúne:
    - motores
    - servos
    - relés
    - saídas digitais
    - PWM
    - atuadores genéricos
    """

    def __init__(self) -> None:
        self.actuators = ActuatorManager()
        self.motors = MotorManager()
        self.servos = ServoManager()
        self.digital = DigitalOutputManager()
        self.pwm = PWMManager()

    def stop_all(self) -> None:
        self.motors.stop_all()
        self.digital.all_off()

        for output in self.pwm.list():
            output.duty_cycle = 0.0

    def status(self) -> dict:
        return {
            "actuators": len(
                self.actuators.list()
            ),
            "motors": len(
                self.motors.list()
            ),
            "servos": len(
                self.servos.list()
            ),
            "digital_outputs": len(
                self.digital.list()
            ),
            "pwm_outputs": len(
                self.pwm.list()
            ),
        }
