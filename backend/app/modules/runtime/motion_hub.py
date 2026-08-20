from __future__ import annotations

from app.modules.devices.calibration_manager import (
    CalibrationManager,
)
from app.modules.devices.encoder_manager import (
    EncoderManager,
)
from app.modules.devices.safety_sensor_manager import (
    SafetySensorManager,
)
from app.modules.runtime.interlock_manager import (
    InterlockManager,
)
from app.modules.runtime.motion_profile import (
    MotionProfile,
)
from app.modules.runtime.trajectory_manager import (
    TrajectoryManager,
)


class MotionHub:
    """
    Camada central para movimento seguro.

    Integra:
    - encoders
    - sensores de segurança
    - intertravamentos
    - perfil de aceleração
    - trajetórias
    - calibração
    """

    def __init__(self) -> None:
        self.encoders = EncoderManager()
        self.safety_sensors = SafetySensorManager()
        self.interlocks = InterlockManager()
        self.calibration = CalibrationManager()
        self.trajectories = TrajectoryManager()

        self.profiles: dict[
            str,
            MotionProfile,
        ] = {}

    def create_profile(
        self,
        name: str,
        maximum_speed: float = 100.0,
        acceleration: float = 50.0,
        deceleration: float = 50.0,
    ) -> MotionProfile:
        profile = MotionProfile(
            maximum_speed=maximum_speed,
            acceleration=acceleration,
            deceleration=deceleration,
        )

        self.profiles[name] = profile

        return profile

    def is_safe(self) -> bool:
        if self.safety_sensors.any_triggered():
            return False

        if not self.interlocks.is_safe():
            return False

        return True

    def emergency_stop(self) -> None:
        for profile in self.profiles.values():
            profile.reset()

    def status(self) -> dict:
        return {
            "encoders": len(
                self.encoders.list()
            ),
            "safety_sensors": len(
                self.safety_sensors.list()
            ),
            "triggered_safety_sensors":
                self.safety_sensors.any_triggered(),
            "interlocks": len(
                self.interlocks.list()
            ),
            "safe": self.is_safe(),
            "trajectories": len(
                self.trajectories.list()
            ),
            "motion_profiles": len(
                self.profiles
            ),
        }
