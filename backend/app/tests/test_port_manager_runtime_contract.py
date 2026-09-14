import pytest

from app.modules.runtime.io_manager import (
    IOManager,
)

from app.modules.uhal.port_manager import (
    PortManager,
)


def test_port_manager_enable_disable_runtime_contract():
    ports = PortManager()

    io = IOManager(
        ports
    )

    io.configure(
        "motor",
        "OUTPUT",
        "float",
    )

    io.write(
        "motor",
        0.5,
    )

    assert (
        io.read(
            "motor"
        )
        == 0.5
    )

    ports.disable(
        "motor"
    )

    with pytest.raises(
        RuntimeError
    ):
        io.write(
            "motor",
            1,
        )

    with pytest.raises(
        RuntimeError
    ):
        io.read(
            "motor"
        )

    ports.enable(
        "motor"
    )

    io.write(
        "motor",
        1,
    )

    assert (
        io.read(
            "motor"
        )
        == 1
    )

    with pytest.raises(
        ValueError
    ):
        ports.register(
            "invalid",
            "sideways",
        )
