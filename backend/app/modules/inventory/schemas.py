from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Any

from pydantic import BaseModel
from pydantic import Field


class StockReceive(BaseModel):
    product_id: str

    quantity: Decimal = Field(
        gt=0
    )

    location: str = "default"

    reason: str = "purchase"

    reference: str | None = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class StockIssue(BaseModel):
    product_id: str

    quantity: Decimal = Field(
        gt=0
    )

    location: str = "default"

    reason: str = "sale"

    reference: str | None = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class StockAdjust(BaseModel):
    product_id: str

    quantity: Decimal = Field(
        ge=0
    )

    location: str = "default"

    reason: str = (
        "inventory_adjustment"
    )

    reference: str | None = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class StockReserve(BaseModel):
    product_id: str

    quantity: Decimal = Field(
        gt=0
    )

    location: str = "default"

    reference: str | None = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class LotCreate(BaseModel):
    product_id: str

    lot_code: str

    quantity: Decimal = Field(
        gt=0
    )

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

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class MinimumStockSet(BaseModel):
    product_id: str

    quantity: Decimal = Field(
        ge=0
    )


class AutomaticConsumption(BaseModel):
    product_id: str

    quantity: Decimal = Field(
        gt=0
    )

    source_type: str

    source_id: str

    location: str = "default"

    use_fefo: bool = True

    reference: (
        str | None
    ) = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )
