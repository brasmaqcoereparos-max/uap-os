import pytest

from app.modules.runtime.io_manager import (
    IOManager,
)
from app.modules.runtime.runtime_context import (
    RuntimeContext,
)
from app.modules.uhal.port_manager import (
    PortManager,
)


class FakeHardwareController:
    def __init__(self):
        self.writes = []
        self.reads = []
        self.pwms = []
        self.input_values = {}

    def write(
        self,
        pin,
        value,
    ):
        self.writes.append(
            (
                pin,
                value,
            )
        )

        return True

    def read(
        self,
        pin,
    ):
        self.reads.append(
            pin
        )

        return self.input_values.get(
            pin
        )

    def pwm(
        self,
        pin,
        duty,
    ):
        self.pwms.append(
            (
                pin,
                duty,
            )
        )

        return True


def test_logical_output_reaches_hardware():
    hardware = FakeHardwareController()

    ports = PortManager()

    io = IOManager(
        ports=ports,
        hardware=hardware,
    )

    io.configure(
        name="lamp",
        direction="output",
        data_type="bool",
        physical_port="GPIO18",
    )

    result = io.write(
        "lamp",
        True,
    )

    assert result is True

    assert hardware.writes == [
        (
            "GPIO18",
            True,
        )
    ]

    assert (
        io.read(
            "lamp"
        )
        is True
    )


def test_logical_input_reads_hardware():
    hardware = FakeHardwareController()

    hardware.input_values[
        "GPIO17"
    ] = True

    ports = PortManager()

    io = IOManager(
        ports=ports,
        hardware=hardware,
    )

    io.configure(
        name="door_sensor",
        direction="input",
        data_type="bool",
        physical_port="GPIO17",
    )

    value = io.read(
        "door_sensor"
    )

    assert value is True

    assert hardware.reads == [
        "GPIO17"
    ]

    assert (
        ports.get_value(
            "door_sensor"
        )
        is True
    )


def test_pwm_reaches_hardware():
    hardware = FakeHardwareController()

    ports = PortManager()

    io = IOManager(
        ports=ports,
        hardware=hardware,
    )

    io.configure(
        name="motor_speed",
        direction="output",
        data_type="float",
        physical_port="GPIO12",
    )

    result = io.pwm(
        "motor_speed",
        0.75,
    )

    assert result is True

    assert hardware.pwms == [
        (
            "GPIO12",
            0.75,
        )
    ]

    assert (
        io.read(
            "motor_speed"
        )
        == 0.75
    )


def test_unmapped_port_remains_virtual():
    hardware = FakeHardwareController()

    ports = PortManager()

    io = IOManager(
        ports=ports,
        hardware=hardware,
    )

    io.configure(
        name="virtual_output",
        direction="output",
        data_type="int",
    )

    result = io.write(
        "virtual_output",
        10,
    )

    assert result is None

    assert hardware.writes == []

    assert (
        io.read(
            "virtual_output"
        )
        == 10
    )


def test_disabled_port_blocks_hardware():
    hardware = FakeHardwareController()

    ports = PortManager()

    io = IOManager(
        ports=ports,
        hardware=hardware,
    )

    io.configure(
        name="motor",
        direction="output",
        physical_port="GPIO22",
    )

    ports.disable(
        "motor"
    )

    with pytest.raises(
        RuntimeError
    ):
        io.write(
            "motor",
            True,
        )

    assert hardware.writes == []


def test_runtime_can_bind_hardware():
    hardware = FakeHardwareController()

    context = RuntimeContext(
        "project-hardware"
    )

    assert (
        context.hardware_bound()
        is False
    )

    context.bind_hardware(
        hardware
    )

    assert (
        context.hardware_bound()
        is True
    )

    context.io.configure(
        name="relay",
        direction="output",
        data_type="bool",
        physical_port="GPIO23",
    )

    context.io.write(
        "relay",
        True,
    )

    assert hardware.writes == [
        (
            "GPIO23",
            True,
        )
    ]

    context.unbind_hardware()

    assert (
        context.hardware_bound()
        is False
    )
