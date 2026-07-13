
from fastapi import APIRouter

from app.modules.devices.service import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.get("/")
def list_devices():
    return DeviceService.list()
