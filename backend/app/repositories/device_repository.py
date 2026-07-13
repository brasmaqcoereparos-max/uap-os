from sqlalchemy.orm import Session

from app.models.device import Device


class DeviceRepository:

    @staticmethod
    def list(db: Session):
        return db.query(Device).all()

    @staticmethod
    def get(db: Session, device_id: str):
        return db.query(Device).filter(Device.id == device_id).first()

    @staticmethod
    def create(db: Session, device: Device):
        db.add(device)
        db.commit()
        db.refresh(device)
        return device

    @staticmethod
    def delete(db: Session, device: Device):
        db.delete(device)
        db.commit()
