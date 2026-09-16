import pytest

from app.modules.uhal.port_manager import PortManager


def test_port_registration_contract():
    ports = PortManager()

    port = ports.register(
        name="motor",
        direction="OUTPUT",
        data_type="float",
        device_id="motor-1",
        physical_port="GPIO18",
        metadata={
            "pwm": True,
        },
    )

    assert port.name == "motor"
    assert port.direction == "output"
    assert port.data_type == "float"
    assert port.device_id == "motor-1"
    assert port.physical_port == "GPIO18"
    assert port.metadata["pwm"] is True


def test_port_value_contract():
    ports = PortManager()

    ports.register(
        name="sensor",
        direction="input",
        data_type="bool",
    )

    ports.set_value(
        "sensor",
        True,
    )

    assert ports.get_value("sensor") is True


def test_disabled_port_rejects_access():
    ports = PortManager()

    ports.register(
        name="relay",
        direction="output",
    )

    ports.disable("relay")

    with pytest.raises(RuntimeError):
        ports.set_value(
            "relay",
            True,
        )

    with pytest.raises(RuntimeError):
        ports.get_value("relay")


def test_invalid_port_direction_rejected():
    ports = PortManager()

    with pytest.raises(ValueError):
        ports.register(
            name="invalid",
            direction="sideways",
        )
