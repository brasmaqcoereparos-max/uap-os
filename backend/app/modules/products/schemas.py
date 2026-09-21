from __future__ import annotations

from decimal import Decimal
from typing import Any

from pydantic import BaseModel
from pydantic import Field


class SupplierCreate(BaseModel):
    name: str

    document: str = ""
    contact_name: str = ""
    phone: str = ""
    email: str = ""

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class SupplierUpdate(BaseModel):
    name: str | None = None

    document: str | None = None
    contact_name: str | None = None
    phone: str | None = None
    email: str | None = None

    active: bool | None = None

    metadata: (
        dict[str, Any] | None
    ) = None


class ProductCreate(BaseModel):
    name: str

    description: str = ""

    sku: str | None = None
    code: str | None = None

    barcode: str | None = None
    qr_code: str | None = None

    category: str = ""

    supplier_id: str | None = None

    cost_price: Decimal = Field(
        default=Decimal(
            "0.00"
        ),
        ge=0,
    )

    sale_price: Decimal = Field(
        default=Decimal(
            "0.00"
        ),
        ge=0,
    )

    unit: str = "unit"

    active: bool = True

    track_stock: bool = True

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class ProductUpdate(BaseModel):
    name: str | None = None

    description: str | None = None

    barcode: str | None = None
    qr_code: str | None = None

    category: str | None = None

    supplier_id: str | None = None

    cost_price: Decimal | None = Field(
        default=None,
        ge=0,
    )

    sale_price: Decimal | None = Field(
        default=None,
        ge=0,
    )

    unit: str | None = None

    active: bool | None = None

    track_stock: bool | None = None

    metadata: (
        dict[str, Any] | None
    ) = None
