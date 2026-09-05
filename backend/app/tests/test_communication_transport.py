from app.modules.communication.connection_service import (
    communication_connection_service,
)
from app.modules.communication.transport_manager import (
    communication_transport_manager,
)


def test_transports_available():
    transports = (
        communication_transport_manager
        .transports()
    )

    names = {
        item["name"]
        for item in transports
    }

    assert "memory" in names
    assert "http" in names
    assert "websocket" in names
    assert "mqtt" in names
    assert "serial" in names


def test_memory_connection():
    result = (
        communication_connection_service
        .open(
            transport="memory",
            destination="test",
        )
    )

    assert (
        result["connection"][
            "state"
        ]
        == "connected"
    )

    assert (
        result["session"][
            "active"
        ]
        is True
    )


def test_memory_send():
    opened = (
        communication_connection_service
        .open(
            transport="memory",
            destination="test",
        )
    )

    connection_id = (
        opened[
            "connection"
        ]["id"]
    )

    result = (
        communication_connection_service
        .send(
            connection_id=(
                connection_id
            ),
            payload={
                "hello": "uap",
            },
        )
    )

    assert result[
        "success"
    ] is True
