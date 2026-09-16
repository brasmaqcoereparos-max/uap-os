import pytest

from app.modules.runtime.runtime_context import RuntimeContext


class BoundaryHardware:
    def __init__(self):
        self.values = {}
        self.commands = []

    def write(self, pin, value):
        self.values[pin] = value

        self.commands.append(
            (
                "write",
                pin,
                value,
            )
        )

        return True

    def read(self, pin):
        self.commands.append(
            (
                "read",
                pin,
            )
        )

        return self.values.get(pin)

    def pwm(self, pin, duty):
        self.values[pin] = duty

        self.commands.append(
            (
                "pwm",
                pin,
                duty,
            )
        )

        return True


def test_block7_runtime_to_hardware_boundary():
    hardware = BoundaryHardware()

    context = RuntimeContext(
        project_id="block7-final",
        hardware=hardware,
    )

    context.io.configure(
        name="relay",
        direction="output",
        data_type="bool",
        physical_port="GPIO23",
    )

    context.io.configure(
        name="sensor",
        direction="input",
        data_type="bool",
        physical_port="GPIO17",
    )

    context.io.configure(
        name="motor_speed",
        direction="output",
        data_type="float",
        physical_port="GPIO12",
    )

    context.interlocks.register(
        interlock_id="safety-door",
        name="Safety Door",
        condition=lambda: False,
    )

    context.start()

    assert context.state.running is True
    assert context.is_safe() is True

    context.io.write(
        "relay",
        True,
    )

    assert hardware.values[
        "GPIO23"
    ] is True

    hardware.values[
        "GPIO17"
    ] = True

    assert context.io.read(
        "sensor"
    ) is True

    context.io.pwm(
        "motor_speed",
        0.65,
    )

    assert hardware.values[
        "GPIO12"
    ] == 0.65

    context.pause()

    assert context.state.paused is True

    context.resume()

    assert context.state.paused is False

    context.emergency_stop(
        "boundary test"
    )

    assert context.state.running is False
    assert context.state.emergency_stop is True

    with pytest.raises(RuntimeError):
        context.start()

    context.reset_emergency_stop()

    assert context.state.emergency_stop is False

    context.start()

    assert context.state.running is True

    context.stop()

    assert context.state.running is False

    status = context.status()

    assert status[
        "project_id"
    ] == "block7-final"

    assert status[
        "hardware_bound"
    ] is True

    assert status[
        "safe"
    ] is True


def test_block7_active_interlock_blocks_execution_start():
    context = RuntimeContext(
        "block7-unsafe"
    )

    context.interlocks.register(
        interlock_id="emergency-chain",
        name="Emergency Chain",
        condition=lambda: True,
        action="emergency_stop",
    )

    with pytest.raises(RuntimeError):
        context.start()

    assert context.state.running is False
    assert context.state.emergency_stop is True

    status = context.status()

    assert status["safe"] is False

    assert (
        "emergency-chain"
        in status[
            "interlocks"
        ][
            "triggered"
        ]
  )
