from fastapi import APIRouter

from app.modules.simulator.programming.canvas.device_runtime import (
    device_runtime,
)

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.get("/")
def status():

    return device_runtime.status()


@router.post("/start")
def start():

    device_runtime.initialize()

    return device_runtime.status()


@router.post("/stop")
def stop():

    device_runtime.shutdown()

    return device_runtime.status()
