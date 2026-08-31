"""
Rotas públicas do simulador UAP.

Esta API fornece acesso a:
- placas virtuais;
- dispositivos virtuais;
- sensores;
- atuadores;
- controle;
- diagnóstico do simulador.

As rotas existentes foram preservadas.
"""

from fastapi import (
    APIRouter,
    HTTPException,
)

from app.modules.simulator.service import (
    simulator_service,
)


router = APIRouter(
    prefix="/simulator",
    tags=["Simulator"],
)


# ==========================================================
# STATUS
# ==========================================================


@router.get("/status")
def simulator_status():
    return simulator_service.status()


# ==========================================================
# BOARDS
# ==========================================================


@router.get("/boards")
def list_boards():
    return (
        simulator_service.list_boards()
    )


@router.post(
    "/boards/arduino/{board_id}"
)
def create_arduino(
    board_id: str,
    name: str,
):
    return (
        simulator_service.create_arduino(
            board_id,
            name,
        )
    )


@router.post(
    "/boards/esp32/{board_id}"
)
def create_esp32(
    board_id: str,
    name: str,
):
    return (
        simulator_service.create_esp32(
            board_id,
            name,
        )
    )


@router.post(
    "/boards/raspberry/{board_id}"
)
def create_raspberry(
    board_id: str,
    name: str,
):
    return (
        simulator_service.create_raspberry(
            board_id,
            name,
        )
    )


@router.get(
    "/boards/{board_id}"
)
def get_board(
    board_id: str,
):
    board = (
        simulator_service.get_board(
            board_id
        )
    )

    if board is None:
        raise HTTPException(
            status_code=404,
            detail="Board not found",
        )

    return board


@router.delete(
    "/boards/{board_id}"
)
def remove_board(
    board_id: str,
):
    removed = (
        simulator_service.remove_board(
            board_id
        )
    )

    if not removed:
        raise HTTPException(
            status_code=404,
            detail="Board not found",
        )

    return {
        "message": (
            "Board removed"
        ),
        "removed": True,
    }


# ==========================================================
# DEVICES
# ==========================================================


@router.get("/devices")
def list_devices():
    return simulator_service.list()


@router.get(
    "/devices/{device_id}"
)
def get_device(
    device_id: str,
):
    device = (
        simulator_service.get(
            device_id
        )
    )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


# ==========================================================
# ACTUATORS
# ==========================================================


@router.post(
    "/led/{device_id}"
)
def create_led(
    device_id: str,
    name: str,
):
    return (
        simulator_service.create_led(
            device_id,
            name,
        )
    )


@router.post(
    "/button/{device_id}"
)
def create_button(
    device_id: str,
    name: str,
):
    return (
        simulator_service.create_button(
            device_id,
            name,
        )
    )


@router.post(
    "/relay/{device_id}"
)
def create_relay(
    device_id: str,
    name: str,
):
    return (
        simulator_service.create_relay(
            device_id,
            name,
        )
    )


# ==========================================================
# SENSORS
# ==========================================================


@router.post(
    "/temperature/{device_id}"
)
def create_temperature(
    device_id: str,
    name: str,
):
    return (
        simulator_service
        .create_temperature(
            device_id,
            name,
        )
    )


@router.post(
    "/humidity/{device_id}"
)
def create_humidity(
    device_id: str,
    name: str,
):
    return (
        simulator_service
        .create_humidity(
            device_id,
            name,
        )
    )


@router.post(
    "/ultrasonic/{device_id}"
)
def create_ultrasonic(
    device_id: str,
    name: str,
):
    return (
        simulator_service
        .create_ultrasonic(
            device_id,
            name,
        )
    )


# ==========================================================
# CONTROL
# ==========================================================


@router.post(
    "/{device_id}/on"
)
def turn_on(
    device_id: str,
):
    device = (
        simulator_service.turn_on(
            device_id
        )
    )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post(
    "/{device_id}/off"
)
def turn_off(
    device_id: str,
):
    device = (
        simulator_service.turn_off(
            device_id
        )
    )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post(
    "/{device_id}/toggle"
)
def toggle(
    device_id: str,
):
    device = (
        simulator_service.toggle(
            device_id
        )
    )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


# ==========================================================
# RESET
# ==========================================================


@router.post("/reset")
def reset_simulator():
    simulator_service.reset()

    return {
        "message": (
            "Simulator reset"
        )
    }


# ==========================================================
# REMOVE
# ==========================================================


@router.delete(
    "/{device_id}"
)
def remove(
    device_id: str,
):
    # Contrato histórico:
    # sempre respondia "Device removed".
    #
    # Mantemos a mensagem e acrescentamos
    # apenas a informação de resultado.

    removed = (
        simulator_service.remove(
            device_id
        )
    )

    return {
        "message": (
            "Device removed"
        ),
        "removed": bool(
            removed
        ),
            }
