import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Plugin(Base):
    __tablename__ = "plugins"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    version: Mapped[str] = mapped_column(
        String(20),
        default="1.0.0",
    )

    author: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="disabled",
    )
