from fastapi import APIRouter

from app.modules.drivers.service import DriverService

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"],
)


@router.get("/")
def list_drivers():
    return DriverService.supported()


@router.get("/supported")
def supported_drivers():
    return DriverService.supported()
