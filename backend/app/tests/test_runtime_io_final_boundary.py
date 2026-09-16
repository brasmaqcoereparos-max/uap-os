import pytest

from app.modules.runtime.io_manager import IOManager
from app.modules.uhal.port_manager import PortManager


def test_virtual_output_contract():
    ports = PortManager()
    io = IOManager(ports=ports)

    io.configure(
        name="lamp",
        direction="output",
        data_type="bool",
    )

    io.write(
        "lamp",
        True,
    )

    assert io.read("lamp") is True


def test_virtual_pwm_contract():
    ports = PortManager()
    io = IOManager(ports=ports)

    io.configure(
        name="speed",
        direction="output",
        data_type="float",
    )

    result = io.pwm(
        "speed",
        0.5,
    )

    assert result is None
    assert io.read("speed") == 0.5


def test_missing_port_is_rejected():
    io = IOManager()

    with pytest.raises(KeyError):
        io.write(
            "missing",
            True,
        )


def test_input_cannot_be_written():
    io = IOManager()

    io.configure(
        name="door",
        direction="input",
        data_type="bool",
    )

    with pytest.raises(ValueError):
        io.write(
            "door",
            True,
        )
