from app.modules.runtime.runtime_context import RuntimeContext


class FakeHardware:
    def __init__(self):
        self.writes = []

    def write(self, pin, value):
        self.writes.append(
            (pin, value)
        )
        return True

    def read(self, pin):
        return None

    def pwm(self, pin, duty):
        return True


def test_runtime_hardware_bind():
    hardware = FakeHardware()

    context = RuntimeContext(
        "project-bind"
    )

    assert context.hardware_bound() is False

    context.bind_hardware(
        hardware
    )

    assert context.hardware_bound() is True
    assert context.io.hardware is hardware


def test_runtime_hardware_unbind():
    hardware = FakeHardware()

    context = RuntimeContext(
        "project-unbind",
        hardware=hardware,
    )

    assert context.hardware_bound() is True

    context.unbind_hardware()

    assert context.hardware_bound() is False
    assert context.io.hardware is None


def test_bound_runtime_reaches_hardware():
    hardware = FakeHardware()

    context = RuntimeContext(
        "project-output",
        hardware=hardware,
    )

    context.io.configure(
        name="relay",
        direction="output",
        data_type="bool",
        physical_port="GPIO22",
    )

    context.io.write(
        "relay",
        True,
    )

    assert hardware.writes == [
        ("GPIO22", True)
  ]
