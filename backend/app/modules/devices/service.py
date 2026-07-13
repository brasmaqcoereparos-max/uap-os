from sqlalchemy.orm import Session

from app.models.device import Device
from app.repositories.device_repository import DeviceRepository


class DeviceService:

    @staticmethod
    def list(db: Session):
        return DeviceRepository.list(db)

    @staticmethod
    def get(db: Session, device_id: str):
        return DeviceRepository.get(db, device_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        type: str,
        protocol: str,
        ip_address: str,
        serial_port: str,
    ):
        device = Device(
            name=name,
            type=type,
            protocol=protocol,
            ip_address=ip_address,
            serial_port=serial_port,
        )

        return DeviceRepository.create(db, device)

    @staticmethod
    def update(
        db: Session,
        device_id: str,
        name: str,
        type: str,
        protocol: str,
        ip_address: str,
        serial_port: str,
    ):
        device = DeviceRepository.get(db, device_id)

        if not device:
            return None

        device.name = name
        device.type = type
        device.protocol = protocol
        device.ip_address = ip_address
        device.serial_port = serial_port

        db.commit()
        db.refresh(device)

        return device

    @staticmethod
    def delete(
        db: Session,
        device_id: str,
    ):
        device = DeviceRepository.get(db, device_id)

        if not device:
            return False

        DeviceRepository.delete(db, device)

        return True
