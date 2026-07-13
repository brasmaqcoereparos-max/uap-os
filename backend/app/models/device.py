import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    protocol: Mapped[str] = mapped_column(
        String(30),
        default="TCP/IP",
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="offline",
    )

    ip_address: Mapped[str] = mapped_column(
        String(50),
        default="",
    )

    serial_port: Mapped[str] = mapped_column(
        String(50),
        default="",
    )
