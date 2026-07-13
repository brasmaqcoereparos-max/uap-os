from sqlalchemy.orm import Session

from app.models.device import Device


class DeviceService:

    @staticmethod
    def list(db: Session):
        return db.query(Device).all()

    @staticmethod
    def get(db: Session, device_id: str):
        return db.query(Device).filter(Device.id == device_id).first()

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

        db.add(device)
        db.commit()
        db.refresh(device)

        return device

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
        device = db.query(Device).filter(Device.id == device_id).first()

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
    def delete(db: Session, device_id: str):
        device = db.query(Device).filter(Device.id == device_id).first()

        if not device:
            return False

        db.delete(device)
        db.commit()

        return True
