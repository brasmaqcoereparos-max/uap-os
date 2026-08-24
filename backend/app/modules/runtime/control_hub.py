from __future__ import annotations

from app.modules.devices.joystick_manager import (
    JoystickManager,
)

from app.modules.runtime.manual_control import (
    ManualControlManager,
)

from app.modules.runtime.motion_safety import (
    MotionSafetyManager,
)

from app.modules.runtime.position_manager import (
    PositionManager,
)

from app.modules.runtime.position_sequence import (
    PositionSequence,
)

from app.modules.devices.input_manager import (
    InputManager,
)


class ControlHub:
    """
    Centro de controle manual e automático do UAP.
    """

    def __init__(self) -> None:

        self.joysticks = JoystickManager()
        self.inputs = InputManager()

        self.manual = ManualControlManager()
        self.safety = MotionSafetyManager()

        self.positions = PositionManager()

        self.sequences = PositionSequence(
            self.positions
        )

    def emergency_stop(self) -> None:

        self.safety.activate_emergency_stop()

        self.manual.disable()

    def reset_emergency_stop(self) -> None:

        self.safety.reset_emergency_stop()

        self.manual.enable()

    def manual_move(
        self,
        target: str,
        speed: float,
        direction: int,
        source: str = "manual",
    ):

        safe_speed = (
            self.safety.validate_speed(
                speed
            )
        )

        return self.manual.command(
            target=target,
            action="move",
            value={
                "speed": safe_speed,
                "direction": direction,
            },
            source=source,
        )

    def save_position(
        self,
        position_id: str,
        name: str,
        values: dict[str, float],
    ):

        return self.positions.capture(
            position_id=position_id,
            name=name,
            current_values=values,
        )

    def add_position_step(
        self,
        position_id: str,
        values: dict[str, float],
    ):

        return self.sequences.add(
            position_id,
            values,
        )

    def clear_position_steps(self):

        return self.sequences.clear()

    def status(self) -> dict:

        return {
            "manual_control":
                self.manual.enabled,

            "emergency_stop":
                self.safety.limits.emergency_stop,

            "joysticks":
                len(
                    self.joysticks.list()
                ),

            "positions":
                len(
                    self.positions.list()
                ),

            "position_steps":
                len(
                    self.sequences.list()
                ),
    }
