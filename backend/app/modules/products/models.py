from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from decimal import Decimal
from typing import Any


def utc_now():
    return datetime.now(
        timezone.utc
    )


@dataclass
class Supplier:
    id: str
    name: str

    document: str = ""
    contact_name: str = ""
    phone: str = ""
    email: str = ""

    active: bool = True

    metadata: dict[str, Any] = field(
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
            "name": self.name,
            "document": self.document,
            "contact_name": (
                self.contact_name
            ),
            "phone": self.phone,
            "email": self.email,
            "active": self.active,
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
class Product:
    id: str
    name: str
    sku: str
    code: str

    description: str = ""

    barcode: str | None = None
    qr_code: str | None = None

    category: str = ""

    supplier_id: str | None = None

    cost_price: Decimal = Decimal(
        "0.00"
    )

    sale_price: Decimal = Decimal(
        "0.00"
    )

    unit: str = "unit"

    active: bool = True

    track_stock: bool = True

    metadata: dict[str, Any] = field(
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
    def margin_value(self):
        return (
            self.sale_price
            - self.cost_price
        )

    @property
    def margin_percent(self):
        if self.sale_price <= 0:
            return Decimal(
                "0.00"
            )

        return (
            self.margin_value
            / self.sale_price
            * Decimal("100")
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": (
                self.description
            ),
            "sku": self.sku,
            "code": self.code,
            "barcode": self.barcode,
            "qr_code": self.qr_code,
            "category": self.category,
            "supplier_id": (
                self.supplier_id
            ),
            "cost_price": str(
                self.cost_price
            ),
            "sale_price": str(
                self.sale_price
            ),
            "margin_value": str(
                self.margin_value
            ),
            "margin_percent": str(
                self.margin_percent
            ),
            "unit": self.unit,
            "active": self.active,
            "track_stock": (
                self.track_stock
            ),
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
