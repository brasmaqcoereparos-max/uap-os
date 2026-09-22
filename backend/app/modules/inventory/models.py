from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from datetime import datetime
from datetime import timezone
from decimal import Decimal
from typing import Any


def utc_now():
    return datetime.now(
        timezone.utc
    )


def decimal_value(
    value,
) -> Decimal:
    return Decimal(
        str(
            value
        )
    )


@dataclass
class StockBalance:

    product_id: str

    location: str = "default"

    on_hand: Decimal = Decimal(
        "0"
    )

    reserved: Decimal = Decimal(
        "0"
    )

    updated_at: datetime = field(
        default_factory=utc_now
    )

    @property
    def available(
        self,
    ) -> Decimal:

        return (
            self.on_hand
            - self.reserved
        )

    def touch(self):

        self.updated_at = utc_now()

    def to_dict(self):

        return {
            "product_id": (
                self.product_id
            ),
            "location": (
                self.location
            ),
            "on_hand": str(
                self.on_hand
            ),
            "reserved": str(
                self.reserved
            ),
            "available": str(
                self.available
            ),
            "updated_at": (
                self.updated_at
                .isoformat()
            ),
        }


@dataclass
class StockMovement:

    id: str

    product_id: str

    movement_type: str

    quantity: Decimal

    location: str = "default"

    lot_id: str | None = None

    reason: str = ""

    reference: (
        str | None
    ) = None

    before_quantity: Decimal = Decimal(
        "0"
    )

    after_quantity: Decimal = Decimal(
        "0"
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=utc_now
    )

    def to_dict(self):

        return {
            "id": self.id,
            "product_id": (
                self.product_id
            ),
            "movement_type": (
                self.movement_type
            ),
            "quantity": str(
                self.quantity
            ),
            "location": (
                self.location
            ),
            "lot_id": (
                self.lot_id
            ),
            "reason": self.reason,
            "reference": (
                self.reference
            ),
            "before_quantity": str(
                self.before_quantity
            ),
            "after_quantity": str(
                self.after_quantity
            ),
            "metadata": dict(
                self.metadata
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }


@dataclass
class StockReservation:

    id: str

    product_id: str

    quantity: Decimal

    location: str = "default"

    reference: (
        str | None
    ) = None

    status: str = "active"

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=utc_now
    )

    updated_at: datetime = field(
        default_factory=utc_now
    )

    def touch(self):

        self.updated_at = utc_now()

    def to_dict(self):

        return {
            "id": self.id,
            "product_id": (
                self.product_id
            ),
            "quantity": str(
                self.quantity
            ),
            "location": (
                self.location
            ),
            "reference": (
                self.reference
            ),
            "status": self.status,
            "metadata": dict(
                self.metadata
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "updated_at": (
                self.updated_at
                .isoformat()
            ),
        }


@dataclass
class InventoryLot:

    id: str

    product_id: str

    lot_code: str

    quantity: Decimal

    location: str = "default"

    manufacture_date: (
        date | None
    ) = None

    expiration_date: (
        date | None
    ) = None

    supplier_id: (
        str | None
    ) = None

    reference: (
        str | None
    ) = None

    active: bool = True

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=utc_now
    )

    updated_at: datetime = field(
        default_factory=utc_now
    )

    def touch(self):

        self.updated_at = utc_now()

    @property
    def expired(self) -> bool:

        if self.expiration_date is None:
            return False

        return (
            self.expiration_date
            < date.today()
        )

    def to_dict(self):

        return {
            "id": self.id,
            "product_id": (
                self.product_id
            ),
            "lot_code": (
                self.lot_code
            ),
            "quantity": str(
                self.quantity
            ),
            "location": (
                self.location
            ),
            "manufacture_date": (
                self.manufacture_date
                .isoformat()
                if self.manufacture_date
                else None
            ),
            "expiration_date": (
                self.expiration_date
                .isoformat()
                if self.expiration_date
                else None
            ),
            "supplier_id": (
                self.supplier_id
            ),
            "reference": (
                self.reference
            ),
            "active": self.active,
            "expired": self.expired,
            "metadata": dict(
                self.metadata
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "updated_at": (
                self.updated_at
                .isoformat()
            ),
        }
