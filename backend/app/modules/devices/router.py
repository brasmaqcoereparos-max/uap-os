from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.device import DeviceCreate, DeviceUpdate
from app.modules.devices.service import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.get("/")
def list_devices(db: Session = Depends(get_db)):
    return DeviceService.list(db)


@router.get("/{device_id}")
def get_device(device_id: str, db: Session = Depends(get_db)):
    device = DeviceService.get(db, device_id)

    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    return device


@router.post("/")
def create_device(
    device: DeviceCreate,
    db: Session = Depends(get_db),
):
    return DeviceService.create(
        db=db,
        name=device.name,
        type=device.type,
        protocol=device.protocol,
        ip_address=device.ip_address,
        serial_port=device.serial_port,
    )


@router.put("/{device_id}")
def update_device(
    device_id: str,
    device: DeviceUpdate,
    db: Session = Depends(get_db),
):
    updated = DeviceService.update(
        db=db,
        device_id=device_id,
        name=device.name,
        type=device.type,
        protocol=device.protocol,
        ip_address=device.ip_address,
        serial_port=device.serial_port,
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Device not found")

    return updated


@router.delete("/{device_id}")
def delete_device(
    device_id: str,
    db: Session = Depends(get_db),
):
    deleted = DeviceService.delete(db, device_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Device not found")

    return {"message": "Device deleted successfully"}
