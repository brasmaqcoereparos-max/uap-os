from fastapi import APIRouter, HTTPException

from app.modules.simulator.service import simulator_service

router = APIRouter(
    prefix="/simulator",
    tags=["Simulator"],
)


@router.get("/devices")
def list_devices():
    return simulator_service.list()


# -----------------------
# Atuadores
# -----------------------

@router.post("/led/{device_id}")
def create_led(device_id: str, name: str):
    return simulator_service.create_led(device_id, name)


@router.post("/button/{device_id}")
def create_button(device_id: str, name: str):
    return simulator_service.create_button(device_id, name)


@router.post("/relay/{device_id}")
def create_relay(device_id: str, name: str):
    return simulator_service.create_relay(device_id, name)


# -----------------------
# Sensores
# -----------------------

@router.post("/temperature/{device_id}")
def create_temperature(device_id: str, name: str):
    return simulator_service.create_temperature(
        device_id,
        name,
    )


@router.post("/humidity/{device_id}")
def create_humidity(device_id: str, name: str):
    return simulator_service.create_humidity(
        device_id,
        name,
    )


@router.post("/ultrasonic/{device_id}")
def create_ultrasonic(device_id: str, name: str):
    return simulator_service.create_ultrasonic(
        device_id,
        name,
    )


# -----------------------
# Controle
# -----------------------

@router.post("/{device_id}/on")
def turn_on(device_id: str):
    device = simulator_service.turn_on(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post("/{device_id}/off")
def turn_off(device_id: str):
    device = simulator_service.turn_off(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post("/{device_id}/toggle")
def toggle(device_id: str):
    device = simulator_service.toggle(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.get("/{device_id}")
def get_device(device_id: str):
    device = simulator_service.get(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.delete("/{device_id}")
def remove(device_id: str):
    simulator_service.remove(device_id)

    return {
        "message": "Device removed"
    }
