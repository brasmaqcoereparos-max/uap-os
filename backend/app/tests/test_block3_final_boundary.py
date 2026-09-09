from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_library import (
    ComponentLibrary,
)

from app.modules.simulator.programming.simulator.device.device_catalog import (
    DeviceCatalog,
)

from app.modules.simulator.programming.simulator.device.device_registry import (
    DeviceRegistry,
)

from app.modules.uhal.compatibility import (
    HardwareCompatibilityChecker,
)

from app.modules.uhal.device_model import (
    UniversalDevice,
)


class SimulatedDevice:

    def __init__(
        self,
        name="sim",
    ):
        self.name = name

    def update(self):
        return {
            "ok": True,
        }

    def to_dict(self):
        return {
            "name": self.name,
        }


def test_block3_component_catalog_device_simulator_hardware_boundary():
    component_library = (
        ComponentLibrary()
    )

    device_catalog = (
        DeviceCatalog()
    )

    device_registry = (
        DeviceRegistry()
    )

    component_library.register(
        Component,
        name="Motor",
        category="motion",
        icon="motor.svg",
    )

    device_catalog.register(
        "motor_sim",
        SimulatedDevice,
        category="motion",
        icon="motor.svg",
    )

    component = (
        component_library.create(
            "Motor",
            name="M1",
            component_type="motor",
            metadata={
                "required_capabilities": [
                    "gpio",
                    "pwm",
                ],
            },
        )
    )

    simulated_device_class = (
        device_catalog.get(
            "motor_sim"
        )
    )

    simulated_device = (
        simulated_device_class(
            name="M1-sim"
        )
    )

    device_registry.register(
        simulated_device
    )

    component.bind_device(
        simulated_device
    )

    board = UniversalDevice(
        device_id="board",
        name="Board",
        device_type="controller",
    )

    board.add_capability(
        "gpio"
    )

    board.add_capability(
        "pwm"
    )

    requirements = (
        component.get_metadata(
            "required_capabilities"
        )
    )

    compatibility = (
        HardwareCompatibilityChecker()
        .check(
            board,
            requirements,
        )
    )

    assert (
        component.has_device()
        is True
    )

    assert (
        device_registry.exists(
            "M1-sim"
        )
        is True
    )

    assert (
        component.update_device()
        == {
            "ok": True,
        }
    )

    assert (
        compatibility.compatible
        is True
  )
