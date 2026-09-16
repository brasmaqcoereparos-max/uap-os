from app.modules.runtime.io_manager import IOManager
from app.modules.uhal.port_manager import PortManager


class FakeHardware:
    def __init__(self):
        self.writes = []
        self.reads = []
        self.pwms = []
        self.values = {}

    def write(self, pin, value):
        self.writes.append(
            (pin, value)
        )
        self.values[pin] = value
        return True

    def read(self, pin):
        self.reads.append(pin)
        return self.values.get(pin)

    def pwm(self, pin, duty):
        self.pwms.append(
            (pin, duty)
        )
        self.values[pin] = duty
        return True


def test_output_reaches_physical_hardware():
    hardware = FakeHardware()

    io = IOManager(
        ports=PortManager(),
        hardware=hardware,
    )

    io.configure(
        name="relay",
        direction="output",
        physical_port="GPIO23",
    )

    assert io.write(
        "relay",
        True,
    ) is True

    assert hardware.writes == [
        ("GPIO23", True)
    ]


def test_input_reads_physical_hardware():
    hardware = FakeHardware()
    hardware.values["GPIO17"] = True

    io = IOManager(
        ports=PortManager(),
        hardware=hardware,
    )

    io.configure(
        name="door",
        direction="input",
        physical_port="GPIO17",
    )

    assert io.read("door") is True
    assert hardware.reads == ["GPIO17"]


def test_pwm_reaches_physical_hardware():
    hardware = FakeHardware()

    io = IOManager(
        ports=PortManager(),
        hardware=hardware,
    )

    io.configure(
        name="motor",
        direction="output",
        physical_port="GPIO12",
    )

    assert io.pwm(
        "motor",
        0.75,
    ) is True

    assert hardware.pwms == [
        ("GPIO12", 0.75)
    ]
