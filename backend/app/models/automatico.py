"""
Modelo de automação do UAP.
"""

import uuid

from sqlalchemy import Boolean
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Automation(Base):

    __tablename__ = "automations"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(
            uuid.uuid4()
        ),
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
