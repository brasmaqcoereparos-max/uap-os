from fastapi import APIRouter, HTTPException

from app.modules.simulator.service import simulator_service

router = APIRouter(
    prefix="/simulator",
    tags=["Simulator"],
)


@router.get("/devices")
def list_devices():
    return simulator_service.list()


@router.post("/led/{device_id}")
def create_led(
    device_id: str,
    name: str,
):
    return simulator_service.create_led(
        device_id,
        name,
    )


@router.post("/button/{device_id}")
def create_button(
    device_id: str,
    name: str,
):
    return simulator_service.create_button(
        device_id,
        name,
    )


@router.post("/relay/{device_id}")
def create_relay(
    device_id: str,
    name: str,
):
    return simulator_service.create_relay(
        device_id,
        name,
    )


@router.post("/{device_id}/on")
def turn_on(device_id: str):
    device = simulator_service.turn_on(device_id)

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post("/{device_id}/off")
def turn_off(device_id: str):
    device = simulator_service.turn_off(device_id)

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post("/{device_id}/toggle")
def toggle(device_id: str):
    device = simulator_service.toggle(device_id)

    if not device:
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
