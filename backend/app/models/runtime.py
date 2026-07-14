import uuid

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Runtime(Base):
    __tablename__ = "runtime"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="stopped",
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )
